def checkio(expression):
    list = "{}()[]"
    cnt = []
    for tkn in expression:
         if tkn in list[0::2]: cnt.append(tkn)
         elif tkn in list[1::2]:
             if len(cnt) >=1 and tkn == list[list.find(cnt[-1])+1]: cnt.pop()
             else: cnt=["dead"]
    return cnt == []
