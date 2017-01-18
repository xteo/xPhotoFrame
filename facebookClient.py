import facebook

class facebookClient(object):
    def __init__(self):
        access_token = 'EAACEdEose0cBAKTo1ZCJhqkfrErK1TuGhCILNqohSnIMF51eckuMfZCUxVqNfRquPQukvkCOglp5IKdzFPi0xNyy3LjTRL85RvCFiYHjFrYZARZBy4lo8CesgxXsgDGwRJXBwYie7VbZAjvrK4RH0NUbnPY1vubgDVqNSJQzTVQZDZD'
        self.graph = facebook.GraphAPI(access_token)

