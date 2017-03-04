import urllib.request
import ssl

from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap, QColor

from instagramClient import instagramClient
from facebookClient import facebookClient
from datetime import datetime
import dateutil.parser as dateparser

class Post(object):
    """ the post the photo frame inspect"""

    def __init__(self):
        """  """

    def _boldHashtag(self, caption):
        parts = caption.split(" ")
        newParts = []
        for aPart in parts:
            if aPart.startswith("#"):
                hashtag = "<font color='LightSkyBlue' size='4'>%s</font>" % aPart
                newParts.append(hashtag)
            else:
                newParts.append(aPart)

        return " ".join(newParts)

    def getCaption(self):
        return ""

    def getLikesCount(self):
        return 0

    def __loadPixmapAtUrl(self, urlPath):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        try:
            url_data = urllib.request.urlopen(urlPath, context=ctx).read()
        except TypeError:
            url_data = urllib.request.urlopen(urlPath).read()


        pixmap = QPixmap()
        pixmap.loadFromData(url_data)

        return pixmap

    def getUrl(self):
        return ""

    def getImageHandle(self, index):
        return ""

    def getPixmap(self):
        url = self.getUrl()
        pixmap = self.__loadPixmapAtUrl(url)
        return pixmap

    def getLocation(self):
        return ""

    def getDate(self):
        return ""

    def getUserName(self):
        return ""

    def getUserPixmap(self):
        url = self.getUserImageUrl()
        pixmap = self.__loadPixmapAtUrl(url)
        return pixmap

    def getUserImageUrl(self):
        return ""

class instagramPost(Post):
    """ From Instagram """

    def __init__(self, instagramMedia):
        """ """
        self.__media = instagramMedia
        ## setup Instragram Support
        self.__instagramClient = instagramClient()

    def getLikesCount(self):
        return self.__media.like_count

    def getCaption(self):
        return self._boldHashtag(self.__media.caption.text)

    def getUrl(self):
        return self.__media.images['standard_resolution'].url

    def getImageHandle(self, index):
        return "image://%s/%d" % ("instagram", index)

    def getLocation(self):
        return str(self.__media.location.name)

    def getDate(self):
        return self.__media.created_time.strftime("%A %d. %B %Y")

    def getUserName(self):
        return self.__media.user.username

    def getUserImageUrl(self):
        user = self.__instagramClient.api.user(user_id=self.__media.user.id)
        return user.profile_picture

    def getImageUserHandle(self, index):
        return "image://%s/%d" % ("instagramUser", index)



class facebookPost(Post):
    """ From Instagram """

    def __init__(self, facebookMedia):
        """ """
        self.__media = facebookMedia
        ## setup Instragram Support
        self.__facebookClient = facebookClient()

        debug = False
        if debug:
            print(self.__media.keys())

            for aKey in self.__media.keys():
                print(aKey, self.__media[aKey])


    def getLikesCount(self):
        if "likes" in self.__media:
            return len(self.__media["likes"]['data'])
        else:
            return 0

    def getCaption(self):
        return self._boldHashtag(self.__media['message'])

    def getUrl(self):
        #print(self.__media.keys())
        photoId = self.__media['object_id']
        profile = self.__facebookClient.graph.get_object(photoId)

        #print(profile.keys())
        #for aKey in profile.keys():
        #    print(aKey, profile[aKey])
        return profile['images'][0]['source']

        #return self.__media['picture']

    def getImageHandle(self, index):
        return "image://%s/%d" % ("facebook", index)

    def getLocation(self):
        if "place" in self.__media:
            return str(self.__media['place']['name'])
        else:
            print (self.__media.keys())
            return ""

    def getDate(self):
        datetime_object = dateparser.parse(self.__media["created_time"])
        return datetime_object.strftime("%a %d. %b %Y")

    def getUserName(self):
        return self.__media['from']['name']

    def getUserImageUrl(self):
        #user = self.__instagramClient.api.user(user_id=self.__media.user.id)
        return ""

    def getImageUserHandle(self, index):
        return "image://%s/%d" % ("facebookUser", index)



