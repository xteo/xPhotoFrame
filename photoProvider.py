from PyQt5.QtCore import QUrl, QSize

from PyQt5.QtQuick import QQuickImageProvider


class photoProvider(QQuickImageProvider):
    def __init__(self, posts=[]):
        QQuickImageProvider.__init__(self, QQuickImageProvider.Pixmap)

        self.__posts = posts

    def setPosts(self, posts):
        self.__posts = posts

    def requestPixmap(self, id, size):

        post = self.__posts[(int(id))]
        pixmap = post.getPixmap()

        return pixmap , QSize(100, 100)

    def urlHandle(self):
        return ""


class instagramProvider(photoProvider):
    def __init__(self, posts=[]):
        photoProvider.__init__(self,posts)

    def urlHandle(self):
        return "instagram"