original_dict = {'apple': 30, 'banana': 10, 'cherry': 50}

#### Ascending order

# sort by keys
# method 1
sorted_dict_asc_keys_1 = dict(sorted(original_dict.items()))
print(sorted_dict_asc_keys_1)

# method 2
sorted_dict_asc_keys_2 = dict(sorted(original_dict.items(), key=lambda item:item[0]))
print(sorted_dict_asc_keys_2)

# sort by values
sorted_dict_asc_values = dict(sorted(original_dict.items(), key=lambda item:item[1]))
print(sorted_dict_asc_values)

#### Descending order
sorted_dict_desc_keys = dict(sorted(original_dict.items(),reverse=True))
print(sorted_dict_desc_keys)

sorted_dict_desc_values = dict(sorted(original_dict.items(), key=lambda item:item[1], reverse=True))
print(sorted_dict_desc_values)