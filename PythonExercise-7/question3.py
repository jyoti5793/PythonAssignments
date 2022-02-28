def attribute_error():
    try:
        x=3
        x.append(5)
        
        print(x)
    except AttributeError as e:
        print(e)

attribute_error()