import pyautogui
import keyboard
import time

# Seu usuário e senha do Instagram
USERNAME = "flx.natan"
PASSWORD = "11780natan"

# Coordenadas fornecidas
COORDS_ID = (882, 320)  # Coordenada para o campo "ID"
COORDS_PIN = (872, 382)  # Coordenada para o campo "PIN"
COORDS_ENTER = (925, 436)  # Coordenada para o botão "ENTER"
COORDS_PERFIL = (97, 755)  # Coordenada para "Perfil"
COORDS_OPCOES = (1324, 175)  # Coordenada para "Opções"
COORDS_DEFINICOES_PRIVACIDADE = (941, 527)  # Coordenada para "Definições e Privacidade"
COORDS_AMIGOS_CHEGADOS = (442, 860)  # Coordenada para "Amigos Chegados"

# Coordenadas para o primeiro item da lista
COORDS_INICIAL = (1664, 384)  # Coordenada inicial
DESLOCAMENTO = (0, 77)  # Deslocamento entre as coordenadas (no seu caso é 77 na coordenada Y)

# Número de itens na lista (ajuste conforme o número real de itens)
NUM_ITENS = 100  # Ajuste este número conforme o total de itens na lista

# Número de cliques antes de rolar a página
CLICKS_BEFORE_SCROLL = 7

# Abrir o menu Iniciar do Windows
keyboard.press_and_release("win")
time.sleep(1)

# Digitar "Google Chrome"
keyboard.write("Google Chrome", delay=0.1)
time.sleep(1)

# Pressionar Enter para abrir o Chrome
keyboard.press_and_release("enter")
time.sleep(3)  # Aguarda o Chrome abrir

# Focar na barra de endereços
keyboard.press_and_release("ctrl+l")
time.sleep(1)

# Digitar a URL de login do Instagram
keyboard.write("https://www.instagram.com/accounts/login/", delay=0.1)
time.sleep(1)

# Pressionar Enter para acessar o site
keyboard.press_and_release("enter")
time.sleep(7)  # Tempo maior para garantir que a página carregue completamente

# **Clicar no campo de usuário usando as coordenadas fornecidas**
pyautogui.click(COORDS_ID[0], COORDS_ID[1])  # Clica nas coordenadas de ID
time.sleep(1)

# Digitar o nome de usuário
keyboard.write(USERNAME, delay=0.1)
time.sleep(1)

# Garantir que o nome de usuário foi digitado antes de continuar
time.sleep(3)

# **Clicar no campo de senha usando as coordenadas fornecidas**
pyautogui.click(COORDS_PIN[0], COORDS_PIN[1])  # Clica nas coordenadas de PIN
time.sleep(1)

# Digitar a senha
keyboard.write(PASSWORD, delay=0.1)
time.sleep(2)

# **Clicar no botão "Enter" usando as coordenadas fornecidas**
pyautogui.click(COORDS_ENTER[0], COORDS_ENTER[1])  # Clica no botão de login (ENTER)
time.sleep(8)  # Tempo para o login ser processado

# **Clicar no "Perfil" após o login**
pyautogui.click(COORDS_PERFIL[0], COORDS_PERFIL[1])  # Clica nas coordenadas de Perfil
time.sleep(5)

# **Clicar em "Opções"**
pyautogui.click(COORDS_OPCOES[0], COORDS_OPCOES[1])  # Clica nas coordenadas de Opções
time.sleep(5)

# **Clicar em "Definições e Privacidade"**
pyautogui.click(COORDS_DEFINICOES_PRIVACIDADE[0], COORDS_DEFINICOES_PRIVACIDADE[1])  # Clica nas coordenadas de Definições e Privacidade
time.sleep(5)

# **Clicar em "Amigos Chegados"**
pyautogui.click(COORDS_AMIGOS_CHEGADOS[0], COORDS_AMIGOS_CHEGADOS[1])  # Clica nas coordenadas de Amigos Chegados
time.sleep(7)

# Função para rolar a página
def scroll_page():
    pyautogui.scroll(-500)  # Rolando para baixo

# Iniciar o loop para clicar nos amigos da lista
cliques = 0
for i in range(NUM_ITENS):
    # Calcula a coordenada do próximo item, com base na coordenada inicial e no deslocamento
    next_coord = (COORDS_INICIAL[0], COORDS_INICIAL[1] + i * DESLOCAMENTO[1])

    # Mover para o item e clicar
    pyautogui.moveTo(next_coord[0], next_coord[1])
    pyautogui.click(next_coord[0], next_coord[1])
    time.sleep(1)  # Tempo entre os cliques

    # Incrementar o contador de cliques
    cliques += 1

    # Se o número de cliques for 7, rolar a página e reiniciar o contador
    if cliques == CLICKS_BEFORE_SCROLL:
        scroll_page()  # Realiza o scroll para baixo
        time.sleep(1)  # Aguarda o tempo do scroll ser processado
        cliques = 0  # Reseta o contador de cliques

    # Pausa entre iterações para evitar sobrecarga
    time.sleep(2)
