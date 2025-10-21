# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git Commit Message Convention ⭐ **PRIORITY**

**This is the most important convention in this repository.**

### Format
```
keyword(topic) : 한글 설명
```

### Keywords
- `add` - 새로운 문제 풀이 추가
- `fix` - 기존 풀이 버그 수정
- `update` - 풀이 개선 또는 복잡도 최적화
- `docs` - 문서 수정 (README, CLAUDE.md 등)
- `refactor` - 코드 리팩토링

### Single Problem Commit
```
add(001_해시) : 두개뽑아서더하기 문제 풀이
fix(003_스택) : 올바른괄호 문제 풀이 버그 수정
update(010_DP) : N으로표현 풀이 최적화 (O(n²) → O(n))
```

### Multiple Changes in One Commit
```
add(updates) : 여러 문제 풀이 및 문서 업데이트

- 001_해시_두개뽑아서더하기 문제 풀이 추가
- 002_해시_완주하지못한선수 문제 풀이 추가
- 003_스택_올바른괄호 문제 풀이 추가
- 메인 README.md 인덱스 테이블 업데이트
```

### Key Rules
✅ **DO**:
- 키워드는 **영어** (add, fix, update, docs, refactor)
- 한줄 설명과 본문 리스트는 **한글**
- 문제 번호와 주제 명시 예: `001_해시`, `010_DP`
- 의미 있는 설명 작성 (예: 최적화 전후 복잡도 언급)

❌ **DON'T**:
- 한글로 키워드 사용
- 의미 불명확한 메시지 (예: "수정함", "추가")
- 영어 설명 사용

### Commit Examples
```bash
# 새 문제 풀이
git commit -m "add(001_해시) : 두개뽑아서더하기 문제 풀이"

# 버그 수정
git commit -m "fix(005_정렬) : 가장큰수 풀이 오류 수정"

# 성능 개선
git commit -m "update(010_DP) : N으로표현 풀이 메모이제이션으로 최적화"

# 문서 수정
git commit -m "docs : CLAUDE.md 커밋 메시지 규칙 추가"

# 여러 문제 한번에 추가
git commit -m "add(problems) : 해시 주제 3문제 풀이 추가

- 001_해시_두개뽑아서더하기
- 002_해시_완주하지못한선수
- 003_해시_전화번호목록"
```

---

## Project Overview

**CoTe** (코딩 테스트 - Coding Test) is a personal algorithm practice repository for daily problem-solving and learning.

### Purpose
- Daily coding test practice with structured problem-solving documentation
- Learning and mastering algorithms and data structures
- Recording problem-solving approaches and reflections
- Building a portfolio of solved problems with detailed explanations

### Key Characteristics
- **Language**: Python 3
- **Documentation**: Korean
- **Structure**: Template-based folder organization with problem-per-folder approach
- **No external dependencies**: Standalone pure Python implementations
- **Git-based tracking**: Each problem is a commit checkpoint

## Repository Structure

### Main Files
- `README.md` - Project overview, problem index table, and learning statistics
- `CLAUDE.md` - This guidance file (for AI assistants)
- `LICENSE` - Project license
- `.gitignore` - Python-specific ignore patterns

### Problem Organization

```
CoTe/
├── _template/                           # Reusable template for new problems
│   ├── README.md                        # Problem documentation template
│   └── solution.py                      # Code solution template
│
├── 001_해시_두개뽑아서더하기/
│   ├── README.md                        # Problem record with approach & reflections
│   └── solution.py                      # Implementation
│
├── 002_해시_완주하지못한선수/
│   ├── README.md
│   └── solution.py
│
└── NNN_주제_문제명/                      # Naming: {number}_{topic}_{problem}
    ├── README.md
    └── solution.py
```

### Naming Convention
- **Number**: Sequential `001`, `002`, `003`... (incremental order of problems solved)
- **Topic**: Algorithm category (해시, 스택, 정렬, DFS, BFS, DP, etc.)
- **Problem Name**: Korean problem title

**Examples**:
- `001_해시_두개뽑아서더하기/`
- `002_해시_완주하지못한선수/`
- `003_스택_올바른괄호/`
- `010_DP_N으로표현/`

## Problem Documentation Template

Each problem's `README.md` follows this structure:

```markdown
# [문제명]

#태그1 #태그2 #태그3

## 풀이 과정
### 핵심 아이디어
### 접근 방법
### 코드

## 회고
### 배운 점
### 어려웠던 부분
### 개선할 점

---
**복잡도**: O()
**풀이 날짜**:
```

### Documentation Philosophy
- **Focus on process**: Emphasize thinking process, not just final solution
- **Minimal metadata**: No redundant information (links, problem descriptions already in original sources)
- **Reflective learning**: Strong emphasis on learnings, difficulties, and improvements
- **Concise but detailed**: Balance between brevity and meaningful explanation

## Common Tasks

### Creating a New Problem
```bash
# 1. Copy template folder with new number, topic, and problem name
cp -r _template 001_해시_두개뽑아서더하기

# 2. Navigate to folder
cd 001_해시_두개뽑아서더하기

# 3. Edit README.md with problem approach and solution.py with code
# 4. Test solution locally
python3 solution.py

# 5. Update main README.md table with new entry
# 6. Commit changes
git add .
git commit -m "add(001_해시) : 두개뽑아서더하기 문제 풀이"
```

### Running a Solution
```bash
cd NNN_주제_문제명
python3 solution.py
```

### Updating Main README
When adding new problems, update `/README.md`:
- Add row to problem index table
- Update total problem count in statistics
- Add problem tags to algorithm categorization section if new topic

## Algorithm Categories

Supported algorithm topics (by hashtag):
- **#해시** - Hash/Dictionary-based problems
- **#스택** **#큐** - Stack/Queue structures
- **#정렬** - Sorting algorithms
- **#DFS** **#BFS** **#이진탐색** - Search techniques
- **#DP** - Dynamic Programming
- **#그래프** **#최단경로** - Graph problems
- **#그리디** - Greedy algorithms
- **#문자열** - String manipulation
- **#구현** - Implementation/Simulation
- **#수학** **#조합론** - Mathematical problems

## Code Review Focus Areas

When reviewing solutions, prioritize:

1. **Complexity Analysis**
   - Time complexity: Be explicit about O() notation
   - Space complexity: Consider auxiliary space
   - Is there a more optimal approach?

2. **Code Clarity**
   - Clear variable names
   - Logical problem-solving flow
   - Comments for non-obvious logic

3. **Edge Cases**
   - Empty inputs
   - Single elements
   - Maximum constraints
   - Special cases mentioned in problem

4. **Pythonic Patterns**
   - Use appropriate data structures (dict, set, deque, etc.)
   - Leverage built-in functions efficiently
   - Follow Python conventions

## Key Files to Reference

### For Adding New Problems
- `_template/README.md` - Documentation structure to follow
- `_template/solution.py` - Code template

### For Project Context
- `README.md` - Project overview and index
- `.gitignore` - Ignored files/directories

## Guidelines for Claude

When assisting with this repository:

1. **Creating New Problems**: Use template structure; maintain naming convention
2. **Documenting Solutions**: Emphasize process over just code; include reflections
3. **Code Analysis**: Focus on complexity, optimization, and algorithm choice justification
4. **Repo Maintenance**: Help update main README index when problems are added
5. **Learning Support**: Suggest algorithmic patterns and optimization opportunities
6. **Language**: Use Korean for documentation and explanations; Python code can use English variable names

## No Special Setup Required

- Pure Python 3 implementation
- No package dependencies
- No build or test framework (testing is manual or manual test cases)
- No development environment setup beyond Python 3

Solutions can be run directly with `python3 solution.py`.
