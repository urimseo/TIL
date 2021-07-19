

# 02_Github

## 원격 저장소 (remote repository)

1. 로컬 git 저장소 준비
2. Github repository 생성
3. Repository default branch 변경 (settings -> repositories)
   - main -> master로 변경

![tempsnip](C:\Users\user\Pictures\tempsnip.png)

## **명령어**

#### **원격 저장소 주소 추가**

```
$ git remote add origin 저장소URL
```

> "git에게 원격 저장소(remote) 추가해줘(add) origin 이라는 이름으로 저장소  URL을!"

- origin은 원격 저장소 이름

  

#### **원격 저장소 목록 보기**

```
$ git remote -v
origin  <https://github.com/urimseo/TIL.git> (fetch)
origin  <https://github.com/urimseo/TIL.git> (push)
```

> 잘못 add 한 경우 삭제하기$ git remote rm origi



#### **원격 저장소에 업로드 (push)**

```
$ git push -u origin master

Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 645 bytes | 645.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To <https://github.com/woongedu/TIL.git>
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

> "git아, push 해줘 origin이라는 이름의 원격저장소에 master 브랜치로!!!!"

> 원격 저장소에는 commit이 올라간다 !!!즉, commit 이력이 없다면 push 할 수 없다.

- 두번째 push 부터는 `u` 생략 가능

  

#### **pull**

- 원격 저장소의 변경사항을 받아옴 (업데이트)

```
$ git pull origin master
```



#### **clone**

- 원격 저장소 전체를 복제

```
$ git clone 저장소URL
```

> [⚠주의⚠] clone 받은 프로젝트는 이미 git init이 되어있음 (remote 도 추가되어 있음)





---

### Git 기존 저장소의 branch명 변경

> 간단한 트러블 슈팅 과정!

​	

- 이미 만들어둔  repository 저장소가 main 브랜치로 설정되어 있어서 main --> master로 브랜치 변경!

1. Repository default branch 확인 (Settings -> Repositories)

   > master로 변경 되어 있는 상태였기 때문에 추가 변경사항은 없었음

2. 브랜치 이름을 변경할 저장소 클릭 -> Settings ->Branches

   - 연필 아이콘을 클릭하여 main -> master 로 변경
   - `master` 입력하고 `Rename branch` 클릭하면 github 화면에서 저장소 정보가 master으로 변경된다.

   ![](C:\Users\user\Pictures\tempsnip.png)

3. git bash 창에서 저장소 이름 변경하기

   - local에 저장소를 clone하고 push도 진행되었던 상태여서 기본 저장소 이름 변경이 필요했다.

   ```git
   git branch -m main master
   git fetch origin
   git branch -u origin/master master
   ```

![image-20210717010616935](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20210717010616935.png)



> 저장소 변경 완료! 항상 한번에 해결이 안돼서 돌아돌아 가지만, 많이 배우는 과정이라 뿌듯하다 😁