import requests
from tmdb import TMDBHelper
from pprint import pprint



def credits(title):
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    cast_id = []
    director_list = []
    movie_id = tmdb_helper.get_movie_id(title)
    if movie_id == None:
        return None
    url = tmdb_helper.get_request_url(method = f'/movie/{movie_id}/credits',region='KR', language='ko')
    data = requests.get(url). json()

    for i in data['cast']:
        if i['cast_id'] < 10:
            cast_id.append(i['name'])

    for i in data['crew']:
        if i['department'] == 'Directing':
            director_list.append(i['name'])

    castcrew = {'cast' : cast_id, 'crew' : director_list  }
    return castcrew

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
