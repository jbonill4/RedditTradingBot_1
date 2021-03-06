# Reddit Trading Bot 1

Live sentiment analysis trading bot that handles cryptocurrencies specifically
Bitcoin, based off the overall sentiment of live comments under r/bitcoin

## Requirements
- Must have [PRAW](https://praw.readthedocs.io/en/latest/) installed
- Must have [TextBlob](https://textblob.readthedocs.io/en/dev/) installed
- Must have [python-binance](https://python-binance.readthedocs.io/en/latest/) installed
- Must have at least [python3.6](https://www.python.org/downloads/) installed 
- Must have [conda](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html) installed 

## Instructions
Create a virtual environment using conda:
- **create --name ENVNAME python=3.6**

Run virtual environment using conda:
- **conda activate ENVNAME**

Fill in config.py with your own personal Reddit username API ID/Secret, and Binance API KEY/Secret
- [How to create Binance API Key](https://www.binance.com/en/support/faq/360002502072)
- [How to create Reddit API Key](https://github.com/reddit-archive/reddit/wiki/OAuth2)

Specify which cryptocurrency you would like to trade. The code is preset to [Bitcoin(BTC)](https://bitcoin.org/en/). In order to switch coins the folowing need to be changed accordingly:
- **TRADE_SYMBOL**
- **reddit.subreddit()**

Run program:
- **python reddittradingbot1.py**







