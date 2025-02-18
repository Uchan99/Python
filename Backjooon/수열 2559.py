'''
1. 아이디어
- 투포인터 활용
- for 문으로, 처음에 K개의 값을 저장
- 다음 인덱스 더해주고, 이전 인덱스를 빼줌
- 이때마다 최대값을 갱신

2. 시간 복잡도
- O(N) = 1e5 > 가능

3. 자료구조
- 각 숫자들 N개 저장 배열 ; int[]
    - 숫자들 최대 100 > INT 가능
- K개의 값을 저장 변수 : int
    - 쵀대 ; K * 100 = 1e5 * 100 = 1e7 > INT 가능
- 최대값 :int
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

temps = list(map(int, input().split()))
maxtemp, ptemp = 0, 0

for i in range(K):
    ptemp += temps[i]

maxtemp = ptemp

for i in range(K, N):
    ptemp = ptemp + temps[i] - temps[i-K]
    maxtemp = max(maxtemp, ptemp)

print(maxtemp)
