# SQuID tuning procedure in UC Berkeley Paleomagnetism lab

1. Turn on Owon Oscilloscope
2. Attach AC_OUT (X_axis) cable to CH 1 and SYNC (X_axis) cable to EXT TRIG
3. Set oscilloscope scale so you can see the signal
4. Unlock the BIAS knob on the SQUID box for the sensor you are tuning and turn all the way counter-clockwise (i.e. to zero) and then increase until you get the cleanest signal on the oscilloscope.
5. Press the LOCK button (lock-loop feedback light should extinguish) and use the BIAS knob to maximize the signal output. Use the OFFSET knob to further maximize the signal and to get a single sine wave---rather than two sine waves.
6. Press the LOCK button (lock-loop light should come back on).
7. Lock the BIAS knob in place.
8. Repeat for Y and Z

## Notes:

The BIAS and OFFSET potentiometers enable biasing of the SQUID with a DC current and injection of a DC flux into the SQUID loop. The full range of bias is ~ 100 μA while the full scale range of offset is one unit of flux. The adjustment of the BIAS control is done to maximize the amplitude of the modulation signal present at the SQUID AC output port.

When LOCK is activated the feedback system is on.

The RESET pushbutton momentarily zeros the output. After a few milliseconds the reset is removed and the feedback system reactivated. Activating reset will return the output to within one flux quanta of zero. To further zero the system output the DC offer control must be used.

The FAST slew and bandwidth pushbutton increases the speed of the feedback system by about 2. Normally fast slew is selected. A lower slew rate may be desirable because in the presence of RFI, lower incidences of flux jumping are sometimes observed for lower bandwidth.
