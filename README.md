# Playful

For my 3-week [Insight Data Science Fellowship](https://www.insightdatascience.com/) project in 2018, I used data from the Steam game store to build an app called Playful to make computer game recommendations for Steam users using [collaborative filtering with implicit feedback](http://yifanhu.net/PUB/cf.pdf). The app isn't live anymore because I stopped paying the AWS instance, but all the code and details you would need to recreate it are here.

## How playful was built
First, I obtained Steam data and performed some initial data exploration using
* scrapy
* API calls
* PostgreSQL

Next I generated, optimized, and validated a collaborative filtering model with implicit feedback using
* sparse matrices
* matrix factorization
* recall@k

Finally I built a web app to turn that model into recommendations for anyone who owns games on Steam using
* item-to-item recommendations 
* pandas
* flask
* Amazon web services

More details are in [this notebook](https://github.com/EFerriss/playful/blob/master/Playful's%20Pipeline.ipynb).
