from instagram.client import InstagramAPI
from post import Post

class instagramClient(object):
    def __init__(self):

        access_token = "10235636.e2204f8.903c791be2874be4a4f9a0981eb5fff2"
        client_secret = "c773313edd684b49a1efbf163d7b0fbf"
        self.api = InstagramAPI(access_token=access_token, client_secret=client_secret)

    def getRecentPost(self):

        return posts
