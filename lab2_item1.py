def is_palindrome(number):
    
    str_num = str(number)
    if str_num == str_num[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

user_input = int(input("Enter an integer: "))
result = is_palindrome(user_input)
print(result)
