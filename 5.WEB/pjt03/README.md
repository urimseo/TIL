# Web PJT - 반응형 웹페이지 구성

[TOC]

### 1. 목표

- HTML을 통한 웹 페이지 마크업 분석
- CSS 라이브러리의 이해와 활용
- 컴포넌트 및 그리스 시스템 활용
- 커뮤니티 서비스 반응형 레이아웃 구성

---

### 2. 준비사항

#### A. 개발도구

1. Visual Studio Code
2. Google Chrome Browser
3. Bootstrap v5

#### B. 제공 Assets

| images/            | 사용할 이미지들이 들어 있습니다.                     |
| ------------------ | ---------------------------------------------------- |
| 01_nav_footer.html | 모든 페이지가 공유할 Navigation bar 및 Footer입니다. |
| 01_nav_footer.css  | Navigation bar 및 Footer의 커스텀 CSS입니다.         |
| 02_home.html       | 사용자가 처음 접속하면 보게 될 페이지입니다.         |
| 02_home.html       | home.html의 커스텀 CSS입니다.                        |
| 03_community.html  | 사용자들끼리 의견을 나누는 게시판입니다              |
| 03_community.css   | community.html 의 스타일의 커스텀 CSS입니다          |

#### C. 필수 라이브러리

- requests

---

### 3. 요구사항

> 커뮤니티 서비스 개발을 위한 화면 구성 단계로, 유저가 보는 프론트 엔드를 개발합 니다. 



#### A. 01_nav_footer

1. **네비게이션 바 (Navigation Bar)**

```html
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top py-0">
    <div class="container-fluid">
      <a class="navbar-brand py-0 " href="02_home.html">
        <img src="images/logo.png" alt="logo" width="130" height="50">
      </a>
      <button class="navbar-toggler " type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon d-none d-md-block"></span>
        <span class="fas fa-hamburger fa-lg d-block d-md-none"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarTogglerDemo02">
        <ul class="navbar-nav ">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="03_community.html">Communitiy</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#staticBackdrop" data-bs-toggle="modal">Login</a>
          </li>
      </div>
    </div>
  </nav> 
```

- 네비게이션 바는 `sticky-top`으로 상단에 고정하고, bootstrap의 `navbar-toggler` 속성이 있는 폼을 사용하였다. 
- `navbar-toggler`  양식에 반응형 웹이 들어가있어서 `breakpoint`를 변경해주었다.
- `md` 사이즈일때 `nav-toggler-icon`이 햄버거로 변해야 하는 과정에서 `d-none`을 사용했다. 
- d-none은 기본적으로 보이지 않는다!! 화면에서 숨기는 속성이고, 추가로 조건을 붙여 특정 사이즈 이상, 이하에서 보일 수 있게 `breakpoint`의 `col`을 설정해주면 된다.
- 햄버거와 `md`에서 보이는 조건을 역으로 설정하여 변화되는것처럼 보이게 하였다. 햄버거 이미지는  `fontawesome`을 가져왔다.

---

- `Login` 리스트에 `modal`을 활용해서 팝업으로 만들어야 하는데,  하이퍼링크에 어떻게 연결해야 하는지 몰라서 많이 헤맸던 것 같다. 
- `href=modal_id` 를 통해 모달id로 연결될 수 있게 하는 것을 알고, `modal`을 추가 작성하여 `Login`과 연결하였다. 

```html
  <!-- Modal -->
  <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title fw-bold" id="staticBackdropLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form class="mx-auto">
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label fw-bold">Username</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
      
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label fw-bold">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>
      
            <div class="mb-3 form-check flex-container">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label " for="exampleCheck1">Check me out</label> 
            </div>
          </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Submit</button>
          </div>
        </div> 
      </div>
    </div>
  </div> 
```

- `modal`은 기존 `Sign-in`을 만들어 봤기 때문에 bootstrap의 `modal`폼에 추가하는 형식으로 작성하였다. 
-  `modal`이`nav` 안에 있을 때는 `disable` 되어서 , 다른 `div`로 작성했더니 정상적으로 작성 폼이 나왔다. 
  `modal`은 `position:fixed` 인 다른 요소 내에 중첩될 때 문제가 발생할 수 있어 가장 최상단에 작성하는 것을 권장한다. `nav-bar` 를 `sticky-top`으로 고정시켜서 그런가 실행이 안되었던 것 같다.



2. footer

```html
  <footer class="d-flex  p-2 justify-content-center align-items-center fixed-bottom  bg-light text-secondary" >
    <p class="mb-0">Web-bootstrap PJT, by Urim</p>
  </footer>
```

- `footer`는 많이 해봐서 이젠 저절로 수평 수직정렬을 외우게 된 것 같다! 색상표도 점점 외워지는중이다!

---

#### B. 02_home

1. 네비게이션 바 

   > A에 작성한 `nav`바와 `foote`r를 그대로 가져와 작성했다. 
   >
   > 장고에서는 html을 따로 작성하고 `include`로 {% include "navbar.html" %}과 같이 불러와서 모듈로 사용했던 것 같다. 하나하나 직접 넣어보니 프레임워크의 고마움을 또다시 경험하게 되었다...!

2. Header

```html
<header>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/header1.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="images/header2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="images/header3.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </header>

  <h1 class="text-center fw-bold  p-5">Boxoffice</h1>
```

- `header`은 Bootstrap의 'Carousel 컴포넌트' 로 쉽게 구현하였다. 
  이미 있는 양식에서 크게 벗어나지 않고 다행히 한번에 하나의 `image`만 불러오면 되었기 때문에 어렵지 않았었다.
- `h1`클래스의 위치가 애매하여 `header` 바깥쪽에 따로 만들어줬다. 



3. Section

```html
<section class="row row-cols-1 row-cols-sm-2 row-cols-md-3 pb my-5">
    <article class="col">
      <div class="card">
        <img src="images/movie1.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Movie Title</h5>
          <p class="card-text">Plzzzzzzzzzzzzzzzzzzzzzzzzz </p>
        </div>
      </div>
    </article>
 <!-- article *5 중략 -->
    
  </section>
```

- `section`은 `breakpoint`를 사용하여 `sm` 미만는 그림 하나, `sm `이상은 그림2개, `md` 이상은 3개가 나오도록 반응형으로 구성하였다. 
- 아직 `flexbox`의 적용해야하는 기준을 잘 못잡겠다. 이번에도 또다시 `flexbox`의 여러 기능들과 정렬을 넣고 많은 실패 끝에... simple is the best를 찾아냈다. 
- 과거 프로젝트를 최대한 참고하지 말고 스스로 해보려고 했지만 많이 부족한걸 느꼈다.



#### c. 03_community

1. 네비게이션 바(Navigation Bar)

```python
<li class="nav-item">
  <a class="nav-link active" aria-current="page"  href="03_community.html">Communitiy</a>
</li>
```

- `Community` 탭에서는 해당 리스트를 강조하기 위하여  `activate` , `aria-current` 를 추가하고, `Home`에서 활성화를 제거하였다.



2. 게시판 목록

```html
	<div class="container"> 
      <div class="row">
        <aside class ="col-12 col-lg-2">
          <ul class= "list-group text-center">
            <a href="#" class="list-group-item list-group-item-action  text-primary ">Boxoffice</a>
            <a href="#" class="list-group-item list-group-item-action  text-primary ">Movies</a>
            <a href="#" class="list-group-item list-group-item-action  text-primary ">Genres</a>
            <a href="#" class="list-group-item list-group-item-action  text-primary ">Actors</a>
          </ul>
        </aside>
```

- 처음에 게시판 목록을 `container`안에 하지 않고 그냥 따로 작성했는데, `Board`와 함께 움직여야 한다는 명세서를 보고 다시 수정하였다! 이 부분에서 굉장히 많이 헤맸던 것 같다.

- 너비가 `lg` 일 때, 좌측 1/6 의 공간을 차지하게 하기 위해서 `col-lg-2`를 넣었고, 기본적으로는 전체 화면을 차지하게 하였다. 

  

3. 게시판

```html
          <!-- Board -->
        <section class="col-12 col-lg-10">
          <div class="d-none d-lg-block">
            <table class="table">
              <thead class="table-dark">
                <th scope="col">영화 제목</th>
                <th scope="col">글 제목 </th>
                <th scope="col">작성자</th>
                <th scope="col">작성시간</th>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Best Movie Ever</td>
                  <td>user</td>
                  <td> 1 minutes ago</td>
                </tr>
          <!-- <tr> 중략 -->
              </tbody>
            </table>
          </div>
        </section>
     </div>
```

- `lg` 이상 화면일 때 보이는 `table`이 `sidebar`와 한 줄에 나와야 하기 때문에 `.container > .row `에 같이 묶여 있다.
- `d-none`을 사용하여 `lg` 크기 이하일때는 보이지 않게 하고, `lg` 이상일 때 `block`으로 보이게 끔 반응형 웹을 구현하였다. 
- 나머지 테이블은 bootstrap을 가져다 수정하였다. 

---

- 너비가 `lg`(992px) 미만일 경우 게시글이 `article`로 보여야 하기 때문에 `article class`를 추가로 만들었다.
- 위의 nav 토글에서 햄버거로 변경하게 보이는것과 같이, `d-none`을 활용해서 위의 `table`과 교차지점에서 보이게 끔 하였다.
- `article`은 Bootstrap의 `List-group`을 사용하여 구성하였다.

---

- 게시판 탐색기 `pagination` 도 Bootstrap에서 가져와 사용하였고, `#`링크로연결 될 수 있도록 하였다. 
- 나중에 실제 여러 페이지가 생기면 링크를 연결해서 각각 다른 페이지의 data를 보여주게 될 것 같은데, 벌써 머리가 아프지만 궁금해졌다!

```html
      <nav aria-label="Page navigation example ">
        <ul class="pagination justify-content-center my-5">
          <li class="page-item"><a class="page-link" href="#">Previous</a></li>
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">3</a></li>
          <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul>
      </nav>
```



---



>프로젝트를 하면서 너무 많은 것을 알게 되었지만, 아직까지는 다트찍기로 구현하는 것 같다. 
>
>확실히 Bootstrap이 CSS를 하나하나 작성하는것 보다 훨씬 편하고, CSS에서 문제가 날 일이 없으니 훨씬 간편하다는 것을 느꼈다. 
>
>Bootstrap에서도 추가로 디자인요소를 더하려면 CSS를 작성해야겠지만, 이번 프로젝트에서는 CSS는 아예 수정을 하지 않고 html로만 작성했다.
>
>CSS의 스타일 적용 우선순위가 아직 헷갈려서 차마 작성하기가😥
>두렵지만 최대한 많이 도전해보고 만들어 보는게 답인것 같다









