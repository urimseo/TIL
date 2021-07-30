import json
from pprint import pprint


# def movie_info(movie):

    # key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']   
    # data = {}
    # for key in key_list:
    #     data[key] = movie[key]
    # return data

def movie_info(movie):
    a = {
    'genre_ids' : movie['genre_ids'], 
    'id' : movie['id'],
    'overview' : movie['overview'],
    'poster_path': movie['poster_path'],
    'title' : movie['title'],
    'vote_average':movie['vote_average']
    }
    return a


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))