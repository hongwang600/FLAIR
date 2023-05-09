import random
import string
import json

LEN_STR = 30
N_SAMPLES = 100


char_list = string.ascii_lowercase
data_list = []


for _ in range(N_SAMPLES):
    # random string generation
    x = random.randint(1000, 9999) 
    y = random.randint(1000, 9999) 
    answer = x*y
    question = "What is the result of " + str(x) + " multiplied by " + str(y) + "?"
    data_list.append({"question": str(question), "answer": str(answer)})

with open("computation.json", "w") as f:
    json.dump(data_list, f)