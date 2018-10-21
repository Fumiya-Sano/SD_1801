# レシートの食材名(1つ) → 一般化された食材名リスト
def generalize_food(my_food_name):
    with open("genre_name_list.txt") as general_food_list:
        # 内包表記
        result = {general_food_name.strip()
                  for general_food_name in general_food_list
                  if general_food_name.strip() in my_food_name}
        return result

# 一般化された食材(１つ) → そのid
def get_genre_id(target_food):
    with open("genre_id.txt") as id_food_text:
        for id_food in id_food_text:
            id, food = id_food.split()
            if food == target_food:
                return id