"""
테스트 실행 모듈 (다중 언어 지원)

각 언어별 테스트 러너를 관리합니다.
"""

from .python import run_tests

__all__ = ["run_tests"]
