#food_name = '吉野屋白菜キムチ'
food_name = str(input())
food_namelist = []
with open("genre_name_list.txt") as genre_name_list:
    for line in genre_name_list:
        if line.strip() in food_name:
            food_namelist.append(line.strip())
    #重複削除
    food_namelist = list(set(food_namelist))
    print(food_namelist)

#matching genre_id

#food_namelist2 = ['キムチ', '白菜']
#food_namelist2 = input()
genre_idlist2 = []
with open("genre_id.txt") as g:
    #name_list2から変更
    for one_food in food_namelist:
        for line2 in g:
            test = line2.split()
            if test[1] in one_food:
                genre_idlist2.append(test[0])
print(genre_idlist2)

import requests
from pprint import pprint
 
url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?'
 
payload = {
    'applicationId': [1098435242683481258],
    'categoryId': genre_idlist2[0],
    }
 
r = requests.get(url, params=payload)
 
resp = r.json()
print ('-'*40)
 
recipe_keys = [1,2,3,4]
recipe_values = [[recipe["recipeUrl"],recipe["recipeTitle"],recipe["foodImageUrl"],recipe["recipeMaterial"],recipe["recipeIndication"],recipe["recipeCost"]] for recipe in resp['result']]

dic = dict(zip(recipe_keys,recipe_values))
pprint(dic)

print ('-'*40)