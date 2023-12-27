from Media import *

class Series(Media):
    def __init__(self,name,director,imdb_score,url,year,casts, g, ns ,ne):
        super().__init__(name,director,imdb_score,url,year,casts)
        
        self.genre = g
        self.number_of_seasons = ns
        self.number_of_episodes = ne