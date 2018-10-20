from flask import Flask, request, jsonify, abort, make_response
import requests
import base64
import json
import string
from PIL import Image
from collections import defaultdict
import argparse
import flask
import os

# --------------------
API_KEY = os.environ["API_KEY"] #取得したAPIkey
GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

rm_word_list = ('合計', '言十', '税', '小計', 'お釣', 'お預', '現金', '割引', '値引', '割り引', '番号', '金額', '支払', 'イント', '期限', '買上', '利用')


# APIを呼び、認識結果をjson型で返す
def request_cloud_vison_api(image_base64):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                # 'content': image_base64.decode('utf-8') # jsonに変換するためにstring型に変換する
                'content': image_base64
            },
            'features': [{
                'type': 'TEXT_DETECTION', # ここを変更することで分析内容を変更できる
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

# 座標とテキストをwordから取り出す
def get_coord_text_from_word(word, y_whole, y_gran):
    x, y = 0, 0
    coords = word["boundingPoly"]["vertices"]
    for coord in coords:
        y += coord["y"]
    norm_y = int(y * y_gran / y_whole)
    x1 = coords[0]['x']
    x2 = coords[1]['x']
    text = word["description"]
    return ((norm_y, (x1, x2)), text)

# 数字だけ取ってくる
def str2int(text):
    number = ''.join(n for n in text if n in string.digits)
    return int(number)

# フィルターにより商品だけを抽出
def get_food(word_dict_value, x_diff, x_gran):
    # スペースの大きさで分ける
    chunk_list = []
    x_pred = word_dict_value[0][1][1]
    text_ls = []
    for text, xs in word_dict_value:
        if (xs[0] - x_pred) < (x_diff / x_gran):
            text_ls.append(text)
        else:
            chunk_list.append(''.join(text_ls))
            text_ls = []
            text_ls.append(text)
        x_pred = xs[1]
    chunk_list.append(''.join(text_ls))

    if len(chunk_list) > 1 and len(chunk_list[0]) > 2:
        if not any(rm_word in chunk_list[0] for rm_word in rm_word_list):
            if not '点' in chunk_list[1]:
                num = str2int('0' + chunk_list[1])
                if num > 9 and num < 10**5:
                    name = chunk_list[0]
                    return {"name" : name, "price" : num}

# json形式からfoodを取り出す
def json2food(result, x_gran, y_gran):
    # 必要な情報をjson形式のものから取り出す
    try:
        main_info, *words = result["responses"][0]['textAnnotations']
        text_whole = main_info["description"]
        x_diff = main_info["boundingPoly"]["vertices"][1]["x"] - main_info["boundingPoly"]["vertices"][0]["x"]
        y_whole = main_info["boundingPoly"]["vertices"][2]["y"]

        word_dict = defaultdict(lambda:[])
        # 座標とtextを取り出す
        for word in words:
            coord, text = get_coord_text_from_word(word, y_whole, y_gran)
            word_dict[coord[0]].append((text, coord[1]))

        # x座標でsort
        for key, val in word_dict.items():
            word_dict[key] = sorted(word_dict[key], key=lambda x : sum(x[1]) / 2)

        # foodを取ってくる
        for value in word_dict.values():
            food = get_food(value, x_diff, x_gran)
            if food:
                yield food
    except:
        return None

def base64_to_food(image_base64):
    x_gran = 10
    y_gran = 15

    # 文字認識させたい画像をtest.pngとする
    result = request_cloud_vison_api(image_base64)
    food_dic = {}
    try:
        food_dic["foods"] = [name_price for name_price in json2food(result, x_gran, y_gran)]
    except:
        food_dic["foods"] = "None"
    return food_dic
# -------------------------

app = Flask(__name__)

@app.route('/')
def index():
    return "こんにちは"


@app.route('/post', methods=['POST']) #Methodを明示する必要あり
def post():
    if request.method == 'POST':
        try:
            image_base64  = request.form['picture']
            result = base64_to_food(image_base64)
        except:
            return make_response("データタイプをbase64にしてください")

    else:
        result = "no picture."
    return make_response(jsonify(result))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
