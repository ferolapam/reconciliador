@echo off
pushd %~dp0
call .\.venv\Scripts\activate.bat
python -m uvicorn app.service:app --host 127.0.0.1 --port 8000 --reload
pause
popd
