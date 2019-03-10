"""docstring"""
def add(vocabulary, word):
    """Adding"""
    if word[1] in vocabulary.keys():
        if word[2] not in vocabulary[word[1]]:
            vocabulary[word[1]].append(word[2])
        if word[2] in vocabulary.keys():
            if word[1] not in vocabulary[word[2]]:
                vocabulary[word[2]].append(word[1])
        else:
            vocabulary[word[2]] = [word[1]]
    elif word[2] in vocabulary.keys():
        if word[1] not in vocabulary[word[2]]:
            vocabulary[word[2]].append(word[1])
        if word[1] in vocabulary.keys():
            if word[2] not in vocabulary[word[1]]:
                vocabulary[word[1]].append(word[2])
        else:
            vocabulary[word[1]] = [word[2]]
    else:
        vocabulary[word[1]] = [word[2]]
        vocabulary[word[2]] = [word[1]]
    return vocabulary

def count(vocabulary, word):
    """Counting"""
    if word[1] in vocabulary.keys():
        return len(vocabulary[word[1]])
    return 0

def check(vocabulary, word):
    """Checking"""
    if word[1] in vocabulary.keys() and word[2] in vocabulary[word[1]]:
        answer = "Yes"
    else:
        answer = "No"
    return answer

ALLWORDS = dict()
print('Работаем сколько вводов?')
for i in range(0, int(input())):
    com = input()
    words = com.split()
    if  words[0] == "add":
        add(ALLWORDS, words)
    elif words[0] == "count":
        print(count(ALLWORDS, words))
    elif words[0] == "check":
        print(check(ALLWORDS, words))
