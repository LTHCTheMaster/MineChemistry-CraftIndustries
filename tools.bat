:startscript
@echo off
cls
if "%~1" == "gen" (
	python tools/tools.py "image rp" "cls" "registry elements" "cls" "registry solid" "cls" "registry block" "cls" "translation" "cls"
	goto :exit
)
if "%~1" == "full" (
	del /Q zip\*.zip
	python tools/tools.py "image rp" "cls" "registry elements" "cls" "registry solid" "cls" "registry block" "cls" "translation" "cls" "zip" "cls"
	goto :exit
)
if "%~1" == "build" (
	del /Q zip\*.zip
	python tools/tools.py "image build elements elementsBuildTest" "cls" "image build periodic periodicBuildTest" "cls" "image build templates templatesExport" "cls" "export exportTest" "cls"
	goto :exit
)
if "%~1" == "workspace" (
	del /Q zip\*.zip
	python tools/tools.py "image build elements elementsBuildTest" "cls" "image build periodic periodicBuildTest" "cls" "image build templates templatesExport" "cls" "export exportTest" "cls" "image rp" "cls" "registry elements" "cls" "registry solid" "cls" "registry block" "cls" "translation" "cls" "zip" "cls"
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
