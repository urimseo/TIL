import json

    #1. movies.json 불러오고 movies.json 에서  영화의 id를 받아온다.
    #2. movies파일의 디렉토리를 만들기
    #13. json 파일 
    #3. f-string...!!!!!!!!!
    # a = open('data/movie,' encoding =UTF8 )

def max_revenue(movies):
 
    max = 0
    max_name = ""
    for movie in movies:

        movie_id = movie['id']
        movies_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_111 = json.load(movies_file)

        revenue_info = movie_111['revenue']
        if revenue_info > max:
            max = revenue_info
            max_name = movie_111['title']
    return max_name


if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))