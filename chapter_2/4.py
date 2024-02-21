import asyncio

async def add_one(number: int) -> int:
    return number+1

async def main():
    one_ = await add_one(1)
    two_ = await add_one(2)
    
    print(one_)
    print(two_)

asyncio.run(main())