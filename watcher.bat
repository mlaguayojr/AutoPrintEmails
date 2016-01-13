echo off
title Email Service Check
color 0f
cls

echo ""> fetch.log

:check
ping localhost -n 16 >nul
:: if you run this program alongside many other python programs, you should change python.exe to whatever you compile this script as.
:: use py2exe to compile python scripts to executables.
tasklist | findstr /c:"python.exe"
if %errorlevel%==0 (goto alive) else (goto dead)


:alive
echo %time% - running
ping localhost -n 120 >nul
goto check

:dead
echo %time% - died, starting it again
echo %time% - dead >> fetch.log
start run.bat
goto check
