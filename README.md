<div align="center"> 

# `OpenMindLLM` 

![Static Badge](https://img.shields.io/badge/mission-increase_knowledge_capacity_through_ai-purple)

<br />

![GitHub top language](https://img.shields.io/github/languages/top/jonasplima/OpenMindLLM) 
![GitHub last commit](https://img.shields.io/github/last-commit/jonasplima/OpenMindLLM)

<p class="align center">
<h4><code>OpenMindLLM</code> is an open-source framework for increasing knowledge capacity through AI.</h4>
</p>
</div>

____________
## Quickstart

### Required Python Version 
Ensure you have at least python3.10 installed on you operating system. Otherwise, when you attempt to run the pip install commands, the project will fail to build due to certain dependencies. 

### Setting up the environment

Follow these steps to get all OpenMindLLM related apps installed and configured.

1. Navigate to where you want the project to live on your system in a semi-permanent place on your computer.

```bash
# Find a home for OpenMindLLM
cd /where/you/keep/code
```

2. Clone the project to your computer.

```bash
# Clone OpenMindLLM to your computer
git clone https://github.com/jonasplima/OpenMindLLM.git
```

3. Enter OpenMindLLM's main directory

```bash
# Enter the project folder (where you cloned it)
cd OpenMindLLM
```  

4. Create the virtual environment using `venv`
```bash
python -m venv omllm_venv
```

5. Activate the environment
- Windows: 
```bash
omllm_venv\Scripts\activate
```

- MacOS and Linux: 
```bash
source omllm_venv/bin/activate
```
6. Install the requirements: 

> If you are running your environment in a CPU, run the below command.
```bash
pip install -r requirements.txt
```

> If you are in Linux and running your environment to use a local GPU, run the below command.
```bash
pip install -r requirements.txt -e .[gpu]
```

```bash
sudo apt install nvidia-cudnn


export LD_LIBRARY_PATH=`python -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'`
```



Restart your shell or run: 
```bash 
source ~/.bashrc  # or source ~/.zshrc, depending on your shell
```

7. Restart your shell to reload everything.

8. Now you are up and running! 