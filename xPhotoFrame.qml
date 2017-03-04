import QtQuick 2.6

Rectangle {
    id: rootFrame

    width: 768
    height: 1024
    color: "#f2f2f2"
    scale: 1
    transformOrigin: Item.Center
    rotation: 0

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        enabled: true

        onClicked: {
            Qt.quit();
        }

        Rectangle {
            id: imageBg
            x: 0
            y: 0
            width: 768
            height: 1024
            color: "#000000"
            border.width: 0
        }

        Image {
            id: mainImage
            x: 0
            y: 50
            width: 768
            height: 813
            fillMode: Image.PreserveAspectCrop
            source: imageUrl
        }

        Text {
            id: dateValue
            x: 483
            y: 8
            width: 277
            height: 36
            color: "#ffffff"
            text: dateText
            horizontalAlignment: Text.AlignRight
            font.pixelSize: 30
        }

        Text {
            id: locationValue1
            x: 8
            y: 8
            width: 474
            height: 36
            color: "#ffffff"
            text: locationText
            horizontalAlignment: Text.AlignLeft
            leftPadding: 0
            font.pixelSize: 30
        }

        Text {
            id: commentValue
            x: 8
            y: 869
            width: 752
            height: 232
            color: "#ffffff"
            text: commentText
            font.family: "Tahoma"
            wrapMode: Text.WordWrap
            font.pixelSize: 25
        }


    }
}
