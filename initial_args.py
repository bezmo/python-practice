"""関数の初期値の振る舞いを確認するためのスクリプト

関数の初期値は、関数定義時に生成されたオブジェクトを使い回す。
このため、初期値にオブジェクトを指定する場合は振る舞いに注意すること。
"""
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

