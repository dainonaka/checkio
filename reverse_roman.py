def reverse_roman(roman_string):
    dict = {"M":1000,"CM":900,"D":500,"CD":400, "C":100, "XC":90,
            "L":50, "XL":40, "X":10, "IX": 9, "V":5, "IV":4, "I":1}
    res = 0
    while roman_string:
        if len(roman_string) > 1 and \
           roman_string[0:2] in dict.keys():
            res += dict[roman_string[0:2]]
            roman_string = roman_string[2:]
        elif roman_string[0] in dict.keys():
            res += dict[roman_string[0]]
            roman_string = roman_string[1:]   
    return res
