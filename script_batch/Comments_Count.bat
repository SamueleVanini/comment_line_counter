@ECHO OFF
setlocal enableDelayedExpansion
set @path=%~dp0
set @filepy=Comments_Count.py
set @path=%@path:\script_batch=%
set @path=%@path%%@filepy%
python %@path% %1 > Output
SET /p Perc_Comm=<Output
ECHO %Perc_Comm%
ECHO. >Output
if %2 EQU DEL DEL Output