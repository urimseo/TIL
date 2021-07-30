# python을 활용한 데이터 수집



## 목표
-  Python 기본 문법 실습

- 파일 입출력에 대한 이해

- 데이터 구조에 대한 분석과 이해 

- 데이터를 가공하고 JSON 형태로 저장 

  

## 준비사항

### A. TMDB API

1. 평점 순 영화정보 API 서비스
2. 장르 리스트 정보 API 서비스
3. 영화 상세정보 API 서비스

### B. 개발언어/프로그램

- Python 3.8 이상

### C. 필수 라이브러리

- json

## 요구사항

커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를
추출해 나가는 과정을 진행합니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내
용입니다.



#### A. 제공되는 영화 데이터의 주요내용 수집

샘플 영화데이터가 주어집니다. 이중 서비스 구성에 필요한 정보만 뽑아 반환하 는 함수를 완성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

i. 데이터
1. 제공되는 movie.json 파일을 활용합니다.
2. movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.

ii. 결과

1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids
  키에 해당하는 정보만 가져옵니다.
2. 가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성합
  니다.

```PYTHON

def movie_info(movie):

    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids'] 
    data = {}
    for key in key_list:
        data[key] = movie[key]
    return data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```

- 데이터에서 특정 키를 추출할 때, 해당 키값을 리스트로 선언하여 movie.json에서 키값을 반복문을 통하여 확인했습니다.
- for문에서 반복 할 때, data에 키,벨류 쌍을 dict{}에 할당하여 data를 출력하였습니다. 





#### B. 제공되는 영화 데이터의 주요내용 수정

이전단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함 수를 완성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다. 

i. 데이터
1. 제공되는 movie.json, genres.json 파일을 활용합니다.
2. movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.
3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

ii. 결과

1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids
  키에 해당하는 정보만 가져옵니다.

2. genres.json파일을 이용하여 genre_ids를 genre_names로 변환하여 dictionary에 추가합니다.

3. 완성된 dictionary를 반환하는 함수 movie_info를 완성합니다.

   

```python
def movie_info(movie, genres):
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    dict = {}
    old = 'genre_ids'
    new = 'genre_names'
    for key in key_list:
        dict[key] = movie[key]
    dict[new] = dict.pop(old)
    print(dict)

    #1. dict안의 genre_numbers에 있는 리스트 만큼 돌고
    #2. 그 안의 리스트 인덱스로 접근하여 값을 비교
    #3. 같은 값이 나오면 바꿔치기 
    
    data = []
    for i in dict['genre_names']:
        for genre in genres:  
            if i == genre['id']:  
                i = genre['name'] 
                data.append(i)
        dict['genre_names'] = data
    return dict
```

- A에서 만든 dict{}에서 'genre_ids'키 이름을 'genre_names'로 바꾸기 위하여 pop()함수를 사용했습니다. `dict[newname] = dict.pop(oldname)`으로 사용했습니다.
- A에서 만든 dict{}에서 'genre_names'로 (2번)반복하였습니다.
- 중첩 for문을 사용하여 'genre_names'의 value값과 'id'의 value 값을 비교하고, 맞으면 'name'의 value 값을 data[]라는 빈 리스트에 apppend 하였습니다.
- 'name' vlaue 를 'genre_names'에 할당하고 data 를 return 하였습니다.





#### C. 다중 데이터 분석 및 수정

TMDB기준 평점이 높은 20개의 영화데이터가 주어집니다. 이 중 서비스 구성에
필요한 정보만 뽑아 반환하는 함수를 완성합니다. 완성된 함수는 향후 커뮤니티
서비스에서 제공되는 영화 목록을 제공하기 위한 기능으로 사용됩니다.

i. 데이터

1. 제공되는 movies.json, genres.json 파일을 사용합니다.
2. movies.json은 영화 전체 정보를 가지고 있습니다.
3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

ii. 결과

1. 이전 단계의 함수 구조를 재사용합니다.
2. 영화 전체 정보를 수정하여 반환하는 함수 movie_info를 완성합니다

```python
def movie_info(movies, genres):
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    result =[]
    for movie in movies: #20 
        data = {}
        for key in key_list:  #6
            data[key] = movie[key] #키값으로 정렬된 data 리스트 만들어짐
            genre_ids = movie['genre_ids'] # ids숫자만 있는 리스트
            
            genre_name = []
            for genre_info in genres:
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
```

- 빈 딕셔너리 data를 선언하고 key_list 에 해당하는 키 값으로 정렬된 data를 넣었습니다.
- genre_ids에 moie['genre_ids'] 숫자만 있는 리스트를 할당합니다.
- id 의 숫자와 'name'을 비교하여 genre_name[]에 할당합니다.
- result_data에 해당 키 값을 모두 할당한 후, 모든 movies 를 합쳐서  result를 return합니다.



#### D. 알고리즘을 통한 데이터 출력

세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은
수익을 낸 영화를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니
티 서비스에서 메인 페이지 기본정보로 사용됩니다.
i. 데이터
1. movies.json과 movies폴더 내부의 파일들을 사용합니다.
2. movies.json은 영화 전체 데이터를 가지고 있습니다.
3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.
4. movies 폴더의 파일의 이름은 영화의 id로 구성되어있습니다. 아래는 13번 id를 가지고 있는 영화의 상세정보입니다.
5. 수익정보는 상세정보 파일을 통해 확인 할 수 있습니다.

ii. 결과
1. 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성합
  니다.

```python
def max_revenue(movies):
 
    max = 0
    max_name = ""
    for movie in movies:

        movie_id = movie['id']
        movies_file = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        movie_111 = json.load(movies_file)
        
		# 수익 정보 값, id 저장. 
        revenue_info = movie_111['revenue']
        if revenue_info > max:
            max = revenue_info
            max_name = movie_111['title']
    return max_name

if __name__ == 'main':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
```

- movies.json 불러오고 movies.json 에서 영화의 id를 받아왔습니다.
- movies파일에 접근하기 위하여 f-string을 써서 디렉토리에 'id'값으로 파일명에 접근을 합니다.

- 파일에 접근 한 후  첫 수익 벨류값을 max 에 할당 하여 반복되며 들어오는 수익 값과 max를 비교하여 가장 큰 수가 max에 담기도록 합니다.
- max의 값이 들어있는 파일의 title 값을 return 합니다.





#### E. 알고리즘을 통한 데이터 출력

세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월
에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 해당 데이
터는 향후 커뮤니티 서비스에서 추천기능의 정보로 사용됩니다.
i. 데이터
1. movies.json과 movies폴더 내부의 파일들을 사용합니다.
2. movies.json은 영화 전체 데이터를 가지고 있습니다.
3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.
4. movies 폴더의 파일의 이름은 영화의 id로 구성되어있습니다. 아래는 13번 id를 가지고 있는 영화의 상세정보입니다
5. 개봉일 정보는 상세정보 파일을 통해 확인 할 수 있습니다.

ii. 결과
1. 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies
를 완성합니다.

```python
def dec_movies(movies):
 
    result= []
    for movie in movies:
        movie_id = movie['id'] 

        movies_file = open(f'data/movies/{movie_id}.json', encoding = 'UTF8')
        movie_111 = json.load(movies_file)
        
        # 개봉일. 
        release = movie_111['release_date']
        if release[5:7] == '12':
            result.append(movie_111['title'])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

```

- e의 코드에서 수익 정보 대신 개봉일을 받아옵니다. 
- 개봉일의 월에 해당하는 부분을 slicing 한 후,  12와 일치하면 result에 영화 제목을 담습니다.
- 누적해서 담긴 영화 제목 리스트를 return 합니다

