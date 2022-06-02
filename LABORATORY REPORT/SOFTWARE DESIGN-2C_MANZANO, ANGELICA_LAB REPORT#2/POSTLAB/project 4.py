def _init_(self,bank):
   EasyFrame._init __(self,title="ATM")
   self.unsuccessfulLoginCount=
   name=self.nameField.getText()
   pin=self.pinField.getText()
   self.account=self.bank.get(name,pin)
   if self.account:
       self.unsuccessfulLoginCount=0
       self.statusField.setText("Hello,+name+"!")
       self.balanceButton["state"]="normal"
       self.depositButton["state"]="normal"
       self.withdrawButton["state"]="normal"
       self.loginButton["text"]="Logout"
       self.loginButton["command"]=self.logout
   else:
       self.unsuccessfulLoginCount+=1
       if self.unsuccessful LoginCount>2:
           self.messageBox(title="Attention",\
           self.loginButton["state"]="disabled"
       else:
           self.messageBox(title="Attention",
       self.statusField.setText("Name and pin not found!")
def login(self):
                      message="Police is on the way")
                      message"Police will be called after
                      str(3-self.unsuccessfulLoginCount)+more consecutive login fails!")
