# Trump Tweet Chatbot

First and foremost thanks to the OpenAI team for providing their GPT-2 Transformer as an open source project! This is a fork of their work using some handy scripts developed by Nate Shepard (https://github.com/nshepperd) in his own fork of OpenAI's project. The model trains on a corpus of tweets from Donald Trump's entire Twitter archive in order to create a realistic chatbot.

## Project File Overview

- [`download_model.py`](download_model.py) script used to download OpenAI models.
- [`tweet_preprocessor.py`](tweet_preprocessor.py) my personal script for preprocessing tweets in csv file.
- [`src/encode.py`](src/encode.py) Nate Sheppard's script for encoding tweets into a format the model can read.
- [`src/train.py`](src/train.py) Nate Sheppard's script for training your own GPT-2 model.
- [`src/interactive_conditional_samples.py`](src/interactive_conditional_samples.py) script for interactive text generation, with small change made by me for the option to stop generation after one tweet.
- [`trump_tweets.csv`](trump_tweets.csv) a file of tweets from Donald Trump's Twitter account.

## Requirements

You’ll need the following:

- [Python 3.6.8](https://www.python.org/downloads/release/python-368/) (other Python 3 versions may work as well)
- Python's PIP package installer
- GPU with CUDA 10.0 is recommended and was installed on my machine while developing. It is encouraged for significantly faster training.

## Getting Started

The commands below are for Windows and my Python alias is "python" but yours may be "python3", "py -3", etc.

Make sure you have the virtualenv package in your global Python environment.

```
python -m pip install virtualenv
```

Move this project to its own folder and setup a virtual environment inside of it.

```
python -m venv env
```

Activate your virtual environment.

```
env/Scripts/activate
```

Install the project's dependencies into your virtual environment.

```
pip install -r requirements.txt
```

Download the OpenAI's 117M model to your local machine.

```
python download_model.py 117M
```

Preprocess the trump_tweets.csv file included in this repo.

```
python tweet_preprocessor.py
```

Encode your preprocessed text file into a format that is readable for the model.

```
python src/encode.py parsed_trump_tweets.txt parsed_trump_tweets.npz
```

Train your model on the now-encoded tweets.

```
python src/train.py --dataset parsed_trump_tweets.npz --sample_every 1000 --sample_num 1
```

Create a new folder under models and title it "tweeter".

```
mkdir models/tweeter
```

Go to checkpoint/run1/ folder and copy the following files: checkpoint, model-XXXX.data-00000-of-00001, model-XXXX.index, model-XXXX.meta. Paste them into your tweeter folder.

Go to models/117M and copy the following files: encoder.json, hparams.json, vocab.bpe. Paste them into your tweeter folder as well.

Run your trained model and feed it prompts to react to. It tends to work best if your prompt is open-ended and ends with a verb (ex. "America is"). If you use a person's name in your prompt, be sure to capitalize it properly for best results.

```
python src/interactive_conditional_samples.py --temperature .5 --top_p .9 --model_name tweeter
```
