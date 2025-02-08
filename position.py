import pyautogui
import keyboard

print("Clique em qualquer lugar da tela para capturar as coordenadas.")
print("Pressione 'Esc' para sair.")

while True:
    if keyboard.is_pressed('esc'):
        print("Saindo...")
        break  # Encerra o script se 'Esc' for pressionado
    
    if pyautogui.mouseInfo():  # Verifica se o mouse foi clicado
        x, y = pyautogui.position()
        print(f"Coordenadas do clique: X={x}, Y={y}")
        # Aguardar o clique para que as coordenadas sejam capturadas novamente
        pyautogui.sleep(1)
