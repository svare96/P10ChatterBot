# P10ChatterBot

## Installation
There are a couple of steps needed to make this work.

First step is to make sure that you are running a python version between 3.6 and 3.8.

Then you need to create a new virtual environment.

Type the following command in your root folder, and make sure you create the environment in the correct Python version (Here, v3.8):
```
py -3.8 -m venv env
```

Next, you have to activate your new virtual environment.

Mac:
```
source env/bin/activate
```

Windows:
```
env\Scripts\activate.bat //in CMD
env\Scripts\activate.ps1 //in Powershell
```

When you need to exit the environment, deactivate the environment by typing:
```
deactivate
```

Once this is done, you should install the ChatterBot library, before installing all the other requirements:
```
pip install ./ChatterBot
```

Then you should be able to install the remaining requirements:
```
pip install requirements.txt
```

## How to Use

### Training
To train the model, simply run the *train.py* file. 

At the moment, it is setup to train with a corpus of different sentences in english.

To edit, please read [ChatterBot training documentation](https://chatterbot.readthedocs.io/en/stable/training.html).

### Running the Bot
To run the model, simply run the *chatbot.py* file.

Now, you can write a sentence, and the bot will answer.
