#!/usr/bin/env python

import os
import numpy as np
from astropy.table import Table, QTable
import astropy.units as u
import matplotlib.pyplot as plt
import argparse

def hubblefit():
    """This script fits the velocity and distance data from SIMBAD to
    obtain the Hubble constant."""

    # Second option: Read the path to Hubble data file from the command line
    # Obtain command line arguments
    parser = hubblefit_arguments()
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

    # Calculate the model line using the fit result a
    x = hubble_data['Distance']
    y = a[0] * hubble_data['Distance']

    # Calculate the age of the universe
    h = a[0] * u.km / u.s / u.Mpc
    age = 1.0 / h
    print("Hubble constant = {0:.2f}".format(h))
    print("Age of Universe = {0:.2f}".format(age.to(u.Gyr)))

    # (Optional) Save the result to a file
    if args.save:
        table = QTable()
        table['H_0'] = np.array([h.value]) * h.unit
        table['Age'] = np.array([age.to(u.Gyr).value]) * age.to(u.Gyr).unit
        table.write(args.save, format='fits')

    # (Optional) Plot the galaxy data, the fit and show the results
    if args.plot:
        plt.plot(hubble_data['Distance'], hubble_data['Velocity'], 'ob')
        plt.plot(x, y, '-r')
        plt.xlabel("Distance (Mpc)")
        plt.ylabel("Velocity (km/s)")
        plt.text(25., 300., "H$_0$ = {0:.2f} km/s/Mpc".format(h.value))
        plt.text(25., 150., "Age = {0:.2f}".format(age.to(u.Gyr)))
        plt.show()


def hubblefit_arguments():
    """Obtain command line arguments."""
    parser = argparse.ArgumentParser(description="Hubble expansion fit.")
    parser.add_argument('datafile', help='Input FITS file containing distances and velocities for galaxies', type=str)
    parser.add_argument('--plot', help='Plot the data and fit.', dest="plot", action="store_true", default=False)
    parser.add_argument('--save', help='Save the result to a named file', type=str)
    return parser


if __name__ == "__main__":
    hubblefit()