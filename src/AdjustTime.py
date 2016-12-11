import sys
import os
import datetime 

def main():
	if len(sys.argv) < 2:
		print('Please provide srt file path.')
		return
	path = sys.argv[1]
	d = datetime.timedelta(seconds=int(sys.argv[2]))
	outputpath = path + '.out'	
	fout = open(outputpath, 'w')
	with open(path, 'r') as f:
		for line in f:
			if '-->' not in line:
				fout.write(line)
				continue
			newline = getLineWithNewTime(line, d)
			fout.write(newline)
	fout.close()

def getLineWithNewTime(line, delta):
	print('old:' + line)
	splits = line.split('-->')
	start = datetime.datetime.strptime(splits[0].strip(), '%H:%M:%S,%f')
	nstart = start + delta
	end = datetime.datetime.strptime(splits[1].strip(), '%H:%M:%S,%f')
	nend = end + delta
	nline = nstart.strftime('%H:%M:%S,%f')[:-3] + ' --> ' +  nend.strftime('%H:%M:%S,%f')[:-3] + '\n'
	print('new:' + nline)
	return nline

main()