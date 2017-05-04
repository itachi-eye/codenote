cnt = 0
for n in range(1, 22):
    for a in range(1, 10):
        if len(str(a ** n)) == n:
            cnt += 1
            print(a, n)
print(cnt)
