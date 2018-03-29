# Keithley Gate Sweep (for fixed Vds) for 2400 SourceMeter

# Variable intake and assignment
import sys
startv = sys.argv[1]
stopv = sys.argv[2]
stepv = sys.argv[3]
fixedv = sys.argv[4]
filename = sys.argv[5]
startvprime = float(startv)
stopvprime = float(stopv)
stepvprime = float(stepv)
steps = (stopvprime - startvprime) / stepvprime 

# Import PyVisa and choose GPIB Channel 25 as Drain-Source and 26 as Gate
import visa
rm = visa.ResourceManager()
rm.list_resources()
Keithley = rm.open_resource('GPIB0::25::INSTR')
Keithleygate = rm.open_resource('GPIB0::26::INSTR')
Keithley.write("*RST")
Keithleygate.write("*RST")
Keithley.timeout = 25000
Keithleygate.timeout = 25000

# Turn off concurrent functions and set sensor to current with fixed voltage
Keithleygate.write(":SENS:FUNC:CONC OFF")
Keithleygate.write(":SOUR:FUNC VOLT")
Keithleygate.write(":SENS:FUNC 'CURR:DC' ")

# Set
Keithley.write(":SOUR:FUNC VOLT")
Keithley.write(":SOUR:VOLT:MODE FIXED")
Keithley.write(":SOUR:VOLT:RANG 20")
Keithley.write(":SOUR:VOLT:LEV ", fixedv)
Keithley.write(":SENS:CURR:PROT 1")

# Voltage starting, ending, and spacing values based on input
Keithleygate.write(":SOUR:VOLT:STAR ", startv)
Keithleygate.write(":SOUR:VOLT:STOP ", stopv)
Keithleygate.write(":SOUR:VOLT:STEP ", stepv)
Keithleygate.write(":SOUR:SWE:RANG AUTO")

# Set compliance current (in A), sweep direction, and data acquisition
Keithleygate.write(":SENS:CURR:PROT 1")
Keithleygate.write(":SOUR:SWE:SPAC LIN")
Keithleygate.write(":SOUR:SWE:POIN ", str(int(steps)))
Keithleygate.write(":SOUR:SWE:DIR UP")
Keithleygate.write(":TRIG:COUN ", str(int(steps)))
Keithleygate.write(":FORM:ELEM CURR")

# Set sweep mode and turn output on
Keithleygate.write(":SOUR:VOLT:MODE SWE")
Keithley.write(":OUTP ON")
Keithleygate.write(":OUTP ON")

# Initiate sweep, collect ACSII current values, and turn output off
result = Keithleygate.query(":READ?")
yvalues = Keithleygate.query_ascii_values(":FETC?")
Keithleygate.write(":OUTP OFF")
Keithley.write(":OUTP OFF")
Keithleygate.write(":SOUR:VOLT 0")
Keithley.write(":SOUR:VOLT 0")

# Import Pyplot, NumPy, and SciPy
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Create xvalues array and calculate conductance
xvalues = np.arange(startvprime,stopvprime,stepvprime)
slope, intercept, r_value, p_value, std_error = stats.linregress(xvalues, yvalues)

# Plot values and output conductance to command line
print("Conductance:", slope, "Siemens")
plt.plot(xvalues,yvalues)
plt.xlabel(' Gate Voltage (V)')
plt.ylabel(' Drain-Source Current (A)')
plt.title('Gate Sweep')
plt.figtext(0.7, 0.2, 'Vds=' + str(fixedv) + 'V', fontsize=15)
plt.show()
np.savetxt(filename, (xvalues,yvalues)) 
