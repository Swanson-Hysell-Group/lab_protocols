# demag_gui.py usage and tips

![](./images/demag_gui.png)

## Installing

This program is part of the [PmagPy repository](https://github.com/ltauxe/PmagPy) which can be downloaded or cloned from Github. To run demag_gui.py it is necessary to download and install a working version of [python 2.7](https://www.python.org/downloads/), the latest version of the GUI library [wxpython](http://www.wxpython.org/download.php), and the basic scientific libraries that are part of the [scipy project](http://www.scipy.org/install.html). The easiest way to get all that you need is to install the Enthought Canopy distribution as described in the PmagPy cookbook: http://earthref.org/PmagPy/cookbook/#QQ2-1-2.

## Launching

The GUI may be launched through the command line by navigating to the directory containing demag_gui.py and running it with:

```bash
python ./demag_gui.py
```

If PmagPy has been added to your PATH you can simply type demag_gui.py at the command line.

The demag_gui program can be started through the QuickMagIC program that is also part of PmagPy. QuickMagIC can be started by navigating to the directory containing it and running it with:

```bash
python ./QuickMagIC.py
```

QuickMagIC can also be used to convert files to magic format prior to launching demag_GUI. The program can be started by clicking on the demag_gui button in the QuickMagIC GUI, shown below. **Note:** on OSX it is recommended to launch through the QuickMagIC program as on wxpython 2.9 the drop down boxes seem to behave better when demag_gui is launched this way:

![](./images/QuickMagicLauncher.png)

## Interpretation of Specimen Data

### Adding Interpretations:  
You can analyze specimen component data by adding fits with the add fit button. Additionally, you can select the fit you would like to edit or view by using the drop down box under the add fit button. Once you have selected a fit, the shape of the end points of the selected fit will turn to a diamond shape to distinguish them from the other data points.  
![](./images/Fit.jpg)

Once you have selected the desired fit you can edit its bounds using the drop down boxes under the bounds header  
![](./images/BoundsBox.png)

Alternatively you can double click the list of measurement steps on the left to pick out the bounds of your interpretation. The included steps in the currently selected interpretation. are shown in blue on this list and measurement steps marked bad are shown in yellow. **Note:** in case of duplicate measurements the first *good* measurement with the same treatment is used.  
![](./images/DataBox.png)

When first created, the fit will be given a generic name such as *Fit 1*. You can change the name of the fit from the default by typing into the drop down box containing fits then pressing enter. The default fit type is a least-squares line. You can choose different fits such as a line anchored to the origin or a plane by using the drop down menu under specimen mean type.  
![](./images/SpecimenMeanType.png)

The choice between coordinate systems (i.e. specimen, geographic or tilt-corrected) is available on the left above the list of steps. The orientation of the Zijderveld projection can also be changed here.  
![](./images/ProjectionChoice.png)  

The properties of the currently selected fit to the data can be seen in the upper center of the GUI in a box labeled specimen mean statistics.  
![](./images/FitData.png)

### Flagging Bad Measurement Data

You can set acceptance criteria by using Analysis/"Acceptance Criteria"/"Change Acceptance Criteria". These criteria will be written to a pmag_criteria table. If any measurement steps should be excluded from the intepretation of a specimen they can be flagged as 'bad' by right clicking on the list of measurement steps to the left of the GUI. Any measurement marked as 'bad' will be colored yellow in the step list and will be shown as an empty rather than filled circle on the Zijdeveld, equal area and M/M_0 plots. To change a 'bad' measurement back to being 'good' one can right click on it again. Upon doing so, the yellow highlighting will go away, the data will be shown colored in within the plots and any fit that spans that data point will be recalculated to include it. These 'good' or 'bad' flags are exported into the MagIC tables with the fits to the specimens.

### Plot Interface

The 4 plots that take up the majority of the center of the GUI are where you will see your data and interpretations displayed. The Zijderveld and the 2 equal area plots are by default set to zoom when you left click and drag your left mouse button you will zoom to the dragged out rectangle (currently equal area plots do not draw this rectangle as you drag your mouse, but still zoom). On the Zijderveld plot, it is possible to switch between zoom and pan functionality by right clicking. Once in pan mode, the mouse will turn into a hand allowing you then to click and move around the plot. On both the Zijderveld and equal area plots if you wish to return to the original plot simply click the middle mouse button to return to home position. **Note:** in the absence of a middle mouse button pressing both right and left mouse buttons at the same time works on most laptops in the case of macbooks clicking with two fingers should work, and if using Apple's magic mouse we recommend you download the [MagicPrefs](http://magicprefs.com/) program which will allow you to configure your mouse however you prefer. One the equal area plots you can double click on an interpretation to switch the specimen and current interpretation to the clicked interpretation.

### Saving Specimen Interpretations

Once you have picked out your interpretations, you can save the session data in two different ways: (1) as a .redo file which will allow you to have the fits preserved to be view again with demag_gui or (2) as MagIC pmag tables to be uploaded to the MagIC database or otherwise processed. In addition, you may save image files of the plots.

#### The .redo File:

You can use Analysis/"Save current interpretations to a redo file" to create this file type or you can just hit the save button next to add fit, this method is recommended as it prevents accidental pressing of the clear all interpretations button. **Note:** this file type does **NOT** load previous interpretations on start up you must go to the menu option Analysis/"Import previous interpretations from a redo file" to restore your previous session.

#### The Pmag Tables:

By going to the menu File/"Save MagIC pmag tables" you can export your interpretations made in Demag GUI to the MagIC pmag tables which can then be used by other MagIC programs or uploaded to the MagIC database. You can export any or all of the 3 coordinate systems upon selecting this option and you may choose to save pmag_samples, pmag_sites, and pmag_results tables in addition to the pmag_specimens table that is output. If you choose to output additional information you will be prompted by a pop up window for additional information. **Note:** this save format loads on start up of the GUI immediately restoring your session, also selection of this option will overwrite your demag_gui.redo file in the working directory.  

#### Images of Plots:

Select the menu option File/"Save plot"/"Save all plots" to save all plots alternatively you can save any of the plots individually. If you zoom on any of the plots the zoomed image will be saved not the origionally plotted image although the plot will redraw and reset it's zoom level. 

<!---
Some example images can be seen below:

![Zijderveld with 3 interpretations](../images/Z35_1a_Zij.png)  
![Equal Area plot of specimen data and interpretations](../images/Z35_1a_EqArea.png)  
![M/M0](../images/Z35_1a_M_M0.png)  
![The Higher order mean plot with fisher mean for all specimens in study](../images/Z35_site.png)  
\pagebreak
-->

### Deleting Specimen Interpretations

If you would like to delete a single interpretation, select the one you wish to delete from the interpretation drop down menu and click delete. Alternatively if you wish to clear all interpretations you may go to the menu option Analysis/"Clear all current interpretations".  
<!--- ![](../images/SaveDelete.png) -->

## Higher Level Plots and Interpretation

The set of drop down boxes to the right of the interpretation data is there to determine what level you want to analyze in the higher level analysis options include: site, sample, location, and study. The drop down below this selects which of the available sites, samples, location, or studies you want to display.
<!--- ![](../images/HigherOrderOptions.png) -->

You can then select how to group your data by using the drop down menu under the show header. You can select what kind of mean to take using the first drop down under the mean header. Which interpretations to use for the means can be selected under the second drop down menu. You can then use the remove/replace button to remove or replace the set of points belonging to the current specimen in the higher order mean.
<!--- ![](../images/HigherOrderMeanOptions.png)  -->

You can view the mean statistics of all fits for the selected fit type in the bottom left of the GUI.
<!--- ![](../images/HigherOrderMeanOutput.png)  -->

### Interpretation Editor

In order to more easily view and edit specimen interpretation data there is a specimen interpretation editor which can be launched from the tools menu of the Demag GUI. This panel details the fits made to the data and their parameters from which you can select which interpretation to view by double clicking on it. In the list, the currently selected interpretation is highlighted blue as shown in the image below. You can mark interpretations as bad which removes them from any Fisher means or other high level means by right clicking on their entry in the list. All interpretations marked bad are colored yellow in the list and marked as a 'x' on the plot. Interpretations can be highlight by clicking on the list and holding the shift or ctrl key (command key on mac) to select multiple interpretations. Doing so allows you to delete or alter the characteristics of multiple interpretations at once without having to select each one in turn. This mass alteration is allowable using the the Name/Color/Bounds boxes to input the changes and then clicking the "apply changes to highlighted fits" button. You can delete highlighted fits using the "delete highlighted fits" button. The "add fit" button in the interpretation editor adds a fit to the current specimen. In the case of interpreting large data sets, you can reduce the number of items plotted on the equal area at the bottom of the editor and the number of entries in the log by changing the display settings. The equal area plot on the bottom works just like the higher level equal area on the main Demag GUI panel allowing you to select interpretations on it by double clicking and to zoom by clicking and dragging.

![](./images/InterpEditor.png)
