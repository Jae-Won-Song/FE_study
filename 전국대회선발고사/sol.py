# 그리드 알고리즘

def solution (rank, attendance):
# 변수 초기화
    answer = 0
    cnt = 0

    for i in range (1, len(rank) + 1):
        # 1부터 len(rank)까지의 숫자들을 포함하는 범위를 생성
        # len(rank)는 학생들의 수만큼 증가
        num = rank.index(i)
        # rank리스트에서 값이 i인 학생의 index를 반환후 num변수에 저장
        # [1,4], [1,8], [1,3] ...
        if attendance[num]:
            # 학생의 출석여부와 index 값을 확인, cnt에 저장
            answer += num * 100 **(2 - cnt)
            cnt += 1
        if cnt == 3:
            break
    return answer