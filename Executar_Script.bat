@echo off

:: Define o diretório do arquivo .bat como o diretório atual
cd /d "%~dp0"

:: Ativa o ambiente virtual
call .venv\Scripts\activate

:: Executa o script Python
python Conectar.py
pause