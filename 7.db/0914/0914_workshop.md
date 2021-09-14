# SQL & ORM

> 0914 workshop

## 1. SQL Query

> 위 countries 테이블을 바탕으로 아래 문제에 해당하는 SQL query문을 작성하고 실행하시오

1) countries 테이블을 생성하시오.

```sqlite
CREATE TABLE classmates(
room_num TEXT NOT NULL,
check_in TEXT NOT NULL,
check_out TEXT NOT NULL,
grade TEXT NOT NULL,
price INT NOT NULL
);
```

2. 데이터를 입력하시오.

```sqlite
INSERT INTO classmates VALUES
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);
```

3. 테이블의 이름을 hotels로 변경하시오.

```sqlite
ALTER TABLE classmates RENAME TO hotels;
```



4. 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오.

```sqlite
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

--B203|900
--1102|850
```



5. grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.

```sqlite
SELECT grade, COUNT(grade) FROM hotels GROUP BY grade ORDER BY COUNT(grade) DESC;

/* 
suite|2
superior|1
deluxe|1
*/
```



6. 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.

```sqlite
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='deluxe';

--B203|2019-12-31|2020-01-03|suite|900
--303|2020-01-01|2020-01-03|deluxe|500
```



6. 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

```sqlite
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price ASC;
```

- 오름차순이 default이기때문에 `ASC` 적지 않아도 무방하다.



## 2. SQL ORM 비교

1. user 테이블 전체 데이터를 조회하시오.

```sqlite
SELECT * FROM users_user;
```

```shell
User.objects.all()
```

2. id가 19인 사람의 age를 조회하시오

```sqlite
SELECT age FROM users_user WHERE id=19;
```

```shell
User.objects.get(pk=19)
```

3. 모든 사람의 age를 조회하시오

```sqlite
SELECT age FROM users_user;
```

```shell
User.objects.values('age')
```

4. age가 40 이하인 사림들의 id와 balance를 조회하시오

```sqlite
SELECT id, balance FROM users_user WHERE age<=40;
```

```shell
User.objects.filter(age__lte=40).values('id','balance')
```

5. last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오. 

```sqlite
SELECT first_name FROM users_user
WHERE last_name ='김' AND balance >= 500;
```

```shell
User.objects.filter(last_name='김', balance__gte=500).values('first_name')
```

6. first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오. 

```sqlite
SELECT balance FROM users_user 
WHERE first_name LIKE '%수' AND country='경기도';
```

```shell
User.objects.filter(first_name__endswith='수', country='경기도')
```

7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오. 

```sqlite
SELECT COUNT(*) FROM users_user
WHERE balance >= 2000 OR age <= 40;
```

```shell
User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()
```

8. phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오. 

```sqlite
SELECT COUNT(*) FROM users_user
WHERE phone LIKE '010%';
```

```shell
User.objects.filter(phone__startswith='010').count()
```

9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오.

```sqlite
UPDATE users_users SET country='경기도'
WHERE first_name='옥자' AND last_name='김'
--확인
SELECT country FROM users_user
WHERE first_name='옥자' AND last_name='김';
```

```shell
user = User.objects.get(first_name='옥자', last_name='김')
user.country='경기도'
user.save()
```

10. 이름이 ‘백진호’인 사람을 삭제하시오. 

```sqlite
DELETE FROM users_user 
WHERE first_name='진호' AND last_name='백'

SELECT * FROM users_user 
WHERE first_name='진호' AND last_name='백'
```

```shell
User.objects.get(first_name='진호', last_name='백').delete()

User.objects.get(first_name='진호', last_name='백')
```

11. balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오

```sqlite
SELECT first_name, last_name, balance FROM users_user
ORDER BY balance DESC LIMIT 4;
```

```shell
User.objects.values('first_name', 'last_name', 'balance').order_by('-balance')[:4]
```

12. phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오. 

```sqlite
SELECT * FROM users_user
WHERE phone LIKE '%123%' AND age<30;
```

```shell
User.objects.filter(phone__contains='123', age__lt=30)
```

13. phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오

```sqlite
SELECT DISTINCT country FROM users_user
WHERE phone LIKE '010%';
```

```shell
User.objects.filter(phone__startswith='010').values('country').distinct()
```

14. 모든 인원의 평균 age를 구하시오.

```sqlite
SELECT AVG(age) FROM users_user;
```

```shell
User.objects.aggregate(Avg('age'))
```

15. 박씨의 평균  balance를 구하시오 

```sqlite
SELECT AVG(balance) FROM users_user
WHERE last_name='박';
```

```shell
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```

16. 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오. 

```sqlite
SELECT MAX(balance) FROM users_user
WHERE country='경상북도';
```

```shell
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```

17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오

```sqlite
SELECT first_name FROM users_user
WHERE country='제주특별자치도' ORDER BY balance DESC LIMIT 1;
```

```shell
User.objects.filter(country='제주특별자치도').values('first_name').order_by('-balance')[:1]
```

