# Keithley-IV-Sweep
Python (PyVisa) script for IV (Current-Voltage) measurements on a Keithley 2400 (GPIB/SCIP communication).


Instructions:

  1. Install the necessary Python libraries (NumPy, SciPy, and MatPlotLib) and GPIB driver for Mac/Linux (http://www.ni.com/product-documentation/5458/en/) or Windows (http://www.ni.com/product-documentation/5326/en/).

  2. Place the KeithleyIVSweep.py file in your home (or current Python) directory.
  
  3. From the command line (in Mac, just use Terminal), run 'python KeithleyIVSweep.py startV endV stepV outputfile'. 
  
  4. For example, an IV sweep from -100 mV to 100 mV with a step voltage of 1 mV would be obtained by running 'python KeithleyIVSweep.py -0.100 0.100 0.001 Sweep1.txt' where the output text file named Sweep1.txt would be created and stored in your home (or current Python) directory.
