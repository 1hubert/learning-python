import os

import mutagen
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TDRC, TRCK, APIC

# ID3 info:
# APIC: picture
# TIT2: title
# TPE1: artist
# TRCK: track number
# TALB: album
# TDRC: year


os.chdir('2011.10.16 [TDDC-0010] Labradrite [M3-28] [YT MP3]')

nr_of_tracks = int(input('How many tracks there is in this album: '))
album_name = str(input('Album name: '))
artist = str(input('Artist: '))
year = str(input('Year: '))

for i in range(1, nr_of_tracks+1):
    for file in os.listdir(os.getcwd()):
        if i < 10:
            if file.startswith(f'0{i}'):
                full_track_filename = file
        else:
            if file.startswith(f'{i}'):
                full_track_filename = file

    # adding tags
    print("Adding tags and cover to " + full_track_filename)
    try:
        tags = ID3(os.getcwd() + "\\" + full_track_filename)
    except mutagen.id3.ID3NoHeaderError:
        tags = ID3()

    # those tags are different in each iteration    
    tags["TRCK"] = TRCK(encoding=3, text=str(i))

    title = full_track_filename.split(' - ')[1].strip('.mp3').strip('.flac')
    tags["TIT2"] = TIT2(encoding=3, text=title)

    # those tags are constant
    tags["TALB"] = TALB(encoding=3, text=album_name)
    tags["TPE1"] = TPE1(encoding=3, text=artist)
    tags["TDRC"] = TDRC(encoding=3, text=year)

    pic_file = os.getcwd() + "\\" + "folder.jpg"
    imagedata = open(pic_file, 'rb').read()
    tags["APIC"] = APIC(3, 'image/jpeg', 3, 'Cover', imagedata)

    # saving tags
    tags.save(os.getcwd() + "\\" + full_track_filename, v2_version=3)
