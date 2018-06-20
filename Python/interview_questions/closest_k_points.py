'''
Given a list of 2d points and an integer k, find the k closest points to the origin.
'''
import math
import operator


def k_closest(k, points):
	'''
	First Attempt
	'''
	memo = {}

	for i, p in enumerate(points):
		memo[i] = get_distance(p)
	print(memo)

	sorted_memo = sorted(memo.items(), key=operator.itemgetter(1))

	return sorted_memo[:k]


def get_distance(point):
	return math.sqrt(point[0]**2 + point[1]**2)


if __name__ == '__main__':
	test_points = [(1, 1), (-1, -1), (2, 4), (3, 4), (-2, 1), (-1, 0)]
	k = 2
	print(k_closest(k, test_points))

