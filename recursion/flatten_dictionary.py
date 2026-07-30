def flatten_a_dictionary(nested_dict):
    def dfs(cur_dict, cur_prefix):
        for k, v in cur_dict.items():
            new_key = f"{cur_prefix}.{k}" if cur_prefix else k
            if isinstance(v, dict):
                dfs(v, new_key)
            else:
                res[new_key] = v

        return res

    res = {}
    dfs(nested_dict, '')
    return res

# nested_dict = {"a":{"b":{"c":{"d":1,"e":2}}}}
# nested_dict = {
#                 "a":
#                     {"b":
#                         {"c":
#                             {
#                                 "d":1,
#                                 "e":2
#                             }
#                         }
#                     }
#             }
nested_dict = {
                "a":
                    {
                        "b":1, 
                        "c":2
                    },
                "d":
                    {
                        "e":3
                    },
                "f":
                    {
                        "g":4
                    }
            }

res = flatten_a_dictionary(nested_dict)
print(res) # {"a.b.c.d":1}