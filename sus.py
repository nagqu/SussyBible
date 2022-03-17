from dotenv import dotenv_values
from random import randint
import tweepy
import requests
import re
import time

config = dotenv_values(".env")

auth = tweepy.OAuth1UserHandler(
    config["API_KEY"], config["API_SECRET"],
    config["ACCESS"], config["ACCESS_SECRET"]
)
api = tweepy.API(auth)

impostors = ["Amogus", "Yellow", "Red", "Crewmate", "Bean", "Crewpostor"]
kills = ["vote out", "game end", "eject"]
escapes = ["vent"]

# kill -> vote out, game end
# escape -> vent
# Judas -> impostor sus


def get_verse():
    verse = requests.get('https://labs.bible.org/api/?passage=random')
    text = verse.text
    text = text.replace("<b>", "").replace("</b> ", " ")
    return text


def make_sussy(verse):
    status = False
    # Regex trigger
    if re.search("the lord|jesus|god|messiah|father|kill|escape|judas", verse, flags=re.IGNORECASE):
        print("Regex Triggered")
        verse = re.sub("Judas", "Sussy Baka", verse)

        verse = re.sub("the lord|jesus|god|messiah",
                       impostors[randint(0, len(impostors) - 1)], verse, flags=re.IGNORECASE)

        verse = re.sub(
            "Father|Lord", impostors[randint(0, len(impostors) - 1)], verse)

        verse = re.sub("escape", escapes[randint(
            0, len(escapes) - 1)], verse, flags=re.IGNORECASE)

        verse = re.sub("kill", kills[randint(0, len(kills) - 1)],
                       verse)
        verse = re.sub("Kill", kills[randint(0, len(kills) - 1)].capitalize(),
                       verse)
        status = True
    return verse, status


def fuck():
    sussy_verse, status = make_sussy(get_verse())
    while not status:
        sussy_verse, status = make_sussy(get_verse())

        # Check if verse fits the tweet length
        sussy_len = len(sussy_verse)
        if status and sussy_len <= 280:
            break
    api.update_status(sussy_verse)


if __name__ == "__main__":
    try:
        api.verify_credentials()
        while True:
            fuck()
            time.sleep(3600)
    except tweepy.errors.Unauthorized as e:
        print(f"Auth Failed: {e}")
