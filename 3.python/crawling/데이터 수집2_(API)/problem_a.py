import requests
from tmdb import TMDBHelper



def popular_count():
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    url = tmdb_helper.get_request_url(language = 'ko', region= 'KR')

    #딕셔너리 형태로 
    data = requests.get(url). json()
    return len(data['results'])
    

if __name__ == '__main__':
    print(popular_count())


