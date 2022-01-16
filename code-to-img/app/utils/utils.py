import os
import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib import parse

def get_driver(ex_path):

    # Options chrome
    chrome_options = Options() 

    # Disable chrome opening window and size the window
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" %"1920,1080")

    # Create driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=ex_path)

    # max window
    driver.maximize_window()
    
    return driver

def read_file(file):

    # Open file and read it
    with open(file, 'r') as _f:
        text = _f.read()

    return text


def encode_text(file):

    # Read file
    clip_text = read_file(file)
    
    # encode text
    uri_encoded_clip_text = parse.quote_plus(clip_text)

    return uri_encoded_clip_text

def get_files(path):

    # get all files in directory
    files = glob.glob('{}/*'.format(path))
    for file in files:
        if os.path.isfile:
            yield file


def take_snapshot(web, file, OUTPUT_DIR):

    # get file name
    elem = web.find_element_by_xpath("//div[@id='export-container']")

    # output file name
    out_file = os.path.basename(file).split('.')[0]

    # save file
    file_path = '{}/{}.png'.format(OUTPUT_DIR, out_file)
    elem.screenshot(file_path)

def find_correct_url(encoded_text, type_file):

    if type_file == 'C':
        lang = '&l=text%2Fx-csrc'
    elif type_file == 'C':
        lang = '&l=text%2Fx-c%2B%2Bsrc'
    elif type_file == 'C#':
        lang = '&l=text%2Fx-csharp'
    elif type_file == 'C++':
        lang = '&l=text%2Fx-c%2B%2Bsrc'
    elif type_file == 'bash':
        lang = 'application%2Fx-sh'
    elif type_file == 'html':
        lang = '&l=htmlmixed'
    elif type_file == 'java':
        lang = '&l=text%2Fx-java'
    elif type_file == 'kotlin':
        lang = '&l=text%2Fx-kotlin'
    elif type_file == 'latex':
        lang = '&l=stex'
    elif type_file == 'php':
        lang = '&l=text%2Fx-php'
    elif type_file == 'scala':
        lang = '&l=text%2Fx-scala'
    else:
        lang = '&l='+type_file
    
    url = "https://carbon.now.sh?code=" + encoded_text + '&t=verminal' + lang

    return url


def code_to_img(file, type_file, web):
    
    # Print file
    print("{} Processing-{} {}".format('*'*10, file, '*'*10))

    # Encoded the text of the file
    encoded_text = encode_text(file)

    # url to carbon
    url = find_correct_url(encoded_text, type_file)
    web.get(url)

    # output directory
    output_dir = os.path.join("app", "output_img", type_file)

    # create output directory if not exists
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # take snapshot
    take_snapshot(web, file, output_dir)