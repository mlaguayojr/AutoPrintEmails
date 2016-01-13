echo off
color 0f
cls

:log
echo Script started at %time% on %date% >> fetch.log
::change the line below to wherever you saved the script to
call "loc\fetchEmails.py"
echo Script broke at %time% >> fetch.log
goto log
