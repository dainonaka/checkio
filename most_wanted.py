def checkio(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list = [(text.lower()).count(letter) for letter in alphabet]
    return alphabet[list.index(max(list))]
