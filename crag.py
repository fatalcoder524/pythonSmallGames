import random
from tabulate import tabulate
n,rounds,maxscore=0,13,0
playerList=[]
class Player:
    def __init__(self,id,name,score,category):
        self.id=id
        self.name=name
        self.score=score
        self.category=category

def createPlayer(playerNum):
    global playerList
    name=input("Enter Player {:d} name: ".format(playerNum))
    playerList.append(Player(playerNum,name,0,[]))

def selectCategory(player):
    global playerList
    categories=["","1. Ones","2. Twos","3. Threes","4. Fours","5. Fives","6. Sixes","7. Even Straight","8. Odd Straight","9. High Straight","10. Low Straight","11. Three-Of-A-Kind","12. Thirteen","13. Crag"]
    for i in range(1,14):
        if not i in playerList[player].category:
            print(categories[i])
    category=int(input("Select a Category: "))
    if(category>0 and category<14 and not category in playerList[player].category):
        playerList[player].category.append(category)
    else:
        print("Wrong Option or Category already Selected.")
        selectCategory(player)

def rollDice(diceFinal):
    dice=[]
    for i in range(3):
        if(diceFinal[i]==0):
            dice.append(random.choice([1,2,3,4,5,6]))
        else:
            dice.append(diceFinal[i])
    return dice

def selectDice(dice,diceFinal,pRound):
    if(pRound==1):
        ans=input("Do You want to finalize any Dice? (Y/N): ")
        if(ans=='Y' or ans=='y'):
            selection=list(map(int,input("Enter the dice number(1-3);Can select multiple dice seperated by space: ").split()))
            for i in selection:
                diceFinal[i-1]=dice[i-1]
    else:
        for i in range(3):
            if diceFinal[i]==0:
                diceFinal[i]=dice[i]

class Switcher(object):
    def choice(self,i,diceFinal):
        method_name='case_'+str(i)
        method=getattr(self,method_name,lambda :'Invalid')
        return method(diceFinal)
    
    def case_1(self,diceFinal):
        score=0
        for i in range(3):
            if diceFinal[i]==1:
                score+=1
        return score
    
    def case_2(self,diceFinal):
        score=0
        for i in range(3):
            if diceFinal[i]==2:
                score+=2
        return score
    
    def case_3(self,diceFinal):
        score=0
        for i in range(3):
            if diceFinal[i]==3:
                score+=3
        return score
    
    def case_4(self,diceFinal):
        score=0
        for i in range(3):
            if diceFinal[i]==4:
                score+=4
        return score
    
    def case_5(self,diceFinal):
        score=0
        for i in range(3):
            if diceFinal[i]==5:
                score+=5
        return score
    
    def case_6(self,diceFinal):
        score=0
        for i in range(3):
            if diceFinal[i]==6:
                score+=6
        return score
    
    def case_7(self,diceFinal):
        score=0
        if diceFinal==[2,4,6]:
            score=20
        return score
    
    def case_8(self,diceFinal):
        score=0
        if diceFinal==[1,3,5]:
            score=20
        return score
    
    def case_9(self,diceFinal):
        score=0
        if diceFinal==[4,5,6]:
            score=20
        return score
    
    def case_10(self,diceFinal):
        score=0
        if diceFinal==[1,2,3]:
            score=20
        return score
    
    def case_11(self,diceFinal):
        score=0
        if len(set(diceFinal)) <= 1:
            score=25
        return score
    
    def case_12(self,diceFinal):
        score=0
        if sum(diceFinal)==13:
            score=26
        return score
    
    def case_13(self,diceFinal):
        score=0
        if len(set(diceFinal)) == 2 and sum(diceFinal)==13:
            score=50
        return score

def checkCategory(player,diceFinal):
    global playerList
    categorySelected=playerList[player].category[len(playerList[player].category)-1]
    s=Switcher()
    playerList[player].score+=s.choice(categorySelected,diceFinal)
    print("Player {:d} Score= {:d}".format(player,playerList[player].score))

def checkMaxScore(player):
    global playerList,maxscore
    if playerList[player].score>maxscore:
        maxscore= playerList[player].score
    if(playerList[player].score==244):
        print("Player {} Wins!!!".format(player))
        exit(0)

def main():
    global n,rounds,playerList,maxscore
    playerList.append([])
    print("+------------------------------+")
    print("+ Welcome to Crag Dice Game!!! +")
    print("+------------------------------+")
    n=int(input("Enter the number of players: "))
    for i in range(1,n+1):
        createPlayer(i)
    for i in range(1,rounds+1):
        for player in range(1,n+1):
            print("+------------------------------------------------------------------------------------------------------------------------+")
            print("{}'s Move:".format(playerList[player].name))
            diceFinal=[0,0,0]
            selectCategory(player)
            for pRound in range(1,3,1):
                dice=rollDice(diceFinal)
                print("Current Dice Roll: ",*dice)
                selectDice(dice,diceFinal,pRound)
            diceFinal.sort()
            checkCategory(player,diceFinal)
            checkMaxScore(player)
    winnerList=[]
    print("+------------------------------------------------------------------------------------------------------------------------+")
    for i in range(1,n+1):
        if playerList[i].score==maxscore:
            winnerList.append(i)
    scoreTable=[]
    for i in range(1,n+1):
        scoreTable.append([playerList[i].id,playerList[i].name,playerList[i].score])
    print("\n\n")
    print(tabulate(scoreTable,headers=["Player No.","Player Name","Player Score"]))
    print("\n\n")
    if len(winnerList)>1:
        print("+--------------------------------------------+")
        print("+ Players ",*winnerList," are the winners!!! +")
        print("+--------------------------------------------+")
    else:
        print("+-----------------------------------------+")
        print("+ Player ",*winnerList," is the winner!!! +")
        print("+-----------------------------------------+")
    
if __name__ == '__main__':
    main()
