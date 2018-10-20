# -*- coding: utf-8 -*-
 
import requests
from pprint import pprint
 
url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?'
 
payload = {
    'applicationId': [1098435242683481258],
    'categoryId': '11-445-1511',
    }
 
r = requests.get(url, params=payload)
 
resp = r.json()
print ('-'*40)
 
recipe_keys = [1,2,3,4]
recipe_values = [[recipe["recipeUrl"],recipe["recipeTitle"],recipe["foodImageUrl"],recipe["recipeMaterial"],recipe["recipeIndication"],recipe["recipeCost"]] for recipe in resp['result']]

dic = dict(zip(recipe_keys,recipe_values))
pprint(dic)

"""
# 必要なモジュールの読み込み
from flask import Flask, jsonify, abort, make_response

# Flaskクラスのインスタンスを作成
# __name__は現在のファイルのモジュール名
api = Flask(__name__)

# GETの実装
@api.route('/get', methods=['GET'])
def get():
    return make_response(jsonify(dic))

# エラーハンドリング
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# ファイルをスクリプトとして実行した際に
# ホスト0.0.0.0, ポート3001番でサーバーを起動
if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3001)
"""