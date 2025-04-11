#!/usr/bin/env python

import numpy as np
from astropy.table import Table
import astropy.units as u
import matplotlib.pyplot as plt


def hubblefit():
    """This script fits the velocity and distance data from SIMBAD to
    obtain the Hubble constant."""

    # Read the hubble data table
    hubble_data = Table.read('hubble_data.fits')

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

    # Plot the galaxy data, the fit and show the results
    plt.plot(hubble_data['Distance'], hubble_data['Velocity'], 'ob')
    plt.plot(x, y, '-r')
    plt.xlabel("Distance (Mpc)")
    plt.ylabel("Velocity (km/s)")
    plt.text(25., 300., "H$_0$ = {0:.2f} km/s/Mpc".format(h.value))
    plt.text(25., 150., "Age = {0:.2f}".format(age.to(u.Gyr)))
    plt.show()


if __name__ == "__main__":
    hubblefit()