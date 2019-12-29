# Git

git에 대해서 공부를 해보았습니다.



## git의 혁신 - branch

지금부터 branch를 만드는 방법에 대해서 알아보겠습니다.

Tip

> add와 commit을 동시에 하는 방법

```shell
$ git commit -am "커밋 메세지"
```

**But -a는 한번도 add한 적이 없는 파일은 되지 않는다**



### Branch를 나누는 이유

1. 고객 맞춤으로 몇몇 기능을 추가 할 때
2. 개발자 자신이 필요 없어 보이는 기능을 추가해 달라고 고객이 요청하는 경우 다시 되돌아 갈 때
3. 테스트를 통해 문제점을 확인해 볼 때



##### branch 확인

```shell
$ git branch
> * master
```

위 명령어를 통해 branch를 확인할 수 있다. 

`*master`는 현재 속해 있는 branch를 나타낸다.



##### branch 만들기

```shell
$ git branch exp  # exp : branch 이름
```



##### branch 없애기

```shell
$ git branch -d
```



##### branch 이동

```shell
$ git checkout exp # exp : 이동할 branch
```



이동한 exp branch에서 파일을 만들어도 master branch에 가면 파일들이 사라지고 원래 master branch에서 만들어진 파일들만 존재한다.



### branch 정보확인



##### 로그에 모든 branch를 표시하고, 그래프로 표현하고, 브랜치 명을 표시하고, 한줄로 표시할 때

```shell
$ git log --branches --decorate --graph --oneline
```



##### branch 간에 비교할 때

```shell
$ git log "비교할 브랜치 명 1".."비교할 브랜치 명 2"
```

-p : 코드를 비교할 때



##### branch 간에 코드를 비교할 때

```shell
$ git diff "비교할 브랜치 명 1".."비교할 브랜치 명 2"
```



### branch 병합



##### B branch를 A branch로 병합할 때

```shell
$ git checkout A
$ git merge B
```



