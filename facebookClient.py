
import facebook

class facebookClient(object):
    def __init__(self):
        access_token = 'EAACEdEose0cBAGZCTFdKb4ZBNhxS71sS0g7m29mFAvRAhFjTNsCgsllcZAgPnjYFrOoZAm5PELVZCpnlvl9NKRCIEuUjWI0TuKiEICvdsLgjmq1KfVWXl6xkjw88g8rS45xBn8hkUb2CelWbCZB5dEk4x8ET5bqKlmdXbjtZBXqVNURrdlInBdaMjH18uZByuPUZD'
        self.graph = facebook.GraphAPI(access_token)

