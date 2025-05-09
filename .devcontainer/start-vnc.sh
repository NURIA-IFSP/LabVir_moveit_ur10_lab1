#!/bin/bash

# Configurações de ambiente
export USER=${USER:-ubuntu}
export HOME=/home/$USER
export DISPLAY=:1

# Mata instâncias antigas e limpa arquivos temporários
vncserver -kill $DISPLAY >/dev/null 2>&1 || true
rm -rf /tmp/.X1-lock /tmp/.X11-unix/X1 $HOME/.vnc/*

# Cria xstartup para o XFCE
mkdir -p "$HOME/.vnc"
cat <<EOF > "$HOME/.vnc/xstartup.turbovnc"
#!/bin/sh
unset SESSION_MANAGER
exec startxfce4
EOF
chmod +x "$HOME/.vnc/xstartup.turbovnc"

# Inicia o Xvfb (display virtual)
Xvfb $DISPLAY -screen 0 1920x900x24 +extension GLX +render -noreset >/dev/null 2>&1 &

# Inicia o TurboVNC no display :1
vncserver $DISPLAY -geometry 1280x900 -depth 24 \
    -xstartup "$HOME/.vnc/xstartup.turbovnc" \
    -securitytypes TLSNone \
    -nohttpd \
    -noxstartup >/dev/null 2>&1

# Aguarda inicialização
sleep 3

# Inicia o websockify se não estiver em execução
if ! pgrep -f "websockify.*6080" > /dev/null; then
    echo "Iniciando websockify em :6080..."
    websockify --web /usr/share/novnc 6080 localhost:5901 >/dev/null 2>&1 &
else
    echo "websockify já está em execução. Pulando."
fi


# Inicia aplicativos (se necessário)
bash "$HOME/start-apps.sh"

# Mantém o container ativo
tail -f /dev/null