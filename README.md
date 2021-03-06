# Lyric Generator

- Scrapes song lyrics from the web using urllib requests library
- Uses the lyrics to create a stochastic Markov Model
- Uses the Model to generate new lyrics based on the probability of occurrence


# What are Markov Chains?

Markov Chains are stochastic processes, i.e, random variables which evolve over time. The essence of the Markov Property is that **the future only depends on the immediate past**. That is, you only have to *condition* on *one* previous step to get all of the relevant information about predicting the future; conditioning on steps further in the past gives *no valuable information.*


# Use of Markov Chains here

Markov Chains are used to build a probabilistic model of the possible occurrences of the next word following the current word. This weighted probability is then used to randomly select a next word from the list of possible choices.


# Web Scraping

The web scraping is done from azlyrics.com. Input is taken from the user regarding the artist name and this artist name is searched.

The links are taken from possible matches of artist name and the song links are opened using urllib.request.urlopen().

The lyrics are then extracted out, filtered and cleaned and put in lyrics.txt for further processing by the driver function.