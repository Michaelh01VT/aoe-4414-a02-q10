# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
# Converts LLH coordinates to ECEF coordinates
# Parameters:
#  lat_deg: Latitude in degrees
#  lon_deg: Longitude in degrees
#  hae_km: Height above ellipsoid in kilometers
# Output:
#  ECEF coordinates in kilometers
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys
import math

# Constants
R_E = 6378.1363  # Earth radius
e_E = 0.081819221456  # Earth eccentricity

# Helper function converting degree to radian
def deg_to_rad(deg):
    return deg * math.pi / 180.0

# Function to convert LLH to ECEF
def llh_to_ecef(lat_deg, lon_deg, hae_km):
    lat_rad = deg_to_rad(lat_deg)
    lon_rad = deg_to_rad(lon_deg)
    sin_phi_gd = math.sin(lat_rad)
    cos_phi_gd = math.cos(lat_rad)
    C_E = R_E / math.sqrt(1 - (e_E ** 2) * (sin_phi_gd ** 2))
    S_E = (R_E * (1 - e_E ** 2)) / math.sqrt(1 - (e_E ** 2) * (sin_phi_gd ** 2))
    r_X = (C_E + hae_km) * cos_phi_gd * math.cos(lon_rad)
    r_Y = (C_E + hae_km) * cos_phi_gd * math.sin(lon_rad)
    r_Z = (S_E + hae_km) * sin_phi_gd
    return r_X, r_Y, r_Z
if len(sys.argv) == 4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
    r_x_km, r_y_km, r_z_km = llh_to_ecef(lat_deg, lon_deg, hae_km)
    print(f'{r_x_km:.6f}')
    print(f'{r_y_km:.6f}')
    print(f'{r_z_km:.6f}')
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    exit()
