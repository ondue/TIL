### 원격저장소 실습

> 맥북 => 윈도우 데스크탑

### git bash 설치

* 이미 설치가 되있었다 -> 멋모르고 설치한 것으로 추정

### Clone

- 원격 저장소를 복제

```bash
$ git clone https://github.com/ondue/TIL.git
Cloning into 'TIL'...
remote: Enumerating objects: 46, done.
remote: Counting objects: 100% (46/46), done.
remote: Compressing objects: 100% (33/33), done.
remote: Total 46 (delta 9), reused 46 (delta 9), pack-reused 0
Unpacking objects: 100% (46/46), done.
```

- 해당 폴더로 이동 및 사용자 설정

```bash
$ git config --global user.email "ondue@kakao.com"
$ git config --global user.name "ondue"
$ git config --global -l
user.email=ondue@kakao.com
user.name=ondue
```

### 추가해보기

* 원격저장소 실습 내용을 저장하는 파일 생성

```bash
$ touch 09_remote_tr.md
```

* 해당 내용까지 저장 후 push

