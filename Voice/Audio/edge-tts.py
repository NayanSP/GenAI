import asyncio
import edge_tts

async def generate():
    communicate = edge_tts.Communicate(
        "Hello, welcome to my YouTube channel.",
        "en-US-AriaNeural"
    )
    await communicate.save("output_edge_tts.mp3")

asyncio.run(generate())