# Smart Desk

An all-in-one Streamlit assistant that combines company research, social media sentiment monitoring and AI writing tools.

## Pages

| Page | File | What it does |
|------|------|--------------|
| About Company | `about.py` | Wikipedia summary and logo for a company |
| Company reputation on social media | `media.py` | Fetches recent tweets about a company (Tweepy) and analyses their sentiment with the expert.ai NL API |
| Programming | `program.py` | Generates code for a programming question with Cohere's generation model (few-shot prompt) |
| Short Essay | `shorts.py` | Writes a short essay on any topic with Cohere |

Sign-up and login are stored in a local SQLite database (`data.db`).

## Tech stack

Python, Streamlit, Cohere, Tweepy, expert.ai NL API, NLTK, wikipedia

## Configuration

Supply your API credentials through environment variables or Streamlit secrets, not in the source code:

```bash
export COHERE_API_KEY="..."
export TWITTER_BEARER_TOKEN="..."
export EAI_USERNAME="..."
export EAI_PASSWORD="..."
```

## Getting started

```bash
pip install -r requirements.txt
streamlit run app.py
```
