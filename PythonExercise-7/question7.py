def reverse_string(word):
        try:
            if len(word)%2==0:
                print(word[::-1])
        except TypeError as e:
            print(e)
        except:
            print("Something went wrong!")



reverse_string(7)
