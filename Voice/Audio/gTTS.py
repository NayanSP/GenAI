from gtts import gTTS

text = """

I've been chasing him across the continent, tracking the trail of blood and broken bodies that he leaves in his wake. He is always one step ahead, this phantom brutalizer, leaving bodies beaten to a pulp, then meticulously posed in everyday poses. The brutality is his calling card, the relaxed poses I have taken to understand as a statement, of sorts.

For me, it all began when he killed my wife, but I do not know how long he had been active at that point. The police never suspected me, so I can't but imagine his atrocities were well known to them. I began my crusade then, going down every crooked alley and ransacking flophouses, some times in a daze, in search of the monster who killed my wife. Once or twice I was the first to find one of his victims. One, I was later told she had been a law student from somewhere down south, was still warm when I got to her. He laid low some time after that one, but I never relented, and followed a string of clues out of town, across the state line.

For a while, I suspected that he led me astray, that the little clues he left at his crime scenes were diversions, meant to send me on a wild goose chase. Once I found the mangled corpse of a transient posed like he was stretching his back on a park bench I knew I was still on track. Once I found the note in the corpse's hand reading "You really should talk to someone about this. Your friend and monster, U" I realized that not only had he intended to be followed, he had intended for it to be me who followed him.

I have never seen hide nor hair of this monster who walks like a man, but what little I've gathered from those who have spoken to witnesses, he is a powerfully repulsive creature. Hunched, scrabbling along more like a chimp than a man, a bestial snarl in his face, but the eyes are said to be the worst part by far. Even so, I know that he has ways of getting around, both in public and on various means of transport, so surely he must be able to disguise his animal nature. After all, he manages to arrive ahead of me wherever he goes, somehow, and I find myself cursing my need to sleep.

In my restless dreams, I some times see him. He is every bit as abhorrent as I could ever imagine. Some times, he chases me, other times, I chase him. Other times still, I find myself staring into his terrible, terrible eyes as he appraises me with a predator's cunning. His eyes as free of a soul as he is of conscience. I awaken with a scream more often than not from these dreams.

My eyes flash open, I'm drenched in a cold, slimy sweat. I had dreamt that the murderer was just outside my hotel room, peering in at me, and I out at him through the poorly illuminated bathroom window. As I watched in stunned horror, he had reached out a hand, an arthritic claw more than anything, and slathered a message in red on the window. My mind reads his missive, without meaning to, and definitely without wanting to, and as the message pierces my mind, I wake up. I get up, I have no idea what time it is, or what day it is, and my muscles and joints ache like I have aged decades.

I stumble to the bathroom, longing for water to quench the burning sensation in my throat. As I get there, I realize something impossible, and yet, entirely unavoidably true. The bathroom has no window. The message is instead slathered on the mirror in what I now realize is coagulating blood. "You + Me = 1" I look down on my hands.
"""

tts = gTTS(text=text, lang='en')
tts.save('output_gtts.mp3')
print('Audio Saved')

# Pros:
# Very easy to use
# Generates MP3 directly
# Works well for basic narration

# Cons:
# Requires internet access
# Voices are less natural than modern AI voices