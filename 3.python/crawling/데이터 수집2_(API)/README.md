# Python을 활용한 데이터 수집 II



### 목표

- Python 기본 문법 실습

- 데이터 구조에 대한 분석과 이해

- 요청과 응답에 대한 이해

- API의 활용과 문서 분석

  

### 준비사항

#### A. 사용 데이터 

1. TMDB API(https://developers.themoviedb.org/3)
2. 영화 정보 및 API 서비스

#### B. 개발언어/프로그램

- Python 3.8 이상

#### C. 필수 라이브러리

- requests



### 요구사항

커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 영화 데이 터를 수집하는 과정입니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니 다. 완성된 기능들은, 향후 커뮤니티 서비스에서 활용할 수 있습니다.



---

### A. problem__py : 영화 개수 카운트 구현

> popular를 기준으로 가져온 영화 목록의 개수를 출력합니다. 

```python
import requests
from tmdb import TMDBHelper

def popular_count():
    # api_key 할당
	tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
 	# API 요청에 필요한 주소 구성
    url = tmdb_helper.get_request_url(language = 'ko', region= 'KR')

    #딕셔너리 형태로 제공
    data = requests.get(url). json() 
    #data딕셔너리의 'results'키의 value(리스트 내부에 딕셔너리)반환
    return len(data['results'])

if __name__ == '__main__':
    print(popular_count())  #20
```

- TMDBHelper 클래스의 인스턴스 변수에 접근하여 api_key 를 할당 
- API 요청에 필요한 주소를 get_request_url에 접근하여 url 을 설정
- 딕셔너리 형태로 data에 선언 후 data딕셔너리의 'results'키 값의 길이를 반환

> TMDBHelper 의 클래스를 import 해 올 때, tmdb.py 에서 인스턴스 변수를 선언하여도 클래스만 import 해왔기 때문에 함수에 적용이 안되는 걸 알게 되어 변수 접근 범위에 대해 더 많은 공부를 할 수 있었다. 

> tmbd_helper인스턴스 변수를 popular_count 내부에 선언하였는데, 만약 api키 값이 변경되거나, 만료되었을 때 모든 함수에서 이 apikey값을 변경해야 한다.
>
> 함수의 재사용성을 생각하면 외부에 선언하고 함수 사용시마다 apikey를 따로 선언해 주는 것이 재사용성이 좋을 것 같다. 



---

### B. problem_b.py: 특정 조건에 맞는 영화 출력

> popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력합니다.

```python
def vote_average_movies():
 
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    url = tmdb_helper.get_request_url(language = 'ko', region= 'KR')
    data = requests.get(url). json() 

    movie_list = []
    #딕셔너리 'result'리스트 내 하나의 딕셔너리마다 조건 비교하여 추가
    for v in data['results']:
        if v['vote_average'] >= 8:
            movie_list.append(v)

    return movie_list
```

- problemA의 import 와 url 선언은 동일하다.
- data의 'result' value 값이  딕셔너리들을 모아 놓은 리스트 이기 때문에, value 내부의 key가 평점을 가리키면 그 키의 value 를 8과 비교하였다. 
- 새로운 리스트에 해당 딕셔너리를 추가하여 반환하였다.  

> 딕셔너리에서 키값을 접근하는 법과, 그 키값의 형태에 맞는 메서드를 사용하는 법을 실습을 통해 연습할 수 있었다.



---

### C. problem_c.py: 평점 순 정렬 

> 영화목록을 평점순으로 출력하는 함수를 완성합니다. 해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보로 사용됩니다.
>
> 받아온 데이터 중 평점이 높은 영화 다섯개의 정보를 리스트로 반환하는 함수 ranking을 완성합니다.

```python
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
            
	#itemgetter
    data1 = sorted(movie_list, key = itemgetter('vote_average'), reverse=True)
    return data1[0:5] 

if __name__ == '__main__':
    pprint(ranking())

```

- itemgetter를 활용하여 b에서 만든 `movie_list`를 평점 기준으로 내장함수 `sorted`를 활용하여 정렬한 후, 오름차순으로 정렬하기 위하여 `reverse = True` 를 하였다.
- 정렬된 `data1`을 5개만 출력하기 위해 슬라이싱 하여 반환했다.

> 외부 라이브러리(itemgetter)를 활용하여 value 기준으로 굉장히 간단하게 정렬할 수 있다는 것을 배웠다. 
>
>  리스트를 슬라이싱 하며 반환하면 간단하게 원하는 조건을 만족하여 출력할 수 있다는 것을 깨달았다. 



---

### D. problem_d.py: 제목 검색, 영화 추천

> 제공된 영화 제목을 기준으로 추천영화 목록을 출력합니다.

```python
def recommendation(title):
	
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    #영화 id 가져오기
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
```

- tmdb.py 의 get_request_url을 사용하여 매개변수(title)이 변할때마다 url이 변경 될 수 있도록 f-string으로 `{movie_id}`를 출력할 수 있게 했다.
- data의 'result'키 값의 value 만 results에 선언하였다. 
- 조건문을 사용하여 
  - 추천한 리스트가 있으면 title_list 에 넣어서 return `if`
  - 올바르지 않은 영화 제목으로 id가 없는 경우 `elif`  
  - id 값은 없지만 추천 영화가 없는 경우 빈 리스트 반환  `else`

> id 값과 result 값이 모두 다를 경우 각각의 조건에 맞춰 return 값을 다르게 지정해야 하는 것에서 헤맸던 것 같다. 
>
> movie id를 url 에 값을 넣어주기 전에 id값이 없으면 None 리턴하는 조건을 미리 선언하면 `elif`를 따로 설정해주지 않아도 된다.



---

### E. problem_e.py: 배우, 제작진 리스트 출력

> 영화에 출연한 배우들과 제작진의 정보가 저장된 딕셔너리를 출력합니다.
>
> 반환되는 딕셔너리는 cast, crew 두개의 key를 가지고 각각 배우 리스트 와 제작진 리스트를 value로 갖습니다.

```python
def credits(title):
    tmdb_helper = TMDBHelper('86ebf6dce9605d8e49b65b057c5e7b0a')
    cast_id = []
    director_list = []
    #movie_id 값이 없으면 None반환
    movie_id = tmdb_helper.get_movie_id(title)
    if movie_id == None:
        return None
    url = tmdb_helper.get_request_url(method = f'/movie/{movie_id}/credits',region='KR', language='ko')
    data = requests.get(url). json()
    
	#배우 이름 리스트
    for i in data['cast']:
        if i['cast_id'] < 10:
            cast_id.append(i['name'])
	#감독 이름 리스트 
    for i in data['crew']:
        if i['department'] == 'Directing':
            director_list.append(i['name'])
            
	#완성된 딕셔너리
    castcrew = {'cast' : cast_id, 'crew' : director_list  }
    return castcrew
```

- d와는 다르게 movie_id 값을 url 선언 전에 None으로 반환할 수 있게 하였다.
- data의 'cast'키와 'crew'키에 각각 접근해서 value 값이 조건에 맞을 경우 리스트에 append 하는 반복문을 각각 만들어 배우 리스트와 감독 이름 리스트를 만들었다.
- 새로운 딕셔너리를 만들어 key와 value를 만들었다.

> 각각 두개의 리스트를 만들고, 새로운 딕셔너리에 넣어서 만드 것이 간단한데 처음에 너무 어렵게 접근을 했다.
>
> 각각 다른 값을 가지고 와서 하나의 새로운 정보를 가진 딕셔너리를 만드는 것이 너무 재미있고, 활용도가 높을 것 같다.!