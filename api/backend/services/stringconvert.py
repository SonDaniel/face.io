import json
import os

def save_to_disk(text, filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + "/" + filename
    with open(path, "w") as f:
        f.write(text)

def convert(d):
    text = parse(d)
    return segment(text)

def parse(d):
    d = json.loads(d)
    entirestring = ''
    transcript = []
    for result in d.get('results'): 
        for entry in result.get("alternatives"):
            entirestring += entry.get("transcript")
            transcript.append(entry.get("transcript"))
    save_to_disk(". ".join(transcript), "stt_text.txt")
    return entirestring

def segment(entirestring):
    arr = entirestring.lower().split("next question")
    finalarr = []
    for sentence in arr:
        temp = ''
        words = sentence.split()
        for w in words :
            if w == 'ibm' or w == 'yourself' or w == 'strengths' or w == 'job' :
                temp += w
                qa = {}
                qa['question'] = temp
                temp = ''
            else :
                temp += w + " "
        qa['answer'] = temp
        finalarr.append(qa)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + "/" + 'stt_text.json'
    with open(path, 'w') as f:
        json.dump({"response": finalarr}, f)
    return finalarr

        
    

