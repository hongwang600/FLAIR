import random
import string
import json

data_list = []

def replace_spaces_with_random_letters(s):
    flag = 0
    for i in range(len(s)):
        if s[i] == " ":
            random_letters = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            _s_ = s[:i] + random_letters + s[i+1:]
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