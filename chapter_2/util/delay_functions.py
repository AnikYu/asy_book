import asyncio

async def delay(sec):
    print(f'Sleep {sec}')
    await asyncio.sleep(sec)
    print(f'Сон закаончился {sec} sec')
    return sec    