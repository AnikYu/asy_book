import asyncio
from util.delay_functions import delay

async def main():
    sleep_ = asyncio.create_task(delay(3))
    print(type(sleep_))
    result = await sleep_
    print(result)
    
asyncio.run(main())