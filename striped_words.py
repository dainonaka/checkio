VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
def checkio(text):
    list = ((text.replace(","," ")).replace("."," ").replace("?"," ").replace("!", " ")).upper().split(" ")
    cnt = 0
    for word in list:
        if all([word[num] in VOWELS for num in range(0,len(word),2)]) and \
           all([word[num] in CONSONANTS for num in range(1,len(word),2)]) and \
           len(word) >= 2:
            cnt += 1
        elif all([word[num] in CONSONANTS for num in range(0,len(word),2)]) and \
           all([word[num] in VOWELS for num in range(1,len(word),2)]) and \
           len(word) >= 2:
            cnt += 1
    return cnt
#How can I replace non-alphabets in shorter sentense?!?!

