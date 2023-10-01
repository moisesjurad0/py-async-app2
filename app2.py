import asyncio

async def background_task():
    # Simulate some time-consuming task
    await asyncio.sleep(5)
    print("Background task is complete")

async def main():
    loop = asyncio.get_event_loop()    
    loop.run_in_executor(None, background_task)


    # Continue with other tasks or operations
    print("Main thread continues running")

    # At some point later, you can await the background task
    #await task
    print("Main thread continues after background task")
        


if __name__ == "__main__":
    asyncio.run(main())
