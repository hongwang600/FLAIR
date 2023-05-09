# FLAIR

This repository contains the datasets and evaluation framework for the paper "Bot or Human? Detecting ChatGPT Imposters with A Single Question". The paper proposes a new framework named FLAIR (Finding Large Language Model Authenticity via a Single Inquiry and Response) to detect conversational bots in an online manner. The approach aims to differentiate human users from bots using single-question scenarios.

## Datasets

The questions are divided into two categories:

* Questions that are easy for humans but difficult for bots (e.g., counting, substitution, positioning, noise filtering, and ASCII art)
* Questions that are easy for bots but difficult for humans (e.g., memorization and computation)

Below are the description for each FLAIR question:

1. Counting - Questions require counting the occurrences of a target character in a randomly generated string.
2. Substitution - Questions require deciphering a string where each character is substituted with another character based on a substitution table.
3. Positioning - Questions require finding the k-th character after the j-th appearance of a character c in a randomly generated string.
4. Random Editing - Questions require performing drop, insert, swap, and substitute operations on a random string and providing three different outputs.
5. Noise Injection - Questions are common sense questions with added noise by appending uppercase letters to words within the question.
6. ASCII Art - Questions present an ASCII art and require providing the corresponding label as the answer.
7. Memorization - Questions require enumerating items within a category or answering domain-specific questions that are difficult for humans to recall.
8. Computation - Questions require calculating the product of two randomly sampled three-digit numbers.

## Evaluation
![Image text](https://github.com/hongwang600/FLAIR/edit/main/results.png)

## Implementation Details
### 1. Counting
1. Sample a candidate character set from the entire alphabet

## Contributing

We welcome contributions to expand the dataset and improve the detection of conversational bots. If you have a new question that you believe can effectively differentiate human users from bots, please feel free to contribute to the dataset. 
