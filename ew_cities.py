def subnetworks(net, crushes):
    crushes = set(crushes)
    for num in range(len(net)):
        net[num] = set(net[num])-crushes
    cnt = 0
    try:net.remove(set())
    except: pass
    for n in range(len(net)):
        if not any([net[n] & net[m] for m in range(len(net)) if not n >= m]):
            cnt += 1
    return cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
