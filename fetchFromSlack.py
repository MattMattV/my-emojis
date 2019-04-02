#!/usr/bin/env python3

from json import loads
from os.path import basename
from pathlib import Path
from pprint import pprint
from typing import Dict

import os
import shutil

import requests


def requestEmojis() -> str:
    userProvidedToken = input("Feed me with a slack token please : ")

    if userProvidedToken == "":
        print("No token provided")
        exit(1)

    response = requests.get(
        "https://slack.com/api/emoji.list", {"token": userProvidedToken}
    )

    if response.status_code != 200:
        print("Something went wrong with Slack")
        print(f"Slack API replied with {response.status_code}")
        exit(2)

    return response.text


def getEmojisToDownload(rawJson: str) -> Dict[str, str]:
    loadedJson = loads(rawJson)

    if "emoji" not in loadedJson:
        print("Invalid response")
        exit(3)

    return {
        k: v for k, v in loadedJson.get("emoji").items() if not v.startswith("alias:")
    }


def store(emojis: Dict[str, str]) -> None:
    for name, url in emojis.items():
        extension = basename(url).split(".")[1]

        if not Path(f"{os.getcwd()}/output/{name}.{extension}").exists():
            response = requests.get(url, stream=True)

            if response.status_code != 200:
                print(f"Something went wrong while downloading {name}")
                continue

            with open(f"./output/{name}.{extension}", "wb") as emojiFile:
                emojiFile.write(response.content)

            print(f"Downloaded {name}")
        else:
            print(f"File already exists for {name}")


if __name__ == "__main__":
    emojis = getEmojisToDownload(requestEmojis())

    store(emojis)
