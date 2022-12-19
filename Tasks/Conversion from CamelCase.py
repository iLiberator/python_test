def from_camel_case(name: str) -> str:
    # replace this for solution
    temp = list(name)
    for x in temp:
        if x.isupper():
            if temp.index(x) == 0:
                temp[temp.index(x)] = x.lower()
            elif temp.index(x) != 0:
                temp[temp.index(x)] = '_' + x.lower()
    return ''.join(temp)


print(from_camel_case('MyFunctionName'))

'''
name = 'MyFunctionName'
temp = list(name)
for x in temp:
    if x.isupper():
        if temp.index(x) == 0:
            temp[temp.index(x)] = x.lower()
        elif temp.index(x) != 0:
            temp[temp.index(x)] = '_' + x.lower()
'''
        

#assert from_camel_case("MyFunctionName") == "my_function_name"
#assert from_camel_case("IPhone") == "i_phone"