# FLAIR

This repository contains the datasets and evaluation framework for the paper "[Bot or Human? Detecting ChatGPT Imposters with A Single Question](https://arxiv.org/abs/2305.06424)". The paper proposes a new framework named FLAIR (Finding Large Language Model Authenticity via a Single Inquiry and Response) to detect conversational bots in an online manner. The approach aims to differentiate human users from bots using single-question scenarios.

## Datasets

The questions are divided into two categories:

* Questions that are easy for humans but difficult for bots (e.g., counting, substitution, positioning, noise filtering, and ASCII art)
* Questions that are easy for bots but difficult for humans (e.g., memorization and computation)

Below are the description for each FLAIR question:

1. Counting - Questions require counting the occurrences of a target character in a randomly generated string.
2. Reverse - Questions require reversing the characters of a random word with consecutive double or triple letters.
3. Substitution - Questions require deciphering a string where each character is substituted with another character based on a substitution table.
4. Positioning - Questions require finding the k-th character after the j-th appearance of a character c in a randomly generated string.
5. Random Editing - Questions require performing drop, insert, swap, and substitute operations on a random string and providing three different outputs.
6. Noise Injection - Questions are common sense questions with added noise by appending uppercase letters to words within the question.
7. ASCII Art - Questions present an ASCII art and require providing the corresponding label as the answer.
8. Memorization - Questions require enumerating items within a category or answering domain-specific questions that are difficult for humans to recall.
9. Computation - Questions require calculating the product of two randomly sampled four-digit numbers.

## Evaluation
![Image text](https://github.com/hongwang600/FLAIR/blob/main/exp.png)

## Implementation Details
We choosed ten users for our user study.
### 1. Counting
1. To conduct this experiment, we will first generate a candidate character set by randomly sampling 3 to 5 letters from the entire alphabet.
2. Using the generated character set, we will create a random string by sampling k times, where k is set to 30 for this experiment.
3. Next, we will randomly select a character from the generated string and ask users to count the number of times it appears.
4. Each participant is allocated with 10 counting questions. Answers should match the results exactly.

### 2. Reverse
1. We randomly choose 100 different english words with consecutive double or triple letters. The words are from dictionaries and this [document](https://digitalcommons.butler.edu/cgi/viewcontent.cgi?article=5741&context=wordways).
2. The letters of the words are reversed to create the dataset.
3. Each participant is allocated with 10 Reverse questions. Answers should match the results exactly.

### 3. Substitution
1. We randomly choose 100 different english words as the original strings. 
2. Then, we designed a random substitution rule to substitute characters within the words.
3. Given the words and different substitution rules, participants should perform substitution and output the correct results.
4. To standardize the experiment, each user will be allocated 10 substitution questions. Answers should match the results exactly.

### 4. Positioning
1. For our experiment, we will start by generating a candidate character set by randomly sampling 6 to 10 letters from the entire alphabet.
2. Using the generated character set, we will create a random string by sampling k times, where k is set to 30 for this experiment.
3. Next, we will randomly select a character from the generated string. Users should find the k-th character after the j-th occurence of the selected character.
4. Each participant is allocated with 10 positioning questions. Answers should match the results exactly.

### 5. Random Edit
1. For the first category of questions, we will randomly drop k zeros or ones from a sequence of 20 bits.
2. For the second category of questions, we will randomly add k zeros or ones to a sequence of 20 bits.
3. In the third category, we will randomly substitute k zeros with ones or k ones with zeros in a sequence of 20 bits.
4. The fourth category of questions will involve randomly swapping zeros and ones k times in a sequence of 20 bits.
5. Each participant is allocated 10 random edit questions from 2 categories. Answers should pass our answer checker.

### 6. Noise Injection
1. To design our experiment, we first collected a set of 100 common sense questions along with their corresponding answers. Additionally, we generated a set of 400 random words to serve as noise.
2. In order to inject noise into the common sense questions, we replaced the spaces within the questions with uppercase random words.
3. Users will be presented with the noisy questions and are required to remove the random words and answer the questions correctly.
4. Each participant is allocated 10 noise injection questions from 2 categories. It is important to note that all answers that make sense will be considered correct.

### 7. ASCII arts
1. To conduct our experiment, we first collected a set of 50 ASCII arts from https://www.asciiart.eu/
2. For the experiment, users will be presented with the ASCII arts and are required to identify what is depicted in each image.
3. Each participant is allocated 5 ASCII questions. It is important to note that all answers that make sense will be considered correct.

### 8. Memorization
1. We have collected 100 questions from various professional fields, including both numerical and knowledge-based questions. 
2. For numerical questions, users are required to provide an answer with an error margin of no more than 5%. 
3. For knowledge-based questions, users must provide accurate answers.
4. Each participant is allocated 10 random memorization questions.

### 9. Computation
1. Users are required to complete a multiplication question involving two randomly generated four-digit numbers within a time limit of 10 seconds. 
2. Any answers submitted after the time limit will be marked as incorrect.
3. In order for the answer to be considered correct, the margin of error must be within 5%.

## Contributing

We welcome contributions to expand the dataset and improve the detection of conversational bots. If you have a new question that you believe can effectively differentiate human users from bots, please feel free to contribute to the dataset via submitting a pull request to this repo. 

## Citation
Please cite our paper if you find this repository helpful in your research or you use our data:
```
@article{FLAIR,
  title={Bot or Human? Detecting ChatGPT Imposters with A Single Question},
  author={Wang, Hong and Luo, Xuan and Wang, Weizhi and Yan, Xifeng},
  journal={arXiv preprint arXiv:2305.06424},
  year={2023}
}
```
