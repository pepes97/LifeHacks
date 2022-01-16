source ~/miniconda3/etc/profile.d/conda.sh

conda create -n "todo-app" python="3.7"
conda activate "todo-app"

# install python requirements
pip install -r requirements.txt