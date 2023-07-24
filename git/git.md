# git 

## 버전관리
 “버전 관리” 는 무엇이고 우리는 왜 이것을 알아야 할까? 버전 관리 시스템은 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템이다. 이 책에서는 버전 관리하는 예제로 소프트웨어 소스 코드만 보여주지만, 실제로 거의 모든 컴퓨터 파일의 버전을 관리할 수 있다.

### 분산 버전 관리 시스템 (DVCS)

![DVCS](./assets/distributed.png)

### 세가지 상태
![DVSC](./assets/areas.png)

## 명령어
```shell
git init
```
- .git directory를 생성하는 명령어

```shell
git add . 
```
- `working directory`에 있는 파일, 폴더를 `staging area`에 추가 
- add 하기 전 파일이 저장 되어있는지 확인 

```shell 
git commit -m 'message'
```
- `staging area`에 올라간 파일들 저장 

```shell
git remote add origin <remoteurl>
```
- 원격저장소 주소를 `origin`이라는 별명으로 저장
-  한번 연결 후 이후에는 push 명령어만 사용하여 업로드


```shell
git push origin master 
```
- `master` 배린치를 `origin` 원격저장소로 업로드