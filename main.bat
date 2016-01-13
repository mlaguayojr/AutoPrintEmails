echo off
color 0f
title Email wait
cls
::number of seconds to wait
::if the computer has to login to a domain, this helps
set /a t=20

:loop
echo Loading email in %t% seconds
set /a t=%t%-1
if %t%==0 (goto done) else (ping localhost -n 2 >nul)
cls
goto loop

:done
cls
echo Checking internet
ping google.com
if %errorlevel%==0 (goto runEmail) else (goto done)

:runEmail
start watcher.bat
