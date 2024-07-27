<h1 align='center'>PythonCourse</h1>

### ***This is a warehouse for python-program course, including practices & demo code.***

### ***Follow these steps to create a conda virtual env in your computer.***


# 1. Miniconda(recommend) or Anaconda
## Precautions
### ***If you are using M1/M2/M3 devices. Please download the correct file.***
![image](https://github.com/jiaowoguanren0615/PythonCourse/blob/main/sample_picture/miniconda_install.png)  

## [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
## [Anaconda](https://www.anaconda.com/download/)


# 2. Create and activate a conda virtual environment  

```shell
conda create -n YourEnvName python=version
```

### Here is an example for creating a virtual env named torch2, the python version=3.9
```shell
conda create -n torch2 python=3.9

conda activate torch2
```



<span style="color:red">-- **NOTE** These follow steps are optional if you are not currently learning machine learning or deep learning -- </span>

# 3. Install PyTorch package
## Recommend installing the GPU version based on your platform
## [pytorch-website](https://pytorch.org/)


# 4. Install Tensorboard package
```shell
pip install tensorboard
```


# 5. Install Graphviz (optional)
## [Download | Graphviz](https://www.graphviz.org/download/)


# 6. Install other packages
```shell
pip install -U jupyter numpy pandas matplotlib seaborn torchviz tqdm mglearn torchinfo transformers scikit-learn Pillow timm
```


# 7. Add more conda environments to jupyter
##  (step1) check your conda env package by running: "conda list" or "pip list" after activating your virtual env. Run step1 command if you don't have the package named ipykernel. If you had installed this package, then run step2 command.
```shell
conda install ipykernel
```

##  (step2) python -m ipykernel install --user --name YourEnvName --display-name "Name in Jupyter" 
### For example: I create a conda-env named "torch2", I want it to show the name "T2" in jupyter. Then run this follow code:
```shell
python -m ipykernel install --user --name torch2 --display-name "T2"
```

# 8. Edit jupyter-lab(notebook) configuration
## For jupyter-lab
```shell
jupyter lab --generate-config

vim ~/.jupyter/jupyter_lab_config.py
```
## For jupyter-notebook
```shell
jupyter notebook --generate-config

vim ~/.jupyter/jupyter_notebook_config.py
```