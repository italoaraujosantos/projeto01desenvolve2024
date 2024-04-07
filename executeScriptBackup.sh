#!/bin/bash


execute(){
  HOME=$(echo $HOME)

  cd ~/
  if [ ! -d Backup ]
  then
      mkdir Backup
  fi
  
  origem=$HOME/Documentos/ArquivosTeste
  destino=$HOME/Backup

  cd $HOME/Boticario/Scripts
  python3 Python/scriptBackup.py $origem $destino

}

execute 
