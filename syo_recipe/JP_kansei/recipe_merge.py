import requests
from pprint import pprint
from flask import Flask, request, jsonify, abort, make_response
import json

import jasu

# -------------------------

app = Flask(__name__)

@app.route('/')
def index():
    return "こんにちは"


@app.route('/post', methods=['POST']) 
def post():
    if request.method == 'POST':
        # try:
        passive_dict  = request.form
        target_food = passive_dict["1"]
        result = jasu.my_food_to_recipe(target_food)
        # except:
        #     return make_response("データがおかしい")

    else:
        result = "postにしてよ！！"
    return make_response(jsonify(result))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)