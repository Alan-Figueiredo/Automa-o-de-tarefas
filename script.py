import pyautogui as pg
import time 
import pyperclip as pc

#pg.PAUSE = 0.5

time.sleep(2)
link = ''
pg.hotkey('ctrl','t')
pc.copy(link)
pg.hotkey('ctrl','v')
pg.press('enter')
time.sleep(3)
pg.click(x=670, y=495) # logar
time.sleep(5)
pg.click(x=24, y=132) # iniciar processo
time.sleep(10)
pg.click(x=267, y=455) # escolher empresa
pg.click(x=270, y=503) # selecionar empresa 
time.sleep(1)
pg.click(x=577, y=432) # fluxo de pagamentos
time.sleep(1)
pg.click(x=549, y=649) # notas de despesa Produto/serviço
time.sleep(1)
pg.click(x=529, y=532) # escolher arquivo
time.sleep(1)
pg.click(x=442, y=309) #selecionar nota 
pg.press('enter')
time.sleep(8)
pg.click(x=130, y=512) # clicar na nota 
time.sleep(1)
pg.click(x=944, y=432) # selecionar setor 
for a in range(15):
    pg.press('down') #abaixar 15x 
pg.press('enter')
pg.press('tab')
pg.press('tab')
pg.press('tab')

#preenchimento dos dados 
time.sleep(2)
pg.write('') # numero da nota 
pg.press('tab')
pg.write('') # cpnj
pg.press('tab')
pg.write('') # valor da nota 
pg.press('tab')
pg.write('') # data de emissão
pg.press('tab')
pg.write('') # fornecedor 
pg.press('tab')
pg.press('tab')
pg.write('') # data de vencimento
pg.press('tab')
pg.write('') # metodo de pagamento 
pg.press('tab')
pg.write('') #rateio 