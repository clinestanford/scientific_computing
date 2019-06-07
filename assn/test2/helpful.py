

import scipy as sp 

x = [1,2,3]
y = [2,3,3.5]

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

def gaussia_pdf(x, sigma=1, mu=0):
	a = 1.0 / (sigma * math.sqrt(2*math.pi))
	b = math.e**(-.5*(((x-mu)/sigma)**2))
	return a * b

def approximage_iq():
	iqc = lambda x: gaussia_pdf(x, sigma=16, mu=100)
	print(simson_rule_aux(iqc, 120, 126, 6))

def error(f,x,y):
	return sp.sum((f(x) - y)**2)

pcoeffs, err, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

f1 = sp.poly1d(sp.polyfit(x,y,1))

print(f1(2))
print(pcoeffs, err, error(f1,x,y))

#boolean indexing
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


##using numpy
np.median(array)
array.mean()
from scipy import stats
stats.mode(array)[0][0] ##will return the most frequently occuring values

stats.mode()