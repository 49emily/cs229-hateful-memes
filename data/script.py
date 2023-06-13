import json
import shutil
from PIL import Image

def generateData(type):
    file =  open(type + '/metadata.jsonl', "w")
    for line in open("data/" + type + ".jsonl", 'r', encoding='utf-8'):
        obj = json.loads(line)
        img_num = str(obj['id']).zfill(5)
        obj['file_name'] = img_num + ".jpg"
        file.write(json.dumps(obj) + "\n")
        im = Image.open("data/img/" + img_num + ".png")
        rgb_im = im.convert('RGB')
        rgb_im.save(type + "/" + img_num + ".jpg")

generateData("train")
generateData("dev")
# generateData("test")

# trainFile = open("train.jsonl", "w")
# for line in open('data/train.jsonl', 'r', encoding='utf-8'):
#     obj = json.loads(line)
#     obj['file_name'] = str(obj['id']) + ".png"
#     trainFile.write(json.dumps(obj) + "\n")


# devFile = open("dev.jsonl", "w")
# for line in open('data/dev.jsonl', 'r', encoding='utf-8'):
#     obj = json.loads(line)
#     obj['file_name'] = str(obj['id']) + ".png"
#     devFile.write(json.dumps(obj) + "\n")

# testFile = open("test.jsonl", "w")
# for line in open('data/test.jsonl', 'r', encoding='utf-8'):
#     obj = json.loads(line)
#     obj['file_name'] = str(obj['id']) + ".png"
#     testFile.write(json.dumps(obj) + "\n")

# f = open("data/dev.jsonl")
# dev = json.load(f)

# dev['file_name'] = dev['id']

# with open("dev.json", "w") as outfile:
#     json.dump(dev, outfile)


# f = open("data/test.jsonl")
# test = json.load(f)

# test['file_name'] = test['id']

# with open("test.json", "w") as outfile:
#     json.dump(test, outfile)
