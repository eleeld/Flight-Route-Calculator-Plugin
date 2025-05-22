from qgis.core import *
from qgis.gui import *
import time
from time import strftime

@qgsfunction(group='Custom',referenced_columns=["dist_nm", "speed_knots"])
def calculate_time_taken(value1, value2):
    time_sec = ((60*60*(int(float(value1))/int(float((value2))))))
    time_convert = time.gmtime(time_sec)
    result_time = time.strftime("%H:%M:%S",time_convert)
    return result_time