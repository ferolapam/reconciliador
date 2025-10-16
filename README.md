# Reconciliador - Demo (FastAPI)

Projeto demo de microserviço para reconciliação de faturas (POC).
Estrutura pronta para uso local, CI (GitHub Actions), Docker e integração com time.

## O que tem aqui
- `app/` - código da API (FastAPI)
- `tests/` - testes unitários com pytest
- `Dockerfile`, `docker-compose.yml` - containerização
- `.github/workflows/ci.yml` - pipeline CI executando testes
- `Makefile` - comandos úteis de desenvolvimento
- `requirements.txt` / `requirements-dev.txt` - dependências
- `pre-commit-config.yaml` - formatação/linters (opcional)
- `.env.example` - variáveis de ambiente de exemplo

## Como usar (Windows / PowerShell)
1. Abrir terminal integrado no VS Code (ou PowerShell) na pasta do projeto.
2. Criar e ativar venv:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   *Se você receber bloqueio, execute `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force` (uma vez).*

3. Instalar dependências (runtime):
   ```powershell
   pip install --upgrade pip
   pip install -r app/requirements.txt
   ```

4. Rodar a API localmente:
   ```powershell
   python -m uvicorn app.service:app --reload --port 8000
   ```
   Abra: `http://localhost:8000/docs`

5. Rodar testes:
   ```powershell
   pip install -r app/requirements-dev.txt
   pytest -q
   ```

6. Docker (opcional):
   ```bash
   docker build -t reconciliador:local .
   docker run -p 8000:8000 reconciliador:local
   ```

## Subir para o GitHub
1. Crie repositório no GitHub.
2. No terminal (na raiz do projeto):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Reconciliador (FastAPI)"
   git branch -M main
   git remote add origin https://github.com/SEU-USUARIO/SEU-REPO.git
   git push -u origin main
   ```

## Observações para o time
- Arquitetura simples, focada em testabilidade e observability: logs e endpoints pequenos.
- CI roda testes automaticamente; adicionar análise estática conforme critérios do time.
