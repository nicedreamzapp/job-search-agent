@echo off
rem Runs job-search-agent once. Point Windows Task Scheduler at this file.
rem Any arguments are passed through, for example: run-jobscout.bat --dry-run
rem Output is appended to jobscout.log in the state folder.
setlocal
cd /d "%~dp0.."

set "LOGDIR=%USERPROFILE%\.local\state\jobscout"
if defined JOBSCOUT_STATE_DIR set "LOGDIR=%JOBSCOUT_STATE_DIR%"
if not exist "%LOGDIR%" mkdir "%LOGDIR%"

rem Job titles and company names are not always plain ASCII. Without this,
rem output redirected to a file uses the Windows code page and can error.
set "PYTHONIOENCODING=utf-8"

where py >/dev/null 2>nul
if %errorlevel%==0 (
    py -3 jobscout.py %* >> "%LOGDIR%\jobscout.log" 2>&1
) else (
    python jobscout.py %* >> "%LOGDIR%\jobscout.log" 2>&1
)
exit /b %errorlevel%
