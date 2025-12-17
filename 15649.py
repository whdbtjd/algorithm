N, M = map(int, input().split())

arr = []              # 현재 수열
visited = [False] * (N + 1)  # 숫자 사용 여부

def backtrack():

    if len(arr) == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            backtrack()

            # 되돌리기
            arr.pop()
            visited[i] = False

backtrack()
