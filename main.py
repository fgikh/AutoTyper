import pyautogui, time #importar o pyautogui
time.sleep(3) #tempo para comecar em segundos
texto = open('paragrafo1.txt', encoding='utf8') #abrir o arquivo de texto1
for texto in texto:
    pyautogui.press('tab') #paragrafo
    pyautogui.typewrite(texto) #escrever texto1
    pyautogui.press ('enter') #ir para outra linha
    time.sleep(0.5) #coolsown
texto = open('paragrafo2.txt', encoding='utf8')  #abrir arquivo de texto2
for texto in texto:
    pyautogui.press ('tab') #paragrafo
    pyautogui.typewrite(texto) #escrever texto2
    pyautogui.press ('enter')
    time.sleep(0.5) #cooldown
texto = open('paragrafo3.txt', encoding='utf8')  #abrir arquivo de texto3
for texto in texto:
    pyautogui.press('tab') #paragrafo
    pyautogui.typewrite(texto) #escrever texto3
    time.sleep(3) #cooldown
    pyautogui.hotkey('Ctrl','b') #salvar
    time.sleep(2) #cooldown
    pyautogui.moveTo(200, 350) #posicao do mouse
    time.sleep(2) #cooldown
    pyautogui.leftClick(x=200, y=350)  #posicao do click
    time.sleep(4) #cooldown
    pyautogui.typewrite('arquivoBot', interval=0.05) #nome do arquivo
    time.sleep(1) #cooldown
    pyautogui.leftClick(x=500, y=470) #posicao do click
    time.sleep(1) #cooldown
    pyautogui.press('esc') #sair da tela
    time.sleep(1) #cooldown

                                                                                        
                                                                                        


