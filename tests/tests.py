import asyncio

from engine import AsyncEngine, Event

if __name__ == '__main__':
    # easy use example

    EVENT_TIME = "timer"

    engine = AsyncEngine(work_core=200)


    async def func(data):
        print(data)
        await asyncio.sleep(1)


    engine.register(EVENT_TIME, func)
    engine.start()
    # 当前主线程调用
    from time import time

    start = time()
    # 模拟推送1000000的事件
    for _ in range(100000):
        # asyncio.run(engine.put(Event(EVENT_TIME, f"当前数据为{_}")))
        engine.put(Event(EVENT_TIME, f"当前数据为{_}"))

    # 拿到任务结束的时间
    while True:
        if engine._queue.empty():
            end = time()
            break
    print(f"耗时: {(end - start) * 1000} ms")
