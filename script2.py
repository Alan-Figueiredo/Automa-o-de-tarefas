import pyautogui as pg
import time 
import pyperclip as pc

teste = ['2022','2021','2321','7898','5645']

time.sleep(3)

for a in teste:
    
    pg.write(a) # numero da nota 
    pg.press('enter')
    pg.write('07705502221') # cpnj
    pg.press('enter')
    pg.write('123,32') # valor da nota 
    pg.press('enter')
    pg.write('02/02/2022') # data de emissão
    pg.press('enter')
    pg.write('testeltda123') # fornecedor 
    pg.press('enter')
   # pg.press('tab')
    pg.write('20/03/2022') # data de vencimento
    pg.press('enter')
    pg.write('Boleto') # metodo de pagamento 
    pg.press('enter')
    pg.write('padrao') #rateio
    pg.press('enter')
    pg.press('enter')
    