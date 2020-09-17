J = "ab"
S = "aabbccd"

count = 0
for ch in S:
    if ch in J:
        count += 1
print(count)
