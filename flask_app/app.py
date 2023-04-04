from flask import Flask
import psycopg2
import pandas as pd
import random
import os
import time

app = Flask(__name__)


def generate_insult():
    adjectives = [
        "abrasive", "annoying", "arrogant", "asinine", "belligerent", "big-headed", "boorish",
        "brainless", "callous", "careless", "clueless", "clumsy", "cocky", "conceited",
        "cowardly", "crass", "cruel", "cynical", "dense", "disrespectful", "dull",
        "egotistical", "foolish", "greedy", "grumpy", "gullible", "hasty", "ignorant",
        "imbecilic", "immature", "impudent", "incompetent", "inept", "insipid", "irritable",
        "lazy", "mean", "narrow-minded", "obnoxious", "overbearing", "petty", "pompous",
        "pretentious", "rude", "selfish", "shallow", "short-sighted", "stupid", "thoughtless"
    ]

    nouns = [
        "airhead", "blockhead", "boor", "buffoon", "bungler", "clod", "cretin", "dimwit",
        "dolt", "dope", "dunce", "fool", "goofball", "halfwit", "idiot", "ignoramus",
        "imbecile", "incompetent", "jerk", "klutz", "knucklehead", "lout", "lummox",
        "moron", "nincompoop", "ninny", "nitwit", "numskull", "oaf", "pinhead", "prat",
        "scatterbrain", "simpleton", "slacker", "slob", "slowpoke", "snob",
        "wastrel", "whiner", "windbag", "witling", "yahoo", "yokel"
    ]

    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    noun = random.choice(nouns)

    insult = f"You are a {adjective1}, {adjective2} {noun}!"
    return insult


@app.route('/')
def insult():
    message = generate_insult()
    return message


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
