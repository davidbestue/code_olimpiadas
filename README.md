### Sistema para evaluar el resultado de las olimpiadas  

Manera basica de correrlo (sin entrar en environment)

Abrir anaconda, ir al path y poner
python -i resultados_olimpiadas.py

En python 2 y python3  

Para crear el .cmd que lo abra, seguir [estas](https://www.pythoncentral.io/execute-python-script-file-shell/) indicaciones.
Brevemente:  
- Abrir un .txt y poner "path/python.exe""path to .py"
-Guardar como --> Cambiar a toto tipo de archivos --> escribir extensión .cmd.  


Para python 2 y python3 se necesitan los modulos pandas, numpy, Easygui y tkMessageBox.  
Para instalar easygui: 
conda install -c dataonlygreater easygui
Para instalar tkMessageBox

El excel file tiene la siguiente estructura
Filas: votos
Columnas: actuante
En cada cell se ponen 4 numeros (votacion por pregunta)
