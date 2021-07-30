import json


def dec_movies(movies):
 
    result= []
    for movie in movies:
        movie_id = movie['id'] 

        movies_file = open(f'data/movies/{movie_id}.json', encoding = 'UTF8')
        movie_111 = json.load(movies_file)
        
        
        release = movie_111['release_date']
        if release[5:7] == '12':
            result.append(movie_111['title'])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
