@ECHO OFF
python C:\Users\SVanini\PycharmProjects\comment_line_counter\Comments_Count.py %1 > Output
SET /p MYVAR=<Output
ECHO %MYVAR%
DEL Output