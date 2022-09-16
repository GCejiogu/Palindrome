letters = input("please enter word here: ")
All_caps = letters.upper()


def palindrome(All_caps):

    Reverse = All_caps[::-1]

    if Reverse == All_caps:
        print("It's a Palindrome")

    else:
        print("It's not a Palindrome")


palindrome(All_caps)
