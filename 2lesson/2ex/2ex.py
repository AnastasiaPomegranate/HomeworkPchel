"""docstring"""
import json
import os
import bz2
import re
JSON_FOLD = "JsonFolder"
JSON_OUTPUT = "JsonOutput"

def open_archive(tmppath):
    """Unpack archive"""
    names = []
    for name in os.listdir():
        if name[0:2] == "RC":
            names.append(name)
    if not os.path.exists(tmppath):
        os.makedirs(tmppath)
    for name in names:
        with open(tmppath + "/" + name[0:-3], 'wb') as new_file, bz2.BZ2File(name, 'rb') as file:
            for data in file:
                new_file.write(data)

def parse_archive(tmppath):
    """Parse archive"""
    word_vocabulary = {}
    for name in os.listdir(tmppath):
        for line in open(tmppath + "/" + name, "r"):
            data = json.loads(line)
            if data["body"] != "[deleted]":
                for word in re.findall(r"[\w']+", data["body"]):
                    if len(word) >= 4 and word not in word_vocabulary.keys():
                        word_vocabulary[word] = 1
                    elif len(word) >= 4:
                        word_vocabulary[word] += 1
        print(name + "parsed")
    return word_vocabulary

def output(vocabulary, path):
    """Write file out"""
    sorted_list = [(i, vocabulary[i]) for i in sorted(vocabulary.keys(), key=vocabulary.get, reverse=True)]
    vocabulary.clear()
    for i in range(0, 20):
        vocabulary[sorted_list[i][0]] = sorted_list[i][1]
    with open(path, 'w') as outfile:
        return json.dump(vocabulary, outfile, sort_keys=False, indent=4)

open_archive(JSON_FOLD)
output(parse_archive(JSON_FOLD), JSON_OUTPUT)
