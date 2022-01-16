# Code to Image

A simple python utility tool to convert programming code into beautiful image snippets.

## Table of Contents

* [Environment Setup](#Environment-Setup)
    * [Windows System](#Windows-System)
    * [Linux System](#Linux-System)

* [Run](#Run)

## Enviroment Setup

1. Download this repository (you can use also git clone)

### Windows System

1. Install **Anaconda** using the following [instruction](https://docs.anaconda.com/anaconda/install/windows/#) instruction

2. Open Anaconda Prompt

3. Run the following commands

```
conda create --name code-to-img python==3.7
```

Just answer the prompts as you proceed.

4. Activate the env

```
conda activate code-to-img
```

5. Go to code-to-img folder with the prompt and run the following command

```
pip install -r requirements.txt
```

6. Download chromedriver from [this site](https://chromedriver.chromium.org/downloads) anche choose the version

7. Download the `chromedriver_win32.zip` also for Windows 64

8. Extract the folder that you have downloaded and in the `main.py` change the path of `driver_chrome` and set the path of your chomedriver execution file

### Linux System

1. Install **Anaconda** using the following [instruction](https://docs.anaconda.com/anaconda/install/linux/) instruction

2. Open Terminal

I strongly advise utilizing the bash script `setup.sh` to set up the python environment for this project.

3. Run the following command to quickly setup the env needed to run our code: 

```
bash ./todo_setup.sh
```
It's a bash command that will setup a conda environment with everything you need. Just answer the prompts as you proceed.

4. Enable env with the following command

```
conda activate todo-app
```

5. Download chromedriver from [this site](https://chromedriver.chromium.org/downloads) anche choose the version

6. Download the `chromedriver_linux64.zip` also for Linux

8. Extract the folder that you have downloaded and in the `main.py` file change the path of `driver_chrome` and set the path of your chomedriver execution file

# Run

```
python main.py --input_dir INPUT_DIR --driver_chome -- DRIVER_CHROME
```

where:

* `INPUT_DIR` is the directory code of files that you want to convert in images snippet. For instance: `app/input_code/python` means that you want to convert in images all python files that you have in that directory. Default is: `app/input_code`
* `DRIVER_CHROME` is the path of your `chromedriver` execution file

For instance:

```
python main.py --input_dir app/input_code/python --driver_chrome /home/sveva/Downloads/chromedriver_linux64/chromedriver
```

# Sample of Screenshot

| <img src="https://img.icons8.com/fluency/50/000000/linux-terminal.png"/> | <img src="https://img.icons8.com/color/50/000000/c-programming.png"/> | <img src="https://img.icons8.com/color/50/000000/c-sharp-logo.png"/> |
| :-: | :-: | :-: | 
| <img src="app/clips_sample/bash/hello_world.png" width="500px"> | <img src="app/clips_sample/C/hello_world.png" width="450px">  | <img src="./app/clips_sample/Csharp/hello_world.png" width="465px">  |

|<img src="https://img.icons8.com/color/50/000000/c-plus-plus-logo.png"/> | <img src="https://img.icons8.com/color/50/000000/html-5--v1.png"/> | <img src="https://img.icons8.com/color/50/000000/java-coffee-cup-logo--v1.png"/> |
| :-: | :-: | :-: | 
| <img src="app/clips_sample/C++/hello_world.png" width="420px">  | <img src="app/clips_sample/html/hello_world.png" width="456px"> | <img src="app/clips_sample/java/hello_world.png" width="520px"> |

| <img src="https://img.icons8.com/color/50/000000/javascript--v1.png"/> | <img src="https://img.icons8.com/color/50/000000/kotlin.png"/> | <img src="https://img.icons8.com/fluency/50/000000/texshop.png"/> |
| :-: | :-: | :-: | 
| <img src="app/clips_sample/javascript/hello_world.png" width="500px">  | <img src="app/clips_sample/kotlin/hello_world.png" width="440x"> | <img src="app/clips_sample/latex/hello_world.png" width="380px"> |

| <img src="https://img.icons8.com/officel/50/000000/markdown.png"/> | <img src="https://img.icons8.com/offices/50/000000/php-logo.png"/> | <img src="https://img.icons8.com/color/50/000000/python--v1.png"/> |
| :-: | :-: | :-: | 
| <img src="app/clips_sample/markdown/hello_world.png" width="500px">  | <img src="app/clips_sample/php/hello_world.png" width="500x"> | <img src="app/clips_sample/python/hello_world.png" width="445px"> |

| <img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/50/000000/external-scala-a-general-purpose-programming-language-with-strong-static-type-system-logo-shadow-tal-revivo.png"/> | <img src="https://img.icons8.com/color/50/000000/swift.png"/> | 
| :-: | :-: | 
| <img src="app/clips_sample/scala/hello_world.png" width="400px">  | <img src="app/clips_sample/swift/hello_world.png" width="510x"> | 