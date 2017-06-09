@ECHO OFF
setlocal enableDelayedExpansion
set @path=%~dp0
set @filepy=Comments_Count.py
set @path=%@path:\script_batch=%
set @path=%@path%%@filepy%
python %@path% %1 > Output
SET /p MYVAR=<Output
ECHO %MYVAR%
ECHO. >Output
if %2=="DEL" DEL Output