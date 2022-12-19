def to_camel_case(name: str) -> str:
    # replace this for solution
    name = name.capitalize()
    for x in name:
        if x == '_':
            ind = name.index(x)
            name = name.replace(name[ind : ind+2], name[ind+1].upper())
    return name


print(to_camel_case("my_function_name"))

#assert to_camel_case("my_function_name") == "MyFunctionName"
#assert to_camel_case("i_phone") == "IPhone"