# Converting from RAPID (CIT) formation to MagIC
=================

PmagPy provides tools for converting .sam format files into MagIC format both through the Pmag GUI application which is availible as a standalone download for Mac OSX users with no need for a local Python installation. Users on all platforms with a scientific Python installation (see PmagPy Cookbook for how to get started) can also run the GUI. Command line tools are also availible for .sam conversion. Conversion using Pmag GUI then allows a user to utilize the built-in Demag GUI program for data analysis.

  * [Use Pmag GUI](#Converting-.sam-data-files-into-MagIC-format-using-Pmag-GUI)
  * [Use the command line program](#Converting-.sam-data-files-into-MagIC-format-at-the-command-line)

# Converting .sam data files into MagIC format using Pmag GUI

To do this conversion, you need to download the Pmag_GUI OSX standalone program (https://github.com/PmagPy/PmagPy-Standalone-OSX/releases) or launch the pmag_gui.py from the command line. There isn't a functional Windows standalone app at this time.

Once Pmag GUI is downloaded, you should open the appropriate folder and double click the icon (depending on your security settings, you may have to right click the icon and then select “ok” the first time you open it).

Click 1. convert magnetometer files to MagIC format:

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui.png" width="750">

Choose CIT format and click import file:

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_format.png" width="350">

Choose a .sam file, add sampling protocols, choose sample-site naming convention, indicate the number of terminal characters that distinguish specimen from sample, add a location (required!), chose whether replicate measurements should be kept or averaged. Then click ok.

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_conversion.png" width="750">

You should get a message that looks like this. Click ok:

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_conversion_confirmation.png" width="350">

You will return to this menu. Choose "skip to next step":

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_format.png" width="350">

You then will encounter a menu where you have the ability to combine different MagIC formatted files to one measurements file. Since MagIC contributions are at the study level, this menu allows for multiple sites to be combined. The steps up to this point can be run on multiple .sam files which can be combined at this menu. Once all the .magic files (converted .sam files) you wish to deal with are added here click ok.

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_combine.png" width="450">

You should get this confirmation message (click ok):

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_combine_confirmation.png" width="350">

You then combine the additional files that contain sample/site/location info and click ok:

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_combine2.png" width="900">

You should get this confirmation message (click ok):

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui_combine_confirmation2.png" width="350">

You should now return to the main Pmag GUI window:

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/pmag_gui.png" width="750">

You can then click Demag GUI to launch Demag GUI. Please see the PmagPy Cookbook (https://earthref.org/PmagPy/cookbook/) for instructions related to using Demag GUI.

<img src="https://github.com/Swanson-Hysell-Group/lab_protocols/raw/master/Data_Analysis/images/demag_gui.png" width="950">

# Converting .sam data files into MagIC format at the command line

To execute this protocol you need to download PmagPy (https://github.com/ltauxe/PmagPy) and have it added to your path. There are installers as part of the PmagPy project that will add the directory to your path for you (see more info within the PmagPy cookbook: http://earthref.org/PmagPy/cookbook/) or, if you are using a Mac, you can add `export PATH=~/PmagPy:./:$PATH` to your .profile or .bash_profile file in your home directory.

(1) Within Terminal, navigate into directory with the .sam and data files you wish to convert.

(2) Use the CIT_magic.py program to convert the data from .sam file format into MagIC format. You can find out about all the options availible in CIT_magic.py by typing `CIT_magic.py -h`

Here is what it looks like to run the function:

CIT_magic.py -f *name of the .sam file* -spc *# of characters denoting the specimen* -ncn *# corresponding to naming convention (see below)* -A *include this if you don't want to average multiple measurments* 

Here is an example:

CIT_magic.py -f SLB15.sam -spc 1 -ncn 3 -A

-ncn NCON: specify naming convention

Sample naming convention:
            [1] XXXXY: where XXXX is an arbitrary length site designation and Y
                is the single character sample designation.  e.g., TG001a is the
                first sample from site TG001.    [default]
            [2] XXXX-YY: YY sample from site XXXX (XXX, YY of arbitary length)
            [3] XXXX.YY: YY sample from site XXXX (XXX, YY of arbitary length) [default]
            [4-Z] XXXXYYY:  YYY is sample designation with Z characters from site XXX

-spc NUM : specify number of characters to designate a  specimen, default = 0
-loc LOCNAME : specify location/study name, must have either LOCNAME or SITEFILE or be a synthetic
-mcd [FS-FD:SO-MAG,.....] colon delimited list for method codes applied to all specimens in .sam file
-A: don't average replicate measurements
