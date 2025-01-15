call D:\Code\zbToolLib\.venv\Scripts\activate.bat
py -m build --wheel
py -m twine upload dist/*
call D:\Code\zbToolLib\.venv\Scripts\deactivate.bat
pause