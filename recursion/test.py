import copy

def flatten_a_dictionary(nested_dict):
    new_key = ""
    new_dict = {}
    nested_dict_copy = copy.deepcopy(nested_dict)
    for key in nested_dict:
        while len(nested_dict_copy)>0:
            for k, v in nested_dict_copy.items():
                if isinstance(v, dict):
                    new_key = f"{new_key}.{k}" if new_key else k
                    print(nested_dict)
                    nested_dict_copy = nested_dict[key]
                else:
                    new_key = ""
                    new_dict[new_key] = v
                    break
    print('new', new_dict)
    return new_dict
        


nested_dict = {"a":{"b":1, "c":2},"d":{"e":3},"f":{"g":4}}
res = flatten_a_dictionary(nested_dict)
print(res) # {"a.b.c.d":1}