#!/usr/bin/env python3
#
# Copyright (C) 2023
#			Written by Nasrun (Nas) Hayeeyama
#

VERSIONNUMBER = 'v1.0'
PROGRAM_DESCRIPTION = "For testing in this "

########################################################
#
#	STANDARD IMPORTS
#

import uuid

import argparse

########################################################
#
#	LOCAL IMPORTS
#

from data.User import User

########################################################
#
#	Standard globals
#

########################################################
#
#	Program specific globals
#

########################################################
#
#	Helper functions
#

########################################################
#
#	Class definitions
#

########################################################
#
#	Function bodies
#

########################################################
#
#	main
#	
def main():
	
	# initial parser instance
	parser = argparse.ArgumentParser( description=PROGRAM_DESCRIPTION )

	# add arguments and option here

	# parse args
	args = parser.parse_args()

	user = User( uuid.uuid4(), 'test' )

	print( user )

########################################################
#
#	call main
#

if __name__=='__main__':
	main()

