# Steps:

## Step 01: Create an empty remote repository


## step 02 :Initialize the git local repository  and connect it to the remote
```bash
git init
git add README.md
git commit -m "First commit"
git branch -M main
git remote add origin https://github.com/damanpreet26/dvc-ml-demo.git
git push -u origin main 
```

```bash
touch .gitignore
```


## Step 03 :conda environment creation and activation
```bash
conda create -n new_env python=3.8 -v
conda activate new_env
```

## Step 04: create a setup.py file
```bash
touch setup.py
```
paste below content and make the necessary changes---
```python
from setuptools import  setup

##long_desc=""
with open("README.md","r") as f:
    long_desc= f.read()


setup(
    name="src",
    version="0.0.1",
    author="demon",
    description="A small package for dvc pipeline",
    long_description=long_desc,
    url="https://github.com/damanpreet26/dvc-ml-demo",
    author_email="damanpreets26@gmail.com",
    package=["src"],
    license="GPU",
    python_requires=">=3.7",
    install_requires=[
        "dvc","pandas","sklearn"
    ]
)
```

## Step 05: create requirementts and dependencies file
```bash
touch requirements.txt
pip install -r requirements.txt
```

## Step 06: initialize DVC
```bash
dvc init
```

## Step 07: create basic folder structure
```bash
mkdir -p src/utils
mkdir config
```

## Step 08: create a config file
```bash
touch config/config.yaml
```

content of config.yaml file

```yaml
data_source: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv
artifacts:
  artifacts_dir: artifacts
  raw_local_dir: raw_local_dir
  raw_local_files: data.csv
```

## Step 09 : create the src/stage_01_load_save.py and src/utils/all_utils.py file 
```bash
touch src/stage_01_load_save.py rc/utils/all_utils.py
```

content of both these files can be refered 

## Step 10: create the dvc.yaml file and add the stage 01:
```bash
touch dvc.yaml
```
content of dvc.yaml file is below:
```yaml
stages:
  load_data_stage:
    cmd: python src/stage_01_load_save.py --config=config/config.yaml
    deps:
      - src/stage_01_load_save.py
      - src/utils/all_utils.py
      - config/config.yaml
    outs:
      - artifacts/raw_local_dir/data.csv
```

## Step 11 : run the dvc repro command
```bash
dvc repro
```

## Step 12 : commit and push the changes to git
```bash
git add .
git commit -m "making commit"
git push -u origin main 
```

