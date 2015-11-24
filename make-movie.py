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
	
	# This is the same as sying:
	# f= nc.Dataset(args.input_file)
	with nc.Dataset(args.input_file) as f:
		vorticity = f.variables['vorticity_z']
		vorticity = vorticity[:]
	

	return True

if __name__=="__main__":
	sys.exit(main())


