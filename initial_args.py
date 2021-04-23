from typing import List

def sample(s: str, l: List[str] = []):
    l.append(s)
    print(l)


sample('a')
# >>> ['a']

sample('b')
# >>> ['a', 'b']

sample('c')
# >>> ['a', 'b', 'c']

sample('d', [])
# >>> ['d']

