import asyncio
import edge_tts

TEXT = "Hello world"

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        "en-US-AriaNeural"
    )
    await communicate.save("output.mp3")

asyncio.run(main())