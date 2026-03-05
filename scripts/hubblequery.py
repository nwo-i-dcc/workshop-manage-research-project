#!/usr/bin/env python

from astroquery.simbad import Simbad
from astropy import constants as const
from astropy.table import QTable


def main():
    """This script retrieves the latest velocities and distances for the objects that
    Edwin Hubble used to find the famous Hubble universe expansion law in 1929."""

    # These are the galaxies that Edwin Hubble used
    hubble_objects = ['NGC 278', 'NGC 404', 'NGC 584', 'NGC 936', 'NGC 1023', 'NGC 1700',
                      'NGC 2681', 'NGC 2683', 'NGC 2841', 'NGC 3034', 'NGC 3115', 'NGC 3368',
                      'NGC 3379', 'NGC 3489', 'NGC 3521', 'NGC 3623', 'NGC 4111', 'NGC 4526',
                      'NGC 4565', 'NGC 4594', 'NGC 5005', 'NGC 5866']

    # Retrieve the data from SIMBAD using astroquery.Simbad
    simbad = Simbad()
    simbad.add_votable_fields('distance', 'velocity')
    hubble_data = simbad.query_objects(hubble_objects)

    # Convert redshifts to velocities and convert MAIN_ID to strings
    c = const.c.to('km/s')
    for i in range(hubble_data['rvz_radvel'].size):
        # If the datatype is redshift (z), then multiply with c to obtain velocity in km/s
        if hubble_data['rvz_type'][i] == 'z':
            hubble_data['rvz_radvel'][i] = hubble_data['rvz_radvel'][i] * c.value
        # Convert the column with source IDs from object to strings (otherwise conversion to FITS fails)
        hubble_data['main_id'][i] = str(hubble_data['main_id'][i])

    # Check that we get some data back
    print(hubble_data['main_id', 'mesdistance.dist', 'mesdistance.unit', 'rvz_radvel'])

    # Create a new astropy table with the required columns
    newtable = QTable([hubble_data['main_id'], hubble_data['mesdistance.dist'],
                      hubble_data['mesdistance.unit'].astype('U4'), hubble_data['rvz_radvel']],
                      names=('Object', 'Distance', 'Distance_unit', 'Velocity'),
                      dtype=('U15', 'f8', 'U4', 'f8'))

    # Write the data to a FITS file
    newtable.write('hubble_data.fits', format='fits')

if __name__ == "__main__":
    main()
