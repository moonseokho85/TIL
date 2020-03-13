def find_name(x):
    name_dict = {
        39: "Justin",
        14: "John",
        67: "Mike",
        105: "Summer"
    }
    result = set()
    if x in name_dict:
        return name_dict[x]
    else:
        return "?"

print(find_name(39))
print(find_name(1))