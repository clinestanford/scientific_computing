#!/usr/bin/python

####################################
# module: hw09_s19.py
# YOUR NAME
# YOUR A#
####################################

import csv
import matplotlib.pyplot as plt
import os


def generate_file_names(ftype, rootdir):
		'''
		recursively walk dir tree beginning from rootdir
		and generate full paths to all files that end with ftype.
		sample call: generate_file_names('.jpg', /home/pi/images/')
		'''
		for path, dirlist, filelist in os.walk(rootdir):
				for file_name in filelist:
						if not file_name.startswith('.') and \
							 file_name.endswith(ftype):
								yield os.path.join(path, file_name)
				for d in dirlist:
						generate_file_names(ftype, d)

def display_csv_file(csv_file_path):
	fd = {}
	with open(csv_file_path, 'r') as instream:
		reader = csv.reader(instream, delimiter = ",")
		for row in reader:
			print(row)

def read_csv_file(csv_file_path):
	fd = {}
	with open(csv_file_path, 'r') as instream:
		reader = csv.reader(instream, delimiter = ",")
		next(reader)
		# reader.next() #to skip the header
		for row in reader:
			secs, up, down, lat = int(row[0]), float(row[1]), \
														float(row[2]), float(row[3])
			fd[secs] = (up, down, lat)
		return fd

def plot_bee_traffic(csv_fp):

	fd = read_csv_file(csv_fp)

	time = []
	up = []
	down = []
	lat = []

	for key in fd.keys():
		time.append(key)
		up.append(fd[key][0])
		down.append(fd[key][1])
		lat.append(fd[key][2])

	ally = up + down + lat

	fig1 = plt.figure(1)
	fig1.suptitle("Bee Traffic for " + csv_fp.split('/')[1])
	plt.xlabel('t (seconds)')
	plt.ylabel('moving bees')
	plt.ylim(0, max(ally) + .5)
	plt.xlim(min(time) - 2, max(time) + 2)
	plt.grid()
	plt.plot(time, up, label="upward", c='r')
	plt.plot(time, down, label="downward", c='g')
	plt.plot(time, lat, label="lateral", c='b')
	plt.legend(loc='best')
	plt.show(block=True)


def bee_traffic_estimate(t, md='u', fd={}):
	assert md == 'u' or md == 'd' or md == 'l'
	vals = fd.get(int(t))
	if vals is None:
		return None
	elif md == 'u':
		return vals[0]
	elif md == 'd':
		return vals[1]
	elif md == 'l':
		return vals[2]

def make_bee_traffic_estimator(fd, md):
	assert md == 'u' or md == 'd' or md == 'l'
	return lambda t: bee_traffic_estimate(t, md=md, fd=fd)


import numpy as np
def bee_traffic_stats(fd):
	
	up_est = make_bee_traffic_estimator(fd, 'u')
	down_est = make_bee_traffic_estimator(fd, 'd')
	lat_est = make_bee_traffic_estimator(fd, 'l')

	return (sr_approx(up_est, 5, 28, 23), sr_approx(down_est, 5, 28, 23), sr_approx(lat_est, 5, 28, 23))

def find_smallest_up_down_gap_file(csv_dir):

	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,0,0,1e6)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if abs(curUp - curDown) < best[4]:
			best = (file, curUp, curDown, curLat, abs(curUp - curDown))

	return best


def find_largest_up_down_gap_file(csv_dir):
	
	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,0,0,0)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if abs(curUp - curDown)> best[4]:
			best = (file, curUp, curDown, curLat, abs(curUp - curDown))

	return best


############################

def find_max_up_file(csv_dir):
	
	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,0,0)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if curUp > best[1]:
			best = (file, curUp, curDown, curLat)

	return best

def find_min_up_file(csv_dir):
	
	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,1e6,0,0)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if curUp < best[1]:
			best = (file, curUp, curDown, curLat)

	return best

###########################

def find_max_down_file(csv_dir):

	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,0,0)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if curDown > best[2]:
			best = (file, curUp, curDown, curLat)

	return best

def find_min_down_file(csv_dir):
	
	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,1e6,0)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if curDown < best[2]:
			best = (file, curUp, curDown, curLat)

	return best

def find_max_lat_file(csv_dir):
	
	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,0,0)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if curLat > best[3]:
			best = (file, curUp, curDown, curLat)

	return best

def find_min_lat_file(csv_dir):
	
	generator = generate_file_names(".csv", csv_dir)

	#(fp, up, down, lat, gap)
	best = (0,0,0,1e6)

	for file in generator:
		fd = read_csv_file(file)
		curUp, curDown, curLat = bee_traffic_stats(fd)
		if curLat < best[3]:
			best = (file, curUp, curDown, curLat)

	return best


def sr_approx(func, a, b, n):
  
  interval = (b - a) / n
  vals = [func(i) for i in np.arange(a, b + interval, interval)]

  area = vals[0] + vals[len(vals)-1]

  for i in range(1, len(vals) - 1):
    if i % 2 != 0:
      area += vals[i] * 4
    else:
      area += vals[i] * 2

  return (area * interval * (1/3))

	
if __name__ == '__main__':
	#plot_bee_traffic("bee_traffic_estimates/192_168_4_5-2018-07-01_08-00-10.csv")
	print(find_max_up_file('bee_traffic_estimates'))