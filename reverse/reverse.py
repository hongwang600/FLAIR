import random
import string
import json

N_SAMPLES = 100

data_list = []

# open the file of random words
with open('rand_words.txt', 'r') as f:
    words_list = [line.strip().lower() for line in f]

for _ in range(N_SAMPLES):
    rand_word = random.sample(words_list, 1)[0]
    question = "Please reverse the word " + rand_word + '.'
    data_list.append({"question": str(question), "answer": rand_word[::-1]})

with open("reverse.json", "w") as f:
    json.dump(data_list, f)