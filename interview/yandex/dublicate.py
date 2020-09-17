import sys

input_count = int(sys.stdin.readline().strip())

last = None
for i in range(input_count):
	item = sys.stdin.readline().strip()

	if item != last:
		print(item)
		last = item
