
import os
from app.utils.utils import get_files, code_to_img, get_driver

def main(args):    

    # Driver
    web = get_driver(args.driver_chrome)
    
    # Input files
    for file in get_files(args.input_dir):
        
        if os.path.split(args.input_dir)[1] == 'input_code':
            if os.path.isdir(file):
                for f in get_files(file):
                    type_file = os.path.split(file)[1]
                    code_to_img(f, type_file, web)
        else:
            type_file = os.path.split(args.input_dir)[1]
            code_to_img(file, type_file, web)