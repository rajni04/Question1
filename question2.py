
def max_score(dc):
    for key, value in dc.items():
        print(f'{key} : {value}')
    return dc




dict1 = {1 : "name1", 2 : "name2"}
dict2={1 : 50, 2: 60,3 : 70}
new_dict=max(max_score(dict2))

# all_values = dict2.values()
# max_value = max(all_values.items(all_values))
