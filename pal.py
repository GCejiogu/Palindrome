


letters = input("please enter word here: ")


def palindrome(letters):

    Reverse = letters[::-1]

    if Reverse == letters:
        print("It's a Palindrome")

    else:
        print("It's not a Palindrome")


palindrome(letters)
