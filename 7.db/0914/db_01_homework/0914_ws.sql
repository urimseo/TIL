--테이블 생성
CREATE TABLE classmates(
room_num TEXT NOT NULL,
check_in TEXT NOT NULL,
check_out TEXT NOT NULL,
grade TEXT NOT NULL,
price INT NOT NULL
);

--데이터 입력
INSERT INTO classmates VALUES
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);

--데이터 조회 
SELECT * FROM classmates;

--sqlite프로그램->는 실시간 코드 실행 프로그램 -> 여기서만 .명령어가 작동 
-- / SQLite -> python file처럼 sqlfile  -> c드라이브의 exe프로그램 실행한 것 


--테이블 이름 변경
ALTER TABLE classmates RENAME TO hotels;

-- 4. 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오.
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

--5. grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.
SELECT grade, COUNT(grade) FROM hotels GROUP BY grade ORDER BY COUNT(grade) DESC;

--6.
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='deluxe';

--7
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price ASC;