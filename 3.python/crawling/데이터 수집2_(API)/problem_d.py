import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):


    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    movie_id = tmdb_helper.get_movie_id(title)
    url = tmdb_helper.get_request_url(method = f'/movie/{movie_id}/recommendations',region='KR', language='ko')
    data = requests.get(url). json()
    results = data.get('results')

    title_list = []
    if results:
        for i in results:
            title_list.append(i['title'])
        return title_list
    elif results == None:
        return None
    else :
        return results
  

if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))
