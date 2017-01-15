import sys

from PyQt5.QtCore import QUrl, QTimer

from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication

from instagramClient import instagramClient

import photoProvider

import post

class xPhotoFame(QQuickView):
    def __init__(self):
        QQuickView.__init__(self)

        self.__context = self.rootContext()
        self.__engine = self.__context.engine()

        # the list of Post we are currently showing
        self.__posts = []

        self.__currentPostIndex = 0

        # current Provider
        self.__currentPhotoProvider = None

        ## setup Instragram Support
        self.__instagramClient = instagramClient()

        # setup the Instagram Provider
        self.__instagramProvider = photoProvider.instagramProvider()
        self.__engine.addImageProvider("instagram", self.__instagramProvider)

        self.setSource(QUrl('./MainForm.ui.qml'))

    def setupAsInstagramFeed(self):
        self.__posts = []
        recent_media, next_ = self.__instagramClient.api.user_recent_media()
        for aMedia in recent_media:
            self.__posts.append(post.instagramPost(aMedia))

        self.__instagramProvider.setPosts(self.__posts)

        self.__currentPhotoProvider = self.__instagramProvider

    def __setPostIndex(self, index):
        self.__currentPostIndex = index

        post = self.__posts[index]

        self.__context.setContextProperty("imageUrl", "image://%s/%d" %
                                                    (self.__instagramProvider .urlHandle(), index) )

        self.__context.setContextProperty("likesText", post.getLikesCount())
        self.__context.setContextProperty("commentText", post.getCaption())
        self.__context.setContextProperty("locationText", post.getLocation())
        self.__context.setContextProperty("dateText", post.getDate())




    def __showNextPost(self):
        newIndex = self.__currentPostIndex+1
        if newIndex >= len(self.__posts):
            newIndex = 0

        self.__setPostIndex(newIndex)
        QTimer.singleShot(1000, self.__showNextPost)

    def startSlideShow(self):
        self.__setPostIndex(0)
        self.__showNextPost()



if __name__ == '__main__':
    # Create the application instance.
    app = QApplication(sys.argv)

    photoFrame = xPhotoFame()
    photoFrame.setupAsInstagramFeed()
    photoFrame.show()
    photoFrame.startSlideShow()

    sys.exit(app.exec_())