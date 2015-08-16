# The ARAM Generator Launcher 'start.py'
from typrint import typrint
import main
import time
import sys
import os
import urllib
typrint('Checking Latest Versions...')
import check
time.sleep(0.5)
os.system('cls')

typrint('Hello! This is a Python Based Vainglory ARAM Generator')
typrint('You can type help at any point to see available commands')
typrint('==========================================')
heroch = ['all','melee','range','free']
typrint('Which type of heroes would you like?')
print 'Available choices are:',heroch
chflag = True
while chflag:
    choice = raw_input('Your Choice is: ')
    hlp = False
    if choice.lower() == 'help':
        print 'Available choices are:',
        print(heroch)
        hlp = True
        
    for i in range(len(heroch)):
        if choice.lower() == heroch[i]:
            typrint('==========================================')
            nstart = main.aramgen(data.heroes[i])
            chflag = False
            hlp = True
    if not hlp:
        try:
            nstart
        except NameError:
            typrint('Wrong choice please try again or type help too see available choices')

nstart.roll()
typrint('================ Team A ==================')
for i in range(3): 
    typrint('%s Plays %s' %(nstart.team_a[i],nstart.hero_a[i]))
typrint('================ Team B ==================')
for i in range(3): 
    typrint('%s Plays %s' %(nstart.team_b[i],nstart.hero_b[i]))
typrint('==========================================')

flag = True
rollch = []
for i in range(3):
    rollch.append('reroll %s' %(nstart.team_a[i]))
for i in range(3):
    rollch.append('reroll %s' %(nstart.team_b[i]))
rollch.append('restart')
rollch.append('quit')
while flag:
    choice = raw_input('What would you like to do?: ')
    hlp = False
    if choice.lower() == 'help':
        print 'Available choices are:',
        print(rollch)
        hlp = True
    for i in range(3):
        if choice.lower() == rollch[i]:
            hlp = True
            nstart.reroll('a',i)
            typrint('==========================================')
            typrint('%s Plays %s' %(nstart.team_a[i],nstart.hero_a[i]))
            typrint('==========================================')
    for i in range(3,6):
        if choice.lower() == rollch[i]:
            hlp = True
            nstart.reroll('b',i-3)
            typrint('==========================================')
            typrint('%s Plays %s' %(nstart.team_b[i-3],nstart.hero_a[i-3]))
            typrint('==========================================')
    if choice.lower() == 'restart':
            hlp = True
            os.system('cls')
            import start
    
    if choice.lower() == 'quit':
        hlp = True
        exit()
    if not hlp:
        typrint('Wrong choice please try again or type help too see available choices')
