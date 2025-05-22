from qgis.utils import qgsfunction
from qgis.core import *
from qgis.gui import *

@qgsfunction(group='Custom',referenced_columns=["length_nm","fuel_burn", "speed_knots"])
def calculate_fuel_burn(value1, value2, value3):
    time_hours =  (float(value1)/float(value3))
    fuel_burn_journey = (int(value2))*time_hours
    return fuel_burn_journey