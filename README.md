분산시스템 프로젝트
=============

### 분산 데이터베이스 Primary Based Protocol 성능 비교 분석

### 프로젝트 개요
Remote Write (Primary Based Protocol)를 사용하여 노드 갯수가 증가함에 따라 성능이 어떻게 변하는지 측정합니다.

노드는 리더노드 1개와 일반 노드 여러개로 구성되어있습니다.

### 환경

1. Ubuntu, MySQL를 사용합니다.

2. Node(Ubuntu) 갯수 제한은 없습니다.

### 사용방법

1. main.py이 있는 폴더에 ip.py를 만들어야합니다.

ip.py
```
ip="Input Your IP"

leaerIp = "Input Leader IP"

def isNotLeader():
    return not (ip == leaerIp)
```

2. 리더 노드부터 실행합니다.
```
py main.py
```

3. test/totalTest.py 안에 nodeList 리스트 값을 노드들의 IP로 수정해줍니다.
```
nodeList = [
    "15.164.166.41"#, "15.164.102.73", "15.164.165.83", "13.209.49.42", "15.164.163.33", "54.180.115.55", "13.209.4.198", "13.125.216.88"
]
```

4. totalTest.py를 사용하여 성능을 테스트합니다.
