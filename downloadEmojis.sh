#!/bin/bash

mkdir -p output;

jq -r '.[] | "curl -s -o \"output/\(.name)\(.extension)\" \"\(.url)\""' "$1" |
while read -r line; do eval "$line"; done