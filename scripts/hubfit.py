#!/usr/bin/env python

import os
import numpy as np
import argparse
from astropy.table import Table
import matplotlib.pyplot as plt

def hubfit():
    """This script fits the velocity and distance data from SIMBAD to
    obtain the Hubble constant."""

    # Second option: Read the path to Hubble data file from the command line
    # Obtain command line arguments
    parser = hubfit_arguments()
    args = parser.parse_args()

    # We check if the input datafile exists
    if not os.path.isfile(args.datafile):
        print("Error: Input data file not found.")
        return

    # Read the hubble data table
    hubble_data = Table.read(args.datafile)

    # Fit the distance and velocity to a straight line using numpy linalg
    # Somehow, the lstsq function requires the x coordinates to be 2D
    distance = np.array(hubble_data['Distance'])
    distance = distance[:, np.newaxis]
    (a, res, rank, s) = np.linalg.lstsq(distance, hubble_data['Velocity'], rcond=None)

    x = hubble_data['Distance']
    y = a * hubble_data['Distance']

    if args.plot:
        plt.plot(hubble_data['Distance'], hubble_data['Velocity'], 'ob')
        plt.plot(x, y, '-r')
        plt.xlabel("Distance (Mpc)")
        plt.ylabel("Velocity (km/s)")
        plt.text(20., 300., "H$_0$ = {0} km/s/Mpc".format(a[0]))
        plt.show()

def hubfit_arguments():
    """Obtain command line arguments."""
    parser = argparse.ArgumentParser(description="Hubble expansion fit.")
    parser.add_argument('datafile', help='Input FITS file containing distances and velocities for galaxies', type=str)
    parser.add_argument('--plot', help='Plot the data and fit.', dest="plot", action="store_true", default=False)
    parser.add_argument('--save', help='Save the result to a named file', type=str)
    return parser


if __name__ == "__main__":
    hubfit()