# Converting .sam magnetic data files into MagIC format

To execute this protocol you need to download PmagPy (https://github.com/ltauxe/PmagPy) and have it added to your path. There are installers as part of the PmagPy project that will add the directory to your path for you (see more info within the PmagPy cookbook: http://earthref.org/PmagPy/cookbook/) or, if you are using a Mac, you can add `export PATH=~/PmagPy:./:$PATH` to your .bash_profile in your home directory.

(1) Within Terminal, navigate into directory with the .sam and data files you wish to convert.

(2) We will use the CIT_magic.py program to convert the data from .sam file format into MagIC format. You can find out about all the options availible in CIT_magic.py by typing `CIT_magic.py -h`

CIT_magic.py -f [name of the .sam file] -spc 1 -ncn 

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
