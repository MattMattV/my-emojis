import os
from os.path import basename

table  = "| Preview | shortcode |\n"
table += "|---------|-----------|\n"

emojis = sorted(os.listdir(f"{os.getcwd()}/output"), key=os.path.realpath)

for emoji in emojis:
    name = basename(emoji).split(".")[0]
    table += f"| ![{name}](./output/{emoji}) | `{name}` |\n"

with open(f"{os.getcwd()}/PREVIEW.md", "w") as file:
    file.write(table)