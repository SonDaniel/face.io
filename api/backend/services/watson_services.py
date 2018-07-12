from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import WatsonApiException
import video_to_audio
import stringconvert
import os 
import yaml
import json

class WatsonServices:
    '''
    Makes API calls to Watson Tone Analyzer and Speech-to-Text services. 
    '''

    def __init__(self):
        self.yml = self._get_configs()
        self.stt_client = self._get_client("stt")
 
    def _get_configs(self):
        yml = None
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path+"/config.yaml") as stream:
            try:
                yml = yaml.load(stream)
            except yaml.YAMLError as e:
                print e
        return yml
    
    def _get_client(self, client_type):
        if client_type == "stt":
            return SpeechToTextV1(
                            url=self.yml.get("speech_to_text").get("endpoint"),
                            username=self.yml.get("speech_to_text").get("username"),
                            password=self.yml.get("speech_to_text").get("password")
                        )
        else:
            return ToneAnalyzerV3(
                            version=self.yml.get("tone_analyzer").get("version"), 
                            username=self.yml.get("tone_analyzer").get("username"), 
                            password=self.yml.get("tone_analyzer").get("password")
            )

    def convert_stt(self, video_input):
        # Must specify file in same directory or abs. path to file for now
        audio = video_to_audio.get_audio(video_input)
        stt_text = json.dumps(
                    self.stt_client.recognize(
                        audio=audio,
                        # must change to audio/format_type or throws error
                        content_type='audio/wav',
                        timestamps=True,
                        word_confidence=True),
                indent=2)

        print "stt text======================"
        print stt_text
    
        return stringconvert.convert(stt_text)
    
    def get_tone(self, json_data):
        tone_analyzer = self._get_client("tone")
        mime = 'application/json'
        # text = stringconvert.convert(self.convert_stt(video_input))
        text = "I love turtles!"
        tones = {}
        try:
            for line, index in enumerate(text):
                tones[index] = tone_analyzer.tone({"text": line}, mime)
        except WatsonApiException as e:
            print "Method failed with status code " + str(e.code) + ": " + e.message 
        return tones