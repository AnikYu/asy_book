import asyncio

async def coroutine(num):
    return num+1

result = asyncio.run(coroutine(1))
print(result)