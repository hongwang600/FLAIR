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

        cnt_0 = target_str.count('0')
        cnt_1 = target_str.count('1')
        if cnt_0 > OPERATIONS and cnt_1 > OPERATIONS:
            possible_results = comb(cnt_0, OPERATIONS, exact=True) * comb(cnt_1, OPERATIONS, exact=True)
            if possible_results > CANDIDATES:
                break


    question = "Randomly swap " + str(OPERATIONS) + " pairs of '0' and '1' in the string: " + target_str + ". Give me " + str(CANDIDATES) + " different results."
    data_list.append({"question": str(question)})

with open("random_swap.json", "w") as f:
    json.dump(data_list, f)