# TODO App

TODO app is an application where you can write down a to-do list.

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
conda create --name todo-app python==3.7
```

Just answer the prompts as you proceed.

4. Activate the env

```
conda activate todo-app
```

5. Go to TODO-app folder with the prompt and run the following command

```
pip install -r requirements.txt
```

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

## Run 
After completing the above steps, you can start the application run the following command

```
python main.py
```
5. Then go to [http://localhost:5000](http://localhost:5000) to interact with the application

## Example of the Application Dashboard

We show two different modes, day and night.

### Light mode

![](./app/static/img/todo-light.png)

### Dark mode

![](./app/static/img/todo-dark.png)

