# ARAM Generator Base Code 'main.py'
from random import randint

class aramgen:
    def __init__(self,hlist):
        self.team_a = []
        self.team_b = []
        self.hlist = list(hlist)
        for i in range(3):
            self.team_a.append(raw_input('Enter Player %d on Team A ign: ' %(i+1)))
        for i in range(3):
            self.team_b.append(raw_input('Enter Player %d on Team B ign: ' %(i+1)))

    def roll(self):
        self.hero_a = []
        self.hero_b = []
        self.hlist_ = list(self.hlist)

        for i in range(3):
            if i >= 1:
                self.hlist_.remove(self.hero_a[i-1])
            self.end = len(self.hlist_)-1
            self.hero_a.append(self.hlist_[randint(0,self.end)])
            
        self.hlist_ = list(self.hlist)

        for i in range(3):
            if i >= 1:
                self.hlist_.remove(self.hero_b[i-1])
            self.end = len(self.hlist_)-1
            self.hero_b.append(self.hlist_[randint(0,self.end)])
            
        
    def reroll(self,team,player):
        self.hlist_ = list(self.hlist)
        if team == 'a':
            team = self.hero_a
            for i in self.hero_a:
                self.hlist_.remove(i)
            self.end = len(self.hlist_)-1
            self.hero_a[player] = self.hlist_[randint(0,self.end)]
                
        if team == 'b':
            team = self.hero_b
            for i in self.hero_b:
                self.hlist_.remove(i)
            self.end = len(self.hlist_)-1
            self.hero_b[player] = self.hlist_[randint(0,self.end)]
    
    
