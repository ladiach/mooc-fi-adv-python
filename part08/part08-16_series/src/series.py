# Write your solution here:
class Series():
	 
    def __init__(self, title:str, nr_seasons:int, genres:list):
        self.title = title
        self.seasons = nr_seasons
        self.genres = genres
        self.ratings = []
    
    def __str__(self):
        genres_list = ", ".join(self.genres)
    
        if len(self.ratings) ==0:
            return f"{self.title} ({self.seasons} seasons) \n genres: {genres_list} \n no ratings"
        else:
            avg = sum(self.ratings)/len(self.ratings)
            return f"{self.title} ({self.seasons} seasons) \n genres: {genres_list} \n {len(self.ratings)} ratings, average {avg:.1f} points"
    
    
    def rate(self, rating:int):
        self.ratings.append(rating)
    
    
def minimum_grade(rating:float, series_list:list):
    matches_found = []
    
    for serie in series_list:
        for r in serie.ratings:
            if r >= rating:
                matches_found.append(serie)
                break
    
    return matches_found
    
def includes_genre(genre:str, series_list:list):
    matches = []
    
    for serie in series_list:
        if genre in serie.genres:
            matches.append(serie)
    
    return matches
    
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    
    series_list = [s1, s2, s3]
    includes_genre("Comedy", series_list)