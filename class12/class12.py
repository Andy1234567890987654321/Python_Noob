d = {}
while True:
    k = input("key:")
    v = input("value")
    d[k] = v
    print(d)
    if input("要不要離開(n)?") == "n":
        break

while True:
    k = input("key:")
    if k in d:
        d.pop(k)
    print(d)
    if input("要不要離開(n)?") == "n":
        break
for k, v in d.items():
    print(f'{k}={v}')
