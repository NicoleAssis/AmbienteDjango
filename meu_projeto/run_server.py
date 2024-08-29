import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meu_projeto.settings")
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
