import asyncio

async def hello_world_message():
    await asyncio.sleep(1)
    return 'Hello'

async def main():
    mess = await hello_world_message()
    print(mess)

asyncio.run(main())