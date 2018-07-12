import sys
import re
import moviepy.editor as mp

def get_audio(video_input):
    clip = mp.VideoFileClip(video_input)
    audio_output = re.sub('\.mov$', '',video_input)
    clip.audio.write_audiofile(audio_output+'.wav')
    return clip
