:startscript
@echo off
cls
python tools/tools.py
:choice
set /P c=[1;92mDo you want to restart the script[Y/N]?[0m
if /I "%c%" EQU "Y" goto :startscript
if /I "%c%" EQU "N" goto :exit
goto :choice
:exit
cls
@echo on
