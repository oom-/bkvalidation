# BkValidation
Remplis l'enquête de satisfaction automatiquement et vous retourne le code.
### Example:
```
./getCode.py 22407 1 4 16 21 03
Ok, c'est parti pour un burger gratos !
Initialisation du navigateur :
Ok.
Remplissage du formulaire :
1%
1%
2%
3%
7%
11%
12%
13%
32%
34%
41%
45%
51%
70%
81%
85%
85%
86%
86%
94%
97%
Code de validation : WH027291
```
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
