from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import numpy as np
import random
import json
from collections import Counter

class ImageToAscii:
    def __init__(self, char_set='simple', width=64, height=64, density=1.0):
        self.char_set = char_set
        self.width = width
        self.height = height
        self.density = density
        self.ascii_char_sets = {
            'simple': '@%#*+=-:. ',
            'complex': '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. ',
            'blocks': '█▓▒░ ',
        }

    def preprocess(self, image, brightness=1.0, saturation=1.0, sharpness=1.0, contrast=1.0, hue=0.0):
        """
        Apply preprocessing to the image such as adjusting brightness, saturation, sharpness, contrast, and hue.
        """
        if brightness != 1.0:
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(brightness)
        
        if saturation != 1.0:
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(saturation)
        
        if sharpness != 1.0:
            enhancer = ImageEnhance.Sharpness(image)
            image = enhancer.enhance(sharpness)
        
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast)
        
        if hue != 0.0:
            pass

        return image

    def resize_image(self, image):
        return image.resize((self.width, self.height))

    def adjust_space_density(self, line):
        white_space = ' ' * int(1 / self.density)
        return white_space.join(line)

    def pixels_to_chars(self, image):
        # Convert image to grayscale if it is not already
        if image.mode != 'L':
            image = image.convert('L')
        
        # Convert image to numpy array
        pixels = np.array(image)
        
        # Find the minimum and maximum pixel values
        min_pixel = pixels.min()
        max_pixel = pixels.max()
        
        # Normalize pixels to range [0, 1]
        if min_pixel == max_pixel:
            normalized_pixels = np.zeros_like(pixels, dtype=np.float32)
        else:
            # Normalize pixels to range [0, 1]
            normalized_pixels = (pixels - min_pixel) / (max_pixel - min_pixel)
        
        
        # Map normalized pixels to characters
        char_set = self.ascii_char_sets[self.char_set]
        chars = "".join([char_set[int(pixel * (len(char_set) - 1))] for pixel in normalized_pixels.flatten()])
        
        return chars

    def generate(self, image, brightness=1.0, saturation=1.0, sharpness=1.0, contrast=4.0, hue=0.0):
        image = self.preprocess(image, brightness, saturation, sharpness, contrast, hue)
        image = self.resize_image(image)
        image = image.convert("L")  # Convert to grayscale
        chars = self.pixels_to_chars(image)
        ascii_art = "\n".join([self.adjust_space_density(chars[index:index + self.width]) 
                               for index in range(0, len(chars), self.width)])
        return ascii_art

def ascii_to_square_image(file_path, output_path):
    with open(file_path, 'r') as file:
        lines = [line.rstrip() for line in file]

    char_width = 16 
    char_height = 16 
    img_size = 64 * max(char_width, char_height) 

    image = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("DejaVuSansMono.ttf", 16)  

    y = 0
    for line in lines:
        x = 0
        for char in line:
            draw.text((x, y), char, font=font, fill='black')
            x += char_width
        y += char_height

    image.save(output_path)


root_dir = "./ascii_data"  # Adjust this to your actual directory
target_files = ['A.png', 'B.png', 'C.png', 'D.png']
converter = ImageToAscii(char_set='simple', width=64, height=64, density=4)

for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    if os.path.isdir(subdir_path):
        # mkdir
        select_dir = os.path.join(subdir_path, 'select')
        rotate_dir = os.path.join(subdir_path, 'rotate')
        crop_dir = os.path.join(subdir_path, 'crop')

        os.makedirs(select_dir, exist_ok=True)
        os.makedirs(rotate_dir, exist_ok=True)
        os.makedirs(crop_dir, exist_ok=True)

        # select
        with open(os.path.join(subdir_path, 'obj.json'), 'r') as file:
            obj_json = json.load(file)
        selected_item = random.choice(obj_json)
        positions = ['A', 'B', 'C', 'D']
        qa_dict = {}
        qa_dict['question'] = f'Please select the ascii arts that contain {selected_item}. Output a python list that contains the results like in a alphabetical order without any explanation.\nYour Output: '
        qa_dict['answer'] = [positions[i] for i in range(len(obj_json)) if obj_json[i] == selected_item]

        with open(os.path.join(select_dir, 'qa.json'), 'w') as file:
            json.dump(qa_dict, file, indent=4)

        # rotate
        angles = [random.choice([0, 90, 180, 270]) for _ in range(4)]
        qa_dict = {}
        unique_elements = list(set(obj_json))
        if len(unique_elements) == 2:
            element1, element2 = unique_elements
        else:
            raise ValueError("obj_json does not contain exactly two different elements.")

        qa_dict['question'] = f'Please rotate images of {element1} and {element2} (A, B, C, and D) to their correct orientations. For each image, specify the clockwise rotation angle needed, choosing from 0, 90, 180, or 360 degrees. Output the angles as a Python list without any explanation.\nYour Output: '
        qa_dict['answer'] = angles


        with open(os.path.join(rotate_dir, 'qa.json'), 'w') as file:
            json.dump(qa_dict, file, indent=4)

        # crop
        value_counts = Counter(obj_json)
        different_value = [key for key, count in value_counts.items() if count == 1][0]
        different_index = obj_json.index(different_value)
        index_to_letter = ['A', 'B', 'C', 'D']
        cropped_item = index_to_letter[different_index]

        qa_dict = {}
        qa_dict['question'] = f'Please identify the index of the image that best matches the cropped section. Choose from A, B, C, or D. Output the single index without any additional explanation.\nYour Output: '
        qa_dict['answer'] = cropped_item
        with open(os.path.join(crop_dir, 'qa.json'), 'w') as file:
            json.dump(qa_dict, file, indent=4)


        target_img = Image.open(os.path.join(subdir_path, cropped_item + '.png'))
        width, height = target_img.size
        left = width // 2
        upper = height // 2
        corner_index = random.randint(0, 3)

        new_image = Image.new('RGBA', (width, height))

        if corner_index == 0:  
            top_right_crop = target_img.crop((left, 0, width, upper))
            bottom_left_crop = target_img.crop((0, upper, left, height))
            bottom_right_crop = target_img.crop((left, upper, width, height))
            new_image.paste(top_right_crop, (left, 0))
            new_image.paste(bottom_left_crop, (0, upper))
            new_image.paste(bottom_right_crop, (left, upper))

        elif corner_index == 1:  
            top_left_crop = target_img.crop((0, 0, left, upper))
            bottom_left_crop = target_img.crop((0, upper, left, height))
            bottom_right_crop = target_img.crop((left, upper, width, height))
            new_image.paste(top_left_crop, (0, 0))
            new_image.paste(bottom_left_crop, (0, upper))
            new_image.paste(bottom_right_crop, (left, upper))

        elif corner_index == 2:  
            top_left_crop = target_img.crop((0, 0, left, upper))
            top_right_crop = target_img.crop((left, 0, width, upper))
            bottom_left_crop = target_img.crop((0, upper, left, height))
            new_image.paste(top_left_crop, (0, 0))
            new_image.paste(top_right_crop, (left, 0))
            new_image.paste(bottom_left_crop, (0, upper))

        elif corner_index == 3:  
            top_left_crop = target_img.crop((0, 0, left, upper))
            top_right_crop = target_img.crop((left, 0, width, upper))
            bottom_right_crop = target_img.crop((left, upper, width, height))
            new_image.paste(top_left_crop, (0, 0))
            new_image.paste(top_right_crop, (left, 0))
            new_image.paste(bottom_right_crop, (left, upper))

        txt_path = os.path.join(crop_dir, 'target.txt')
        png_path = os.path.join(crop_dir, 'target.png')

        ascii_txt = converter.generate(new_image)
        with open(txt_path, 'w') as f:
            f.write(ascii_txt)
        ascii_to_square_image(txt_path, png_path)

        for image_file in os.listdir(subdir_path):
            if image_file in target_files:
                i = target_files.index(image_file)
                image_path = os.path.join(subdir_path, image_file)
                ori_image = Image.open(image_path)

                # For select task
                txt_path = os.path.join(select_dir, os.path.splitext(image_file)[0] + '.txt')
                png_path = os.path.join(select_dir, os.path.splitext(image_file)[0] + '_ascii.png')
                ascii_txt = converter.generate(ori_image)
                with open(txt_path, 'w') as f:
                    f.write(ascii_txt)
                ascii_to_square_image(txt_path, png_path)
                

                # For rotate task
                txt_path = os.path.join(rotate_dir, os.path.splitext(image_file)[0] + '.txt')
                png_path = os.path.join(rotate_dir, os.path.splitext(image_file)[0] + '_ascii.png')
                rotated_image = ori_image.rotate(angles[i])
                ascii_txt = converter.generate(rotated_image)
                with open(txt_path, 'w') as f:
                    f.write(ascii_txt)
                ascii_to_square_image(txt_path, png_path)

                # For crop task
                txt_path = os.path.join(crop_dir, os.path.splitext(image_file)[0] + '.txt')
                png_path = os.path.join(crop_dir, os.path.splitext(image_file)[0] + '_ascii.png')
                width, height = ori_image.size
                
                if corner_index == 0:  
                    crop_area = (0, 0, width // 2, height // 2)
                elif corner_index == 1:  
                    crop_area = (width // 2, 0, width, height // 2)
                elif corner_index == 2:  
                    crop_area = (width // 2, height // 2, width, height)
                elif corner_index == 3:  
                    crop_area = (0, height // 2, width // 2, height)

                
                cropped_image = ori_image.crop(crop_area)
                ascii_txt = converter.generate(cropped_image)
                with open(txt_path, 'w') as f:
                    f.write(ascii_txt)
                ascii_to_square_image(txt_path, png_path)

                print(f"Generated ASCII art for {subdir_path}")