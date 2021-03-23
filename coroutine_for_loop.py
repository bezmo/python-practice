import asyncio
import random
from typing import Coroutine, List


# コルーチンについて
# コルーチンは async def で定義される関数
# イベントループ内でのみ実行できる。または、イベントループ内で実行する関数の中で await を
# 使用して実行できる。
#

async def sleep_print(i: int) -> int:
    print(f'start: {i}')
    await asyncio.sleep(random.uniform(1, 5))
    print(f'end: {i}')
    return i


async def main():
    coroutines: List[Coroutine] = []

    for i in range(5):
        coroutines.append(sleep_print(i))

        if len(coroutines) == 3:
            for val in await asyncio.gather(*coroutines):  # coroutineをまとめて実行
                print(f'return: {val}')
            coroutines.clear()
    else:
        for val in await asyncio.gather(*coroutines):  # coroutineをまとめて実行
            print(f'return: {val}')
        coroutines.clear()


if __name__ == '__main__':
    # main()の実行結果
    #
    # >>> python async_for_loop.py
    # start: 0
    # start: 1
    # start: 2
    # end: 2
    # end: 0
    # end: 1
    # return: 0
    # return: 1
    # return: 2
    # start: 3
    # start: 4
    # end: 3
    # end: 4
    # return: 3
    # return: 4
    #
    # 待ちをランダムにしているので、リスト順と終了順はバラバラだが、
    # gather()から帰ってくる順番はリスト順となっている
    #
    asyncio.get_event_loop().run_until_complete(main())
