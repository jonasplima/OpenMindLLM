from setuptools import setup, find_packages

setup(
    name='OpenMindLLM',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'python-dotenv==1.0.1',
        'langchain==0.2.2',
        'langchain-community==0.2.3',
        'faster-whisper==1.0.2', 
    ],
    extras_require={
        'gpu': ['nvidia-cublas-cu12==12.5.2.13', 'nvidia-cudnn-cu12==9.1.1.17'], 
    },
)
