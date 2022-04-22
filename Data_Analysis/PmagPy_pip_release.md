making pip releases.
read this: https://github.com/PmagPy/PmagPy/blob/master/CONTRIBUTING.md#compile-and-release-guide
- be an owner of our pmagpy-cli and pmagpy projects [look in pypirc in home]
conda install twine [upload securely to PyPi]
to test:  
rm -rf build dist && python setup.py sdist bdist_wheel && twine upload dist/* -r testpypi
to download this:  pip install -i https://testpypi.python.org/pypi pmagpy
to do it for real: 
run tests:  
in pmagpy_tests - look at the README
increment version number with version.py
rm -rf build dist && python setup.py sdist bdist_wheel && twine upload dist/*
rm -rf build dist && python command_line_setup.py sdist bdist_wheel && twine upload dist/*
for project too large error - delete releases here: https://pypi.org/manage/project/pmagpy/releases/
