from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException
import yaml

class WatsonServices:
    '''
    Makes API calls to Watson Tone Analyzer and Speech-to-Text services. 
    '''

    def __init__(self, audio=None):
        self.yml = self._get_configs()
        self.audio = audio
        self.text = self._speech_to_text()

    def _get_configs(self):
        yml = None
        with open("/Users/biz/ibm_hackathon_env/facial/face.io/api/backend/services/config.yaml") as stream:
            try:
                yml = yaml.load(stream)
            except yaml.YAMLError as e:
                print e
        return yml

    def _speech_to_text(self):
        #TODO: call Watson STT here
    
        # str =  "Please tell my wife I love her very much"
        str = "Go fuck yourself!"
        return str
    
    def get_tone(self):
        tone_analyzer = ToneAnalyzerV3(
                            version=self.yml.get("tone_analyzer").get("version"), 
                            username=self.yml.get("tone_analyzer").get("username"), 
                            password=self.yml.get("tone_analyzer").get("password")
                        )
        mime = 'application/json'
        tone = {}
        try:
            tone = tone_analyzer.tone({"text": self.text}, mime)
            print "-----outputting tone response: "
            print tone
            print "------end of output------"
        except WatsonApiException as e:
            print "Method failed with status code " + str(e.code) + ": " + e.message 
        return tone