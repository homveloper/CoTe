# 코딩 테스트 학습 로드맵 🎯

> **1:1 컨설팅 기반 체계적 학습 가이드**
> 입문부터 고급까지, 단계별로 실력을 쌓아가는 학습 경로

---

## 📍 현재 위치 파악

### 당신의 현재 레벨: **입문 (Level 0-1)**
- ✅ 기본 배열 조작 가능
- ✅ 간단한 정렬 활용 가능
- ✅ 완전탐색 개념 이해 시작
- 🎯 **다음 목표**: 기본 자료구조 마스터 → 초급 알고리즘 패턴 학습

---

## 🗺️ 학습 로드맵 (4단계)

```
입문 (1-2개월)  →  초급 (2-3개월)  →  중급 (3-4개월)  →  고급 (지속)
  기본 문법           자료구조           알고리즘            최적화
  완전탐색            해시/스택/큐        DFS/BFS/DP         복잡도 분석
  배열/정렬           이진탐색            그래프              고급 자료구조
```

---

## 📚 단계별 상세 학습 경로

### **Level 0-1: 입문 단계** (현재 단계)
**목표**: 프로그래밍 기본기 다지기, 문제 해결 감각 키우기

#### 학습 주제
| 순서 | 주제 | 학습 목표 | 추천 문제 수 |
|------|------|-----------|--------------|
| 1 | **배열/리스트 조작** | 인덱싱, 슬라이싱, 내장 함수 | 5-7문제 |
| 2 | **문자열 처리** | split, join, 정규식 기초 | 5-7문제 |
| 3 | **정렬 활용** | sort, sorted, key 함수 | 5-7문제 |
| 4 | **완전탐색 (Brute Force)** | 이중 for문, 모든 경우의 수 | 5-7문제 |
| 5 | **구현/시뮬레이션** | 문제 조건 그대로 구현 | 5-7문제 |

#### 핵심 개념
```python
# 1. 배열 조작 필수 패턴
arr = [1, 2, 3, 4, 5]
arr[::-1]              # 뒤집기
arr[::2]               # 짝수 인덱스
list(set(arr))         # 중복 제거
sorted(arr, key=lambda x: -x)  # 정렬

# 2. 완전탐색 기본 패턴
for i in range(n):
    for j in range(i+1, n):  # 조합
        # 모든 쌍 검사

# 3. 구현 팁
answer = []
for x in data:
    if 조건:
        answer.append(처리(x))
return answer
```

#### 프로그래머스 추천 문제
- **Lv.0-1**:
  - 배열 뒤집기, 평균 구하기, 짝수 홀수 개수
  - 문자열 다루기, 자릿수 더하기
  - 정수 내림차순으로 배치하기
  - 나누어 떨어지는 숫자 배열
  - 두 정수 사이의 합
  - 문자열 내 p와 y의 개수
  - 약수의 합

#### 학습 방법
1. **하루 1-2문제** (30분-1시간)
2. **시간 제한**: 처음엔 30분, 안 풀리면 힌트/풀이 참고
3. **복습**: 못 푼 문제는 3일 후 다시 풀기
4. **기록**: README에 "왜 틀렸는지", "배운 점" 반드시 작성

---

### **Level 2: 초급 단계** (입문 완료 후)
**목표**: 핵심 자료구조 마스터, 알고리즘 패턴 익히기

#### 학습 주제
| 순서 | 주제 | 학습 목표 | 추천 문제 수 | 중요도 |
|------|------|-----------|--------------|--------|
| 1 | **해시 (Hash)** | dict, set 활용, O(1) 탐색 | 7-10문제 | ⭐⭐⭐ |
| 2 | **스택 (Stack)** | 괄호, 짝찾기 패턴 | 5-7문제 | ⭐⭐⭐ |
| 3 | **큐/덱 (Queue/Deque)** | BFS 준비, 회전 문제 | 5-7문제 | ⭐⭐ |
| 4 | **힙 (Heap)** | 우선순위 큐, 정렬 대체 | 5-7문제 | ⭐⭐⭐ |
| 5 | **이진탐색** | 정렬 배열, 파라메트릭 서치 | 7-10문제 | ⭐⭐⭐ |

#### 핵심 개념

**1. 해시 (가장 중요!)**
```python
# 패턴 1: 빈도수 세기
counter = {}
for x in arr:
    counter[x] = counter.get(x, 0) + 1

# 패턴 2: 빠른 존재 확인
seen = set(arr)
if target in seen:  # O(1)
    ...

# 패턴 3: 인덱스 저장
index_map = {val: i for i, val in enumerate(arr)}
```

**2. 스택 (짝찾기의 정석)**
```python
# 괄호, 태그 짝찾기
stack = []
for char in s:
    if char in '({[':
        stack.append(char)
    else:
        if not stack or not match(stack[-1], char):
            return False
        stack.pop()
return len(stack) == 0
```

**3. 이진탐색 (정렬 배열 필수)**
```python
# 패턴 1: 값 찾기
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 패턴 2: 파라메트릭 서치 (최대/최소값 찾기)
def parametric_search(arr, condition):
    left, right = min_value, max_value
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if condition(mid):
            answer = mid
            right = mid - 1  # 더 작은 값 탐색
        else:
            left = mid + 1
    return answer
```

**4. 힙 (우선순위 큐)**
```python
import heapq

# 최소 힙 (기본)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
min_val = heapq.heappop(heap)  # 1

# 최대 힙 (음수 활용)
heap = []
heapq.heappush(heap, -3)
max_val = -heapq.heappop(heap)  # 3

# K번째 최소/최대값 찾기
# 상위 K개 유지하는 힙
```

#### 프로그래머스 추천 문제
- **해시**: 완주하지 못한 선수, 전화번호 목록, 위장, 베스트앨범
- **스택/큐**: 올바른 괄호, 기능개발, 프린터, 다리를 지나는 트럭
- **힙**: 더 맵게, 디스크 컨트롤러, 이중우선순위큐
- **이진탐색**: 입국심사, 징검다리, 순위 검색

#### 학습 방법
1. **개념 먼저**: 각 자료구조의 **언제 쓰는지** 이해
2. **패턴 암기**: 위 코드 패턴을 직접 타이핑하며 체화
3. **하루 1문제** (1시간)
4. **같은 유형 3문제 연속**: 패턴이 보일 때까지
5. **복잡도 분석**: 매 문제마다 시간복잡도 계산 습관

---

### **Level 3: 중급 단계** (초급 완료 후)
**목표**: 그래프/트리 탐색, 동적계획법 정복

#### 학습 주제
| 순서 | 주제 | 학습 목표 | 추천 문제 수 | 중요도 |
|------|------|-----------|--------------|--------|
| 1 | **DFS (깊이우선탐색)** | 재귀, 백트래킹 | 10-15문제 | ⭐⭐⭐ |
| 2 | **BFS (너비우선탐색)** | 최단거리, 레벨탐색 | 10-15문제 | ⭐⭐⭐ |
| 3 | **동적계획법 (DP)** | 메모이제이션, 점화식 | 15-20문제 | ⭐⭐⭐ |
| 4 | **그래프 기초** | 인접리스트, 사이클 판단 | 7-10문제 | ⭐⭐⭐ |
| 5 | **그리디 (Greedy)** | 최적해 증명 | 7-10문제 | ⭐⭐ |
| 6 | **최단경로** | 다익스트라, 벨만포드 | 5-7문제 | ⭐⭐ |

#### 핵심 개념

**1. DFS (재귀의 정석)**
```python
# 패턴 1: 그래프 DFS
visited = set()
def dfs(node, graph):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, graph)

# 패턴 2: 격자 DFS (상하좌우)
def dfs(x, y, grid):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if grid[x][y] == 0 or visited[x][y]:
        return

    visited[x][y] = True
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        dfs(x + dx, y + dy, grid)

# 패턴 3: 백트래킹 (조합/순열)
def backtrack(path, start):
    if len(path) == target_length:
        result.append(path[:])
        return

    for i in range(start, n):
        path.append(arr[i])
        backtrack(path, i + 1)
        path.pop()  # 백트래킹
```

**2. BFS (최단거리의 정석)**
```python
from collections import deque

# 패턴 1: 그래프 BFS
def bfs(start, graph):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

# 패턴 2: 최단거리 (레벨별 탐색)
def bfs_shortest(start, end, graph):
    visited = set([start])
    queue = deque([(start, 0)])  # (노드, 거리)

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist + 1))

# 패턴 3: 격자 BFS (미로 최단거리)
def bfs_grid(start_x, start_y, grid):
    queue = deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y, dist = queue.popleft()
        if grid[x][y] == target:
            return dist

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited and grid[nx][ny] != 0:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
```

**3. DP (점화식의 정석)**
```python
# 패턴 1: 1차원 DP
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = dp[i-1] + 추가계산
    # 또는: dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

# 패턴 2: 2차원 DP (격자, LCS)
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# 패턴 3: 메모이제이션 (Top-down)
memo = {}
def dp_recursive(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return base_case

    memo[n] = dp_recursive(n-1) + dp_recursive(n-2)
    return memo[n]

# DP 문제 접근법
# 1. 작은 문제로 나눌 수 있는가?
# 2. 중복 계산이 발생하는가?
# 3. 점화식을 세울 수 있는가?
#    dp[i] = f(dp[i-1], dp[i-2], ...)
```

**4. 그래프 표현**
```python
# 인접 리스트 (가장 많이 사용)
graph = [[] for _ in range(n)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)  # 무방향 그래프

# 딕셔너리 그래프
graph = {}
for a, b in edges:
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
```

**5. 그리디 (탐욕법)**
```python
# 기본 패턴: 정렬 후 선택
items.sort(key=lambda x: x[1])  # 특정 기준 정렬
answer = 0
for item in items:
    if 조건:
        answer += item
        # 선택하고 다음으로

# 그리디 증명 필요: "이 선택이 최적임을 어떻게 아는가?"
```

#### 프로그래머스 추천 문제
- **DFS/BFS**: 타겟 넘버, 네트워크, 게임 맵 최단거리, 단어 변환
- **DP**: N으로 표현, 정수 삼각형, 등굣길, 도둑질, 사칙연산
- **그래프**: 가장 먼 노드, 순위, 방의 개수
- **그리디**: 체육복, 큰 수 만들기, 조이스틱, 구명보트

#### 학습 방법
1. **DP는 별도 시간 투자**: 가장 어려운 주제, 2주 집중
2. **점화식 세우기 연습**: 손으로 작은 케이스 직접 계산
3. **DFS/BFS는 반드시 손코딩**: 코드 흐름 외우기
4. **하루 1문제** (1.5-2시간)
5. **못 풀면 30분 고민 후 풀이 참고** → 다음날 다시 풀기

---

### **Level 4: 고급 단계** (중급 완료 후)
**목표**: 고난도 알고리즘, 최적화 기법 마스터

#### 학습 주제
| 주제 | 학습 목표 | 비고 |
|------|-----------|------|
| **유니온 파인드** | 집합 병합, 사이클 판단 | 그래프 고급 |
| **트라이 (Trie)** | 문자열 검색 최적화 | 문자열 고급 |
| **세그먼트 트리** | 구간 쿼리 O(log n) | 고급 자료구조 |
| **위상 정렬** | 순서가 있는 작업 | 그래프 고급 |
| **최소 스패닝 트리** | 크루스칼, 프림 | 그래프 고급 |
| **KMP, 라빈카프** | 문자열 매칭 | 문자열 고급 |
| **비트마스킹** | 집합을 비트로 표현 | 최적화 기법 |

#### 핵심 개념

**유니온 파인드**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        # 랭크 기반 합치기
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
```

**다익스트라 (최단경로)**
```python
import heapq

def dijkstra(start, graph, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (거리, 노드)

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist
```

#### 프로그래머스 추천 문제
- **Lv.3-4**: 순위, 섬 연결하기, 가장 먼 노드, 합승 택시 요금

---

## 🎓 효과적인 학습 방법론

### 1. **문제 풀이 3단계 프로세스**

```
[1단계] 문제 이해 (5분)
  ├─ 입력/출력 형식 파악
  ├─ 제약 조건 확인 (n의 범위 → 시간복잡도 추정)
  └─ 예제 손으로 풀어보기

[2단계] 접근 방법 선택 (10분)
  ├─ 어떤 자료구조/알고리즘?
  ├─ 완전탐색으로 해결 가능? (n ≤ 10: O(2^n), n ≤ 500: O(n^3))
  ├─ 최적화 필요? (해시, 이진탐색, DP)
  └─ 의사코드 작성

[3단계] 구현 및 검증 (30-50분)
  ├─ 코드 작성
  ├─ 예제 테스트
  ├─ 엣지 케이스 확인 (빈 배열, 최대값, 중복 등)
  └─ 제출 후 회고
```

### 2. **시간 복잡도 빠른 판단법**

| n의 범위 | 가능한 시간복잡도 | 알고리즘 힌트 |
|----------|-------------------|---------------|
| n ≤ 10 | O(2^n), O(n!) | 완전탐색, 백트래킹 |
| n ≤ 20 | O(2^n), O(n^2 * 2^n) | 비트마스킹, 백트래킹 |
| n ≤ 500 | O(n^3) | DP, 플로이드-워셜 |
| n ≤ 2,000 | O(n^2) | 이중 for문, DP |
| n ≤ 100,000 | O(n log n) | 정렬, 이진탐색, 힙 |
| n ≤ 1,000,000 | O(n) | 해시, 그리디, 누적합 |
| n ≥ 10^6 | O(log n), O(1) | 이진탐색, 수학 |

**예시**:
- n=5, 모든 조합 탐색 → O(2^5) = 32 → 완전탐색 OK
- n=100,000 → O(n^2)는 불가 (100억) → O(n log n) 필요

### 3. **막혔을 때 대처법**

#### 30분 규칙
```
0-30분: 혼자 고민 (아이디어, 의사코드)
  ↓ 막히면
30-60분: 힌트 찾기 (분류 태그, 유사 문제)
  ↓ 여전히 막히면
60분+: 풀이 참고 → 이해 → 다음날 다시 풀기
```

#### 디버깅 체크리스트
- [ ] 인덱스 에러 (범위 벗어남)
- [ ] 초기값 설정 실수
- [ ] 자료형 문제 (int vs float, list vs set)
- [ ] 얕은 복사 vs 깊은 복사
- [ ] 재귀 종료 조건
- [ ] 방문 체크 누락 (visited)

### 4. **복습 사이클**

```
Day 1: 문제 풀이
Day 3: 다시 풀기 (코드 보지 않고)
Day 7: 다시 풀기
Day 30: 최종 복습
```

**복습이 더 중요합니다!** 100문제 1번씩보다, 50문제 3번씩이 낫습니다.

### 5. **README 회고 작성 (필수)**

매 문제마다 반드시 작성:
```markdown
## 회고
### 배운 점
- (새로 알게 된 개념, 함수, 패턴)

### 어려웠던 부분
- (어디서 막혔는지, 왜 어려웠는지)

### 개선할 점
- (더 나은 풀이, 최적화 아이디어)
```

---

## 🧠 알고리즘별 핵심 개념 정리

### 자료구조

#### 1. 배열/리스트
- **언제**: 순서가 중요, 인덱스 접근
- **시간복잡도**: 접근 O(1), 탐색 O(n), 삽입/삭제 O(n)
- **Python 팁**: `list.sort()` (제자리), `sorted(list)` (새 리스트)

#### 2. 해시 (dict, set)
- **언제**: 빠른 탐색/존재 확인, 빈도수 세기
- **시간복잡도**: 삽입/탐색/삭제 O(1)
- **Python 팁**: `collections.Counter`, `collections.defaultdict`

#### 3. 스택 (list)
- **언제**: 짝찾기, 괄호, 후입선출(LIFO)
- **시간복잡도**: push/pop O(1)
- **Python 팁**: `stack.append()`, `stack.pop()`

#### 4. 큐/덱 (deque)
- **언제**: BFS, 선입선출(FIFO), 양방향 삽입/삭제
- **시간복잡도**: append/popleft O(1)
- **Python 팁**: `from collections import deque`

#### 5. 힙 (heapq)
- **언제**: 최소/최대값 반복 추출, 우선순위 큐
- **시간복잡도**: push/pop O(log n)
- **Python 팁**: 최대힙은 음수로 (`-x`)

---

### 알고리즘

#### 1. 완전탐색 (Brute Force)
```
모든 경우의 수를 다 해봐도 시간 내에 가능할 때
```
- **사용**: n이 작을 때 (n ≤ 10-20)
- **구현**: 이중 for문, 재귀

#### 2. 이진탐색 (Binary Search)
```
정렬된 배열에서 O(log n) 탐색
```
- **사용**:
  - 특정 값 찾기
  - 조건을 만족하는 최소/최대값 (파라메트릭 서치)
- **주의**: 배열이 정렬되어 있어야 함

#### 3. 그리디 (Greedy)
```
매 순간 최선의 선택 → 전체 최적해
```
- **사용**: 선택의 순서가 결과에 영향 없을 때
- **주의**: 최적해 보장 증명 필요
- **예시**: 동전 교환 (큰 단위부터), 회의실 배정 (끝나는 시간 기준)

#### 4. DFS (깊이 우선 탐색)
```
한 경로를 끝까지 탐색 후 다른 경로
```
- **사용**:
  - 모든 경로 탐색
  - 백트래킹 (조합, 순열)
  - 사이클 탐지
- **구현**: 재귀 or 스택

#### 5. BFS (너비 우선 탐색)
```
레벨별로 탐색 (가까운 노드부터)
```
- **사용**:
  - **최단 거리** (가중치 없는 그래프)
  - 레벨별 탐색
  - 최소 횟수
- **구현**: 큐 (deque)

#### 6. 동적계획법 (DP)
```
큰 문제 → 작은 문제들로 분해 + 메모이제이션
```
- **사용**:
  - 중복 계산이 많을 때
  - 최적 부분 구조 (작은 문제의 최적해 → 큰 문제의 최적해)
- **접근**:
  1. 점화식 세우기 (dp[i] = f(dp[i-1], dp[i-2], ...))
  2. 초기값 설정
  3. 반복문 or 재귀로 구현

#### 7. 최단경로
- **다익스트라**: 가중치 그래프, 음수 간선 없음 → O((E+V) log V)
- **벨만포드**: 음수 간선 있음 → O(VE)
- **플로이드-워셜**: 모든 쌍 최단거리 → O(V^3)

---

## ✅ 학습 체크리스트

### 입문 단계
- [ ] 배열 조작 10문제 이상
- [ ] 정렬 활용 7문제 이상
- [ ] 완전탐색 7문제 이상
- [ ] 시간복잡도 개념 이해
- [ ] 프로그래머스 Lv.1 20문제 이상

### 초급 단계
- [ ] 해시 문제 10문제 이상
- [ ] 스택/큐 문제 10문제 이상
- [ ] 힙 문제 5문제 이상
- [ ] 이진탐색 문제 10문제 이상
- [ ] 각 자료구조 언제 쓰는지 설명 가능
- [ ] 프로그래머스 Lv.2 30문제 이상

### 중급 단계
- [ ] DFS 문제 15문제 이상
- [ ] BFS 문제 15문제 이상
- [ ] DP 문제 20문제 이상
- [ ] 그래프 기초 10문제 이상
- [ ] DFS/BFS 차이 설명 가능
- [ ] 손코딩으로 DFS/BFS 작성 가능
- [ ] 프로그래머스 Lv.2-3 50문제 이상

### 고급 단계
- [ ] 최단경로 알고리즘 구현 가능
- [ ] 유니온 파인드 구현 가능
- [ ] 위상 정렬 구현 가능
- [ ] 프로그래머스 Lv.3-4 30문제 이상

---

## 💡 효율적인 학습 팁

### ✅ DO (꼭 해야 할 것)

1. **매일 코딩** - 하루 1문제라도 꾸준히
2. **손코딩** - 핵심 알고리즘은 손으로 써보기
3. **복습** - 3일, 7일, 30일 주기로 다시 풀기
4. **회고 작성** - README에 배운 점, 어려웠던 점 반드시 기록
5. **시간 제한** - 30분 고민 후 안 풀리면 힌트/풀이 참고
6. **패턴 학습** - 같은 유형 3-5문제 연속으로 풀기
7. **복잡도 분석** - 매 문제마다 시간/공간 복잡도 계산

### ❌ DON'T (피해야 할 것)

1. **풀이만 보기** - 코드 복붙은 실력 향상 없음
2. **연속 실패 방치** - 3번 틀리면 풀이 참고 후 이해
3. **랜덤 문제 풀기** - 단계별, 주제별로 집중 학습
4. **복습 건너뛰기** - 1번 푼 것은 기억 안 남
5. **완벽주의** - 처음부터 최적화 고민하지 말고 일단 풀기
6. **너무 어려운 문제** - 현재 레벨+1 정도만 도전
7. **시간 무제한** - 1시간 넘으면 힌트 보기

---

## 📅 학습 스케줄 예시

### 입문 단계 (4주 계획)
```
Week 1: 배열/문자열 집중 (7문제)
Week 2: 정렬 활용 + 완전탐색 (7+5 = 12문제)
Week 3: 구현 문제 + 복습 (5문제 + 복습)
Week 4: 혼합 + 입문 총정리 (10문제)
```

### 초급 단계 (8주 계획)
```
Week 1-2: 해시 집중 (10문제)
Week 3-4: 스택/큐 집중 (10문제)
Week 5-6: 힙 + 이진탐색 (5+10 = 15문제)
Week 7: 복습 (못 푼 문제 다시)
Week 8: 혼합 문제 (10문제)
```

### 중급 단계 (12주 계획)
```
Week 1-3: DFS 집중 (15문제)
Week 4-6: BFS 집중 (15문제)
Week 7-10: DP 집중 (20문제) - 가장 어려움
Week 11: 그래프 + 그리디 (10문제)
Week 12: 중급 총정리
```

---

## 🎯 단계별 목표 설정

### 입문자 (0-2개월)
- **목표**: 프로그래머스 Lv.1 30문제 달성
- **하루**: 30분-1시간, 1-2문제
- **주간**: 7-10문제

### 초급 (2-5개월)
- **목표**: 프로그래머스 Lv.2 50문제 달성
- **하루**: 1시간, 1문제
- **주간**: 5-7문제

### 중급 (5-10개월)
- **목표**: 프로그래머스 Lv.2-3 80문제 달성
- **하루**: 1.5-2시간, 1문제
- **주간**: 5문제

### 고급 (10개월+)
- **목표**: 프로그래머스 Lv.3-4 50문제 달성
- **하루**: 2시간, 1문제 (어려운 문제는 며칠 소요 가능)

---

## 📖 추천 학습 자료

### 온라인 저지
1. **프로그래머스** - 한국어, 기업 코테 유형
2. **백준** - 방대한 문제 수, 단계별 학습
3. **LeetCode** - 영어, 글로벌 기업 준비

### 책
1. **"이것이 취업을 위한 코딩 테스트다"** - 나동빈 (입문~중급)
2. **"파이썬 알고리즘 인터뷰"** - 박상길 (중급)
3. **"프로그래밍 대회에서 배우는 알고리즘 문제해결전략"** - 구종만 (고급)

### 유튜브
1. **동빈나** - 알고리즘 개념 강의
2. **엔지니어대한민국** - 문제 풀이

---

## 🚀 마무리: 성공하는 학습자의 습관

### 1. 꾸준함 > 완벽함
- 하루 10분이라도 매일 코드 보기
- 못 푼 문제도 기록 (실패도 성장)

### 2. 과정 중심 사고
- "이 문제를 왜 못 풀었지?" 분석
- "어떤 힌트가 있었으면 풀 수 있었을까?" 회고

### 3. 패턴 학습
- 알고리즘은 결국 패턴의 반복
- 비슷한 문제 3개 풀면 패턴이 보임

### 4. 복습이 답
- 1번 푼 문제 = 0점
- 3번 푼 문제 = 합격

### 5. 포기하지 않기
- DP 어려운 건 모두가 같음
- 막히면 쉬운 문제로 돌아가기

---

**"천천히, 하지만 꾸준히. 매일 성장하는 개발자가 되세요!"** 🎯

---

*이 로드맵은 `CLAUDE.md`의 학습 철학을 기반으로 작성되었습니다.*
*문제를 풀 때마다 이 문서를 참고하며 현재 위치를 확인하세요.*
