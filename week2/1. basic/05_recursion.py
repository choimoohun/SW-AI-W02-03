def factorial(n):
    """
    재귀를 사용한 팩토리얼 계산
    
    Args:
        n: 양의 정수
    
    Returns:
        n의 팩토리얼 값
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """
    재귀를 사용한 피보나치 수 계산
    
    Args:
        n: 구하고자 하는 피보나치 수의 인덱스
    
    Returns:
        n번째 피보나치 수
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 테스트 케이스
if __name__ == "__main__":
    # 팩토리얼 테스트
    print("=== 팩토리얼 계산 ===")
    for i in range(6):
        result = factorial(i)
        print(f"{i}! = {result}")
    print()
    
    # 피보나치 테스트
    print("=== 피보나치 수열 ===")
    for i in range(10):
        result = fibonacci(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 추가 테스트
    print("=== 추가 테스트 ===")
    print(f"10! = {factorial(10)}")
    print(f"fib(15) = {fibonacci(15)}")


