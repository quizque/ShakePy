

title ShakePi Envorment Setup

rem Change directory to batch file location
cd %~dp0..

rmdir /S /Q tmp

py -m venv tmp
cd tmp/Scripts
call activate.bat
pip install -e ../../

pause