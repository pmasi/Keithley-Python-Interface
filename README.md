# Keithley-IV-Sweep
Python (PyVisa) script for IV (Current-Voltage) measurements on a Keithley 2400 (GPIB/SCIP communication).


Instructions:

  1. Install the necessary Python libraries (NumPy, SciPy, and MatPlotLib) and GPIB driver for Mac/Linux (http://www.ni.com/product-documentation/5458/en/) or Windows (http://www.ni.com/product-documentation/5326/en/).

  2. Place the KeithleyIVSweep.py, KeithleyIVSweepFixedGate.py, and/or KeithleyGateSweepFixedGate.py files in your home (or current Python) directory.
  
  3. From the command line (in Mac, just use Terminal), run the following command (depending on file):
  
  'python KeithleyIVSweep.py startV stopV stepV outputfile'
  'python KeithleyIVSweepFixedGate.py startV stopV stepV gateV outputfile'
  'python KeithleyGateSweepFixedDrain.py startgateV stopgateV stepgateV drainV outputfile'
  
  4. For example, a gate from -20 V to 20 V with a step voltage of 1 V and drain voltage of 0.5 V would be obtained by running 'python KeithleyGateSweepFixedDrain.py -20 20 1 0.5 Hello.txt' where the output text file named Hello.txt would be created and stored in your home (or current Python) directory.
