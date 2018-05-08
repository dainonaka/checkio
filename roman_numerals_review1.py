def checkio(data):
    data, ans = str(data), ""
    dict ={4:{'3' : 'MMM', '2': 'MM', '1':'M'},
        3:{'9': 'CM', '8': 'DCCC', '7': 'DCC', '6': 'DC', '5': 'D', '4': 'CD', '3': 'CCC', '2': 'CC', '1': 'C', '0': ''}, 
        2:{'9': 'XC', '8': 'LXXX', '7': 'LXX', '6': 'LX', '5': 'L', '4': 'XL', '3': 'XXX', '2': 'XX', '1': 'X', '0': ''},
        1:{'9': 'IX', '8': 'VIII', '7': 'VII', '6': 'VI', '5': 'V', '4': 'IV', '3': 'III', '2': 'II', '1': 'I', '0': ''}}
    try:
        for num in range(1, len(data) + 1):
            ans = dict[num][data[-num]] + ans
        return ans
    except: return "Wrong value"
