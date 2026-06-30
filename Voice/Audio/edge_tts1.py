import asyncio
import edge_tts

with open("story1.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print('File Read')

TEXT = content

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        "en-US-AriaNeural"
    )
    await communicate.save("Story2.mp3")

asyncio.run(main())