#!/usr/bin/env python

import sys
import argparse
import numpy as np
import netCDF4 as nc

"""
Comments here about the script
"""

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_file', help="Input file containing our data")
	parser.add_argument('field_name', help="Data field to anumate")	
	args = parser.parse_args()
	return True

if __name__=="__main__":
	sys.exit(main())


