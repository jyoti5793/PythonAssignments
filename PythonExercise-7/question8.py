def count_characters(word):
    try:
        if len(word) < 10:
            raise ValueError("Oops! Too short string")

        print(word[:10])

    except ValueError as e:
        print(e)

count_characters("guyfyt")
