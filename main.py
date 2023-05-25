from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(text).sentiment.polarity

    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return Mood(emoji="😀", sentiment=sentiment)
    elif sentiment <= hostile_threshold:
        return Mood(emoji="😡", sentiment=sentiment)
    else:
        return Mood(emoji="😐", sentiment=sentiment)

if __name__ == "__main__":
    while True:
        txt: str = input("Enter some text: ")
        mood: Mood = get_mood(txt, threshold=0.3)

        print(f"Mood: {mood.emoji} ({mood.sentiment})")