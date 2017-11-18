from pprint import pprint
dict1={'City':"Moscow",'t':'5','wind':"west"}
dict2={'City':"Rome",'t':'26','wind':"South"}
dict3={'City':"London",'t':'7','wind':"nord"}
all_dict={"Ilya":dict1,'Anna':dict2,"Olga":dict3}
name=input("Введите имя: ")
city=all_dict[name]["City"]
t=all_dict[name]['t']
wind=all_dict[name]['wind']



print("Данные по имени: ", city, t, wind)
