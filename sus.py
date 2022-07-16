from dotenv import dotenv_values
from random import randint
from requests_oauthlib import OAuth1
import urllib
import time
import requests
import re
import time
import logging

logging.basicConfig(filename="sussybible.log",
                    encoding="utf-8", level=logging.DEBUG)

apiCalls = 0
apiCallsTotal = 0

config = dotenv_values(".env")
oauth_header = OAuth1(config["API_KEY"], config["API_SECRET"],
                      config["ACCESS"], config["ACCESS_SECRET"], signature_type='auth_header')

impostors = ["Amogus", "Yellow", "Red", "Crewmate", "Bean", "Crewpostor"]
kills = ["vote out", "game end", "eject"]
escapes = ["vent"]

# kill -> vote out, game end
# escape -> vent
# Judas -> impostor sus


def get_verse():
    verse = requests.get('https://labs.bible.org/api/?passage=random')
    text = verse.text
    text = re.sub("<b>|</b>", "", text)
    global apiCalls
    apiCalls += 1
    logging.info("Verse got")
    return text


def make_sussy(verse):
    status = False
    # Regex trigger
    if re.search("the lord|jesus|god|messiah|father|kill|escape|judas|christ|among us|true", verse, flags=re.IGNORECASE):
        logging.info(f"Regex triggered on verse: {verse}")
        verse = re.sub("Judas", "Sussy Baka", verse)

        verse = re.sub("the lord|jesus|god|messiah|christ|lord|father",
                       impostors[randint(0, len(impostors) - 1)], verse, flags=re.IGNORECASE)

        verse = re.sub("escape", escapes[randint(
            0, len(escapes) - 1)], verse, flags=re.IGNORECASE)

        verse = re.sub("kill", kills[randint(0, len(kills) - 1)],
                       verse)
        verse = re.sub("Kill", kills[randint(0, len(kills) - 1)].capitalize(),
                       verse)
        verse = re.sub("true", "sus", verse)
        verse = re.sub("True", "Sus", verse)
        verse = re.sub("among us", "among us 👀", verse)
        verse = re.sub("Among us", "Among us 👀", verse)
        status = True
    return verse, status


def post_verse():
    sussy_verse, status = make_sussy(get_verse())
    while not status:
        sussy_verse, status = make_sussy(get_verse())
        # Check if verse fits the tweet length
        sussy_len = len(sussy_verse)
        if status and sussy_len <= 280:
            try:
                verse_enc = urllib.parse.quote(sussy_verse, safe='')
                url = f"https://api.twitter.com/1.1/statuses/update.json?status={verse_enc}"
                _ = requests.post(url, auth=oauth_header)
                break
            except Exception as e:
                logging.warning(f"Exception encountered: {e}")


    global apiCalls
    global apiCallsTotal
    apiCallsTotal += apiCalls

    logging.info("Found verse that fits and is changed")
    logging.info(f"Posted on {time.ctime(time.time())}")
    logging.info(f"Tweet content: {sussy_verse}")
    logging.info(f"Verse API calls until tweet got: {apiCalls}")
    logging.info(
        f"Total verse API calls since script was started: {apiCallsTotal}")
    apiCalls = 0


if __name__ == "__main__":
    post_verse()
    time.sleep(3600)
