-- 주석
/* 여러줄 주석
    여러줄 주석! 
    SQL 구문은 대소문자 구분x(중요!!!)
    기본 문법 (변하지 않는 부분 -> 대문자)
    변하는 부분 -> 소문자
*/

-- 데이터 전체 조회 SELECT
SELECT * FROM examples;

--select * from examples:

--테이블 생성
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

CREATE TABLE classmates(
name TEXT,
age INT,
address TEXT
);
-- INT 랑 INTEGER랑 똑같음

--데이터 전체 조회
SELECT * FROM classmates;

--데이터 입력
INSERT INTO classmates (name, age) VALUES ('홍길동', 600)

--43P
INSERT INTO classmates VALUES ('홍길동', 30, '서울');

--pk값 
SELECT rowid, * FROM classmates;

--테이블 삭제 
DROP TABLE classmates;

--다시 생성
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');

INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울')



-- drop으로 삭제 후 pk값 빼고 다시 생성
CREATE TABLE classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

--다중 데이터 삽입 
INSERT INTO classmates VALUES
('홍길동', 31, '서울'),
('김철수', 32, '경기'),
('이싸피', 33, '광주'),
('박삼성', 34, '부산'),
('최전자', 35, '대전');

--특정 컬럼만 조회(select) - 63p
SELECT rowid, name FROM classmates;

--limit
SELECT rowid, name FROM classmates LIMIT 1;

--offset
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

--where 주소가 서울인 사람만 찾아오기 if 문 같은것...
-- 표시해 줄 데이터는 select에서 결정 where가 조건!
SELECT rowid, name FROM classmates WHERE address='서울';

--distinct
SELECT DISTINCT age FROM classmates;

--delete 데이터 삭제
DELETE FROM classmates WHERE rowid=5;

INSERT INTO classmates VALUES('최전자', 35,'대전');

--데이터 수정 update
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;


--98p Table users 생성
CREATE TABLE users(
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

--where
SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age >= 30 AND last_name='김';

--count, avg, max, min, sum
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age>=30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(age) FROM users WHERE age>=30;

--like operator 120p
SELECT * FROM users WHERE age LIKE '2_';

SELECT COUNT(*) FROM users WHERE age LIKE '2_';

SELECT * FROM users WHERE phone LIKE '02-%';

SELECT * FROM users WHERE first_name LIKE '%준';

SELECT * FROM users WHERE phone LIKE '%5114%';

--order by
SELECT * FROM users ORDER BY age ASC;

SELECT * FROM users ORDER BY age, balance DESC;
-- age는 기본값(ASC)정렬, 잔고 DESC정렬
-- 나이로 오름차순 정렬 한 후, 같은 나이에서는 DESC 정렬 

--P.136
SELECT rowid, * FROM users ORDER BY age ASC LIMIT 10;

SELECT * FROM users ORDER BY age ASC, last_name ASC LIMIT 10;


--group by p.141
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name; --COUNT(*)의 이름을 name_count로 변경


--alter table

CREATE TABLE articles(
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES('1번제목', '1번내용');

ALTER TABLE articles RENAME TO news;

--새로운 컬럼 추가
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL; -- 에러남

--해결방법 1 notnull 제외
ALTER TABLE news ADD COLUMN created_at TEXT; 
INSERT INTO news VALUES('제목', '내용', datetime('now'));
SELECT * FROM news;

-- 해결방법2 기본값 지정 
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '임시제목';