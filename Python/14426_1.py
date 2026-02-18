import sys
from collections import defaultdict 
input = sys.stdin.readline

"""
문자열 탐색하는 트리(트라이) 만들기
딕셔너리로 구현
"""
N, M = map(int, input().split())
# trie[x] : 햔제 노드에서 선택할 수 있는 알파벳과 그에 해당하는 인덱스를 저장
trie: list[tuple[str, int]] = [{}]

# 집합 S의 원소
for _ in range(N):
  word = input().rstrip()
  cur_node = 0
  for ch in word:
    
    if ch not in trie[cur_node]: # 현재 위치에 ch가 없다면 
      # 새로운 노드 할당
      trie[cur_node][ch] = len(trie) 
      trie.append({})
    
    cur_node = trie[cur_node][ch] # cur_node 를 찾거나 생성한 위치로 이동

cnt = 0
for _ in range(M):
  word = input().rstrip()
  
  cur_node = 0
  for ch in word:
    if ch not in trie[cur_node]:
      break
    cur_node = trie[cur_node][ch]
  else:
    cnt += 1
  
print(cnt)