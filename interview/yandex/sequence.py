import sys

input_count = int(sys.stdin.readline().strip())

max_count = 0
count = 0
for i in range(input_count):
	item = sys.stdin.readline().strip()

	if item == '1':
		count += 1
		max_count = max(max_count, count)
	else:
		count = 0
print(max_count)
