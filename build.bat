call D:\Code\zbMcLib\.venv\Scripts\activate.bat
py -m build --wheel
py -m twine upload dist/*
call D:\Code\zbMcLib\.venv\Scripts\deactivate.bat
pause