import random
import json
from scipy.special import comb

def check_unique(lst):
    return len(lst) == len(set(lst))

# if s1 is a non-contiguous substring of s2
def is_subsequence(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s1)


# check the result of a single question.
def check_rand_insert(answers, target_str, target_char, k):
    if check_unique(answers):
        flag = True
        for answer in answers:
            target_0 = target_str.count('0')
            target_1 = target_str.count('1')
            ans_0 = answer.count('0')
            ans_1 = answer.count('1')

            if target_char == '0':
                if not (ans_0 == target_0 + k and ans_1 == target_1 and is_subsequence(target_str, answer)):
                    flag = False
            if target_char == '1':
                if not (ans_1 == target_1 + k and ans_0 == target_0 and is_subsequence(target_str, answer)):
                    flag = False

        if flag == True:
            return True
        else:
            return False
    else:
        return False

# example
print(check_rand_insert(['1000100', '0100100', '0010010'], '00000', '1', 2))