class InvalidNumError(Exception):
    def __init__(self, message):
        self.message = message

def find_marks(marks):
    try:
        if marks > 100 or marks ==0:

            raise InvalidNumError("Error! Try again")
        else :
            print("Result Processing")

    except InvalidNumError as err:

        print(err.message)
find_marks(0)