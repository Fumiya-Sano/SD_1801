import requests
# レシートの食材名(1つ) → 一般化された食材名リスト
def generalize_food(my_food_name):
    with open("genre_name_list.txt") as general_food_list:
        # 内包表記
        result = {general_food_name.strip()
                  for general_food_name in general_food_list
                  if general_food_name.strip() in my_food_name}
        return result

# 一般化された食材(１つ) → そのid → レシピ提案
def get_genre_id(target_food):
    with open("genre_id.txt") as id_food_text:
        for id_food in id_food_text:
            id, food = id_food.split()
            if food == target_food:
                return id

def my_food_to_recipe(my_food_name):
    general_food_list = generalize_food(my_food_name)
    ids = [get_genre_id(general_food) 
           for general_food in general_food_list]


    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?'
    
    payload = {
        'applicationId': [1098435242683481258],
        'categoryId': ids,
    }
    
    r = requests.get(url, params=payload)
    resp = r.json()

    recipes_dict = {}
    recipe_values = [[{"URL":recipe["recipeUrl"]},{"title":recipe["recipeTitle"]},{"image":recipe["foodImageUrl"]},{"ingredient":recipe["recipeMaterial"]},{"time":recipe["recipeIndication"]},{"cost":recipe["recipeCost"]}] for recipe in resp['result']]
    ls = []
    for recipe_value in recipe_values:
        ls.append({"recipe" : recipe_value})
    recipes_dict["recipes"] = ls
    
    return recipes_dict
