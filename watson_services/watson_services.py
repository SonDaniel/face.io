from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import WatsonApiException
import yaml
import json

class WatsonServices:
    '''
    Makes API calls to Watson Tone Analyzer and Speech-to-Text services.
    '''

    def __init__(self, audio):
        self.yml = self._get_configs()
        self.stt_client = self._get_stt_client()


    def _get_configs(self):
        yml = None
        with open("config.yaml") as stream:
            try:
                yml = yaml.load(stream)
            except yaml.YAMLError as e:
                print e
        return yml

    def _get_stt_client(self):
        speech_to_text = SpeechToTextV1(
                            url=self.yml.get("speech_to_text").get("endpoint"),
                            username=self.yml.get("speech_to_text").get("username"),
                            password=self.yml.get("speech_to_text").get("password")
                        )
        return speech_to_text

    def convert_stt(self, file_name):
        # Must specify file in same directory or abs. path to file for now
        with open(file_name, 'rb') as audio_file:
            print(
                json.dumps(
                    self.stt_client.recognize(
                        audio=audio_file,
                        # must change to audio/format_type or throws error
                        content_type='audio/flac',
                        timestamps=True,
                        word_confidence=True),
        indent=2))

    def get_tone(self):
        tone_analyzer = ToneAnalyzerV3(
                            version=self.yaml.get("tone_analyzer").get("version"),
                            username=self.yaml.get("tone_analyzer").get("username"),
                            password=self.yaml.get("tone_analyzer").get("password")
                        )
        mime = 'application/json'
        tone = {}
        try:
            tone = tone_analyzer.tone({"text": text}, mime)
        except WatsonApiException as e:
            print "Method failed with status code " + str(e.code) + ": " + e.message
        return tone
