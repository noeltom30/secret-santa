import random
import emailActions
class SecretSanta:
    def __init__(self):
        self.partiDetails = {}#key is participants name and value is email
        self.partiDetails2 = {}
        self.pairs = {} #the key has to gift the value
        self.alreadyPaired = []
        
    #Main method
    def main(self):
        self.acceptNames()               
        self.pairUp()        
        self.emailSending()
        emailActions.emailDeleter()
               
        
    #to accept inputs
    def acceptNames(self):
        num = int(input("Enter the number of people participating: "))
        for i in range(0, num):
            print("For participant", i+1)
            nameTemp = input("Name: ")
            self.partiDetails[nameTemp] = input("Email: ")
        self.partiDetails2 = self.partiDetails.copy()            
    #pairs up each participant with another        
    def pairUp(self):        
        for participant in self.partiDetails:
            temp = self.generate_random(participant)
            self.pairs[participant] = temp                        
            self.partiDetails2.pop(temp)
    #randomly generates who the participant should gift                
    def generate_random(self, curName):
        while True:
            key = random.choice(list(self.partiDetails2.keys()))            
            if key != curName :
                return key        
    #sends an email to each gifter telling them who they should gift     
    def emailSending(self):
        for gifterReal, gifteeReal in self.pairs.items():
            emailActions.emailSender(gifterReal, gifteeReal, self.partiDetails[gifterReal])
        print("Emails sent successfully")
             

obj = SecretSanta()
obj.main()