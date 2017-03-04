
import facebook

class facebookClient(object):
    def __init__(self):
        access_token = 'EAACEdEose0cBAIF85Xled2cc1JGuiiqcp4wvk3GpKPrzeIZCVpWVpQW9fN5XcjZBrKKbKvSCzenU4i878UoZCdpLrxS93yilC1ae6FCcNJwS6unjI7UX4JaRAtSsZBZBtA9kr4wxq1IffhwUDLzYfyTzdxhqvJJBNf819YjQdONfykcpCfJWUU5uSO4CwSVEZD'
        self.graph = facebook.GraphAPI(access_token)

