@echo off
REM Change directory to where converter.py and singingbot.py are located
cd /d D:/xampp/htdocs/MusicBot

REM Run the converter.py script
echo Running converter.py...
python converter.py

REM Check if the first script was successful
IF %ERRORLEVEL% NEQ 0 (
    echo converter.py failed. Exiting...
    exit /b %ERRORLEVEL%
)

REM Run the singingbot.py script
echo Running singingbot.py...
python singingbot.py

REM Check if the second script was successful
IF %ERRORLEVEL% NEQ 0 (
    echo singingbot.py failed. Exiting...
    exit /b %ERRORLEVEL%
)

echo Both scripts ran successfully!
pause
