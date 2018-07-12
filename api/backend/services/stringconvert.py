import json
def convert(d):
  d = json.loads(d)
  entirestring = ''
  for result in d.get('results'): 
    for entry in result.get("alternatives"):
      entirestring += entry.get("transcript")
  
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
  print finalarr     
  return finalarr

        
    

