# JPA란?

<aside>
💡 자바 어플리케이션에서 관계형 데이터베이스를 사용하는 방식을 정의한 인터페이스

</aside>

- JPA란 자바 ORM 기술에 대한 API 표준 명세를 의미한다.

- JPA는 특정 기능을 하는 라이브러리가 아닌 ORM을 사용하기 위한 인터페이스를 모아둔 것이다.

- JPA는 자바 어플리케이션에서 관계형 데이터베이스를 어떻게 사용해야 하는지 저의 하는 방법중 하나로 단순한 명세이기 때문에 구현이 없다.

- JPA를 정의한 `java.persistence` 패키지의 대부분은 interface, enum, Exception, Annotation들로 이루어져 있다.

- JPA의 핵심이 되는 EntityManager는 아래와 같이 java.persistence 패키지 내에 interface로 정의되어 있다.

- JPA를 사용하기 위해서는 JPA를 구현한 ORM 프레임워크(Hibernate, EclipseLink, DataNucleus..)를 사용해야 한다. 주로 Hibernate를 많이 사용하는 이유는 가장 범용적으로 다양한 기능을 제공하기 때문이다.

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/303051ce-9c68-4207-885e-6905253e6818/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221023T172325Z&X-Amz-Expires=86400&X-Amz-Signature=a1091fa8b9f5aa092ab6fbf7a5cca6b9fc9216e957cce2e1f78c170aed91a725&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

## 동작 과정

- JPA는 애플리케이션과 JDBC 사이에서 동작한다.
- 개발자가 JPA를 사용하면 JPA 내부에서 JDBC API를 사용하여 SQL을 호출하여 DB와 통신한다.

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0c54c845-6751-4a9d-9c7e-194e482eb9db/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221023T172336Z&X-Amz-Expires=86400&X-Amz-Signature=25895509e6b204cb1e7f8ac6dae08efe1fc1e1b8cba02dd12dc5929db7973f1a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/bd8d1e75-ae29-4ab9-bffb-3faddf1203bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221023T172345Z&X-Amz-Expires=86400&X-Amz-Signature=12766b7cf3df70bd6e1df0f139b14508f1ab8c6ed7208386155c3ba161c29df6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

# 2. Hibernate

<aside>
💡 Hibernate는 ‘JPA’라는 명세의 구현체이다.
JPA와 Hibernate는 자바의 interface와 해당 interface를 구현한 class와 같은 관계

</aside>

- Hibernate는 JPA의 구현체이므로 JPA를 사용하기 위해 반드시 Hibernate를 사용할 필요가 없다.
- JPA의 핵심인 `EntityManagerFactory` `EntityManager` `EntityTransaction` 을
  Hibernate에서는 `SessionFactory` `Session` `Transaction` 으로 상속받고 각각 `Impl` 로 구현하고 있다.

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/da0291eb-bd17-4782-aa5c-2915813850c2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221023T172355Z&X-Amz-Expires=86400&X-Amz-Signature=02f74add40833d36d4d214fc82a7adc6e6ef50f79d5a4f31e8dce9592422f7c6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

## 장점

- 생산성
  - Hibernate는 SQL을 직접 사용하지 않고 메소드 호출만으로 query가 수행되기 때문에 반복적인 SQL사용과 CRUD 작업을 직접 하지 않아 생산성이 높아진다.
- 유지보수
  - Mybatis에서는 관련 DAO의 파라미터, 결고, SQL등 모두 수정해야 하지만 JPA는 이런 일을 대신해주기 때문에 유지보수가 용이하다.
- 객체지향적 개발
  - 객체지향적으로 데이터를 관리할 수 있기 때문에 비즈니스 로직에 집중할 수 있다.
  - 로직을 쿼리가 아닌 객체 자체에 집중할 수있다.
- 특정 벤더에 종속적이지 않다.
  - 여러 DB벤더(Mysql, Oracle 등) 마다 SQL 사용이 다르기 때무에 개발 시 선택한 DB를 나중에 변경하는 것이 어렵다.
  - 그러나, JPA는 추상화된 데이터 접근 계층을 제공하기 때문에 특정 벤더에 종속적이지 않다.

## 단점

- 어렵다
  - 많은 내용이 담겨 있어 잘 이해하고 사용하지 않으면 데이터 손실이 일어날 수 있다.
- 성능
  - 메소드 호출로 쿼리 실행을 하기 때문에 직접 호출보다는 성능이 떨어질 수 있다.
  - but 초기의 orm은 그랬으나, 지금은 많이 발전하고 있고 좋은 성능 보여준다.
- 세밀함이 떨어진다
  - 객체간의 매핑(Entity Mapping)이 잘못되거나 잘못 사용하여 의도치 않은 동작을 할 수도 있다.
  - 복잡한 통계 분석 쿼리를 메소드 호출로 처리하는 것은 힘들다.
    - 이를 보완하기 위해 JPA에서는 JPA와 유사한 JPQL을 지원한다.
    - SQL 자체 쿼리를 작성할 수 있도록 지원하기도 함

# 3. Spring Data JPA

![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8fa06053-53a2-474e-9d14-39b3fb92ab2e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221023%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221023T172404Z&X-Amz-Expires=86400&X-Amz-Signature=7e065bfdf74229e30768164c49dea28a9ae959bfd708f586e548d2eae284395b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- JPA를 쉽게 사용하기 위해 스프링에서 제공하는 프레임워크

- 추상화 정도는 `Spring-Data-Jpa` > `Hibernate` > `JPA` 이다.

- Hibernate를 쓰는것과 Spring Data JPA는 사용하는데에 큰 차이가 없으나,,,,
  
  - 구현체 교체의 용이성
  - 저장소 교체의 용이성
  
  의 이유에서 Spring Data JPA를 사용하는게 더 좋다.
  
  <aside>
  💡 Spring Data JPA, Spring Data MongoDB, Spring Data Redis등 Spring Data의 하위 프로젝트들은 findAll(), save()등을 동일한 인터페이스로 가지고 있기 때문에 저장소를 교체해도 기본적인 기능이 변하지않는다.
  
  </aside>

- `EntityManager` 을 실제 개발에서 사용하지않고 `Repository`를 정의하여 사용하는 것이 Spring Data JPA를 사용한 것이고, 이것이 핵심!

- 사용자가 `Repository` 인터페이스에 정해진 규칙대로 메소드를 입력하면, Spring이 알아서 해당 메소드 이름에 적합한 Query를 날리는 구현체를 만들어서 Bean으로 등록해준다.

- Ex) 좋아요 한 Item

```java
package ssoaks.ssoak.api.auction.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ssoaks.ssoak.api.auction.entity.Like;

import java.util.List;

public interface LikeRepository extends JpaRepository<Like, Long> {

    Like findByItemSeqAndMemberSeq(Long itemSeq, Long memberSeq);

    Integer countLikeByItemSeq(Long itemSeq);

    List<Like> findAllByItemSeq(Long itemSeq);
}
```

## Spring Data Jpa와 Hibernate의 차이점

- Hibernate는 JPA 구현체이고, Spring Data JPA는 JPA에 대한 데이터 접근의 추상화이다
- Spring Data JPA는 항상 Hibernate와 같은 JPA 구현체가 필요하다!!
