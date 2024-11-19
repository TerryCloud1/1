keys = ['a', 'b', 'c']
values = ['x','y','z']
idxs = enumerate(zip(keys,values))
print(list(f'{i}:{k} = {v}' for i,(k,v) in idxs))