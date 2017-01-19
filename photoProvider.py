from PyQt5.QtCore import QUrl, QSize

from PyQt5.QtQuick import QQuickImageProvider


class photoProvider(QQuickImageProvider):
    def __init__(self, posts=[]):
        QQuickImageProvider.__init__(self, QQuickImageProvider.Pixmap)

        self._posts = posts

    def setPosts(self, posts):
        self._posts = posts

    def requestPixmap(self, id, size):

        post = self._posts[(int(id))]
        pixmap = post.getPixmap()

        return pixmap , QSize(100, 100)

    def urlHandle(self):
        return ""


class instagramProvider(photoProvider):
    def __init__(self, posts=[]):
        photoProvider.__init__(self,posts)

    def urlHandle(self):
        return "instagram"


class instagramUserProvider(photoProvider):
    def __init__(self, posts=[]):
        photoProvider.__init__(self,posts)

    # def requestPixmap(self, id, size):
    #
    #     post = self._posts[(int(id))]
    #     pixmap = post.getUserPixmap()
    #
    #     return pixmap , QSize(100, 100)

    def urlHandle(self):
        return "instagramUser"



class facebookProvider(photoProvider):
    def __init__(self, posts=[]):
        photoProvider.__init__(self,posts)

    def urlHandle(self):
        return "facebook"


class facebookUserProvider(photoProvider):
    def __init__(self, posts=[]):
        photoProvider.__init__(self,posts)

    # def requestPixmap(self, id, size):
    #
    #     post = self._posts[(int(id))]
    #     pixmap = post.getUserPixmap()
    #
    #     return pixmap , QSize(100, 100)

    def urlHandle(self):
        return "facebookUser"
