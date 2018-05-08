def long_repeat(line):
    list = [1]
    for num in range(1,len(line)):
        if line[num] == line[num -1]: list.append(list[num -1] + 1)
        else: list.append(1)
        return max(list)
