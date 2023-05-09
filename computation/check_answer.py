import json
import random
from tabnanny import check

LEN_STR = 30
N_SAMPLES = 100

# answer is a list containing N_SAMPLES strings
def check_ans(answer, file="counting.json"):
    correct_cnt = 0
    idx_wrong_answers = []
    with open('counting.json', 'r') as file:
        data = json.load(file)
        for i in range(N_SAMPLES):
            if int(answer[i]) * 0.9 < data[i]['answer'] and int(answer[i]) * 1.1 > data[i]['answer']:
                correct_cnt += 1
            else:
                idx_wrong_answers.append(i)

    return correct_cnt, idx_wrong_answers
