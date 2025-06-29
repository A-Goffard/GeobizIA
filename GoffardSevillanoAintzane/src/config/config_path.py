import sys
from pathlib import Path

# Agregar el directorio raíz del proyecto al PYTHONPATH
project_root = Path(__file__).parents[1]  # Sube 1 nivel desde src/config/ al directorio raíz
sys.path.append(str(project_root))