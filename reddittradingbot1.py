# Jason Bonilla
# Live sentiment analysis trading bot that handles cryptocurrencies specifically
# Bitcoin, based off the overall sentiment of live comments under r/bitcoin
import praw
import config
from textblob import TextBlob
from binance.client import Client
from binance.enums import *

# Passing API key and API secret
client = Client(config.BINANCE_KEY, config.BINANCE_SECRET, tld='us')

# configuring the python Reddit API wrapper
reddit = praw.Reddit(
    client_id= config.REDDIT_ID,
    client_secret= config.REDDIT_SECRET,
    password= config.REDDIT_PASS,
    user_agent="USERAGENT",
    username= config.REDDIT_USER,
)

sentimentList= []
neededSentiments = 300

TRADE_SYMBOL = 'BTCUSDT'
TRADE_QUANTIY = 0.0001

# ensures that the coin is not being bought repeatedly 
# waits until a sell signal is recieved in order to proceed
in_position = False

# returns average of sentiment list after 300 comments
def Average(lst):
    if len(lst) == 0:
        return len(lst)
    else:
        return sum(lst[-neededSentiments:]) / neededSentiments

# Most essential part of this bot, repsonisble for executing orders
# side = buy or sell 
# quantity = how many of a coin 
# symbol = currecy pair that is being traded (BTC, Doge UTC, Doge BTC, etc. )
def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        PRINT('SENDING ORDER')
        order = client.create_order(symbol=symbol, side =side, type = order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print('an exception has occured '+ e)
        return False
    return True


# will print the polarity and subjectivity of each comment in the stream.
# 0 means neutral, <0 means negative sentiment and >0 means positive sentiment
# if the average polarity is not neutral then a trade is excecuted  
for comment in reddit.subreddit("bitcoin").stream.comments():
    # prints most recent comments in r/bitcoin
    #print(comment.body)

    redditComment = comment.body
    blob = TextBlob(redditComment)
    print(blob.sentiment)

    sent = blob.sentiment
    print("************** Sentiment is: "+ str(sent.polarity))

    if sent.polarity != 0.0: #any value besides 0 will be used to find out average
        sentimentList.append(sent)

        #print("************* TOTAL SENTIMENT OF LIST IS:"+ round(Average(sentimentList) + "  *************")

        if  len(sentimentList) > neededSentiments and round(Average(sentimentList)) > 0.5:
            print("BUY")
            if in_position:
                print(" ************* BUY ORDER BUT WE OWN ************* ")
            else:
                 print(" ************* BUY ORDER  ************* ")
                 order_succeeded = order(SIDE_BUY, TRADE_QUANTIY, TRADE_SYMBOL)
                 if order_succeeded:
                    in_position = True
        elif  len(sentimentList) > neededSentiments and round(Average(sentimentList)) < -0.5:
            #print(" ************* SELL ************* ")
            if in_position:
                order_succeeded = order(SIDE_SELL, TRADE_QUANTIY, TRADE_SYMBOL)
                if order_succeeded:
                    in_position = False
                else:
                    print("************* SELL ORDER BUT WE DONT OWN *************")