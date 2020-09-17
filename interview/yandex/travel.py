import sys


class Travel:
	def __init__(self):
		self._city_count = int
		self._cities = {}
		self._max_distance = 0
		self._start_city = -1
		self._end_city = -1
		self._ways_len = []

	@property
	def start_city(self) -> int:
		return self._start_city

	def read_input(self) -> None:
		self._city_count = int(sys.stdin.readline().strip() or 0)

		for i in range(self._city_count):
			input_data = sys.stdin.readline().strip().split(' ')
			if len(input_data) == 2:
				self._cities[i+1] = list(map(int, input_data))

		self._max_distance = int(sys.stdin.readline().strip() or 0)

		input_data = sys.stdin.readline().strip().split(' ')
		if len(input_data) == 2:
			self._start_city = int(input_data[0])
			self._end_city = int(input_data[1])

	def read_file(self) -> None:
		with open('yandex/travel_input.txt', 'r') as file:
			self._city_count = int(file.readline())

			for i in range(self._city_count):
				self._cities[i + 1] = list(map(int, file.readline().split(' ')))

			self._max_distance = int(file.readline())
			cities_numbers = list(map(int, file.readline().split(' ')))
			self._start_city = cities_numbers[0]
			self._end_city = cities_numbers[1]

	def calculate(self, way: list, start_city: int) -> None:
		if start_city < 0:
			return None
		way += [start_city]
		if start_city == self._end_city:
			self._ways_len.append(len(way) - 1)
			return None
		else:
			start_coordinates = self._cities[start_city]
			for index, coordinates in self._cities.items():
				if index == start_city:
					continue
				if index in way:
					continue
				distance = abs(coordinates[0] - start_coordinates[0]) + abs(coordinates[1] - start_coordinates[1])
				if distance <= self._max_distance:
					self.calculate(list(way), index)

	def get_min(self) -> int:
		if self._ways_len:
			print(self._ways_len)
			return min(self._ways_len)
		else:
			return -1


travel_obj = Travel()
travel_obj.read_file()
# travel_obj.read_input()
travel_obj.calculate([], travel_obj.start_city)
print(travel_obj.get_min())
