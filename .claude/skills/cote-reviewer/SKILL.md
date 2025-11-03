---
name: cote-reviewer
description: When reviewing coding test solutions. This Skill reviews coding test solutions and provides feedback. it adds an evaluation section to the README.md file in the problem-solving folder, including areas for improvement, strengths, and other application ideas based on the provided template.
---

# CoTe Reviewer

## Instructions

# IMPORTANT : '회고' 영역은 사용자가 직접 작성하는 곳입니다.

1. 코딩 테스트 문제 풀이를 제출하면, 코드를 검토합니다.
2. 문제 풀이 폴더에 있는 README.md 파일에 분석 내용을 추가합니다.
3. 파일 하단에 새로운 섹션을 추가하여 다음 항목들을 포함하여 평가를 작성합니다:
   - 개선할 점
   - 잘한 점
   - 다른 응용 방안
   - 종합 평가
  
자세한 사용 방법은 '_template/README.md' 파일의 '평가' 섹션을 참고하세요.
포함하는 항목들은 예시일뿐 해당 문제와 사용자의 풀이 방식에 따라 조정될 수 있습니다.
종합 평가는 별표나 점수 형식이 아닌 서술형으로 작성해주세요. 평가는 칭찬보다는 비판적이고 건설적인 피드백으로 코딩 테스트 학습자가 인사이트를 얻을 수 있도록 도와주세요.
피드백은 코딩 테스트 관점에서 작성해주세요.

## Examples
Show concrete examples of using this Skill.

### Example 1

**Input:**
```markdown
# [방문길이]
- [문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/49994)

... (rest of the README content) ...

# 평가

## 개선할 점

- 코드에 주석을 추가하여 각 부분의 역할을 명확히 설명하면 가독성이 향상될 것입니다.
- 변수명과 함수명을 더 직관적으로 변경하여 코드의 의도를 쉽게 파악할 수 있도록 하면 좋겠습니다.
- 예외 처리 및 경계 조건에 대한 테스트 케이스를 추가하여 코드의 견고성을 높일 수 있습니다.

## 잘한 점
- set 자료구조를 활용하여 중복 경로를 효과적으로 처리한 점이 매우 좋습니다.
- 함수에서 tuple을 반환하고 언패킹하는 방식을 사용하여 코드의 간결성을 높인 점이 인상적입니다.
```
