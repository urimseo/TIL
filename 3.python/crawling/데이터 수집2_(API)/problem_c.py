import requests
from tmdb import TMDBHelper
from pprint import pprint
from operator import itemgetter



def ranking():
  
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    url = tmdb_helper.get_request_url(region='KR', language='ko')
    data = requests.get(url). json()
    movie_list = []
    for v in data['results']:
        if v['vote_average'] >= 8:
            movie_list.append(v)

    data1 = sorted(movie_list, key = itemgetter('vote_average'), reverse=True)
    return data1[0:5] 
   

if __name__ == '__main__':
    pprint(ranking())

