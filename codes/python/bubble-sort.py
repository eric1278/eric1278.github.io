def bubble_sort(number_list):
	def check(number_list):
		index = 0
		done = False
		while not done:
			if index + 1 >= len(number_list):
				break
			if number_list[index] > number_list[index+1]:
				done = True
			index += 1
		return not done

	while not check(number_list):
		index = 0
		done = False
		while not done:
			if not(index + 1 < len(number_list)):
				break

			if number_list[index] > number_list[index+1]:
				before = number_list[index]
				number_list[index] = number_list[index+1]
				number_list[index+1] = before

			index += 1

	return number_list

print(bubble_sort([1, 100, 4, 9, 5, 0, 8, 0.6, -5]))
