import urllib.request
import ssl

from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap, QColor

from instagramClient import instagramClient

class Post(object):
    """ the post the photo frame inspect"""

    def __init__(self):
        """  """

    def _boldHashtag(self, caption):
        parts = caption.split(" ")
        newParts = []
        for aPart in parts:
            if aPart.startswith("#"):
                hashtag = "<font color='MidnightBlue' size='4'>%s</font>" % aPart
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

#        url_data = urllib.request.urlopen(urlPath , context=ctx).read()
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



