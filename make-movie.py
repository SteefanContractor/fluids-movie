#!/usr/bin/env python

import sys
import argparse
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import netCDF4 as nc

"""
Comments here about the script
"""

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input_file', help="Input file containing our data")
	parser.add_argument('field_name', help="Data field to animate")	
	args = parser.parse_args()
	
	# This is the same as sying:
	# f= nc.Dataset(args.input_file)
	with nc.Dataset(args.input_file) as f:
		# Vorticity is a multidimensional array
		# Time, ocean Z_ocecan, Y_ocean, X_ocean
		vorticity = f.variables['vorticity_z']
		vorticity = vorticity[:]
	
	# This code will be removed
	#import pdb
	#pdb.set_trace()	

	fig = plt.figure()
	vorticity_imgs = []
	for t in range(vorticity.shape[0]):
		#print t
		# Select the first time step, Z coordinate and all Y and X coordinates
		img = plt.imshow(vorticity[t,0,:,:])
		# The following command shows the plot
		#plt.show()
		# The following command saves the plot
		#plt.savefig('image%03d.png' % t)
		vorticity_imgs.append([img])
	
	vorticity_animation = animation.ArtistAnimation(fig, vorticity_imgs, interval=20)

	plt.show()	

	
	return True

if __name__=="__main__":
	sys.exit(main())


