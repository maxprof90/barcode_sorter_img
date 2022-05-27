import os
import shutil
from PIL import Image
from pyzbar import pyzbar
 
ROOT_PATH = r"D:\\"
TARGET_PATH = os.path.join(ROOT_PATH, 'IMAGES')
OUT_PATH = os.path.join(ROOT_PATH, 'RESULT')
 
def get_filenames(dir_path):
    return sorted(os.listdir(dir_path))
 
def split_into_blocks(fname_lst):
    return [fname_lst[n:n+3] for n in range(0, len(fname_lst), 3)]
 
def get_code_from_img(image):
    out = pyzbar.decode(Image.open(image))
    if out:
        return out[0].data.decode()
 
def find_code_from_block(block):
    for img in block:
        code = get_code_from_img(os.path.join(TARGET_PATH, img))
        if code:
            return code, img
    return None, None 

def create_code_folder(code):
    dir = os.path.join(OUT_PATH, code)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir
 
def create_bad_folder():
    dir = os.path.join(OUT_PATH, 'bad')
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir
 
def copy_img_from_block(block, dir, img_ignore = None):
    for img in block:
        if img != img_ignore:
            shutil.copy(os.path.join(TARGET_PATH, img), dir)

  
def main():
    image_blocks = split_into_blocks(get_filenames(TARGET_PATH))
    for block in image_blocks:
        code, img_name = find_code_from_block(block)
        if code:
            code_folder_path = create_code_folder(code)
            copy_img_from_block(block, code_folder_path, img_name)
        else:
            bad_folder = create_bad_folder()
            copy_img_from_block(block, bad_folder)
 
if __name__ == '__main__':
    main()
    
 