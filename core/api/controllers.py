from instagram.controllers import InstagramAPIController


class UserAPIController:

    def createUser(self, data):
        pass

    def getUser(self, pk):
        pass

    def listUsers(self):
        pass

    def updateUser(self, data, pk):
        pass

    def deleteUser(self, pk):
        pass


class APIController:

    def __init__(self, user):
        self.user = user
        self.Instagram = InstagramAPIController(user=user)
    
    def makePost(self, post):
        return self.Instagram.makePost(post=post, user=self.user)