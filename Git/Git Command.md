### Git Command

> git 명령어 정리

0. init

   * ```git init```
   * ```.git/``` 폴더를 생성해준다.

   ![스크린샷 2020-12-29 15.13.44](/Users/kyh/Desktop/스크린샷 2020-12-29 15.13.44.png)

![사진에 대한 설명]()

1. add

   * ```git add <추가하고싶은 파일>```
     * git add . : 현재 폴더의 모든 파일과 폴더를 add
   * working directory -> staging area 로 파일 이동

2. config

   * ```git config --global user.email "myemail@gamail.com"```
     * 이메일의 경우 깃헙에 올릴경우 잔디가 심어지는 기준이므로 정확하게 입력 !

3. commit

   *  ```git commit -m "메세지"```
   * 스냅샷을 찍는 동작
   * add 되어있는 파일들을 하나의 묶음으로 저장
   * 메세지에 들어가는 내용은 기능 단위로

4. remote

   * ```git remote add origin <주소>```
   * 원격 저장소와 현재 로컬 저장소를 연결.

5. push

   * ```git push origin master```

   * 원경저장소에 로컬 저장소의 데이터를 전송

     