# 마크다운(MarkDown)

### 마크다운(MarkDown)이란? 

- 파일 확장자가 **`.md`**로 된 파일.
   **`README.md`**  이 파일이 마크다운 문법으로 작성된 파일임.
- 사용법이 매우 쉽고, 빠르게 문서를 정리 가능
- HTML 마크업을 대신할 수 없어 지나친 의존보다는 쉽고 빠르게 작성하는 용도로 적합

   


## 마크다운(MarkDown)

### 마크다운의 장점

1. 간결하고 문법이 쉽다.
2. 관리가 쉽다.
3. 지원 가능한 플랫폼과 프로그램이 다양하다.
4. 버전관리 시스템을 이용하여 변경이력을 관리할 수 있다.

### 마크다운의 단점

1. 표준이 없어 사용자마다 문법이 상이할 수 있다.
2. 모든 HTML 마크업을 대신하지 못한다.



# 마크다운 문법(syntax)

### 제목(Header)

**`<h1>`**부터 **`<h6>`**까지 제목 표현  - 글머리 1~6까지만 지원

```
# 제목 H1
## 제목 H2
### 제목 H3
#### 제목 H4
##### 제목 H5
###### 제목 H6
```



### 강조(Emphasis)

각각 **`<em>`**, **`<strong>`**, **`<del>`** 태그로 변환됨.

밑줄을 입력하고 싶다면 **`<u></u>`** 태그를 사용

```
이텔릭체는*별표(asterisks)* 혹은 _언더바(underscore)_
두껍게는**별표(asterisks)** 혹은 __언더바(underscore)__

**_이텔릭체_와 두껍게**를 같이 사용가능.
취소선은 ~~물결표시(tilde)~~.
<u>밑줄</u>은 `<u></u>`
```



### 목록(List)

**`<ol>`**, **`<ul>`** 목록 태그로 변환됨.

```
1. 순서가 필요한 목록
1. 순서가 필요한 목록
  - 순서가 필요하지 않은 목록(서브)
  - 순서가 필요하지 않은 목록(서브)
1. 순서가 필요한 목록
  1. 순서가 필요한 목록(서브)
  1. 순서가 필요한 목록(서브)
1. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  * 별표(asterisks)
  + 더하기(plus sign)
```

1. 순서가 필요한 목록
2. 순서가 필요한 목록
   - 순서가 필요하지 않은 목록(서브)
   
   - 순서가 필요하지 않은 목록(서브)
   
     

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  - 별표(asterisks)
  - 더하기(plus sign)



### 링크(Links)

**`<a>`**로 변환

```
[GOOGLE](<https://google.com>)

[NAVER](<https://naver.com> "링크 설명(title)을 작성하세요.")

[상대적 참조](../users/login)

[Dribbble][Dribbble link]

[GitHub][1]

문서 안에서 [참조 링크]를 그대로 사용할 수도 있습니다.

문서 내 일반 URL이나 꺾쇠 괄호(`< >`, Angle Brackets)안의 URL은 자동으로 링크를 사용
구글 홈페이지:<https://google.com>
네이버 홈페이지: <https://naver.com>

[Dribbble link]:<https://dribbble.com>
[1]:<https://github.com>
[참조 링크]:<https://naver.com> "네이버로 이동!"
```

[GOOGLE](https://google.com/)

문서 안에서 [참조 링크](https://naver.com/)를 그대로 사용할 수 있음

다음과 같이 문서 내 일반 URL이나 꺾쇠 괄호(**`< >`**, Angle Brackets)안의 URL은 자동으로 링크를 사용



### 이미지(Images)

**`<img>`**로 변환. 링크과 비슷하지만 앞에 **`!`**가 붙는다.

```
![대체 텍스트(alternative text)를 입력하세요!](<http://www.gstatic.com/webp/gallery/5.jpg> "링크 설명(title)을 작성하세요.")

![Kayak][logo]

[logo]:<http://www.gstatic.com/webp/gallery/2.jpg> "To go kayaking."
```



### 코드(Code) 강조

<pre>, **<code>**로 변환. 숫자 1번 키 왼쪽에 있는 ```(Grave) 입력



### 인라인(inline) 코드 강조

```
`background`혹은 `background-image` 속성으로 요소에 배경 이미지를 삽입가능
```

**`background`**혹은 **`background-image`** 속성으로 요소에 배경 이미지를 삽입



### 수식블록

ctrl + shift + M
$$
a+b = c
$$



### 블록(block) 코드 강조

**```**를 3번 이상 입력하고 코드 종류 작성. (ctrl + shift +k)

```html
​```html
<a href="<https://www.google.co.kr/>" target="_blank">GOOGLE</a>
```

```css
.list > li {
  position: absolute;
  top: 50px;
}
```

```javascript
function func() {
  var a = 'hello';
  return a;
}
```



### 표 만들기

```
## 표(Table)

**`<table>`** 태그로 변환
헤더 셀을 구분할 때 3개 이상의 **`-`**(hyphen/dash) 기호가 필요
헤더 셀을 구분하면서 **`:`**(Colons) 기호로 셀(열/칸) 안에 내용을 정렬
가장 좌측과 가장 우측에 있는 **`|`**(vertical bar) 기호는 생략 가능
```

| 값         |                    의미                     |   기본값 |
| ---------- | :-----------------------------------------: | -------: |
| `static`   |        유형(기준) 없음 / 배치 불가능        | `static` |
| `relative` |        요소**자신**을 기준으로 배치         |          |
| `absolute` | 위치 상***부모*(조상)요소**를 기준으로 배치 |          |
| `fixed`    |       **브라우저 창**을 기준으로 배치       |          |



### 인용문(blockQuote)

```
## 인용문(BlockQuote)  
**(ctrl + shift +q)**
```

**`<blockquote>`** 

> 인용문  (ctrl + shift +q)
>
> > 중첩된 인용문(nested blockquote)
> >
> > > 중중첩된 인용문

