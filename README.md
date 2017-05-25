# BkValidation
### Install
#### Selenium drivers
```
pip install -U selenium
```
#### Unix
```
chmod +x bkvalidation/getCode.py bkvalidation/PhantomJs/phantomjs-unix
```
### Run 
```
Usage: ./getCode.py BKref day month year hh mm
Exemple: ./getCode.py 22407 1 4 16 21 03
```
### Errors
```
error while loading shared libraries: libfontconfig.so.1: cannot open shared object file: No such file or directory
```
* ```apt-get install fontconfig```
* Fontconfig (the package fontconfig or libfontconfig, depending on the distribution).
