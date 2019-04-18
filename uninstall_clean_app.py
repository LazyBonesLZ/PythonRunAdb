#!/usr/bin/python
import subprocess
import os, sys
import getopt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


if __name__ == '__main__':

	""" change commands and add shell"""

	tag = ''

	try:
		opt, args = getopt.getopt(sys.argv[1:], "ht:", ['pkg', 'help'])
		for op, value in opt:
			if op in ("-t", "--pkg"):
				tag = value
			if op in ("-h", "--help"):
				print "Usage: main_app_clean.py -t APP_PKG_NAME"
				print "Options:"
				print "  -t  APP_PKG_NAME should be a bundle id !"
				print ""
				print "Sample : ./main_app_clean.py -t <bundle id>"
				print ""
				sys.exit()
	except getopt.GetoptError:  
            print "Error: Could not find the args."
            print "Usage: main_app_clean.py -t APP_PKG_NAME"
    	    print "Options:"
    	    print "  -t  APP_PKG_NAME should be a bundle id !"
    	    print ""
    	    print "Sample : ./main_app_clean.py -t <bundle id>"
    	    print ""
    	    sys.exit()

	
	if tag == '':
		print "you should input a bundle id  !"
		exit()
	pkg = tag

	print ''
	print '1) uninstalling ' + pkg +' ...'
	unInstallCmd = 'adb uninstall  ' + pkg 
	os.system(unInstallCmd)

	print ''
	print '2) cleaning the cached file...'
	cleanCmd1 = 'adb shell rm -fR /sdcard/.DataBackupTest'
	os.system(cleanCmd1)
	cleanCmd2 = 'adb shell rm -fR /sdcard/.DataBackup'
	os.system(cleanCmd2)
	print ''
	print '	All done !^_^!'
	print ''

	exit()


