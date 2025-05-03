board = input()
result = ''
i = 0

while i < len(board):
    if board[i] == 'X':
        count = 0
        # 'X'로 이루어진 부분의 길이를 계산
        while i < len(board) and board[i] == 'X':
            count += 1
            i += 1
        # 길이가 홀수이면 덮을 수 없음
        if count % 2 != 0:
            result = -1
            break
        # 'AAAA'를 최대한 배치
        result += 'AAAA' * (count // 4)
        # 남은 부분에 'BB'를 배치
        result += 'BB' * ((count % 4) // 2)
    else:
        result += '.'
        i += 1

print(result)
