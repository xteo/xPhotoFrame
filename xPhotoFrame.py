import sys

from PyQt5.QtCore import QUrl, QTimer

from PyQt5.QtQuick import QQuickView, QQuickItem
from PyQt5.QtWidgets import QApplication

from instagramClient import instagramClient

#from facebookClient import facebookClient

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
        self.__engine.addImageProvider(self.__instagramProvider.urlHandle(), self.__instagramProvider)

        self.__instagramUserProvider = photoProvider.instagramUserProvider()
        self.__engine.addImageProvider(self.__instagramUserProvider.urlHandle(), self.__instagramUserProvider)

        """
        self.__facebookClient = facebookClient()
        profile = self.__facebookClient.graph.get_object("me")
        posts = self.__facebookClient.graph.get_connections(profile['id'], 'posts')
        for aPost in posts['data']:
            print(aPost.keys())
            if 'picture' in aPost:
                print(aPost['likes'])
        """
        self.setSource(QUrl('./xPhotoFrame.ui.qml'))

    def setupAsInstagramFeed(self, mode="xteo"):
        self.__posts = []
        recent_media = []
        if mode == "xteo":
            recent_media, next_ = self.__instagramClient.api.user_recent_media()
        elif mode == "feed":
            recent_media, next_ = self.__instagramClient.api.user_media_feed()
        elif mode == "popular":
            recent_media, next_ = self.__instagramClient.api.media_popular()

        for aMedia in recent_media:
            self.__posts.append(post.instagramPost(aMedia))

        self.__instagramProvider.setPosts(self.__posts)
        self.__instagramUserProvider.setPosts(self.__posts)
        self.__currentPhotoProvider = self.__instagramProvider

    def __setPostIndex(self, index):
        self.__currentPostIndex = index

        post = self.__posts[index]

        self.__context.setContextProperty("imageUrl", post.getImageHandle(index) )

        self.__context.setContextProperty("likesText", post.getLikesCount())
        self.__context.setContextProperty("commentText", post.getCaption())
        self.__context.setContextProperty("locationText", post.getLocation())
        self.__context.setContextProperty("dateText", post.getDate())
        self.__context.setContextProperty("userNameText", post.getUserName())

        self.__context.setContextProperty("userLogoImg", post.getImageUserHandle(index))


    def __showNextPost(self):
        newIndex = self.__currentPostIndex+1
        if newIndex >= len(self.__posts):
            newIndex = 0

        self.__setPostIndex(newIndex)
        QTimer.singleShot(1000, self.__showNextPost)

    def startSlideShow(self):
        self.__currentPostIndex = -1
        self.__showNextPost()

if __name__ == '__main__':
    # Create the application instance.
    app = QApplication(sys.argv)

    photoFrame = xPhotoFame()
    photoFrame.setupAsInstagramFeed("xteo")
    photoFrame.rootObject().setTransformOrigin(QQuickItem.Center)
    photoFrame.rootObject().setRotation(-90)
    photoFrame.rootObject().setScale(.8)
    photoFrame.rootObject().setY(-240)
    photoFrame.rootObject().setX(65)
    photoFrame.setResizeMode(QQuickView.SizeViewToRootObject)
#    photoFrame.resize(800,480)
    photoFrame.show()
    photoFrame.showFullScreen()

    photoFrame.startSlideShow()

    sys.exit(app.exec_())