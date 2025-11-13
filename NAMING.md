# 코딩 테스트 네이밍 컨벤션

> 3초 안에 변수명을 결정하기 위한 패턴화된 가이드

## 기본 원칙

1. **도메인 중심**: 문제의 개념을 반영하는 명사/동사 사용
2. **camelCase 사용**: `claimedAt`, `maxCount`, `isValid`
3. **의미 우선**: 타입보다는 역할과 의미를 표현
4. **일관성**: 같은 개념은 항상 같은 단어 사용

---

## 왜 자료구조 접미사를 피할까?

### ❌ 문제점: scoreMap, visitedSet, userList
```python
scoreMap = {}      # Map이라는 정보는 이미 {} 에서 보임
visitedSet = set() # Set이라는 정보는 이미 set()에서 보임
userList = []      # List라는 정보는 이미 []에서 보임
```

### ✅ 해결책: 의미 중심 네이밍
```python
scores = {}        # "점수들"이라는 의미에 집중
visited = set()    # "방문한 것들"이라는 의미에 집중
users = []         # "사용자들"이라는 의미에 집중
```

### 이유

1. **중복 정보 제거**
   - 자료구조는 코드에서 이미 명확함 (`{}`, `set()`, `[]`)
   - 타입 힌트가 있으면 더욱 불필요: `scores: dict[str, int] = {}`

2. **유연성**
   - 자료구조가 바뀌어도 변수명 유지 가능
   - `scoreList` → `scoreSet` 변경 시 모든 참조 수정 필요
   - `scores` → 자료구조 변경해도 변수명 그대로

3. **가독성**
   - `scores[name]`이 `scoreMap[name]`보다 자연스러움
   - `if user in visited`가 `if user in visitedSet`보다 읽기 쉬움

4. **의미가 중요**
   - "무엇을" 담는가가 "어떻게" 담는가보다 중요
   - 코드는 비즈니스 로직을 표현, 자료구조는 구현 세부사항

### 예외: 관계가 명확할 때만 접미사 사용

```python
# ✅ 관계를 표현하는 ByX 패턴
songsByGenre = {}      # 장르별로 노래들을 그룹화
countByName = {}       # 이름별로 카운트를 저장
indexByValue = {}      # 값으로 인덱스를 찾기

# 이런 경우 "By"가 자료구조가 아닌 관계를 표현
```

---

## 반복문 네이밍 패턴

### 1. 단일 컬렉션 순회
```python
# 복수형 컬렉션 → 단수형 아이템
for user in users:
for song in songs:
for edge in edges:
for participant in participants:
```

#### 특수 케이스: 복수 의미 단어
컬렉션 자체가 복수 의미인 경우 원소 네이밍:

```python
# ✅ 문법적 단수형
for person in people:
for child in children:

# ✅ data는 문맥에 맞게
for record in data:    # 레코드 데이터
for entry in data:     # 엔트리들
for row in data:       # 행 데이터
for value in data:     # 값들

# ✅✅ 가장 좋음: 도메인 의미 우선
for user in data:      # 사용자 데이터
for score in data:     # 점수 데이터
for song in data:      # 노래 데이터

# ❌ 비일상적 단어는 피하기
for datum in data:     # 어색함
```

**우선순위**:
1. 도메인 의미 (최우선): `for user in data`
2. 문법적 단수: `for person in people`
3. 문맥 단어: `for record in data`, `for entry in data`
4. 최후의 수단: `for item in data`

#### 범용 원소 이름
도메인을 명확히 할 수 없을 때 사용하는 범용 이름:

```python
# 1순위: item (가장 무난, 추천)
for item in items:
for item in arr:
for item in data:

# 2순위: element (수학/알고리즘 문맥)
for element in array:
for element in sequence:

# 3순위: value (값 강조)
for value in values:
for value in numbers:

# 4순위: entry (레코드성 데이터)
for entry in entries:
for entry in records:
```

**자료구조별 관용 표현**:
```python
# 2D 배열
for row in matrix:
for row in grid:

# 트리/그래프
for node in nodes:
for vertex in vertices:

# 스택/큐
for task in queue:
for frame in stack:
```

**피해야 할 것**:
```python
# ❌ 너무 짧거나 모호
for x in arr:
for val in arr:
for tmp in arr:
for obj in arr:
```

### 2. 인덱스가 필요한 경우
```python
# enumerate 활용
for i, user in enumerate(users):
for idx, song in enumerate(songs):

# 단순 카운터 (i, j, k 허용)
for i in range(n):
for i in range(len(arr)):
```

### 3. 딕셔너리 순회
```python
# 도메인이 명확한 경우
for name, score in scores.items():
for userId, count in plays.items():
for genre, songs in songsByGenre.items():

# 키-값 의미가 불명확할 때만
for key, value in data.items():
```

### 4. 2D 배열/그리드
```python
# 도메인이 있는 경우
for row in grid:
    for cell in row:

for student in classroom:
    for score in student:

# 인덱스가 필요한 경우
for r in range(rows):
    for c in range(cols):
        grid[r][c]

# 둘 다 필요한 경우
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
```

### 5. 여러 컬렉션 동시 순회
```python
# zip 활용
for user, score in zip(users, scores):
for name, age, city in zip(names, ages, cities):
```

### 6. 중첩 반복문
```python
# 인덱스 기반: i, j, k 순서
for i in range(n):
    for j in range(i + 1, n):
        # 조합 탐색

# 도메인 기반
for genre in genres:
    for song in songsByGenre[genre]:
        # 계층적 순회
```

---

## 함수 파라미터 네이밍

### 문제 상황
프로그래머스 문제는 종종 배열인데 단수형 파라미터를 제공합니다:
```python
def solution(participant, completion):  # 배열인데 단수형
def solution(number):                    # 배열인데 단수형
```

### 해결 방법

#### 1. 복수형으로 재할당 (권장)
```python
# ✅ 가장 명확하고 일관적
def solution(participant, completion):
    participants = participant
    completions = completion

    for name in participants:  # 읽기 쉬움!
        ...
```

#### 2. 이미 복수 의미가 있으면 그대로 사용
```python
# ✅ 단어 자체가 복수 의미
def solution(people, limit):     # people은 이미 복수형
def solution(data):              # data는 집합 의미
def solution(children):          # children은 이미 복수형
def solution(information):       # 불가산 명사
```

#### 3. 짧은 함수는 그대로 사용 가능
```python
# ✅ 5줄 이하로 문맥이 명확한 경우
def solution(number):
    return sorted(number)  # 짧아서 OK
```

#### 4. 복잡한 로직은 반드시 복수형으로
```python
# ✅ 10줄 이상, 여러 반복문 있을 때
def solution(participant, completion):
    participants = participant  # 명확성 확보
    completions = completion

    counts = {}
    for name in participants:
        counts[name] = counts.get(name, 0) + 1

    for name in completions:
        counts[name] -= 1

    for name, count in counts.items():
        if count > 0:
            return name
```

### 복수형 변환 참고

```python
# 규칙 복수형
participant → participants
number → numbers
song → songs
player → players

# 불규칙 복수형
person → people
child → children
datum → data (data는 이미 복수)

# 불가산 명사 (그대로)
data → data
information → information
```

### 판단 기준

```python
# 언제 복수형으로 바꿀까?
함수 길이 > 10줄          → 복수형으로 (가독성)
반복문 2개 이상           → 복수형으로 (명확성)
중첩 로직                → 복수형으로 (이해도)
5줄 이하 단순 함수        → 그대로 OK

# 예외
이미 복수형/복수 의미     → 그대로
불가산 명사              → 그대로
```

---

## 일반 변수 네이밍

### 카운터/누적
```python
count = 0
total = 0
maxCount = 0
minValue = float('inf')
answer = 0
```

### 상태/플래그
```python
visited = set()
blocked = set()
claimed = {}
isValid = True
hasValue = False
canProceed = True
```

### 시간/순서
```python
createdAt = 0
updatedAt = 0
lastSeen = -1
timestamp = 0
```

### 컬렉션
```python
# 복수형 사용 (자료구조 무관)
users = []       # 리스트든 셋이든 "사용자들"
songs = set()    # 자료구조가 아닌 의미에 집중
edges = []

# 딕셔너리: 단순 복수형
scores = {}      # 점수들 (이름->점수, ID->점수 등)
counts = {}      # 카운트들
indices = {}     # 인덱스들

# 관계가 명확한 경우 (ByX 패턴)
songsByGenre = {}    # 장르별 노래들
countByName = {}     # 이름별 카운트
indexByValue = {}    # 값으로 인덱스 찾기

# 특수/관용적 표현
graph = {}       # 그래프는 관용적으로 사용
cache = {}       # 용도가 명확할 때
```

### 범위/경계
```python
left = 0
right = len(arr) - 1
start = 0
end = n - 1
```

---

## 함수 네이밍

### 일반 동작
```python
def calculate(x, y):
def find(target):
def build(data):
def update(key, value):
```

### 불린 반환
```python
def isValid(s):
def hasPath(graph, start, end):
def canReach(pos):
def exists(key):
```

### 변환/생성
```python
def toList(data):
def parse(s):
def create(params):
```

---

## 실제 예제

### 예제 1: 해시 - 완주하지 못한 선수
```python
def solution(participants, completions):
    counts = {}

    # 참가자 카운팅
    for name in participants:
        counts[name] = counts.get(name, 0) + 1

    # 완주자 차감
    for name in completions:
        counts[name] -= 1

    # 미완주자 찾기
    for name, count in counts.items():
        if count > 0:
            return name
```

### 예제 2: 정렬 - 가장 큰 수
```python
def solution(numbers):
    # 문자열 변환
    strNums = [str(num) for num in numbers]

    # 정렬
    strNums.sort(key=lambda x: x*3, reverse=True)

    # 결합
    answer = ''.join(strNums)

    return '0' if answer[0] == '0' else answer
```

### 예제 3: DFS - 타겟 넘버
```python
def solution(numbers, target):
    answer = 0

    def dfs(idx, currentSum):
        nonlocal answer

        if idx == len(numbers):
            if currentSum == target:
                answer += 1
            return

        # 더하기
        dfs(idx + 1, currentSum + numbers[idx])
        # 빼기
        dfs(idx + 1, currentSum - numbers[idx])

    dfs(0, 0)
    return answer
```

---

## ❌ 피해야 할 패턴

### 1. 한국어 의역
```python
# ❌ 나쁜 예
사용자_목록 = []
점수_딕셔너리 = {}
완료_여부 = False

# ✅ 대신 이렇게
users = []
scores = {}
isCompleted = False
```

### 2. 타입 접미사 (의미 없는 _list, _dict, _set, Map, Set)
```python
# ❌ 나쁜 예
user_list = []
score_dict = {}
visited_set = set()
scoreMap = {}      # 자료구조 접미사
visitedSet = set()

# ✅ 대신 이렇게
users = []
scores = {}        # 의미에 집중
visited = set()
songsByGenre = {}  # 관계가 명확한 경우만
```

### 3. 의미 없는 짧은 알파벳
```python
# ❌ 나쁜 예 (단, i/j/k는 예외)
for u in users:  # u가 뭔지 불명확
for s in songs:  # s가 뭔지 불명확
for x in data:   # x가 뭔지 불명확

# ✅ 대신 이렇게
for user in users:
for song in songs:
for item in data:
```

### 4. 약어 남발
```python
# ❌ 나쁜 예
usr = []
cnt = 0
tmp = None
res = 0

# ✅ 대신 이렇게
user = {}
count = 0
temp = None  # 정말 임시일 때만
result = 0  # 또는 answer
```

### 5. 불명확한 이름
```python
# ❌ 나쁜 예
data = []  # 너무 포괄적
arr = []   # 배열이란 건 알겠는데 뭐의 배열?
temp = {}  # 임시라는 건 알겠는데 뭘 담는지?

# ✅ 대신 이렇게
songs = []
edges = []
cache = {}  # 캐시 용도 명확
```

### 6. 혼합된 네이밍 스타일
```python
# ❌ 나쁜 예 (snake_case와 camelCase 혼용)
user_count = 0
maxScore = 100

# ✅ 대신 이렇게 (일관성 있게)
userCount = 0
maxScore = 100
```

---

## 예외: i, j, k는 허용

다음 경우에는 `i`, `j`, `k` 사용이 자연스럽고 권장됨:

```python
# ✅ 숫자 인덱스
for i in range(n):
for i in range(len(arr)):

# ✅ 중첩 반복문
for i in range(rows):
    for j in range(cols):
        grid[i][j]

# ✅ 조합/순열 탐색
for i in range(n):
    for j in range(i + 1, n):
        # 두 요소 조합
```

---

## 빠른 의사결정 플로우

1. **반복문인가?**
   - 컬렉션 순회 → 복수형을 단수형으로: `for user in users`
   - 인덱스만 필요 → `i`, `j`, `k` 사용
   - 둘 다 필요 → `enumerate` 사용

2. **상태/플래그인가?**
   - 불린 → `is*`, `has*`, `can*`
   - 집합 → `visited`, `blocked`, `claimed`

3. **카운터/누적인가?**
   - → `count`, `total`, `max*`, `min*`

4. **컬렉션인가?**
   - → 복수형 명사: `users`, `songs`, `scores` (자료구조 무관)
   - 관계 명확 → `*ByX`: `songsByGenre`, `countByName`

5. **그 외**
   - 문제 도메인의 핵심 개념을 영어 명사/동사로 표현
