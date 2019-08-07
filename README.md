# Async_event

> 基于asyncio的 事件引擎封装

# 简单使用 

```
import asyncio

from async_event import AsyncEngine, Event

if __name__ == '__main__':
    # easy use example

    EVENT_TIME = "timer"
    # 创建引擎对象 
    engine = AsyncEngine(work_core=200)


    async def func(data):
        print(data)
        await asyncio.sleep(1)


    # 注册事件和对应的处理函数
    engine.register(EVENT_TIME, func)

    # 开始处理
    engine.start()
    # 当前主线程调用

    # 模拟推送1000000的事件
    for _ in range(100000):
        # asyncio.run(engine.put(Event(EVENT_TIME, f"当前数据为{_}")))
        engine.put(Event(EVENT_TIME, f"当前数据为{_}"))



```
