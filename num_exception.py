# class NotIntError(Exception):
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return "This is not a number!"
#
#
# class NotFloatError(Exception):
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return "This is not a number!"


def main():
    try:
        num = input("enter a number\n")
        if num.count(".") == 1:
            num = float(num)
        else:
            num = int(num)
        num+=1
        print("number + 1 = " + num)
        print(num)
    except EOFError as eof:
        print("EOF character was entered, please enter a number")
    except ValueError as ve:
        print("Please enter a number")
    except TypeError as te:
        if type(num) == chr:
            print("A char was entered, please enter a number")
        elif type(num) == str:
            print("A string was entered, please enter a number")
        elif type(num) == dict:
            print("A dictionary was entered, please enter a number")
        elif type(num) == list:
            print("A list was entered, please enter a number")


if __name__ == '__main__':
    main()
