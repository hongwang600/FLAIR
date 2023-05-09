import random
import string
import json

data_list = []

# open the file of random words
with open('rand_words.txt', 'r') as f:
    words_list = [line.strip().upper() for line in f]
    
data_list = []
def replace_spaces_with_random_letters(s):
    flag = 0
    for i in range(len(s)):
        if s[i] == " ":
            rand_word = random.sample(words_list, 1)[0]
            _s_ = s[:i] + rand_word+ "-" + s[i+1:]
            flag = 1
            break
        
    if flag == 1:
        return _s_
    else:
        return None
    
def noise_inject(s):
    while True:
        s = replace_spaces_with_random_letters(s)
        if s == None:
            break
        _s_ = s
    return _s_
   

# open the file of questions
with open('questions.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    
for line in lines:
    parts = line.split('?')
    original_question = parts[0]+"?"
    answer = parts[1][:-1]
    question = noise_inject(original_question)

    data_list.append({"question": str(question), "answer": str(answer)})

with open("noise_injection.json", "w") as f:
    json.dump(data_list, f)