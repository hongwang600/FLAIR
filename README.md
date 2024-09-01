# FLAIR: Finding Large Language Model Authenticity via a Single Inquiry and Response

Paper: [Bot or Human? Detecting ChatGPT Imposters with A Single Question](https://arxiv.org/abs/2305.06424)

Large language models (LLMs) like GPT-4 have demonstrated remarkable capabilities in natural language understanding and generation. However, these models can be misused for malicious purposes, such as fraud or denial-of-service attacks. Our project, FLAIR (Finding Large Language Model Authenticity via a Single Inquiry and Response), aims to detect whether the party involved in a conversation is a bot or a human using a single question approach.

## Datasets

To evaluate the performance of both LLMs and humans, we constructed a dataset for each category of questions.

### Counting

In the Counting dataset, we used the entire alphabet to generate tasks. Each task involved randomly picking one letter as the target and determining how many times it appeared in a string of 30 characters. The string was constructed to include between 10 and 20 occurrences of the target letter, with the remaining characters selected randomly from the alphabet.

### Substitution

For the Substitution dataset, we began by collecting the top 1500 nouns from the [Talk English website](https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx). We filtered these words to include only those with a length between 5 and 10 characters and then randomly generated 100 pairs of words, each with a corresponding substitution map to transform one word into another. The dataset was curated to ensure valid mappings, and participants were tasked with applying the substitution rule to the original word to produce the correct answer.

### Random Editing

The Random Editing dataset evaluates the model's ability to perform four distinct operations: drop, insert, swap, and substitute. We generated random binary strings of length 20 and applied a specified random operation on each string. Participants were asked to produce three different outputs after performing the operation.

### Searching

In the Searching dataset, we generated 100 random 7x7 grids containing spaces and $\blacksquare$s. We used the Depth-First Search (DFS) algorithm to determine the number of islands in each grid, which served as the ground truth. The participants' task was to identify the correct number of islands.

### ASCII Art Reasoning

In the ASCII Art Reasoning dataset, we used GPT-4 to generate a list of items, which were then converted into ASCII art using an ASCII gradient of '@%\#*+=-:.'. The tasks included selecting ASCII arts containing a specific entity, rotating the ASCII art to the correct orientation, and identifying a cropped portion from the original ASCII art.

**Note**: The ASCII art image data is too large to be included in this repository. Please download it from [Google Drive](https://drive.google.com/file/d/1acLoe-2od8xVFsHOj2fiKipDGH8k3Htj/view?usp=sharing).

### Memorization

The Memorization dataset includes questions that require good memorization skills. We created two types of questions: enumerating items within a given category and answering domain-specific questions. We manually collected 100 categories and 100 questions that are challenging for humans but easier for LLMs.

### Computation

For the Computation dataset, we generated tasks involving four-digit multiplication. We randomly sampled 100 pairs of four-digit numbers and calculated their products as the ground truth.

## Cite

```
@inproceedings{
wang2024bot,
title={Bot or Human? Detecting Chat{GPT} Imposters with A Single Question},
author={Hong Wang and Xuan Luo and Weizhi Wang and Melody Yu and Xifeng Yan},
booktitle={First Conference on Language Modeling},
year={2024},
url={https://openreview.net/forum?id=3HTVP34WWE}
}
```

