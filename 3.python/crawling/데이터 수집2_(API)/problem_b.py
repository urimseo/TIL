import requests
from tmdb import TMDBHelper
from pprint import pprint




def vote_average_movies():
 
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    url = tmdb_helper.get_request_url(language = 'ko', region= 'KR')
    data = requests.get(url). json() 

    movie_list = []
    for v in data['results']:
        if v['vote_average'] >= 8:
            movie_list.append(v)

    return movie_list


if __name__ == '__main__':
    pprint(vote_average_movies())
