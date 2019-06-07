

import unittest

from hw09_s19 import find_max_lat_file, find_min_lat_file, find_min_down_file, find_max_down_file, find_min_up_file, find_max_up_file, find_largest_up_down_gap_file, read_csv_file, bee_traffic_stats, find_smallest_up_down_gap_file, plot_bee_traffic

class TestHw9(unittest.TestCase):

	def test_bee_traffic_stats(self):
		fd = read_csv_file("bee_traffic_estimates/192_168_4_5-2018-07-01_14-00-10.csv")
		print(bee_traffic_stats(fd))

	def test_smallest_gap(self):
		fp, u, d, l, gap = find_smallest_up_down_gap_file("bee_traffic_estimates")
		print(fp, u, d, l, gap)
		plot_bee_traffic(fp)

	def test_smallest_gap(self):
		fp, u, d, l, gap = find_largest_up_down_gap_file("bee_traffic_estimates")
		print(fp, u, d, l, gap)
		plot_bee_traffic(fp)

	def test_max_travels(self):

		fp, u, d, l = find_max_up_file("bee_traffic_estimates")
		print(fp, u, d, l)
		plot_bee_traffic(fp)

		fp, u, d, l = find_min_up_file("bee_traffic_estimates")
		print(fp, u, d, l)
		plot_bee_traffic(fp)

		fp, u, d, l = find_max_down_file("bee_traffic_estimates")
		print(fp, u, d, l)
		plot_bee_traffic(fp)

		fp, u, d, l = find_min_down_file("bee_traffic_estimates")
		print(fp, u, d, l)
		plot_bee_traffic(fp)

		fp, u, d, l = find_max_lat_file("bee_traffic_estimates")
		print(fp, u, d, l)
		plot_bee_traffic(fp)

		fp, u, d, l = find_min_lat_file("bee_traffic_estimates")
		print(fp, u, d, l)
		print("fp: ", fp)
		plot_bee_traffic(fp)


if __name__ == '__main__':
	unittest.main()