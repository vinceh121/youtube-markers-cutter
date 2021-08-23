# youtube-markers-cutter
Small script that cuts your video following Youtube markers

## How does it work?

First this script will fetch the webpage of the Youtube video in order to get the `ytInitialData` object which contains marker data. This object is then parsed and FFMPEG commands are generated to cut the source video according to the timing of the markers.
