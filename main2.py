ds = {} 
for _ in range(int(input())): 
  w1, w2 = input().split()
  ds[w1] = w2
  ds[w2] = w1
print(ds[input()])