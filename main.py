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

# Abrir o menu Iniciar do Windows
keyboard.press_and_release("win")
time.sleep(1)

# Digitar "Google Chrome"
keyboard.write("Google Chrome", delay=0.1)
time.sleep(1)

# Pressionar Enter para abrir o Chrome
keyboard.press_and_release("enter")
time.sleep(3)  # Aguarda o Chrome abrir

# Maximizar a janela do Chrome (pressionando a tecla Windows + seta para cima)
keyboard.press_and_release("win+up")
time.sleep(1)

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
time.sleep(5)
