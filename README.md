# Sentiment-driven-cryptocurrency-trading indicator
## Overview

In this project, a sentiment driven trading indicator is developed with the goal of providing recommendations to users(traders/investors) for investment in cryptocurrencies.  

## Background and Motivation

The cryptocurrency market has been turbulent since its inception, but the recent price fluctuations have been significantly volatile compared to traditional currencies, or even gold. In January 2021, the price of Bitcoin jumped from around $32,000 to $38,000 in a matter of hours, resulting in a $111 billion rise in market value. This rise occurred as a result of the following event: Elon Musk, the founder of firms such as Tesla and SpaceX, changed his Twitter profile bio to just include the term "#bitcoin" in his account description[1]. Many investors entered the crypto market following Elon's tweets to accept payments for Tesla cars in bitcoins. Soon after in April, Elon Musk changed his mind and caused panic among investors by tweeting that Tesla would no longer be accepting payments in Bitcoin owing to the high energy consumption of Bitcoin in the mining process[2]. There were speculation about Elon's ability to influence the cryptocurrency prices through his tweets. This brings to the question at hand: can influential leaders' tweets drive the cryptocurreny or market? It seems unwise to attribute volatility in crytocurrency market to just one person's tweets. 
While cryptocurrency continues to intrigue investors, many people often confuse the crypto market with the stock exchange. Stocks are assest backed by companies, and are traded in certain time periods. These are often adhered to certain regulations and audits by government agencies. Unlike stocks, cryptocurrencies are digital assets with a subjective value, and traded 24*7 largely without regulations, despite the fact that several governments are rapidly developing regulations for digital currencies and trade. Cryptocurreny is still an emerging market and have much higher volatility as compared to stock market, making it a riskier investment for traders. In this context, I am researching to develop a trading indicator by analysing tweets that can inform investors/asset managers/traders whether to invest in cyrptocurrecy market.  Ofcourse, tweets are not the only source of market volatility, there are other factors responsible such as political statements, environmental changes etc. For this project, I am focusing on the sentiment analysis of tweets. 

In this research, we are using natural language processing to build Twitter sentiment driven trading indicators. These indicator are, in general, text classifiers which will be categorized based on the analysis of the sentiment behind the tweets. These indicators can be beneficial for investors/traders/general public to create their trading strategies for investment in cryptocurrencies [3] . 

## Goals
The goal of this project is to build a sentiment analysis classifier (indicator) that can classify the polarity of the text in tweets whether it is positive, negative or neutral. This model will then be deployed to predict the monitor all the tweets containing atleast hashtags of 1 particular cryptocurrency, e.g. Dogecoin and categorise the tone of the tweets in either "positive", or "negative" or "neutral". 

## Methodology 
Firstly, a machine learning model will be trained on a sentiment labelled sentences data set available from [kaggle](https://www.kaggle.com/ankurzing/sentiment-analysis-for-financial-news). This dataset contains 2 columns, one cotaining sentences and other containing sentiment labels - poitive, negative or neutral. The trained model can then be tested on any datasets containing tweets to predict the sentiment of the sentences. 

## Datasets
https://www.kaggle.com/ankurzing/sentiment-analysis-for-financial-news
https://www.kaggle.com/davidwallach/financial-tweets


## Practical Applications
This machine learning model to develop trading strategies for the users based on sentiment analysis could be useful for crytocurrency exchange platforms such as coinbase or wealthsimple [3]. 

## Milestones

## References
[1] The ‘Musk Effect’ in cryptocurrency markets, https://www.law.ox.ac.uk/business-law-blog/blog/2021/04/musk-effect-cryptocurrency-markets
[2] https://economictimes.indiatimes.com/markets/cryptocurrency/extent-of-elon-musks-influence-on-cryptocurrency-where-is-it-headed/articleshow/83037268.cms?from=mdr
[3] https://datapool.app/charts/cryptocurrency/eth_twitter_sentiment_analysis/