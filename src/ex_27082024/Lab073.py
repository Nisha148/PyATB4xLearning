my_shopping_list1 = ["bread", "milk", "butter"]
print(my_shopping_list1[0])
print(len(my_shopping_list1))


def bring_home_more_food(my_list):
    my_list.append("Cheese")
    return my_list


l = bring_home_more_food(my_shopping_list1)
print(l)
