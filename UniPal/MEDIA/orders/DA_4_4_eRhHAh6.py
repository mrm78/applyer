n, k = input().split()
n = int(n)
k = int(k)

arr = []
for i in input().split():
    arr.append(int(i))

#generate graph G 
G = {i : {j:abs(arr[i]-arr[j]) for j in range(i+1, min(n, i+k+1))} for i in range(n)}

#singel shortest path for DAG
d = {i:10000000 for i in range(n)}
d[0] = 0
p = {i:None for i in range(n)}

for u in range(n):
    for v in G[u]:
        if d[v] >= d[u] + G[u][v]:
            d[v] = G[u][v]
            p[v] = u

Sum = 0
v = n-1
while v != 0:
    Sum += G[p[v]][v]
    v = p[v]

print(Sum)