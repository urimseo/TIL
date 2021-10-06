# DB

## 1. Database

- 데이터 베이스는 체계화된 데이터의 모임 (표- `RDBMS`, 사전형- `NOSQL`)
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 (하나 이상의) 자료의 모음으로 그 내용을 고도로 구조화 검색과 생신의 효율화를 꾀한 것



### 1.1 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보를 보장)
- 데이터 일관성 (언제봐도 똑같음!)
- 데이터 독립성(물리적/논리적)  -> 수정, 삭제해도 서로 영향 없음

- 데이터 표준화
- 데이터 보안 유지

## 2. RDB

> 관계형 데이터베이스 (RDB)

- Relational Database
- 키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스 
- 관계형 모델에 기반

### 2.1 스키마

> 스키마(schema) : 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것 .

| column  | datatype |
| ------- | -------- |
| id      | INT      |
| name    | TEXT     |
| address | TEXT     |
| age     | INT      |



### 2.2 테이블

> 테이블 (table) : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

| id   | name   | address | age  |
| ---- | ------ | ------- | ---- |
| 1    | 홍길동 | 제주    | 20   |
| 2    | 김길동 | 서울    | 30   |
| 3    | 박길동 | 독도    | 40   |

### 2.3 열

> 열 (Column) : 각 열에는 고유한 데이터 형식이 지정됨.

- 열, 컬럼, 필드 등의 이름으로 불림

### 2.4 행

> 행 (row) : 실제 데이터가 저장되는 형태

- 행, 로우, 레코드 등의 이름으로 불림 

### 2.5 기본키

> 기본키 (Primary Key) : 각 행(레코드)의 고유 값

- 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨(PK)

## 3. RDBMS

> 관계형 데이터베이스 관리 시스템(RDBMS)

- Relational Database Management System
- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

- 예시
  - MySQL, SQLite, PostgreSQL, ORACLE, MS SQL

##### SQLite

- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

## 4. SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어

- 데이터베이스 스키마 생성 및 수정

- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

### 4.1 SQL 분류

| 분류                                                      | 개념                                                         | 예시                                           |
| --------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| DDL - 데이터 정의 언어<br />(Data Definition Language)    | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE <br />DROP <br />ALTER                  |
| DML - 데이터 조작 언어<br /> (Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT <br />SELECT <br />UPDATE <br />DELETE  |
| DCL - 데이터 제어 언어<br /> (Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT <br />REVOKE<br /> COMMIT <br />ROLLBACK |

### 4.2 SQL Keywords

> Data Manipulation Language

- INSERT - 새로운 데이터 삽입(추가) - C
- SELECT - 저장되어있는 데이터 조회 - R
- UPDATE - 저장되어있는 데이터 갱신 - U
- DELETE - 저장되어있는 데이터 삭제 - D



### 4.3 테이블 생성 및 삭제 

1. 데이터 베이스 생성하기

```sqlite
sqlite3 filename.sqlite3
sqlite> .database
```

- `.`은 sqlite 프로그램의 기능을 실행하는 것. sql 문법 아님!!

- `filename`에는 불러올 파일명 작성
- `.database`로 db연결 확인 



2. `csv` 파일을 table로 만들기

```sqlite
.mode csv
.import dbfilename.csv tablename
.tables
> tablename
```

- `dbfilename`에는 생성해놓은 db파일명을 작성
- `tablename`에는 기존 생성되어있는 table이름을 작성 

- 예시 > `import hellodb.csv examples`



2. SELECT

```sqlite
SELECT * FROM examples;
```

- `SELECT` 문은 특정 테이블의 레코드(행) 정보를 반환!
- `*`는 전체 컬럼을 불러오겠다는 의미 

> (Optional) 터미널 view 변경하기

```sqlite
--컬럼의 이름을 필드 위에 같이 나타내줌
.headers on

-- 컬럼과 필드를 표처럼 깔끔하게 나타내줌
.mode column

--> 이 다음에 SELECT * FROM exampels; 
```



3. CREATE TABLE

> 데이터베이스에서 테이블 생성

```sqlite
CREATE TABEL classmates(id INTEGER PRIMARY KEY, name TEXT);
```

- id는 int형으로 pk값으로 지정, 이름은 TEXT로 

> 특정 테이블의 schema 조회

```sqlite
.schema classmates 
```

- 방금전 생성한 classmates 테이블의 스키마 

  -> CREATE TABEL classmates(id INTEGER PRIMARY KEY, name TEXT); 



4. DROP TABLE

> 데이터베이스에서 테이블 제거 

```sqlite
DROP TABLE classmates;
```



## 5. CRUD

### 1. CREATE

#### 1.1 INSERT

> 테이블에 단일 행 삽입 (inserting a single row into a table)

```sqlite
INSERT INTO 테이블이름(컬럼1, 컬럼2...) VALUES (값1, 값2,...);
```

- 특정 테이블에 레코드(행)을 삽입(생성)

  ```sqlite
  INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
  ```


