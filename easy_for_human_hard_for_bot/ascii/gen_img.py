from openai import OpenAI
import concurrent.futures
import pandas as pd
import tiktoken
import random
import textwrap
import re
import json
import time
from PIL import Image, ImageEnhance, ImageOps
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np
from transformers import pipeline
import os

# 20 random entities, you can choose any other entities based on your need
entities = ['apple', 'cat', 'dog', 'tree', 'toilet', 'cow', 'pyramid', 'boots', 'rainbow', 'bird', 'lamp', 'trophy', 'rocket', 'telescope', 'chair', 'desk', 'hat', 'globe', 'mug', 'windmill']

class GPT:
    def __init__(self, openai_client):
        self.openai_client = openai_client
        self.total_tokens = 0
        self.cost = 0.0
    
    def num_tokens(self, string: str, encoding_name: str) -> int:
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens

    def gpt(self, prompt, max_tokens, temp, model):
        response = self.openai_client.chat.completions.create(
            model=model,
            messages=prompt,
            temperature=temp,
            max_tokens=max_tokens,
        )
        response = response.choices[0].message.content
        prompt_tokens = self.num_tokens(str(prompt), "cl100k_base")
        response_tokens = self.num_tokens(str(response), "cl100k_base")

        pricing = {
            'gpt-4-0125-preview': {'input': 0.01, 'output': 0.03},
            'gpt-4-1106-preview': {'input': 0.01, 'output': 0.03},
            'gpt-4': {'input': 0.03, 'output': 0.06},
            'gpt-4-32k': {'input': 0.06, 'output': 0.12},
            'gpt-3.5-turbo-0125': {'input': 0.0005, 'output': 0.0015},
            'gpt-3.5-turbo': {'input': 0.0030, 'output': 0.0060},
            'gpt-4o': {'input': 0.005, 'output': 0.015},
        }

        rates = pricing.get(model, {'input': 0.0, 'output': 0.0})

        self.cost += (prompt_tokens * rates['input'] + response_tokens * rates['output']) / 1000
        self.total_tokens += prompt_tokens + response_tokens

        return response

    def convert_to_white_background(self, img):
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            alpha = img.convert('RGBA').split()[-1]
            bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
            bg.paste(img, mask=alpha)
            return bg.convert('RGB')
        else:
            return img

    def dalle(self, prompt, img_size, model):
        pricing = {
            ('dall-e-3', '1024x1024'): 0.040,
            ('dall-e-3', '1024x1792'): 0.080,
            ('dall-e-3', '1792x1024'): 0.080,
            ('dall-e-2', '1024x1024'): 0.020,
            ('dall-e-2', '512x512'): 0.018,
            ('dall-e-2', '256x256'): 0.016,
        }
        cost_per_image = pricing.get((model, img_size), 0.0)
        response = self.openai_client.images.generate(
            model=model,
            prompt=prompt,
            size=img_size,
            n=1,
        )
        print(prompt)
        self.cost += cost_per_image
        return response.data[0].url
    
    def gen_img_sequence(self, random_sequence, img_size, model):
        prompts = []
        for item in random_sequence:
            prompt = [
                {"role": "user", "content": textwrap.dedent(f"""\
                Instruction: Your task is optimize user's input for image generation. 
                Example User Input: Create an image of a single cat on a blank background. The background is completely white, emphasizing the cat's features. The picture is oriented upright.
                Example Output: A single cat sitting on a completely white background. The image is upright, emphasizing the distinct features of the cat. The cat is fluffy with a rich, thick coat, displaying a variety of colors such as ginger, black, and white. Its eyes are large and expressive, colored a deep emerald green. The cat's pose is relaxed, with its tail curled around its paws.
                User Input: Create an image of a single {item} on a blank background. The background is completely white, emphasizing the {item}'s features. The picture is oriented upright.
                Output: 
                """)
                }
            ]
            prompts.append(prompt)

        # optimize the prompt for better generation
        optimized_prompts = []
        with ThreadPoolExecutor(max_workers=4) as executor:
            optimized_prompts = list(executor.map(lambda prompt: self.gpt(prompt, 128, 0.7, 'gpt-4o'), prompts))
    
        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(lambda prompt: self.dalle(prompt, img_size, model), optimized_prompts))

        cleared_images = []
        for result in results:
            pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
            pillow_mask = pipe(result, return_mask = True)
            cleared_images.append(self.convert_to_white_background(pipe(result)))
    
        return cleared_images

    def gen_random_sequence(self, random_pair):
        sequence = [random_pair[0]] + [random_pair[1]] * 3
        random.shuffle(sequence)
        return sequence

    def save_images(self, images, folder_name):
        os.makedirs(folder_name, exist_ok=True)
        filenames = ['A.png', 'B.png', 'C.png', 'D.png']

        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            for image, filename in zip(images, filenames):
                path = os.path.join(folder_name, filename)
                futures.append(executor.submit(self.save_image, image, path))

            for future in as_completed(futures):
                future.result()

    def save_image(self, image, path):
        image.save(path)



openai_client = OpenAI(api_key='your api key')
model = GPT(openai_client)


# generate random images
n_samples = 100

previous_samples = set()  
for i in range(n_samples):
    while True:
        random_pair = tuple(sorted(random.sample(entities, 2))) 
        if random_pair not in previous_samples:
            previous_samples.add(random_pair)
            break  

    random_sequence = model.gen_random_sequence(random_pair)
    print(random_sequence)
    imgs = model.gen_img_sequence(random_sequence, '1024x1024', 'dall-e-3')

    folder = f"ascii_data/{'-'.join(random_pair)}"
    model.save_images(imgs, folder)
    with open(folder+'/obj.json', 'w') as file:
        print(random_sequence)
        json.dump(random_sequence, file, indent=4)
