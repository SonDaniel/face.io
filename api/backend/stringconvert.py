import json

# class stringconvert() :
result =  '''{
    "results": [
        {
        "alternatives": [
            {
            "word_confidence": [
                [
                "several", 
                1.0
                ], 
                [
                "tornadoes", 
                1.0
                ], 
                [
                "touch", 
                0.515
                ], 
                [
                "down", 
                0.916
                ], 
                [
                "as", 
                0.314
                ], 
                [
                "a", 
                0.539
                ], 
                [
                "line", 
                1.0
                ], 
                [
                "of", 
                1.0
                ], 
                [
                "severe", 
                1.0
                ], 
                [
                "thunderstorms", 
                0.758
                ], 
                [
                "swept", 
                1.0
                ], 
                [
                "through", 
                1.0
                ], 
                [
                "Colorado", 
                0.989
                ], 
                [
                "on", 
                0.369
                ], 
                [
                "Sunday", 
                0.978
                ]
            ], 
            "confidence": 0.889, 
            "transcript": "Hi I'm Matt and I will be interviewing you Tell me about yourself I go to Berkeley Next question What are your strengths", 
            "timestamps": [
                [
                "several", 
                1.0, 
                1.52
                ], 
                [
                "tornadoes", 
                1.52, 
                2.15
                ], 
                [
                "touch", 
                2.15, 
                2.49
                ], 
                [
                "down", 
                2.49, 
                2.82
                ], 
                [
                "as", 
                2.82, 
                2.92
                ], 
                [
                "a", 
                2.92, 
                3.01
                ], 
                [
                "line", 
                3.01, 
                3.3
                ], 
                [
                "of", 
                3.3, 
                3.39
                ], 
                [
                "severe", 
                3.39, 
                3.77
                ], 
                [
                "thunderstorms", 
                3.77, 
                4.51
                ], 
                [
                "swept", 
                4.51, 
                4.79
                ], 
                [
                "through", 
                4.79, 
                4.95
                ], 
                [
                "Colorado", 
                4.95, 
                5.59
                ], 
                [
                "on", 
                5.59, 
                5.73
                ], 
                [
                "Sunday", 
                5.73, 
                6.35
                ]
            ]
            }
        ], 
        "final": 50
        }
    ], 
    "result_index": 0
    }
    '''

data = json.loads(result)

def convert(d) :
    entirestring = ''


    for x in d['results']: 
        for y in x['alternatives']:
            entirestring = y["transcript"]
    return entirestring.lower().split("next question")

print convert(data)

        
    

