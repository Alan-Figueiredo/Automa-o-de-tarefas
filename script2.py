import pyautogui as pg
import time 
import pyperclip as pc

teste = []

time.sleep(3)

for a in teste:
    
    pg.write(a) # numero da nota 
    pg.press('tab')
    pg.write('') # cpnj
    pg.press('tab')
    pg.write('') # valor da nota 
    pg.press('tab')
    pg.write('') # data de emissão
    pg.press('tab')
    pg.write('') # fornecedor 
    pg.press('tab')
   # pg.press('tab')
    pg.write('') # data de vencimento
    pg.press('tab')
    pg.write('') # metodo de pagamento 
    pg.press('tab')
    pg.write('') #rateio
   
   
    
