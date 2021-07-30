import json
from pprint import pprint

    #1. movies 데이터 들고오기
    #2. movies 데이터에서 한  영화씩 들고와서 key_list 대로 바꾸기  
def movie_info(movies, genres):
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    result =[]
    for movie in movies: #20 # 리스트 접근 인덱싱으로... 
        
        data = { }
        for key in key_list:  #6 # 키값으로 딕셔너리에 접근 
            data[key] = movie[key] #키값으로 정렬된 data 리스트 만들어짐
            genre_ids = movie['genre_ids'] # ids숫자만 있는 리스트
            
            genre_name = [ ]
            for genre_info in genres: # 장르 value 리스트 접근 
                if genre_info["id"] in genre_ids:
                    genre_name.append(genre_info["name"])
            
        result_data = {
            'genre_names' : genre_name,
            'id' : movie['id'],
            'overview' : movie['overview'],
            'poster_path' : movie['poster_path'],
            'title' : movie['title'],
            'vote_average': movie['vote_average']
        }
        result += [result_data]
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))