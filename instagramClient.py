from instagram.client import InstagramAPI

class instagramClient(object):
    def __init__(self):

        #https://www.instagram.com/oauth/authorize/?client_id=e2204f88b90748eb96a44956e2db33ec&redirect_uri=http://localhost/~xteo/index.php&response_type=token&scope=basic+public_content
        access_token = "10235636.e2204f8.2a970ffaabd1426fb14f2859495ef617"
        client_secret = "c773313edd684b49a1efbf163d7b0fbf"
        self.api = InstagramAPI(access_token=access_token, client_secret=client_secret)

