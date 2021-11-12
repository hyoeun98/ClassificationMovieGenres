#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import re


data = pd.read_csv('watcha_crawling.csv')
df = data.drop_duplicates(['title'],ignore_index=True)
df = df.dropna(how="any")

title = list()
story = list()
rating = list()
genre = list()
tag = list()
region = list()
year = list()

rating_regexp = re.compile('\d.\d$')
info_split_regexp = re.compile('\|') 
genre_split_regexp = re.compile('\s\D+[^·]')
year_split_regexp = re.compile('\d+년$')

for i in df['title']:
    title.append(i)
    
for i in df['story']:
    story.append(i)
    
for i in df['rating']:
    rating.append(rating_regexp.findall(i)[0])
    
for i in df['info']:
    info = info_split_regexp.split(i)
    genre.append("".join(genre_split_regexp.findall(info[0])).strip())
    if len(info) == 3: # tag가 안 붙은 작품
        tag.append("no_tags")
        region.append("".join(genre_split_regexp.findall(info[1])).strip())
        year.append("".join(year_split_regexp.findall(info[2])).strip())
        
    else:
        tag.append("".join(genre_split_regexp.findall(info[1])).strip())
        region.append("".join(genre_split_regexp.findall(info[2])).strip())
        year.append("".join(year_split_regexp.findall(info[3])).strip())

movie = pd.DataFrame({'title' : title,
                      'story' : story,
                      'rating' : rating,
                      'genre' : genre,
                      'tag' : tag,
                      'region' : region,
                      'year' : year})
movie.to_csv("movies.csv", mode='w', index=False)

