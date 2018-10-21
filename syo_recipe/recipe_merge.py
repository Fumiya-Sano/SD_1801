import requests
from pprint import pprint

import jasu

#my_food_name = '吉野屋白菜キムチ'
my_food_name = str(input())

general_food_list = jasu.generalize_food(my_food_name)
ids = [jasu.get_genre_id(general_food) 
       for general_food in general_food_list]


url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?'
 
payload = {
    'applicationId': [1098435242683481258],
    'categoryId': ids,
    }
 
r = requests.get(url, params=payload)
 
resp = r.json()
print ('-'*40)
 
recipe_keys = [1,2,3,4]
recipe_values = [[recipe["recipeUrl"],recipe["recipeTitle"],recipe["foodImageUrl"],recipe["recipeMaterial"],recipe["recipeIndication"],recipe["recipeCost"]] for recipe in resp['result']]
dic = dict(zip(recipe_keys,recipe_values))
pprint(dic)

print ('-'*40)