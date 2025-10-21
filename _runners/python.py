"""
Python 테스트 실행 모듈

프로그래머스(Programmers) 문제풀이용 Python 테스트 러너
"""

import time
import tracemalloc
from solution import solution


def format_memory(bytes_value):
    """바이트를 읽기 좋은 형식으로 변환"""
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_value < 1024:
            return f"{bytes_value:.2f}{unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f}TB"


def run_tests(test_cases):
    """
    테스트 케이스 실행

    Args:
        test_cases: 테스트 케이스 리스트 (test.py에서 import)
                   [{"name": "...", "input": ..., "expected": ...}, ...]
    """
    print("=" * 70)
    print("테스트 시작")
    print("=" * 70 + "\n")

    passed_count = 0
    failed_count = 0
    total_time = 0
    max_memory = 0

    for test_case in test_cases:
        name = test_case["name"]
        input_data = test_case["input"]
        expected = test_case["expected"]

        try:
            # 메모리 추적 시작
            tracemalloc.start()
            start_time = time.perf_counter()

            # 입력이 튜플이면 언팩(여러 인자), 아니면 그대로(단일 인자)
            if isinstance(input_data, tuple):
                result = solution(*input_data)
            else:
                result = solution(input_data)

            # 시간과 메모리 측정
            end_time = time.perf_counter()
            peak = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            elapsed_time = end_time - start_time
            total_time += elapsed_time
            max_memory = max(max_memory, peak)

            passed = result == expected
            status = "✓ 통과" if passed else "✗ 실패"

            if passed:
                passed_count += 1
            else:
                failed_count += 1

            print(f"[{status}] {name}")
            print(f"  입력   : {input_data}")
            print(f"  기대값 : {expected}")
            print(f"  결과값 : {result}")
            print(f"  시간   : {elapsed_time*1000:.2f}ms")
            print(f"  메모리 : {format_memory(peak)}")
            print()

        except Exception as e:
            failed_count += 1
            tracemalloc.stop()
            print(f"[✗ 에러] {name}")
            print(f"  입력 : {input_data}")
            print(f"  에러 : {e}")
            print()

    # 결과 요약
    print("=" * 70)
    print(f"테스트 완료: {passed_count} 통과, {failed_count} 실패")
    print(f"총 실행 시간 : {total_time*1000:.2f}ms")
    print(f"최대 메모리  : {format_memory(max_memory)}")
    print("=" * 70)
