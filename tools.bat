:startscript
@echo off
cls
if "%~1" == "gen" (
	python tools/tools.py "image rp" "cls" "registry elements" "cls" "registry solid" "cls" "translation" "cls"
	goto :exit
)
if "%~1" == "full" (
	del zip\DatapackZip.zip
	del zip\ResourcepackZip.zip
	python tools/tools.py "image rp" "cls" "registry elements" "cls" "registry solid" "cls" "translation" "cls" "zip" "cls"
	goto :exit
)
python tools/tools.py
:choice
set /P c=[1;92mDo you want to restart the script[Y/N]?[0m
if /I "%c%" EQU "Y" goto :startscript
if /I "%c%" EQU "N" goto :exit
goto :choice
:exit
cls
@echo on
