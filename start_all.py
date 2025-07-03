import subprocess
import sys
import os

# Cambia estos comandos según tu estructura y sistema operativo
commands = [
    # Arranca el backend FastAPI
    [sys.executable, "-m", "uvicorn", "src.api.main:app", "--reload"],
    # Arranca el frontend Vue (requiere npm instalado y configurado)
    ["npm", "run", "serve", "--prefix", "src/vista/frontend"]
]

processes = []
try:
    for cmd in commands:
        # Abre cada proceso en una ventana nueva (solo Windows)
        if os.name == "nt":
            p = subprocess.Popen(["start", "cmd", "/k"] + cmd, shell=True)
        else:
            p = subprocess.Popen(cmd)
        processes.append(p)
    input("Presiona ENTER para cerrar todos los servicios...\n")
finally:
    for p in processes:
        p.terminate()
