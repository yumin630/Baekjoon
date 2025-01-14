import math

def repair_road():
    # 입력 처리
    n, l = map(int, input().split())
    puddles = [tuple(map(int, input().split())) for _ in range(n)]
    
    # 시작점 기준으로 정렬
    puddles.sort()
    
    # 널빤지 사용 계산
    boards_used = 0
    covered_until = 0  # 현재 덮은 위치 끝점
    
    for start, end in puddles:
        # 현재 구간이 이미 덮여있는 경우
        if covered_until >= end:
            continue
        
        # 덮지 않은 부분부터 시작
        if covered_until < start:
            covered_until = start
        
        # 현재 구간 덮기
        length_to_cover = end - covered_until
        needed_boards = math.ceil(length_to_cover / l)
        boards_used += needed_boards
        
        # 널빤지로 덮은 끝점을 갱신
        covered_until += needed_boards * l
    
    print(boards_used)

# 실행
repair_road()
