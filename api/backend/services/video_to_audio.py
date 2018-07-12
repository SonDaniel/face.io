
import sys
import re
import moviepy.editor as mp

def open_file(filename):
    file = None
    with open(filename, "r") as f:
        file = f.read()
    return file


def get_audio(video_input):
    clip = mp.VideoFileClip(video_input)
    audio_output = re.sub('\.mp4$', '',video_input)
    audio = open_file(audio_output + ".wav")
    if not audio:
        clip.audio.write_audiofile(audio_output+'.wav')
    return open_file(audio_output + ".wav")
