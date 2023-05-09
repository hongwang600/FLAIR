import random
import json
from scipy.special import comb

def check_unique(lst):
    return len(lst) == len(set(lst))

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]

# check the result of a single question.
def check_rand_swap(answers, target_str, k):
    if check_unique(answers):
        flag = True
        for answer in answers:
            target_0 = target_str.count('0')
            target_1 = target_str.count('1')
            ans_0 = answer.count('0')
            ans_1 = answer.count('1')
            dis = edit_distance(answer, target_str)
            if not (target_0 == ans_0 and target_1 == ans_1 and dis == 2*k):
                flag = False

        if flag == True:
            return True
        else:
            return False
    else:
        return False

# example
print(check_rand_swap(['110100', '101010', '011001'], '000111', 2))