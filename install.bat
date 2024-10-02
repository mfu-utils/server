@echo off
set "VENV_NAME=.venv"
set "SCRIPTS=.\%VENV_NAME%\Scripts"
set "PY=%SCRIPTS%\python.exe"

call python3 -m venv %VENV_NAME%
call %PY% -m pip install --upgrade pip
call %PY% -m pip install -r requirements.txt