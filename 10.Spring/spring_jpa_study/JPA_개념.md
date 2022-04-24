# JPA

## ORM(Object - Relational Mapping)

- 객체와 관계형데이터베이스 매핑. 객체와 DB 테이블이 매핑을 이루는 것
- 객체가 테이블이 되도록 매핑 시켜주는 프레임워크
- 프로그램의 복잡도를 줄이고 객체와 쿼리를 분리할 수 있음
- 트랜잭션 처리나 DB관련 작업들을 편리하게 처리
- SQL Query 대신 메서드로 데이터 조작 가능

------

## Hibernate

- JPA를 사용하기 위해 JPA를 구현한 ORM 프레임워크

------

## JPA(Java Persistence API)

- ORM을 사용하기 위한 인터페이스를 모아둔 API
- 자바 어플리케이션과 RDB를 사용하는 방식을 정의한 인터페이스
- ORM에 대한 자바 규격 API
- Hibernate, OpenJPA 가 JPA를 구현한 구현체(ORM을 사용하기 위한 인터페이스를 모아둔 것)
- 인터페이스 이기 때문에 JPA를 사용하기 위해서는 JPA를 구현한 Hibernate 같은 ORM 프레임워크를 사용해야 됨.

## Repository

### 장점

#### 1. 뛰어난 생산성과 유지보수가 용이함

- 더 직관적이고 비즈니스 로직에 집중할 수 있게 도와줌
- 객체지향적으로 DB를 관리할 수 있어서 전체 프로그램 구조를 일관되게 유지 가능
- 컬럼 추가시 SQL을 직접 작성하지 않아서 재사용성이 증가하고 유지보수가 편리해짐
- 컬럼 추가될 때 테이블 수정이나 SQL 수정하는 과정이 줄어듬
- 값을 할당하거나 변수 선언등의 부수적인 코드가 줄어듬
- 각각의 객체에 대한 코드를 별도로 작성하여 가독성이 좋음

#### 2. DBMS에 대한 종속성이 줄어듬

- DBMS 변경시 소스, 쿼리, 구현방법, 자료형 타입 등을 변경할 필요 없음
- 프로그래머는 Object에만 집중하면 되고 DBMS를 교체하는 작업에 비교적 적은 리스크와 시간이 소요됨

### 단점

#### 1. 어려움

- 장점을 잘 살리려면 많은 학습 필요
- 복잡한 쿼리 사용시 불리함
- 기존 DB 환경에서는 사용하기 어려움
- 잘못 사용할 경우 SQL문을 직접 사용하는 것보다 성능 떨어짐
- 대용량 기반의 환경에서 튜닝하기 어려워서 성능이 떨어질 수 있음

#### 예시

##### Entity 클래스

```java
import lombok.*;

import javax.persistence.*;

@Getter         // getter 메소드 생성
@Builder        // 빌더 사용할 수 있게 해줌
@AllArgsConstructor     // 모든 필드값을 파라미터로 받는 생성자 생성
@NoArgsConstructor(access = AccessLevel.PROTECTED)  // 파라미터가 없는 기본 생성자 자동 생성
@Entity(name = "member")    // 테이블 명을 name 에 작성
public class MemberEntity {
    @Id     // 기본키라는 것을 명시하는 역할
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 키 값의 자동생성 전략 설정. default: GenerationType.AUTO
    private long pid;

    @Column(nullable = false, unique = true, length = 30)
    private String username;

    @Column(nullable = false, length = 100)
    private String name;

    public MemberEntity(String username, String name) {     // username과 name 두 가지를 파라미터로 받는 생성자
        this.username = username;
        this.name = name;
    }
}
```

##### Repository

```java
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MemberRepository extends JpaRepository<MemberEntity, Long> {
}
```

##### Cotroller

```java
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController     // JSON 형태의 결과값을 반환해줌 (@ResponseBody가 필요 없음)
@RequiredArgsConstructor    // final 객체를 Constructor Injection 해줌. (Autowired 역할)
@RequestMapping("/v1")      // version1 의 API
public class MemberController {

    private final MemberRepository memberRepository;

    /**
     * 멤버 조회
     * @return
     */
    @GetMapping("member")
    public List<MemberEntity> findAllMember() {
        return memberRepository.findAll();
    }

    /**
     * 회원가입
     * @return
     */
    @PostMapping("member")
    public MemberEntity signUp() {      // 회원가입
        final MemberEntity member = MemberEntity.builder()      // builder를 이용해서 username, name 값을 준다. setter 개념
                .username("test_user@gmail.com")
                .name("test user")
                .build();
        return memberRepository.save(member);       // Repository에 save 즉 db에 값 저장
    }
}
```





참고 자료 및 출처

https://memostack.tistory.com/155

https://goddaehee.tistory.com/209