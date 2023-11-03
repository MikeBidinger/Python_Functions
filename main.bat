@echo OFF 
set CONDAPATH=C:\Users\MB91448\Anaconda3
set ENVNAME=PygameEnv

if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%CONDAPATH%\envs\%ENVNAME%)

call %CONDAPATH%\Scripts\activate.bat %ENVPATH%

cd %~dp0

python main.py

call conda deactivate

pause
@REM timeout /t 21600
