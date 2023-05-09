import random
import json

LEN_STR = 20
N_SAMPLES = 25
OPERATIONS = 2
CANDIDATES = 3

data_list = []
for _ in range(N_SAMPLES):
    # random string generation
    len_str = LEN_STR
    target_str = ''.join(random.choices(['0','1'], k=LEN_STR))  
    target_char = random.sample(['0','1'], k=1)[0]
    

    question = "Randomly insert " + str(OPERATIONS) + " \'" + target_char + "\'" + " to the string: " + target_str + ". Give me " + str(CANDIDATES) + " different results."
    data_list.append({"question": str(question)})

with open("random_insert.json", "w") as f:
    json.dump(data_list, f)