# SQL & ORM

> 0914_homework

## 1. SQL 용어 및 개념

- 스키마: 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것
- 테이블: 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
- 컬럼: 고유한 데이터 형식이 지정되는 열
- 레코드: 단일 구조 데이터 항목을 가리키는 행
- 기본키: 각 행의 고유값

## 2. SQL 문법

> DML이 아닌 것은

1. CREATE
2. UPDATE
3. DELETE
4. SELECT

-> `1` CREATE는 DML이 아닌 DDL이다. DML은 INSERT!



## 3. Relational DBMS

> RDBMS의 개념적 정의와 이를 기반으로 한 DB-Engine의 종류 세가지 이상 작성하시오.

- 관계형 데이터 베이스 관리 시스템(Relational Database Management System)
- 관계형 모델을 기반으로 하는 데이터 베이스 관리시스템을 의미
- DB-Engine
  - MySQL
  - SQLite
  - PostgreSQL
  - ORACLE
  - MS SQL



## 4. INSERT INTO

> 다음과 같은 스키마를 가지는 테이블이 있을 때, 아래의 보기 중 틀린 문장을 고르시오

- `(4) insert into classmates (address, age, name) values ('seoul', 20, '홍길동')`

  -> 칼럼의 순서에 맞게 작성해야 한다. 

  

## 5. 와일드카드 문자

> SQL에서 사용 가능한 와일드카드 문자인 % 와 _을 비교하여 작성하시오.

- `%`  - percent sign

  -  이 자리에 문자열이 있을수도 있고 없을 수도 있다.
  - ex. 김% -> `김`으로 시작하는 모든 사람

- `_` - underscore

  - 반드시 이 자리에 하나의 문자가 존재해야 한다.

  - `a_` -> a로 시작하고 총 2자리인 값, `a__` -> a로 시작하고 총 3자리인 값  

  - ex. 김_ -> `김`으로 로 시작하는 두글자 이름을 가진 사람

    