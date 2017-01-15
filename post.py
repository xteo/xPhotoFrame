import urllib.request
import ssl

from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap, QColor

class Post(object):
    """ the post the photo frame inspect"""

    def __init__(self):
        """  """


    def getCaption(self):
        return ""

    def getLikesCount(self):
        return 0

    def __loadPixmapAtUrl(self, urlPath):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url_data = urllib.request.urlopen(urlPath, context=ctx).read()

        pixmap = QPixmap()
        pixmap.loadFromData(url_data)

        return pixmap

    def getUrl(self):
        return ""

    def getPixmap(self):
        url = self.getUrl()
        pixmap = self.__loadPixmapAtUrl(url)
        return pixmap

    def getLocation(self):
        return ""

    def getDate(self):
        return ""

class instagramPost(Post):
    """ From Instagram """

    def __init__(self, instagramMedia):
        """ """
        self.__media = instagramMedia

    def getLikesCount(self):
        return self.__media.like_count

    def getCaption(self):
        return self.__media.caption.text

    def getUrl(self):
        return self.__media.images['standard_resolution'].url

    def getLocation(self):
        return str(self.__media.location.name)

    def getDate(self):
        return self.__media.created_time.strftime("%A %d. %B %Y")





