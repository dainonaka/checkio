def checkio(n, m):
    l, s, result = bin(max(n,m))[2:], bin(min(n,m))[2:],0
    s = ("0" * abs(len(l)-len(s))) + s
    for cnt in range(len(l)):
        if not s[cnt] ==l[cnt]: result += 1
    return result
