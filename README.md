# Playful

I used data from the Steam game store to build [an app called Playful](http://playful.live) to make computer game recommendations for Steam users using [collaborative filtering with implicit feedback](http://yifanhu.net/PUB/cf.pdf). Playfull was built in 3 weeks in January, 2018 as part of my [Insight](http://insightdatascience.com/) Data Science Fellowship.

## The app
The app is written with flask and hosted on AWS. All files for building the app are in the app folder except the config.py file containing the API key. The model was fit using [lightfm](https://github.com/lyst/lightfm) v1.14, so you'll need that too.

## Where the model came from
Jupyter notebooks coming soon!
