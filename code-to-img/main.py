import os
import argparse
from app import main

def parser_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default=os.path.join("app", "input_code"), help='Input directory')
    parser.add_argument('--driver_chrome', type=str,  default="/home/sveva/Downloads/chromedriver_linux64/chromedriver", help="path chrome driver exe") 

    return parser.parse_args()

if __name__ == '__main__':
    main(parser_arguments())