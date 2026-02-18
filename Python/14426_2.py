import sys
input = sys.stdin.readline

"""
문자열 탐색하는 트리(트라이) 만들기
딕셔너리 지우고 리스트로 구현
"""
def s2i(x:str):
  return ord(x) - 97

N, M = map(int, input().split())
# trie[x] : 햔제 노드에서 선택할 수 있는 알파벳과 그에 해당하는 인덱스를 저장
trie: list[list[int]] = [[-1]*26]

# 집합 S의 원소
for _ in range(N):
  word = input().rstrip()
  cur_node = 0
  for ch in word:
    ch_i = s2i(ch)

    if trie[cur_node][ch_i] == -1: # 현재 위치에 ch가 없다면 
      # 새로운 노드 할당
      trie[cur_node][ch_i] = len(trie) 
      trie.append([-1]*26)
    
    cur_node = trie[cur_node][ch_i] # cur_node 를 찾거나 생성한 위치로 이동

cnt = 0
for _ in range(M):
  word = input().rstrip()
  
  cur_node = 0
  for ch in word:
    ch_i = s2i(ch)
    if trie[cur_node][ch_i] == -1:
      break
    cur_node = trie[cur_node][ch_i]
  else:
    cnt += 1

print(cnt)