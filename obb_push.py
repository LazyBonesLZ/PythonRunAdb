#!/usr/bin/python
import subprocess
import os, sys
import getopt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


if __name__ == '__main__':

	""" change commands and add shell"""

	tag = ''

	try:
		opt, args = getopt.getopt(sys.argv[1:], "ht:", ['tag', 'help'])
		for op, value in opt:
			if op in ("-t", "--tag"):
				tag = value
			if op in ("-h", "--help"):
				print "Usage: obb_push.py -t TAG_NAME"
				print "Options:"
				print "  -t  TAG_NAME.Choose what you want to use tag, should be a obb file path !"
				print ""
				print "Sample : ./obb_push.py -t <obb file path>"
				print ""
				sys.exit()
	except getopt.GetoptError:  
            print "Error: Could not find the args."
            print "Usage: obb_push.py -t TAG_NAME"
    	    print "Options:"
    	    print "  -t  TAG_NAME.Choose what you want to use tag, should be a obb file path !"
    	    print ""
    	    print "Sample : ./obb_push.py -t <obb file path>"
    	    print ""
    	    sys.exit()

	
	if tag == '':
		print "you should input a obb file\'s path !"
		exit()

	print '======to get package name=======>'
	obbFilePath = tag
	if obbFilePath == '':
		print 'you should input a obb file\'s path !'
		exit()
	obbSubDirs = obbFilePath.split('/')
	# index  = len(obbSubDirs) - 1
	obbFileName = obbSubDirs[-1]
	print '>>>obbFileName = ' + obbFileName
	if obbFileName == '' or obbFileName.find('.obb') == -1:
		print 'can not find a obb file in the path !'
		exit()
	
	tmpPackageName = obbFileName.split('.')
	print  tmpPackageName
	packageName = ''
	# for com in tmpPackageName[2:-2]:
	# 	print com
	# 	if com == tmpPackageName[-2]:
	# 	 	packageName += com
	# 	else:
	# 	 	packageName += com + "." 
	packageName = '.'.join(tmpPackageName[2:-1])
	print '>>>package name = ' + packageName


	print '=======adb shell mkdir ========>'
	obbDestPath = 'sdcard/Android/obb/' + packageName
	subDir = ''
	subDirs = obbDestPath.split('/')
	for dir in subDirs:
	 	subDir += '/' + dir
	 	# print subDir 
	 	os.system('adb shell mkdir ' + subDir)

	print '=======adb push obb file to device ========>'
	pushCmd = 'adb push ' + obbFilePath.replace(' ','\\ ')+ ' /' + obbDestPath + '/' 
	# print pushCmd
	os.system(pushCmd)

	exit()


