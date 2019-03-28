# SteamRecommenderSystem
A recommender system built upon the user behaviors & game statistics collected by Steam. Methods Experimented in this project include: Popularity based and Collaborative filtering.


## Dataset
The original dataset is generated entirely from public Steam data via Steam Web API. 
Please view and download the dataset at https://www.kaggle.com/tamber/steam-video-games 

## Introduction
Steam is one of the world's largest game platform with over 30000 games and averaged 47 million daily active users. 
The quality and amount of data Steam has collected is ideal for building a recommender system. This project aims to leverage 
the information Steam gathered to provide users personalized shopping experience by feeding them the content they’re interested in, 
and surprising them with offers that are analyzed to be in their favor.

## Implementation
The project is written in two languages: Python and Spark. Both Codes have been migrated and could be easily accessed on
[Jupyter Notebook](https://jupyter.org/). 

## Models
Models could be found inside of the Recommender_Model folder

* Popularity based
* Collaborative filtering 
   * ALS-based recommender
   * Turicreate 
   * SVD 


## Data supplement
Originally I wrote two Python Scripts to get more sepecific tags of each game which could be used as a supplement to 
compute game similarities and build content-based model.
However, according to the robots.txt document, Steam does not grant permission to scrape data at
https://steamdb.info/
I will try to collect this piece of data from Steam Web API, or extracting the data from the exisiting [dataset](https://steam.internet.byu.edu/) online.

## Performance
Item Similarity



Precision Recall



##### Special thanks to Ella Chen @s93chen
