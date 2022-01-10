source ~/miniconda3/etc/profile.d/conda.sh

# create conda env
read -rp "Enter environment name: " env_name
read -rp "Enter python version (e.g. 3.7) " python_version
conda create -yn "$env_name" python="$python_version"
conda activate "$env_name"

# install python requirements
pip install -r requirements.txt