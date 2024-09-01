import random
import json
from scipy.special import comb

LEN_STR = 20
N_SAMPLES = 25
OPERATIONS = 2
CANDIDATES = 3

data_list = []
for _ in range(N_SAMPLES):
    # random string generation
    while 1:
        target_str = ''.join(random.choices(['0','1'], k=LEN_STR))  
        target_char = random.sample(['0','1'], k=1)[0]
        if target_str.count(target_char) > OPERATIONS:
            possible_results = comb(target_str.count(target_char), OPERATIONS, exact=True)
            if possible_results > CANDIDATES:
                break
    

    question = "Randomly drop " + str(OPERATIONS) + " \'" + target_char + "\'" + " from the string: " + target_str + ". Give me " + str(CANDIDATES) + " different results."
    data_list.append({"question": str(question)})

with open("random_drop.json", "w") as f:
    json.dump(data_list, f)