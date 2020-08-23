from collections import defaultdict

def func(l):
    visited = set()
    # using defaultdcit, because 
    # when we add  a new key, we got no KeyError, but empty list []
    # will be created automatically
    d = defaultdict(list)
       
    if len(l) < 2:
        return l
    
    # TIME O(n), n number of pairs
    for item in l:
        if len(item) == 1:
            d[item[0]] = []
        else:
            d[item[0]].append(item[1])
            d[item[1]].append(item[0])
    
    res = []
    print (d)
    for item in d:
        if item not in visited:
            output = []
            dfs(item, output, visited, d)
            output.sort()
            print (output)
            if len(res) == 0 or len(output) > len(res):
                res = output
            elif len(output) == len(res):
                res = min(res, output)
    
    return res

def dfs(item, output, visited, d):
        if item not in visited:
            visited.add(item)
            output.append(item)
            for neighbor in d[item]:
                dfs(neighbor, output, visited, d)              


# TIME O(n), number of pairs

print(func([['A', 'B'], ['D', 'E'], ['C', 'D']]) == ['C', 'D', 'E'])
"""
print(func([['A', 'B'], ['C', 'D'], ['F', 'E']]) == ['A', 'B'])
print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]) == ['C', 'D', 'E', 'F'])
print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]) == ['A', 'B', 'C', 'D', 'E', 'F'])
print(func([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'], 
            ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
            ['A', 'C'],]) == ['A', 'B', 'C', 'D', 'E', 'F'])
print(func([['item1','item2'],['item3','item4'],['item4','item5']]) == ['item3', 'item4', 'item5'])
print(func([['item1','item2'],['item2','item5'],['item3']]) == ['item1', 'item2', 'item5'])
print(func([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]) == ['item1', 'item2', 'item3'])
print(func([["item1","item2"], ["item1","item3"], ["item2","item7"], ["item3","item7"], ["item5","item6"], ["item3","item7"]]) == ['item1', 'item2', 'item3', 'item7'])
"""