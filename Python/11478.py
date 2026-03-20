string = input()
L = len(string)

substring = set()

for i in range(L):
  for j in range(i+1, L+1):
    substring.add(string[i:j])

print(len(substring))