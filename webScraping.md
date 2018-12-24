# Web Scraping


So I came to know about and learned Selenium when I was working one of my projects. 

## Problem
I had a database, in which there was a column under the tile `name` and there were several other columns associated with this.  
For the sake of explanation , let's say, that the `name` column contained the name of actors and the other columns were `movie title`,`director`,`year of release` and `imdb rating`. Let's assume that the database was collected from various sources, for movies released over several decades.  
The problem was that there existed duplicate entries for the same actor-movie combo becuase the actor's name was different in different entries. In some entries the name was mispelled, in some the name was with and without initial and others their middle names given and not given. For example: **Leonardo DiCaprio**'s name was given as *DiCaprio*, *L diCaprio*, and some others with spelling errors. But when you want to perform some operation on the database, simply `movieCount` for each actor, it would return wrong numbers. So the duplicate entries had to be removed and the misspelled entries had to be renamed. 

## Solution
I had to change the entire `name` column such that the name of any actor was uniform through out. I decided to change the name of the actors with reference to [imdb](https://www.imdb.com/). I knew that if I typed the actor's name along with imdb I would get the right name, like **Leo Dicaprio and imdb** the [top result](https://www.google.com/search?source=hp&ei=w5AgXIPGF4HtvASv9bi4DQ&q=Leo+Dicaprio+and+imdb&btnK=Google+Search&oq=Leo+Dicaprio+and+imdb&gs_l=psy-ab.3..35i39j0i22i30l9.1189.1189..1615...0.0..0.114.215.0j2......0....1j2..gws-wiz.....0.68jybQ_LuZw) in google would be a link to imdb with the right name. But I couldn't manually check for each entry, even if there were 50 actors with 2 name variants, I had to check **100 entries one by one**. So I had to design my code in such a way that it would search for each entry of the column and extract the right name.
