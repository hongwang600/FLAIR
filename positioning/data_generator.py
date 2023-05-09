import random
import string
import json
import re

LEN_STR = 30
N_SAMPLES = 100


char_list = string.ascii_lowercase
data_list = []


for _ in range(N_SAMPLES):
    # random string generation
    num_chars = random.randint(3, 5)
    target_chars = random.sample(char_list, num_chars)
    # To allow the randomness of k, the last two chars should not be the pivot char
    target_str = ''.join(random.choices(target_chars, k=LEN_STR-2))
    pivot_char = random.sample(target_chars, 1)[0]
    target_chars.remove(pivot_char)
    suffix_str = ''.join(random.choices(target_chars, k=2))
    target_str = target_str + suffix_str

    # locate the j-th pivot char
    cnt_pivot_char = target_str.count(pivot_char)
    th_pivot_char = random.randint(1, cnt_pivot_char)
    regex = r'(.*?{x}){{{k}}}'.format(x=pivot_char, k=th_pivot_char)
    match = re.search(regex, target_str)
    pos_th_pivot_char = match.end(1) - 1

    # locate the k-th char after the j-th pivor char
    chars_left = LEN_STR - pos_th_pivot_char - 1
    th_final_char = random.randint(1, chars_left)
    final_char = target_str[pos_th_pivot_char + th_final_char]

    question = "What is the " + str(th_final_char)+ "-th character after the " + str(th_pivot_char) + "-th apperance of the character " + pivot_char + " in the string " + target_str + "?"
    answer = final_char
    
    data_list.append({"question": str(question), "answer": str(answer)})

with open("positioning.json", "w") as f:
    json.dump(data_list, f)