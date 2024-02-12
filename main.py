
""" class character:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack
        
    def displayStats(self):
        print(f'HP: {self.hp}')
        print(f'Attack: {self.attack}')

def num6():
    mario = character(100,15)
    mario.displayStats() """

""" def num7():
    x = 5
    y = "test"
    
    try:
        print(x + y)
    except Exception as e:
        print(e) """

    
def createFile():
    with open('test.txt', 'w') as file:
        file.write('hello world')
        print('File created.')
        return

def readFile():
    with open('test.txt', 'r') as file:
        test = file.read()
        print(f'test.txt: {test}')
        return
    
def num8():
    createFile()
    readFile()

if __name__=="__main__":
    #num6()
    #num7()
    num8()