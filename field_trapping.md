# Trapping the field on a superconducting rock magnetometer

## The "why" behind trapping the field
Below is an excerpt from the Spring 2009 IRM Quarterly  **Free the Flux! (What is “Trapped Flux”?)** written by Julie Bowles:

> You may have come across the phrase “trapped flux” in reference to a SQUID magnetometer. What exactly is trapped flux and how do you get rid of it? The simplest example of trapped flux comes from cooling a superconducting ring in the presence of a magnetic field. Once the ring is below the critical temperature, any attempt to remove the field will generate a persistent current in the ring that opposes the change. The flux threading the loop will therefore remain constant, even if the external field is removed. i.e. -- you have trapped flux. The only way to untrap it is to heat the ring above its critical temperature and set the flux free.

## Procedure in UC Berkeley Paleomag lab

1. **Get good zero reading on fluxgate.** To do this put it into the mu metal shielding. Seek to have symmetry for all the axes when adjusting. Adjust screws so symmetry is achieved. Note that the fluxgate can be mildly AF demagnetized.

2. **Insert fluxgate into magnetometer.** It should be inserted so that it is at the SQuIDs.

3. **Connect nulling coil cable and temperature monitor cable to control monitor.**
Connect the temperature monitor cable into port on magnetometer by the SQuID electronic boxes. A single cable controls heater and gives temperature reading. Connect the nulling cable from the control monitor to the cable that comes out of the magnetometer.

4. **Warm magnetometer and trap the field.**
Another effective way to warm and then cool is to simply turn off the Cryomech compressor (and to savor the brief silence in the lab when it is off). Turn off compressor (press green button) and allow TSH and TSQ to warm up to 8 or 9 K. This warming should take around 10 minutes. The shield stops being superconducting at ~7.2 K. Once the system warms up to 8 or 9 K, turn compressor back on so that the system cools back down. Before turning the compressor back on, adjust nulling coils to get a zero reading on the fluxgate (usually are left with 1 to 3 nT when the field is trapped). Then turn the compressor on continuing adjustments as needed with the coils as it cools. The field will be trapped at ~7.2 K. Once the systems is cooled to ~5 K disconnect nulling coils.

5. **Wait until system fully cools and stabilizes**
Cooling should continue until the SQuID temperature is back to ~3.9K and there is little drift.The 2G Enterprise manual states that the lowest noise environment will be achieved about an hour after the system has cooled down.

## Procedure at the IRM

1. **Get good zero reading on fluxgate.**
Put into mu metal shielding. Seek to have symmetry for all the axes when adjusting. z is 0.05/-0.05 so is considered good; y was 0.03/-0.02; adjust screws so symmetry is achieved. Note that the fluxgate can be AF demagnetized. Once adjusted put tape on fluxgate scress so don't adjust them by accident instead of adjusting the nulling coils in next step.

2. **Insert fluxgate into magnetometer.**
Tape flux gate onto aluminum rod and insert into magnetometer until at SQuIDs.

3. **Attach nulling coils to control monitor.**
Insert cables (x,y,z,coil) into box on magnetometer. A single cable controls heater and gives temperature reading.

4. **Heat up shield.** Turn on heater by holding button for 3 seconds. Heat up to 8 or 9 K. The shield stops being superconducting at ~7.2 K. Once heated up to 8 or 9 K, turn heater off and let cool. Adjust nulling coils while cooling to get a zero reading on the fluxgate (usually are left with 1 to 3 nT when the field is trapped). The field will be trapped at ~7.2 K. Once it was cooled to ~5 K disconnect nulling coils.

## From the 2G Enterprises manual:

FIELD NULLING COILS:
There are four coils mounted outside the dewar vacuum jacket to help establish a low field environment in the measurement region. The calibration constants for these coils are given below and in the front of this manual. To use the coils to change the field it is first necessary to heat the superconducting shield to above its critical temperature as described in the following section. The coils are referred to as axial (to change the field in the sample access direction) and transverse - two orthogonal sets of saddle coils for changing the field in the directions transverse to the dewar axis, and gradient to control the vertical field gradient that is produced by the coldhead and the opening in the ferromagnetic shield. The axial coil is a helmholtz pair of coils wrapped on the d e w a r vacuum jacket. Each transverse coil is a pair of saddle shaped helmholtz coils 1/2 meter long and 1/2 meter circumferential length. The vertical field gradient coil is a 50 turn solenoid wound one the cryocooler mounting tube. The approximate f i e l d constants for these coils with 15 turns in each coil are given below:

It requires about 45 seconds to heat the shield to its non-superconducting state and it can be maintained at this higher temperature (about 10 kelvin) by turning the heater on for about 10 seconds then off at 4 minute intervals and monitoring the diode voltage. When the superconducting shield is heated then first cancel the vertical gradient using the gradient coil . Measure the vertical field at the measurement center and then at +/- 2 cm about the center. Adjust the gradient coil to eliminate the gradient. Next, use the 3 helmholtz coils to reduce the field at the measurement center to below 5 gamma in all three directions. Check the field gradient by measuring the fields at +/- 2 cm about the measurement center and redjust the currents as needed. When the desired internal field is achieved keep the coil currents constant and let the superconducting shield cool to trap the field. Wait until the superconducting shield temperature reaches 5 kelvin or less before turning off the coil currents. This temperature is measured with T1 diode using box 1. Please check the actual equilibrium values for specific SRM. It will require about 20 minutes for the shield to cool after it has been heated to 10 kelvin and another hour before the system lowest noise performance is achieved. Record the setting of each of the 4 potentiometers.

SWITCHING THE SUPERCONDUCTING SHIELD:
The superconducting shield is a crucial part of the SRM. Because of the unique properties of superconducting materials this shield provides very high attenuation of external magnetic field changes and permits the trapping of a specific field environment. Superconducting materials exhibit zero D.C. resistance so any change in magnetic field will produce an in- duced current that flows undiminished so long as the field change is applied. This means that the net magnetic flux linking a superconducting ring will remain constant. For a cylindrical shell structure of the type used on the SRM it can be shown that axial magnetic fields are attenuated by a factor of 31( l / r) , where l is the distance in from the open end of the shield measured on axis and r is the shield radius. Transverse fields are attenuated by a factor of 36(l/2r). For the shield dimensions used in the 7.6 cm (3.0 in) 760 SRM and the 4.1 cm (1.65 inch) 755 this provides an attenuation of axial fields at the measurement center of 101 1 and of transverse fields of 106.

The only operational procedure used with the superconducting shield in the SRM is its thermal switching. To trap a given magnetic field environment it is necessary to produce the desired field with coils, magnetic shields, etc. then turn on the shield heater for about one minute, then turn it off. The field at the SRM access can be measured with a fluxgate magnetometer during this process to determine the value to be trapped. As described in the previous section the field is usually adjusted with the built in nulling coils when the shield is normal. Maintain the desired field as constant as possible for the next 20 minutes. It is best to monitor the superconducting shield temperature (Diode T1, box 1) and wait until it cools to about 5 K at 1.6 volts, before removing the external field source. At this time the shield will be well below its superconducting transition temperature and the field will be trapped by the superconductor. It will take an additional hour or more for the SQUIDS to reach their lowest noise performance.
