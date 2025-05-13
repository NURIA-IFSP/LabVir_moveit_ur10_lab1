# Demonstração - MoveIt + Tangs

Como executar:

Você pode executar em sua máquina local ou via github codespaces:

## Preparação do ambiente na máquina local

1. Baixar o repositorio em sua máquina local:

    ```bash
    git clone git@github.com:NURIA-IFSP/LabVir_moveit_01.git
    ```

2. Abrir o vscode no diretório do projeto:

    ```bash
    code LabVir_moveit_01
    ```

3. Garanta que o docker esteja instalado e rodando:

    ```bash
        docker version
    ```

4. Se não tiver, instalar o docker:

    [Docker Installation Guide](https://docs.docker.com/get-started/get-docker/)

5. Instale a extensão remote - developement: workspace, no vscode:

    - No menu de extensões do VsCode Ctrl + Shift + X procure por: Remote - Development: Workspace

## Execução do container a partir do terminal (sem uso do vscode)

1. Construir a imagem docker do projeto (somente na primeira execução. Pode levar vários minutos!)

     ```bash
        cd .devcontainer
        docker build -t labvir_moveit_01 .
    ```
2. Rodar o container com interface gráfica via vnc
    ```bash
    docker run -it --rm -p 5901:5901 -p 6080:6080 -v $(pwd):/home/ubuntu/workspace --name labvir_moveit_01_container labvir_moveit_01
    ```
3. Acesse o ambiente via navegador no endereço: http://localhost:6080/

## Execução do container no vscode:

1. Clique no botão de play no canto inferior esquerdo do vscode:
    ![image](https://user-images.githubusercontent.com/10620355/221400332-30592847-0224-491f-9347-138279a71770.png)

2. Clique em "Reopen in Container"

3. Aguarde o container ser iniciado, o vscode irá reiniciar e abrir novamente. (Isso pode levar alguns minutos)

## Abra o ambiente de desenvolvimento no seu browser:

1. Abra o terminal PORTS do vscode com o atalho: Ctrl + Shift + P - Forward a Port

2. Clique na primeira porta que estará mapeada no endereço:  http://localhost:6080 

3. O ambiente XFCE4 deverá abrir no seu browser

4. Se desejar, ajuste a resolução para o seu monitor clicando no canto superior esquerdo do ambiente XFCE4 e selecionando "Display Settings"

5. Clique no botão para estender a exibição para a tela inteira - atalho: Ctrl + Shift + F12

6. Abra o vscode no ambiente de desenvolvimento:
    - Canto superior esquerdo do ambiente XFCE4, aplicações -> desenvolvimento -> vscode

7. Abra a pasta de trabalho do projeto - LabVir_moveit_01/catkin_ws

## Inicie a simulação do robô com o ROS:

1. Abra o terminal do vscode com o atalho: Ctrl + Shift + `

2. Execute o comando:

    ```bash
    catkin build
    ```

3. Ao final da compilação dos pacotes, execute o comando:
    ```bash
    source devel/setup.bash
    ```

4. Inicie a simulação do braço robótico Tangs com o comando:
    ```bash
    roslaunch tangs_moveit_config tangs_moveit_sim.launch
    ```

5. Aguarde a simulação do robô ser iniciada.

    - Organize a tela para que o RViz e o Gazebo fiquem lado a lado
    - No Rviz clique em plan and exec e escolha uma posição final para o braço robótico
    - O MoveIt fará os cálculos de trajetória e exibirá no Rviz, estando corretos a simulação
      deve iniciar no ambiente virtual do Gazebo

## Via GitHub Codespaces

Na execução via github Codespaces você não precisará instalar nada em seu computador, terá apenas que ter uma conta no github.

1. Acesse o repositório do projeto no github:
    [https://github.com/NURIA-IFSP/LabVir_moveit_01](https://github.com/NURIA-IFSP/LabVir_moveit_01)
    - Clique no botão "Code" e selecione "Codespaces"
    - O ambiente começará a ser montado no Codespaces (isso pode levar alguns minutos)

2. Feito isso abra o ambiente de desenvolvimento no seu browser, conforme explicado anteriormente e siga os mesmos passos.

3. Avisos Importantes:
    - Após a execução do ambiente você deverá clicar no botão "Stop" para encerrar o ambiente.
    - A execução de ambientes de desenvolvimento é cobrada pelo github, havendo um limite atual de 60 horas de execução por mês, ou 180 horas por mês para usuários com acesso premium. Estudantes e professores podem ter o limite aumentado.