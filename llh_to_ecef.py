# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
# Converts latitude, longitude, and height above ellipsoid (LLH) to Earth-Centered Earth-Fixed (ECEF) coordinates.
# Parameters:
#  lat_deg: Geodetic latitude in degrees
#  lon_deg: Longitude in degrees
#  hae_km: Height above the ellipsoid in kilometers
# Output:
#  ECEF coordinates (r_x_km, r_y_km, r_z_km) in kilometers
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys
import math

# Constants
R_E = 6378.1363  # Earth's radius in kilometers
e_E = 0.081819221456  # Earth's eccentricity

# Helper function to convert degrees to radians
def deg_to_rad(deg):
    return deg * math.pi / 180.0

# Main function to convert LLH to ECEF
def llh_to_ecef(lat_deg, lon_deg, hae_km):
    # Convert lat and lon to radians
    lat_rad = deg_to_rad(lat_deg)
    lon_rad = deg_to_rad(lon_deg)

    # Calculate geodetic latitude (phi_gd) and intermediate values
    sin_phi_gd = math.sin(lat_rad)
    cos_phi_gd = math.cos(lat_rad)

    # Calculate C_E and S_E
    C_E = R_E / math.sqrt(1 - (e_E ** 2) * (sin_phi_gd ** 2))
    S_E = (R_E * (1 - e_E ** 2)) / math.sqrt(1 - (e_E ** 2) * (sin_phi_gd ** 2))

    # Calculate ECEF coordinates
    r_X = (C_E + hae_km) * cos_phi_gd * math.cos(lon_rad)
    r_Y = (C_E + hae_km) * cos_phi_gd * math.sin(lon_rad)
    r_Z = (S_E + hae_km) * sin_phi_gd

    return r_X, r_Y, r_Z

# Script execution
if len(sys.argv) == 4:
    # Parse arguments
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])

    # Call the conversion function
    r_x_km, r_y_km, r_z_km = llh_to_ecef(lat_deg, lon_deg, hae_km)

    # Print results rounded to 6 decimal places
    print(f'{r_x_km:.6f}')
    print(f'{r_y_km:.6f}')
    print(f'{r_z_km:.6f}')
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    exit()
