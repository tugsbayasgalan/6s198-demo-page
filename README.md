# Song Lyric Generation
## Introduction
This repository is associated with the work we have done on our final project for MIT 6.s198 - Deep Learning Practicum - in the 
spring 2018 semester. Our objective was to explore using LSTM models with different parameters and settings in an attempt to 
generate song lyrics given a chosen genre and some words from the user to start with. We primarily experimented with character-by-character
generation and bigram-by-bigram generation. More information can be found in the slideshow presentation and our blog-post-style write up,
both of which are included in this repository as well. 

## Organization
The files in this repository are organized into two parts - files pertaining to the demo UI and files pertaining to the data 
processing and the deep learning models we designed and employed for this project. The files pertaining the UI are available in
the outermost layer of the repository and in the `templates` directory. The files relevant to data processing, the datasets, and 
the deep learning models are in the `notebooks` directory.

## Instructions to run 
First, install Flask
```
sudo pip install Flask 
```


## Credits
We would like to thank our LA Emmanuel Mensah for giving us advice and support when we most needed it and putting up with our questions,
no matter how big or how small they were. We would also like to thank our industry mentors Philip Jacob and Anish Athayle for offering 
their expertise and insights and for helping us avoiding pitfalls wherever possible. Last but not least, we would like to thank 
Professor Hal Abelson, Natalie Lao, and the phenomenal staff of 6.s198 for a great semester!
