from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException
import yaml

class WatsonServices:
    '''
    Makes API calls to Watson Tone Analyzer and Speech-to-Text services. 
    '''

    def __init__(self, audio):
        self.yml = self._get_configs()
        self.text = self._speech_to_text(audio)


    def _get_configs(self):
        yml = None
        with open("config.yaml") as stream:
            try:
                yml = yaml.load(stream)
            except yaml.YAMLError as e:
                print e
        return yml

    def _speech_to_text(self, audio):
        #TODO: call Watson STT here
        pass
    
    def get_tone(self):
        tone_analyzer = ToneAnalyzerV3(
                            version=y.get("tone_analyzer").get("version"), 
                            username=y.get("tone_analyzer").get("username"), 
                            password=y.get("tone_analyzer").get("password")
                        )
        mime = 'application/json'
        tone = {}
        try:
            tone = tone_analyzer.tone({"text": text}, mime)
        except WatsonApiException as e:
            print "Method failed with status code " + str(e.code) + ": " + e.message 
        return tone