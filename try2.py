def funcread(fname) :
	f = open(fname,'r')
	for line in f :
		manage_line(line)

def manage_line(line) :
	splitline=line.split()
	if int( splitline[1]) > int( splitline[2]) :
		print line
		return line

manage_line('data1.txt')

