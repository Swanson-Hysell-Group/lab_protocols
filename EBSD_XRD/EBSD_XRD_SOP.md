# SOP for SEM EBSD analyses and XRD machine analyses

## EBSD

1. Before turning on EBSD software, ramp up SEM current to 10 nA, check tilt correction off on smart SEM so that OIM software does its own tilt correction
2. set stage tilt and back it off, click red switch to send in the detector
3. Turn on OIM software
4. go to setting -> imaging 
5. select small image size and turn on "continuous on" to let the window continuously update image from SEM
6. change parameters to make image look good, close imaging window
7. go to interactive panel ->capture -> capture image for locating pixels when doing EBSD
8. get background: go to side panel, turn off all check boxes in image processing. go to "camera" -> collect background using a reduced window with fast scan rate (1-3) to collect overall background of area of interest -> change gain and exposure to get dull but overall even background -> capture background. go back to image processing and turn on 1,2, and 4 for background removal. 
9. After work is done hit green button to retrieve EBSD detector



## XRD

1. sample prep: this is for powder XRD work. One needs to use the piston and the mortar and pestle set to grind the sample into very fine powder. The use pipets and acetone to get powder and acetone mix onto a piece of sample holder - either with glass stage or low-background crystal holder. load the sample. 
2. open xpert data collector software
3. go to instrument -> connect -> sample spinner -> use the 9/14/2004 Tim owned template
4. Set x-ray current -> instrument settings, choose line focus for shutter. bring the current to 40 mA at 5 mA steps (from 10 mA rest current)
5. go to File -> open program -> open John's template of "blank batch" or use absolute scan - use Tim's 3.100 25 template
6. Measure -> open program -> ok -> name file and put in folder
7. to look at data: open Xpert highscore
8. open .xdml file
9. Treatment -> determine background
10. search peaks -set peak/background ratio to pick good peaks in scan list panel
11. edit the spectra to remove or add peaks
12. Analysis -> search and match -> put restriction parameters to have automated search for peaks -> choose multiphase to get analyses on all material present