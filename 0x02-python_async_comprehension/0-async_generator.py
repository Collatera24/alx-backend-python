#!/usr/bin/env python3
'''Task: Async Generator..
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a random number from 0 to 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform() * 10



# Example usage
async def main():
    async for number in async_generator():
        print(number)

if __name__ == "__main__":
    asyncio.run(main())
