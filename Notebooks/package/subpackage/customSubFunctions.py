def check_palindrome(string):
    string = string.lower().replace(" ","")
    return string == string[::-1]