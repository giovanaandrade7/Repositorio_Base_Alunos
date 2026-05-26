import pyautogui as at
def apertar_tab (qtd):
    for i in range (qtd): #Para poder apertar o botão várias vezes
        at.press("tab")
        at.sleep (0.01)

at.hotkey ("win","r") #Essa função aperta duas teclas ao mesmo tempo
at.write ("chrome", 0.2) #Essa função escreve
at.press ("enter") #essa função pressiona a tecla
at.sleep(1) #esperar
at.write ("www.instagram.com")
at.press ("enter")

email = at.prompt ("Digite o seu e-mail:")
at.write(email, 0.1)
at.press ("tab")


# programa = at.prompt ("Digite o nome do programa que deseja abrir")

# apertar_tab(5)
# at.sleep (3) 
# at.mouseDown (500,500)
# at.moveTo(1000,1001)
