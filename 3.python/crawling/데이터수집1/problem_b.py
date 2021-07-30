import json
from pprint import pprint

def movie_info(movie, genres):
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    dict = {}
    old = 'genre_ids'
    new = 'genre_names'
    for key in key_list:
        dict[key] = movie[key]
    dict[new] = dict.pop(old)



    
    # print(dict)

    #1. dict안의 genre_numbers에 있는 리스트 만큼 돌고
    #2. 그 안의 리스트 인덱스로 접근하여 값을 비교
    #3. 같은 값이 나오면 바꿔치기 
    data = []
    for i in dict['genre_names']: # 한번 반복하면 -> 18, 두번쨰는 80  현재 인덱스로 접근중.
        for genre in genres:  # genre에는 id, name 모두 들어가있다.  총 genre 수만큼 반복
            if i == genre['id']:  # 18 이 genre의 value 값과 일치한다면
                i = genre['name'] #name 의 값을 id에 넣고
                data.append(i)
        dict['genre_names'] = data
    return dict

    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))