import sys
import re

import moviepy.editor as mp
video_input = sys.argv[1]
clip = mp.VideoFileClip(video_input)
audio_output = re.sub('\.mov$', '',video_input)
clip.audio.write_audiofile(audio_output+'.mp3')