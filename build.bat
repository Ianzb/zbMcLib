call D:\Code\zbMcLib\.venv\Scripts\activate.bat
rmdir /S /Q dist
py -m build --wheel
py -m twine upload dist/*
call D:\Code\zbMcLib\.venv\Scripts\deactivate.bat
pause