import sys

input_count = int(sys.stdin.readline().strip())


def brackets(current: str, open_count: int, close_count: int, count):
	if len(current) == count * 2:
		print(current)
		return
	if open_count < count:
		brackets(current + '(', open_count + 1, close_count, count)
	if open_count > close_count:
		brackets(current + ')', open_count, close_count + 1, count)


brackets('', 0, 0, input_count)
