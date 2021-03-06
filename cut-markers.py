#!/usr/bin/python3

import argparse
import re
import json
import os
import requests as req

def parseTime(t):
    parts = []
    res = re.findall(r"([0-9]{1,2})", t)
    for p in res:
        if len(p) == 1:
            p = "0" + p
        parts.append(p)
    if len(parts) == 2:
        parts.insert(0, "00")
    return ":".join(parts)

cli = argparse.ArgumentParser(description = "cut-markers.py")

cli.add_argument("-u", "--youtube-url", type = str, help = "the URL of the Youtube video")
cli.add_argument("-v", "--video", type = str, help = "the path to the video file")
cli.add_argument("-d", "--download", type = bool, help = "download the video using youtube-dl on the PATH")
cli.add_argument("-f", "--output-format", type = str, help = "the output format (the file extension)")

args = cli.parse_args()
if args.youtube_url == None:
	print("Missing Youtube URL")
	exit()

outFormat = "mp4"
if args.output_format:
    outFormat = args.output_format

videoName = args.video

r = req.get(args.youtube_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"})
search = re.search(r"<script nonce=\"[a-zA-Z0-9]+\">var ytInitialData = {(.+)};<\/script>", r.text)

if not search:
    print("Couldn't find ytInitialData")
    exit()

rawJson = search.group(1)

data = json.loads("{" + rawJson + "}")

for d in data["engagementPanels"]:
    if d["engagementPanelSectionListRenderer"]["targetId"] == "engagement-panel-macro-markers-description-chapters":
        markers = d["engagementPanelSectionListRenderer"]["content"]["macroMarkersListRenderer"]["contents"]

for i in range(0, len(markers)):
    marker = markers[i]["macroMarkersListItemRenderer"]
    if i + 1 != len(markers):
        nextMarker = markers[i + 1]["macroMarkersListItemRenderer"]
        nextTime = parseTime(nextMarker["timeDescription"]["simpleText"])
    else:
        nextTime = "60:59:59"
    startTime = parseTime(marker["timeDescription"]["simpleText"])
    title = marker["title"]["simpleText"]
    fileOut = re.sub(r"[^a-zA-Z0-9]", "_", title) + "." + outFormat
    print("#" + title + " --> " + fileOut)
    cmd = "ffmpeg"
    args = []
    args.append("ffmpeg")
    args.append("-i")
    args.append(videoName)
    args.append("-ss")
    args.append(startTime)
    args.append("-to")
    args.append(nextTime)
    args.append(fileOut)
    print(cmd, args)
    for i in range(0, len(args)):
        args[i] = "\"" + args[i] + "\""
    os.system(" ".join(args))

