@ECHO OFF
call "%~dp0env_for_icons.bat"
cd %2
python %1

if [%3] == [] (GOTO normal) else GOTO im_exit

:normal
PAUSE

:im_exit
EXIT
GOTO DONE