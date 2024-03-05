#in automation we use classes a lot to segregate the class utilites, page object etc.,
class loginpage:
    def _init_(self,username,password,sceret):
        self.sceret=sceret
        #init will initalize the value due to login
    def login(self,username,password):
        return username + "----" + password
    def loginwithscerte(self,username,password):
        return username + "----" + password+self.sceret

#we call a class using login=LogInPage()
l=loginpage("&&&&&&&")
print(l.login("admin","passwords"))
#creating a class and calling a member of a class from here
#consuructor type
print(l.loginwithscerte("supervisor","superpass"))