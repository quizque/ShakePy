@echo off
title ShakePi Envorment Setup

rem This file is thrown together and will need to be improved later down the line
rem 


REM check if we are in the right directory
if exist src\ (

    echo Deleating tmp folder... 
    rmdir /S /Q tmp
    IF %ERRORLEVEL% LSS 0 call :FATEL_ERROR

    echo Creating Python venv...
    py -m venv tmp
    IF %ERRORLEVEL% LSS 0 call :FATEL_ERROR

    echo Activating venv...
    cd tmp/Scripts
    call activate.bat
    IF %ERRORLEVEL% LSS 0 call :FATEL_ERROR

    echo Installing ShakePi...
    pip3 install -e ../../
    IF %ERRORLEVEL% LSS 0 call :FATEL_ERROR

    echo Done!
    echo Make sure to select the virtual environment if your IDE supports it (VS Code) 
    pause
    exit

) else (
  echo src folder doesn't exist! Make sure you are running this in the source directory.
  call :FATEL_ERROR 
)


:FATEL_ERROR
echo ========================
echo = AN ERROR HAS OCCURED =
echo ========================
echo.
echo Please report this to the github issues page, make sure to include the entire log and remove any personal information.
pause
exit