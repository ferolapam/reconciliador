## Run local (extra tips)

- Se estiver no Windows PowerShell e tiver problema com ativação:
  `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force` (uma vez).
- Utilize `python -m uvicorn app.service:app --reload --port 8000`
- Se for usar Docker Desktop, garanta que a porta 8000 esteja livre.
