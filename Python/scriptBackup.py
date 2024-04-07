import os
import shutil
import sys

def backup(origem, destino):
  arquivos = os.listdir(origem)

  for arquivo in arquivos:
    dir_origem = os.path.join(origem, arquivo)
    dir_destino = os.path.join(destino, arquivo)
    status=shutil.copy2(dir_origem, dir_destino)
    print(f"Origem: {dir_origem} Destino: {dir_destino}")
  
if __name__ == "__main__":
  parametro= sys.argv[1:]
  origem=parametro[0]
  destino=parametro[1]
  print(parametro)
  backup(origem, destino)

  print("Backup concluido com sucesso.")

