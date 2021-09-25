import json

FILE_PATH = './example.json'

with open(FILE_PATH) as f:
    result = json.load(f)

correct = 0
total = len(result['choosepicture'])
for img in result['choosepicture']:
    res = img.split('-')[-1]
    if res == '1':
        correct += 1 

print("Success rate is ", round(100.0 - (correct / total * 100.0), 2), "%.")