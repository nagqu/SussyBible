from dotenv import dotenv_values
from random import randint
import tweepy
import requests
import re

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


def tests():
    if get_verse() is not None:
        print("Get OK")
    else:
        print("Get Not OK")
    _, statusTrue = make_sussy(
        "Deuteronomy 11:29 When the Lord your God brings you into the land you are to Kill, you must kill the blessing on Mount Gerizim and the curse on Mount Ebal.")
    if statusTrue:
        print("Regex True OK", _)
    else:
        print("Regex True Not OK")
    _, statusFalse = make_sussy(
        "Isaiah 32:20 you will be blessed,you who plant seed by all the banks of the streams, you who let your ox and donkey graze.")
    if statusFalse:
        print("Regex Not OK False")
    else:
        print("Regex False OK")


def get_verse():
    verse = requests.get('https://labs.bible.org/api/?passage=random')
    text = verse.text
    text = text.replace("<b>", "").replace("</b> ", " ")
    # print(text)
    return text


def make_sussy(verse):
    # verse = None
    status = False
    if re.search("the lord|jesus|god|messiah|father|kill|escape|judas", verse, flags=re.IGNORECASE):
        print("Regex Triggered")
        verse = re.sub("the lord|jesus|god|messiah",
                       impostors[randint(0, len(impostors) - 1)], verse, flags=re.IGNORECASE)
        verse = re.sub(
            "Father", impostors[randint(0, len(impostors) - 1)], verse)
        verse = re.sub(
            "Lord", impostors[randint(0, len(impostors) - 1)], verse)
        verse = re.sub("escape", escapes[randint(
            0, len(escapes) - 1)], verse, flags=re.IGNORECASE)
        verse = re.sub("kill", kills[randint(0, len(kills) - 1)],
                       verse)
        verse = re.sub("Kill", kills[randint(0, len(kills) - 1)].capitalize(),
                       verse)
        verse = re.sub("Judas", "Sussy Baka", verse)
        status = True
    # print(verse, status)
    return verse, status


def fuck():
    sussy_verse, status = make_sussy(get_verse())
    while not status:
        sussy_verse, status = make_sussy(get_verse())
        # print(sussy_verse, status)
        if status:
            break
    api.update_status(sussy_verse)
    # print(sussy_verse, status)


if __name__ == "__main__":
    try:
        api.verify_credentials()
        print("Auth Good")
        fuck()
    except:
        print("Auth Failed")
