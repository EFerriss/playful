# Playful

I used data from the Steam game store to build [an app called Playful](http://playful.live) to make computer game recommendations for Steam users using [collaborative filtering with implicit feedback](http://yifanhu.net/PUB/cf.pdf). Playfull was built in 3 weeks in January, 2018 as part of my [Insight](http://insightdatascience.com/) Data Science Fellowship.

## How playful was built
First, I obtained Steam data and performed some initial data exploration using
* scrapy
* API calls
* PostgreSQL

Next I generated, optimized, and validated a model using
* sparse matrices
* matrix factorization
* LightFM

Finally I built a web app to turn that model into recommendations for anyone who owns games on Steam using:
* item-to-item recommendations
* pandas
* flask
* Amazon web services

The files for the app are in the app folder, and [this notebook](https://github.com/EFerriss/playful/blob/master/Playful's%20Pipeline.ipynb) provides more details about how the model was built.
