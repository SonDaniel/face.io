
import sys
import re
import moviepy.editor as mp

def get_audio(video_input):
    clip = mp.VideoFileClip(video_input)
    audio_output = re.sub('\.mp4$', '',video_input)
    clip.audio.write_audiofile(audio_output+'.wav')
    audio = None
    # TODO: don't do this; return the object before saving to local disk
    with open(audio_output + ".wav", "r") as f:
        audio = f.read()
    return audio
