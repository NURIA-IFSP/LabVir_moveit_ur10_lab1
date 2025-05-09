#!/bin/bash

# Navegar para o diretório catkin_ws
echo "Tentando mudar para o diretório: /projeto_1_PosDoc/catkin_ws"
cd /projeto_1_PosDoc/catkin_ws || { echo "Falha ao mudar para o diretório"; exit 1; }

# Exibir o diretório atual
echo "Diretório atual: $(pwd)"

# Listar os arquivos no diretório
ls

# Fonte o arquivo de configuração do workspace
if [ -f devel/setup.bash ]; then
    echo "Fonteando o setup.bash"
    source devel/setup.bash
else
    echo "Arquivo de configuração 'devel/setup.bash' não encontrado!"
    exit 1
fi

# Navegar para o pacote tangs_arm_definition
roscd tangs_arm_definition || echo "Falha ao localizar o pacote 'tangs_arm_definition'"
