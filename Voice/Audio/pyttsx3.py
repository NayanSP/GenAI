import pyttsx3

engine = pyttsx3.init()

txt = """

Mina had just about gotten used to coming across Nicholas Bolt in the strangest places. Her boss' cases took him to every obscure nook and cranny in town, and he was relentless. Still, she had not expected seeing her employer and reluctant mentor staring daggers into his glass of cheap borboun at The Greek Poet.

For a few seconds, Mina considered leaving him to whatever scheme he was up to. She was out to have a good time, and whatever was going on with Nick was sure to be harrowing. Even so, she thought as she made her way across the dance floor towards the bar, she wasn't very good at letting sleeping dogs lie. They had as much in common.


"Hey Nick, what's going on?" Mina asked as she found a free spot between Nick and a couple having an uncomfortably intense discussion, the exact topic of which Mina was unable to pick out over the chatter.

"Oh! Wilhelmina, I didn't see you", Nick said. "What are you doing here?"

Mina found herself adjusting her fringe, a subconscious gesture she had noticed just recently enough to still be annoyed by. "Just happened to be in the area, really. You working a case or what?"

"Curious coincidence. I'm a bit stuck, you see." Nick said, swirling the liquor in his glass like some old-timey soothsayer. "Do you mind if I just bounce some ideas off you? I really am in quite a bind."

Mina nodded. As much as she wanted to get back to her friend and get this night started, it would have to be a pretty juicy conundrum if it stumped her boss.


"I'm in the employ of Adonis Diamantis," Nick said

"What, the film producer?"

"The very same. He's tasked me with tracking down his daughter Ruby. She was last seen by her family leaving the family mansion with one..." Nick pulled out his notebook and started flipping through it "One Shyma Lahiri, who I believe to be a housekeeper of some sort for the family. Through what I could find of witness testimony, I narrowed their path down to two or three alternatives after confirming with my contacts in the taxi service that they did indeed travel by foot. After some additional casing, I manage to locate a witness who could confirm Ms. Diamantis arriving at this location on the night in question. So far, so good."

"So the trail's gone cold?" Mina asked, she cast a glance at Nick's notebook, but the mirrored chicken-scratch he used to keep his notes were quite unreadable, she assumed by design.

"Almost. After developing some semblance of rapport with the bartenders, I have confirmed that she was indeed here, but that she left with a paramour around midnight."

"Uh, excuse me", Mina said. "With a what?"

"Oh," Nick said, reeling in his line of thought with some obvious difficulty. "A... lover, usually illicit."

"Like a side piece?"

"I suppose. However, with this, as you put it, Side Piece, things get less clear by the minute. The staff has been less than helpful for identifying this man, despite me making it quite clear that he may very well be the key to this whole disappearance. I get the feeling this establishment are not too fond of private dicks."


It took every ounce of mental fortitude Mina had to not burst out laughing, and even then, she had to turn from Nick to signal for the bartender for a drink. She had planned to keep sober, if nothing else to not have to interact with her ex who was manning the bar tonight, but this was shaping up to be that kind of night that called for some intoxicants.


"So I am considering several options, we may be dealing with some cross-dresser, or quite possibly a cover-up of some kind, no, this isn't as easy as I thought it would be, not by a long shot." Nick continued on, undaunted.

As soon as she had suppressed the very unprofessional laughter that was building in her chest, Mina turned back. In the progress of overcoming her fit, two very important pieces had clicked into place for her.

"You've been looking for this mystery man, then?" She asked.

"Relentlessly."

"Nick... Nicholas. Where do you think you are?"

"The Greek Poet? If I may, this place is considerably less Homeric than I would suspect, odd choices all around if you don't mind me saying so."

"It's... uh... not that Greek poet it's named after, boss."

"Whatever do you mean."

Mina sighed, there was, apparently, no way around just telling the man. With that in mind, she leaned over and whispered a few key facts about The Greek Poet and it's clientele into Nick's ear.

"Oh..."


Nick's eyes widened. Mina knew the look, this was a lifting of the veil in progress. His eyes darted around the room, as if it was the first time he saw it, or any room for that matter. "I see", he said. "That means ... yes, yes of course. How could I not have... excuse me. I have to go. I have inquiries to make."


And without as much as a word of thanks, Nick left The Greek Poet, a determined stomp in his step. Mina had seen him completely revitalize like that before, but this was the first time it had been her to figure something out before he did. The surge in Mina's mood was only slightly marred when the bartender stepped up to her. "Still want that beer, or are you too busy hunting teenage runaways with your boyfriend?"

Mina held up one finger, then two. "Beer me, and then go fuck yourself, Susan."
"""


engine.save_to_file(text=txt,
                    filename="output_pyttsx3.mp3")
engine.runAndWait()

# Pros:
# Completely offline
# Simple

# Cons:
# Robotic voice
# Not ideal for YouTube content