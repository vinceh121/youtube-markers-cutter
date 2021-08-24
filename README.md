# youtube-markers-cutter
Small script that cuts your video following Youtube markers

## How do I use it?

```shell
$ pip install requests
$ git clone https://github.com/vinceh121/youtube-markers-cutter && cd youtube-markers-cutter
$ youtube-dl https://www.youtube.com/watch\?v\=pvkTC2xIbeY
$ ls
cut-markers.py
'How to Add Chapters to YouTube Videos _ Chapters Explained-pvkTC2xIbeY.mp4'
$ ./cut-markers.py -u https://www.youtube.com/watch\?v\=pvkTC2xIbeY -v 'How to Add Chapters to YouTube Videos _ Chapters Explained-pvkTC2xIbeY.mp4'
$ ls
Are_chapters_available_in_my_country_.mp4
'How to Add Chapters to YouTube Videos _ Chapters Explained-pvkTC2xIbeY.mp4'
When_are_changes_updated_.mp4
cut-markers.py
How_to_disable_chapters_.mp4
YouTube_Chapters.mp4
How_to_add_chapter_markers_.mp4
Intro.mp4
What_are_YouTube_chapters_.mp4
```

## How does it work?

First this script will fetch the webpage of the Youtube video in order to get the `ytInitialData` object which contains marker data. This object is then parsed and FFMPEG commands are generated to cut the source video according to the timing of the markers.
