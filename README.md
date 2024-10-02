# OpenAI Embeddings API

Quick test of using OpenAI's Embeddings api to see how cosine similarities work with natural language. 

### Optional: Docker

If you have docker on your machine, spin up a python session:

```sh
docker run -it --rm --entrypoint bash -v /path/to/openai-embeddings:/root/app python
cd /root/app
```

## Setup

You'll need an API key from [OpenAI](https://platform.openai.com) first. Place it in a `.env` file. 

```sh
echo OPENAI_API_KEY='sk-proj-blah' > .env
```

Next install the python dependencies:

```sh
pip install -r requirements.txt
```

## Run

After installing the dependencies and setting your API key, you can change the `reference_sentence` in `main.py` which will check for similarity 
([cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity)) against the sentences in `sentences.txt`. 

Run it like this:

```sh
python main.py
```

You should see some output like this:

```sh
Reference sentence: What kind of cat do you have?
similary for 'what is you favorite movie?': 0.1967945025298083, tokens used: 6
similary for 'which movies do you enjoy?': 0.24120150669387488, tokens used: 6
similary for 'Do you have a dog?': 0.4884892631968799, tokens used: 6
similary for 'Are there any pets in your house?': 0.5090105981081586, tokens used: 8
similary for 'what country do you live in?': 0.2920796718871967, tokens used: 7
similary for 'who will win the election?': 0.10280451412128476, tokens used: 6
similary for 'What is you favorite music?': 0.25588549275685546, tokens used: 6
similary for 'Are you going to the movies this weekend?': 0.1827440166749661, tokens used: 9
similary for 'what social/chat app do you use at least once a month?': 0.20873076398520216, tokens used: 13
```
