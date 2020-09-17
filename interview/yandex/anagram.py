import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()


def collect_dict(input: str):
	result = {}
	for ch in input:
		if result.get(ch):
			result[ch] += 1
		else:
			result[ch] = 1

	return result


diff = len(str1) == len(str2) and collect_dict(str1) == collect_dict(str2)
print(int(diff))
