from Media import *

class Clip(Media):
    def __init__(self,name,director,imdb_score,url,year,casts):
        super().__init__(name,director,imdb_score,url,year,casts)