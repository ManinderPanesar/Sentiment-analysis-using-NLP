# %% [markdown]
# #### Importing modules/libraries

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
from plotly.offline import iplot
import cufflinks as cf
cf.go_offline()

# %% [markdown]
# #### Loading dataset from Huggingface 

# %%
# load  dataset and split the data into train/validation/test datasets
from datasets import load_dataset, DatasetDict

# load  dataset and split the data into train/validation/test datasets
from datasets import load_dataset, DatasetDict

raw_datasets = load_dataset("financial_phrasebank", "sentences_50agree", split='train')
raw_datasets

# %%
raw_datasets.features

# %% [markdown]
# The _raw datasets_ contains two columns 'sentence' and 'label'. Column _label_ has identified 3 sentiment classes: 0 for 'Negative', 1 for 'Neutral', and 2 for 'Positive'. 

# %% [markdown]
# #### Convert dataset_dictionary to pandas dataframe

# %%
df = pd.DataFrame.from_dict(raw_datasets)
df.head()

# %% [markdown]
# ##### Drop duplicate sentences from the dataframe

# %%
df.drop_duplicates(subset=['sentence'],keep='first',inplace=True)
df.info()

# %% [markdown]
# There are a total of 4838 sentences in the dataframe. 

# %% [markdown]
# Create a column named **sentiment** in the dataframe

# %%
df.loc[df['label']==1,'sentiment'] = 'Neutral'
df.loc[df['label']==0,'sentiment'] = 'Negative'
df.loc[df['label']==2,'sentiment'] = 'Positive'
df.head()

# %%
# The distribution of sentiments

fig = px.pie(df, names='sentiment', title ='Pie chart of different sentiments of tweets')
fig.show()

# %% [markdown]
# The dataset contained about 60% sentences with neutral sentiment, 28% with positive and the rest 12% having negative sentiment. 
# 

# %% [markdown]
# ### Number of Characters

# %%
df['nr_of_char'] = df['sentence'].str.len()
df["nr_of_char"] = df["nr_of_char"] / df["nr_of_char"].max()
df[['sentiment', 'nr_of_char']].pivot(columns = 'sentiment', values = 'nr_of_char').iplot(kind = 'box')

# %% [markdown]
# ### Number of Words

# %%
df['nr_of_words'] = df['sentence'].str.split().str.len()
df[['sentiment', 'nr_of_words']].pivot(columns = 'sentiment', values = 'nr_of_words').iplot(kind = 'box')

# %% [markdown]
# ### Number of punctuation marks

# %%
df['nr_of_punc'] = df['sentence'].str.split(r"\?|,|\.|\!|\"|'").str.len()
df["nr_of_punc"] = df["nr_of_punc"] / df["nr_of_punc"].max()
df[['sentiment', 'nr_of_punc']].pivot(columns = 'sentiment', values = 'nr_of_punc').iplot(kind = 'box')

# %%
from wordcloud import WordCloud, STOPWORDS

# %% [markdown]
# #### Number of stopwords

# %%
stop_words = STOPWORDS
df['nr_of_stopwords'] = df['sentence'].str.split().apply(lambda x: len(set(x) & stop_words))
df['nr_of_stopwords'] = df['nr_of_stopwords'] / df['nr_of_stopwords'].max()
df[['sentiment', 'nr_of_stopwords']].pivot(columns = 'sentiment', values = 'nr_of_stopwords').iplot(kind = 'box')

# %%
df['nr_of_unique_words'] = df['sentence'].apply(lambda x: len(set(x.split())))
df["nr_of_unique_words"] = df["nr_of_unique_words"] / df["nr_of_unique_words"].max()
df.head()

# %%
def wordcount_gen(df,sentiment):
    '''
    Generate Word Cloud
    inputs:
     - df: Tweets dataset
     - sentiment: Neutral/Negative/Positive
    '''
    # Combine all tweets
    combined_tweets = " ".join([tweet for tweet in df[df.sentiment==sentiment]['sentence']])

    #initialize wordcloud object
    wc = WordCloud(background_color ='white', max_words=50, stopwords=STOPWORDS)

    #Generate and plot wordcloud
    plt.figure(figsize=(10,10))
    plt.imshow(wc.generate(combined_tweets))
    plt.title('{} Sentiment Words'.format(sentiment), fontsize=20)
    plt.axis('off')

#Positive sentiment
wordcount_gen(df, 'Positive')

#Negative sentiment
wordcount_gen(df, 'Negative')

#Neutral sentiment
wordcount_gen(df,'Neutral')




