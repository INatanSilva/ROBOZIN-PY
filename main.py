import pyautogui
import keyboard
import time

# Seu usuário e senha do Instagram
USERNAME = "flx.natan"
PASSWORD = "11780natan"

# Coordenadas fornecidas
COORDS_ID = (882, 320)
COORDS_PIN = (872, 382)
COORDS_ENTER = (925, 436)
COORDS_PERFIL = (97, 755)
COORDS_OPCOES = (1324, 175)
COORDS_DEFINICOES_PRIVACIDADE = (941, 527)
COORDS_AMIGOS_CHEGADOS = (442, 860)

# Coordenadas para o primeiro item da lista
COORDS_INICIAL = [1664, 384]  # Usamos lista para poder modificar diretamente
DESLOCAMENTO = 77  # Distância entre os itens
SCROLL_DISTANCE = -500  # Quantidade exata de scroll (negativo para descer)
NUM_ITENS = 100
CLICKS_BEFORE_SCROLL = 7  # Quantos cliques antes de rolar a tela

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
time.sleep(7)  # Tempo para carregar a página

# **Clicar no campo de usuário**
pyautogui.click(COORDS_ID[0], COORDS_ID[1])
time.sleep(1)
keyboard.write(USERNAME, delay=0.1)
time.sleep(3)  # Garantir que foi digitado

# **Clicar no campo de senha**
pyautogui.click(COORDS_PIN[0], COORDS_PIN[1])
time.sleep(1)
keyboard.write(PASSWORD, delay=0.1)
time.sleep(2)

# **Clicar no botão "Enter"**
pyautogui.click(COORDS_ENTER[0], COORDS_ENTER[1])
time.sleep(8)

# **Clicar no "Perfil"**
pyautogui.click(COORDS_PERFIL[0], COORDS_PERFIL[1])
time.sleep(5)

# **Clicar em "Opções"**
pyautogui.click(COORDS_OPCOES[0], COORDS_OPCOES[1])
time.sleep(5)

# **Clicar em "Definições e Privacidade"**
pyautogui.click(COORDS_DEFINICOES_PRIVACIDADE[0], COORDS_DEFINICOES_PRIVACIDADE[1])
time.sleep(5)

# **Clicar em "Amigos Chegados"**
pyautogui.click(COORDS_AMIGOS_CHEGADOS[0], COORDS_AMIGOS_CHEGADOS[1])
time.sleep(7)

# Função para rolar a página, ajustar a posição inicial e continuar os cliques
def precise_scroll():
    global COORDS_INICIAL  # Precisamos modificar a posição inicial após o scroll

    # Captura a posição atual do mouse antes do scroll
    mouse_x, mouse_y = pyautogui.position()

    # Faz o scroll exato (negativo para descer)
    pyautogui.scroll(SCROLL_DISTANCE)
    time.sleep(1)

    # Move o mouse de volta para a posição inicial antes do scroll
    pyautogui.moveTo(mouse_x, mouse_y - abs(SCROLL_DISTANCE))
    time.sleep(1)

    # **Ajusta a posição inicial para o próximo ciclo de cliques**
    COORDS_INICIAL[1] -= abs(SCROLL_DISTANCE)  # Move para cima conforme o scroll

# Iniciar o loop para clicar nos amigos da lista
cliques = 0
for i in range(NUM_ITENS):
    next_coord = (COORDS_INICIAL[0], COORDS_INICIAL[1] + i * DESLOCAMENTO)

    # Mover para o item e clicar
    pyautogui.moveTo(next_coord[0], next_coord[1])
    pyautogui.click(next_coord[0], next_coord[1])
    time.sleep(1)

    cliques += 1

    # Se atingir o limite, faz o scroll e ajusta a posição
    if cliques == CLICKS_BEFORE_SCROLL:
        precise_scroll()
        cliques = 0  # Reseta o contador

    time.sleep(2)  # Pausa entre cliques
