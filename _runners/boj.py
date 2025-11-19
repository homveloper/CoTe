"""
백준(BOJ) 테스트 실행 모듈

백준 문제풀이용 Python 테스트 러너
- 표준 입출력(stdin/stdout) 기반
- 파일 기반 테스트케이스 지원
- 실수 근사값 비교 지원
"""

import sys
import subprocess
import time
from pathlib import Path


# float32 유효 자릿수 기준 허용 오차 (약 7자리)
FLOAT32_RTOL = 1e-6
FLOAT32_ATOL = 1e-6


def is_close(a, b, rtol=FLOAT32_RTOL, atol=FLOAT32_ATOL):
    """두 실수가 허용 오차 내에서 같은지 비교"""
    return abs(a - b) <= atol + rtol * abs(b)


def compare_float_output(result, expected, rtol=FLOAT32_RTOL, atol=FLOAT32_ATOL):
    """
    실수 출력을 근사값으로 비교

    Args:
        result: 실제 출력 문자열
        expected: 기대 출력 문자열
        rtol: 상대 오차 허용 범위 (relative tolerance)
        atol: 절대 오차 허용 범위 (absolute tolerance)

    Returns:
        bool: 근사값 비교 결과
    """
    try:
        # 각 줄의 값들을 실수로 변환
        result_values = []
        expected_values = []

        for line in result.strip().split('\n'):
            result_values.extend([float(x) for x in line.split()])

        for line in expected.strip().split('\n'):
            expected_values.extend([float(x) for x in line.split()])

        if len(result_values) != len(expected_values):
            return False

        # 모든 값이 허용 오차 내에 있는지 확인
        return all(
            is_close(r, e, rtol, atol)
            for r, e in zip(result_values, expected_values)
        )

    except (ValueError, TypeError):
        # 실수 변환 실패 시 문자열 비교로 폴백
        return result == expected


def format_memory(bytes_value):
    """바이트를 읽기 좋은 형식으로 변환"""
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_value < 1024:
            return f"{bytes_value:.2f}{unit}"
        bytes_value /= 1024
    return f"{bytes_value:.2f}TB"


def load_file_testcases(test_file_path):
    """testcases/ 폴더에서 .in/.out 파일 쌍을 로드"""
    testcases_dir = Path(test_file_path).parent / "testcases"
    file_cases = []

    if not testcases_dir.exists():
        return file_cases

    # .in 파일 찾기
    for in_file in sorted(testcases_dir.glob("*.in")):
        out_file = in_file.with_suffix(".out")
        if out_file.exists():
            file_cases.append({
                "name": f"[파일] {in_file.stem}",
                "input": in_file.read_text(),
                "expected": out_file.read_text(),
            })

    return file_cases


def run_tests(test_cases, solution_file=None, float_compare=False):
    """
    백준 테스트 케이스 실행

    Args:
        test_cases: 테스트 케이스 리스트
                   [{"name": "...", "input": "...", "expected": "..."}, ...]
        solution_file: solution.py 경로 (None이면 호출한 파일 기준으로 찾음)
        float_compare: True면 실수 근사값 비교 (float32 유효자릿수 기준)

    Examples:
        from _runners import run_boj_tests

        test_cases = [
            {
                "name": "예제 1",
                "input": "5\\n5 4 3 2 1\\n",
                "expected": "1 2 3 4 5\\n",
            },
        ]

        # 정수/문자열 비교
        run_boj_tests(test_cases)

        # 실수 근사값 비교
        run_boj_tests(test_cases, float_compare=True)
    """
    # solution.py 경로 결정
    if solution_file is None:
        # 호출한 test.py 기준으로 solution.py 찾기
        import inspect
        caller_frame = inspect.stack()[1]
        caller_file = Path(caller_frame.filename)
        solution_file = caller_file.parent / "solution.py"
    else:
        solution_file = Path(solution_file)

    # 파일 기반 테스트케이스 추가
    caller_frame = __import__('inspect').stack()[1]
    test_file_path = caller_frame.filename
    all_cases = test_cases + load_file_testcases(test_file_path)

    if not all_cases:
        print("테스트 케이스가 없습니다.")
        print("test_cases 리스트를 정의하거나 testcases/ 폴더에 .in/.out 파일을 추가하세요.")
        return

    print("=" * 70)
    compare_mode = "실수 근사값" if float_compare else "문자열"
    print(f"백준 테스트 시작 (솔루션: {solution_file.name}, 비교: {compare_mode})")
    print("=" * 70 + "\n")

    passed_count = 0
    failed_count = 0
    total_time = 0

    for test_case in all_cases:
        name = test_case["name"]
        input_data = test_case["input"]
        expected = test_case["expected"].rstrip('\n')

        try:
            # 시간 측정
            start_time = time.perf_counter()

            # 솔루션 실행
            result_proc = subprocess.run(
                [sys.executable, str(solution_file)],
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5  # 5초 타임아웃
            )

            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            total_time += elapsed_time

            # 결과 비교 (trailing newline 제거)
            result = result_proc.stdout.rstrip('\n')
            stderr = result_proc.stderr

            # 비교 방식 선택
            if float_compare:
                passed = compare_float_output(result, expected)
            else:
                passed = result == expected

            status = "✓ 통과" if passed else "✗ 실패"

            if passed:
                passed_count += 1
            else:
                failed_count += 1

            print(f"[{status}] {name}")
            print(f"  시간: {elapsed_time*1000:.2f}ms")

            if not passed:
                # 입력 미리보기 (최대 3줄)
                input_lines = input_data.strip().split('\n')
                input_preview = '\n'.join(input_lines[:3])
                if len(input_lines) > 3:
                    input_preview += "\n    ..."

                print(f"  입력:")
                for line in input_preview.split('\n'):
                    print(f"    {line}")
                print(f"  기대값: {expected}")
                print(f"  결과값: {result}")

                if stderr:
                    print(f"  에러: {stderr.strip()}")

            print()

        except subprocess.TimeoutExpired:
            failed_count += 1
            print(f"[✗ 시간초과] {name}")
            print(f"  5초 타임아웃 초과")
            print()

        except Exception as e:
            failed_count += 1
            print(f"[✗ 에러] {name}")
            print(f"  에러: {e}")
            print()

    # 결과 요약
    print("=" * 70)
    print(f"테스트 완료: {passed_count} 통과, {failed_count} 실패")
    print(f"총 실행 시간: {total_time*1000:.2f}ms")
    print("=" * 70)
