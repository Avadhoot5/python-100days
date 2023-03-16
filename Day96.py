# AsyncIO

import time
import asyncio 
import requests

# async def main():
#     print("hello..")
#     await asyncio.sleep(1)
#     print("..World!")

# asyncio.run(main())

async def function1():
    print("func 1")
    URL = "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8NGslMjBtb3VudGFpbnxlbnwwfHwwfHw%3D&w=1000&q=80"
    response = requests.get(URL)
    open("instagram.jpg", "wb").write(response.content)
    return "Name"

async def function2():
    print("func 2")
    URL = "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8NGslMjBtb3VudGFpbnxlbnwwfHwwfHw%3D&w=1000&q=80"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)

async def function3():
    print("func 3")
    URL = "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8NGslMjBtb3VudGFpbnxlbnwwfHwwfHw%3D&w=1000&q=80"
    response = requests.get(URL)
    open("instagram3.jpg", "wb").write(response.content)

async def main():
    # functions run after 1 another
    # await function1()
    # await function2()
    # await function3()
    # return 3
    # all functions run parallely, parallel execution 
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)
    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

# running the main function
asyncio.run(main())
