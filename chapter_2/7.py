from util.delay_functions import delay
import asyncio

async def add_one(num):
    return num + 1

async def hello_world_message():
    await delay(1)
    return 'Hello'

async def main():
    message = await hello_world_message()
    one_ = await add_one(1)
    
    print(message)
    print(one_)
    
asyncio.run(main())