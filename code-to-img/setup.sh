source ~/miniconda3/etc/profile.d/conda.sh

conda create -n "code-to-img" python="3.7"
conda activate "code-to-img"

# install python requirements
pip install -r requirements.txt