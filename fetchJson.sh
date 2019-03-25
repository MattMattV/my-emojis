#!/bin/bash

ENDPOINT="https://slack.com/api/emoji.list?token="

echo "Feed me with Slack token please"
read -r SLACK_TOKEN

echo "Fetching emojis list"

curl -o dev-tsi-emojis.json "$ENDPOINT$SLACK_TOKEN"

echo "Downloading emojis..."

bash ./downloadEmojis.sh dev-tsi-emojis.json