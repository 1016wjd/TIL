# git 

## 버전관리

### 분산 버전 관리 시스템 (DVCS)

![DVCS](./assets/distributed.png)



## 명령어
```shell
git init
```
- .git directory를 생성하는 명령어

```shell
git add . 
```
- `working directory`에 있는 파일, 폴더를 `index`에 추가 
- add 하기 전 파일이 저장 되어있는지 확인 

```shell 
git commit -m 'message'
```
- 인덱스에 올라간 파일들 저장 


```shell
git push origin master 
```
- `master` 배린치를 `origin` 원격저장소로 업로드