# 트리 순회

- 링크 : [프로그래머스 PCCP 모의고사 2회 1번](https://school.programmers.co.kr/learn/courses/15008/lessons/121685)

```
#트리 #재귀 #전위순회 #중위순회 #후위순회 #클로저
```

## 풀이 과정

### 핵심 아이디어
- 배열로 표현된 완전 이진 트리에서 인덱스 관계를 활용
- 인덱스 `i`의 왼쪽 자식: `2*i + 1`, 오른쪽 자식: `2*i + 2`
- 각 순회 방식은 방문 순서만 다름 (루트-왼-오 vs 왼-루트-오 vs 왼-오-루트)
- 클로저를 활용하여 result 리스트를 캡처

### 접근 방법
1. 각 순회 방식별로 함수 분리 (preorder, inorder, postorder)
2. 내부 헬퍼 함수(inner)를 클로저로 구현하여 result 공유
3. 재귀 종료 조건: 인덱스가 배열 범위를 벗어나면 종료
4. 각 순회 방식에 맞게 노드 방문 순서 조정
   - 전위: 현재 → 왼쪽 → 오른쪽
   - 중위: 왼쪽 → 현재 → 오른쪽
   - 후위: 왼쪽 → 오른쪽 → 현재

### 코드

```python
def preorder(nodes):
    result = []
    def inner(idx):
        if idx >= len(nodes):
            return
        result.append(str(nodes[idx]))
        inner(idx*2 + 1)
        inner(idx*2 + 2)
    inner(0)
    return " ".join(result)

def inorder(nodes):
    result = []
    def inner(idx):
        if idx >= len(nodes):
            return
        inner(idx*2 + 1)
        result.append(str(nodes[idx]))
        inner(idx*2 + 2)
    inner(0)
    return " ".join(result)

def postorder(nodes):
    result = []
    def inner(idx):
        if idx >= len(nodes):
            return
        inner(idx*2 + 1)
        inner(idx*2 + 2)
        result.append(str(nodes[idx]))
    inner(0)
    return " ".join(result)

def solution(nodes):
    return [
        preorder(nodes),
        inorder(nodes),
        postorder(nodes)
    ]
```

## 회고

### 배운 점
- python에서도 람다 함수에 클로저를 사용할 수 있다는 것을 알게 되었다.

### 어려웠던 부분
- 전위, 중위, 후위 순회 방식을 헷갈려서 어려웠다.
- python에서 재귀 함수 인자가 클래스인 경우 레퍼런스 인지 값 복사인지 헷갈렸다.
- 재귀 함수를 오랜만에 사용해서 작성하는 방법을 잊어버렸다.

### 개선할 점
- 트리 순회 방식을 확실히 익히자.

## 평가

### 개선할 점

**1. 코드 중복 (DRY 원칙)**
- 세 개의 순회 함수가 거의 동일한 구조를 가지고 있습니다.
- 공통 로직을 추출하여 하나의 일반화된 함수로 만들 수 있습니다:

```python
def traverse(nodes, mode='preorder'):
    """
    mode: 'preorder', 'inorder', 'postorder'
    """
    result = []

    def inner(idx):
        if idx >= len(nodes):
            return

        if mode == 'preorder':
            result.append(str(nodes[idx]))

        inner(idx*2 + 1)

        if mode == 'inorder':
            result.append(str(nodes[idx]))

        inner(idx*2 + 2)

        if mode == 'postorder':
            result.append(str(nodes[idx]))

    inner(0)
    return " ".join(result)
```

**2. 불필요한 str() 변환**
- `result.append(str(nodes[idx]))`를 매번 호출하는 것보다
- `" ".join(map(str, result))`로 마지막에 한 번만 변환하는 것이 더 효율적입니다.

**3. 함수명 개선**
- `inner`라는 이름보다 `traverse` 또는 `visit`이 의미를 더 명확히 전달합니다.

### 잘한 점

**1. 클로저 활용 ✨**
- 클로저를 사용하여 result 리스트를 캡처한 점이 매우 좋습니다.
- 함수 시그니처가 간결해지고 가독성이 향상되었습니다.
- 레퍼런스 전달로 인한 실수를 방지할 수 있습니다.

**2. 함수 분리**
- 각 순회 방식을 별도 함수로 분리하여 책임이 명확합니다.
- solution() 함수의 의도가 한눈에 파악됩니다.

**3. 정확한 인덱스 계산**
- 배열 기반 완전 이진 트리의 인덱스 관계를 정확히 이해하고 구현했습니다.
- `2*i + 1` (왼쪽 자식), `2*i + 2` (오른쪽 자식)

**4. 적절한 종료 조건**
- `idx >= len(nodes)` 조건으로 범위 체크를 명확히 했습니다.

### 다른 응용 방안

**1. 레벨 순서 순회 (Level Order Traversal)**
- BFS를 활용한 층별 순회 추가 가능
```python
from collections import deque

def levelorder(nodes):
    if not nodes:
        return ""

    result = []
    queue = deque([0])  # 루트 인덱스

    while queue:
        idx = queue.popleft()
        if idx < len(nodes):
            result.append(str(nodes[idx]))
            queue.append(2*idx + 1)  # 왼쪽 자식
            queue.append(2*idx + 2)  # 오른쪽 자식

    return " ".join(result)
```

**2. 반복적(Iterative) 구현**
- 스택을 사용한 비재귀 버전 구현 가능 (콜스택 깊이 제한 회피)

**3. 제너레이터 활용**
- 메모리 효율을 위해 yield를 사용한 제너레이터 패턴 적용 가능

**4. 불완전 이진 트리 지원**
- None 값을 포함한 배열 처리 (현재는 완전 이진 트리만 지원)

### 다른 추천 문제

**기본 트리 순회 문제**
- [백준 1991 - 트리 순회](https://www.acmicpc.net/problem/1991)
  - 난이도: 실버 1
  - 노드 클래스 기반 트리 구현 연습

**트리 응용 문제**
- [프로그래머스 - 길 찾기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/42892)
  - Level 3
  - 좌표로 주어진 노드들을 이진 탐색 트리로 구성 후 순회

- [백준 11725 - 트리의 부모 찾기](https://www.acmicpc.net/problem/11725)
  - 실버 2
  - 트리 구조 파악 및 부모-자식 관계 이해

**심화 문제**
- [백준 5639 - 이진 검색 트리](https://www.acmicpc.net/problem/5639)
  - 골드 4
  - 전위 순회 결과로 후위 순회 결과 구하기

- [프로그래머스 - 양과 늑대](https://school.programmers.co.kr/learn/courses/30/lessons/92343)
  - Level 3
  - 트리 순회 + 백트래킹 조합

### 종합 평가

이 풀이는 **트리 순회의 기본 개념을 정확히 이해**하고 있으며, **클로저를 활용한 깔끔한 구현**이 돋보입니다. 특히 배열 기반 완전 이진 트리의 인덱스 관계를 정확히 파악하고 재귀로 구현한 점이 우수합니다.

다만 **코드 중복**이 아쉬운 부분입니다. 세 개의 순회 함수가 거의 동일한 구조를 가지고 있어 DRY(Don't Repeat Yourself) 원칙을 위배합니다. 실무에서는 유지보수성을 위해 공통 로직을 추출하는 것이 중요합니다.

또한 **str() 변환 시점**을 최적화할 수 있습니다. 매번 append 시 변환하기보다 마지막에 `map(str, result)`를 사용하면 더 pythonic하고 효율적입니다.

**학습 관점에서의 평가:**
- ✅ 전위/중위/후위 순회 개념을 명확히 이해
- ✅ 재귀의 기본 패턴(종료 조건 + 재귀 호출) 숙지
- ✅ 파이썬 클로저 활용 능력 향상
- ⚠️ 코드 리팩토링 및 일반화 능력은 더 발전시킬 여지가 있음

트리 구조의 기초를 다지는 **몸풀기 문제로서 충분히 목표를 달성**했습니다. 다음 단계로는 노드 클래스 기반 트리 구현, 불완전 트리 처리, 그리고 트리 순회를 활용한 복잡한 문제 해결로 나아가시길 추천합니다.

## 추가 학습

### 배열 vs 노드 기반 트리 구현

**배열 기반 (현재 문제)**
```python
# 인덱스 관계만으로 트리 구조 표현
tree = [1, 2, 3, 4, 5, 6, 7]
left_child = 2*i + 1
right_child = 2*i + 2
```
- 장점: 간단, 메모리 연속적, 캐시 친화적
- 단점: 불완전 트리 표현 비효율, 중간 삽입/삭제 어려움

**노드 기반 (일반적인 트리)**
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
```
- 장점: 불완전 트리 표현 자유로움, 동적 구조 변경 용이
- 단점: 포인터 오버헤드, 메모리 분산

### 순회 방식별 활용 사례

**전위 순회 (Preorder)**: 루트 → 왼쪽 → 오른쪽
- 트리 복사
- 트리 직렬화/역직렬화
- 디렉토리 구조 출력 (파일 시스템)

**중위 순회 (Inorder)**: 왼쪽 → 루트 → 오른쪽
- 이진 탐색 트리(BST)의 정렬된 순서 출력
- 수식 트리의 중위 표기법 변환

**후위 순회 (Postorder)**: 왼쪽 → 오른쪽 → 루트
- 트리 삭제 (자식부터 삭제 후 부모)
- 디렉토리 크기 계산
- 수식 트리 계산 (후위 표기법)

### 재귀 깊이 제한 주의

파이썬의 기본 재귀 깊이는 **약 1000**입니다. 깊은 트리의 경우:
```python
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 증가

# 또는 반복문으로 구현 (스택 사용)
def iterative_preorder(nodes):
    if not nodes:
        return ""

    result = []
    stack = [0]  # 루트 인덱스

    while stack:
        idx = stack.pop()
        if idx < len(nodes):
            result.append(str(nodes[idx]))
            # 오른쪽 먼저 push (스택 LIFO 특성)
            if 2*idx + 2 < len(nodes):
                stack.append(2*idx + 2)
            if 2*idx + 1 < len(nodes):
                stack.append(2*idx + 1)

    return " ".join(result)
```

---
**복잡도**:
- 시간: O(N) - 모든 노드를 한 번씩 방문
- 공간: O(N) - result 리스트 + O(H) 재귀 스택 (H는 트리 높이)
  - 완전 이진 트리에서 H = log N
  - 최악의 경우 (편향 트리) H = N

**풀이 날짜**: 2025-11-14
