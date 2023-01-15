def readfile():
    with open('token.txt', "r", encoding="utf_8") as s:
        token = s.read()
    return token
