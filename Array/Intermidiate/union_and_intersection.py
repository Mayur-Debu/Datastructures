def union(set_a,set_b):
    set_a=sorted(set_a).copy()
    set_b=sorted(set_b).copy()
    return set(set_a)|set(set_b)
    pass

def intersection(set_a,set_b):
    set_a=sorted(set_a).copy()
    set_b=sorted(set_b).copy()
    return set(set_a)&set(set_b)
    pass

if __name__ == '__main__':
    set_a=[]
    set_b=[]
    set_a=list(map(int,input('Enter the elements in set A: ').split(" ")))
    set_b=list(map(int,input('Enter the elements in set B: ').split(" ")))
    print(f'Union: {union(set_a,set_b)}')
    print(f'Intersection: {intersection(set_a, set_b)}')
    