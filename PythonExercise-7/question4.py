def index(list):
    try:
        for i in range(0,20):
            print(list[i])
    except IndexError as e:
        print(e)


index([8,4,3])