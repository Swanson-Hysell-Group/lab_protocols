# Converting .sam magnetic data files into MagIC format

To execute this protocol you need to download PmagPy (https://github.com/ltauxe/PmagPy) and have it added to your path. There are installers as part of the PmagPy project that will add the directory to your path for you (see more info within the PmagPy cookbook: http://earthref.org/PmagPy/cookbook/) or you can add `export PATH=~/PmagPy:./:$PATH` to your .bash_profile in your home directory.

- Within Terminal, navigate into directory with the .sam and data files you wish to convert.
- We will use the CIT_magic.py program to convert the data from .sam file format into MagIC format. You can find out about all the options availible in CIT_magic.py by typing `CIT_magic.py -h`
