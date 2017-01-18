import QtQuick 2.6

Rectangle {

    width: 640
    height: 960
    color: "#f2f2f2"

    MouseArea {
        id: mouseArea
        y: 0
        enabled: true

        Rectangle {
            id: imageBg
            x: 0
            y: 62
            width: 640
            height: 640
            color: "#ffffff"
            border.width: 0
        }

        Image {
            id: mainImage
            x: 0
            y: 62
            width: 640
            height: 640
            fillMode: Image.PreserveAspectFit
            source: imageUrl
        }

        Rectangle {
            id: rectangle1
            x: 0
            y: 700
            width: 640
            height: 21
            color: "#ffffff"
        }

        Row {
            id: commentRow
            x: 8
            y: 704
            width: 624
            height: 134
            antialiasing: false
            spacing: 4

            Text {
                id: likesValue
                text: likesText
                font.pixelSize: 12
            }

            Text {
                id: likes
                text: qsTr("Likes")
                font.pixelSize: 12
            }

            Text {
                id: dateValue
                width: 200
                text: dateText
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 12
            }

            Text {
                id: locationValue
                x: 80
                width: 200
                text: locationText
                leftPadding: 0
                horizontalAlignment: Text.AlignRight
                font.pixelSize: 12
            }
        }

        Rectangle {
            id: rectangle
            x: 0
            y: 853
            width: 640
            height: 125
            color: "#383839"

            Text {
                id: sign
                x: 232
                y: 10
                width: 186
                height: 40
                color: "#ffffff"
                text: qsTr("Photo Frame by xTeo")
                font.capitalization: Font.AllUppercase
                font.family: "Times New Roman"
                horizontalAlignment: Text.AlignHCenter
                font.pixelSize: 19
            }
        }

        Text {
            id: commentValue
            x: 8
            y: 727
            width: 624
            height: 120
            text: commentText
            font.family: "Tahoma"
            wrapMode: Text.WordWrap
            font.pixelSize: 18
        }
    }

    Row {
        id: row
        x: 10
        width: 630
        height: 62
        transformOrigin: Item.Center
        spacing: 6

        Image {
            id: userLogo
            y: 5
            width: 50
            height: 50
            source: userLogoImg

            Image {
                id: userMask
                x: 0
                y: 0
                width: 50
                height: 50
                clip: true
                source: "userMask.png"
            }
        }

        Text {
            id: userName
            y: 20
            width: 200
            text: userNameText
            verticalAlignment: Text.AlignVCenter
            font.weight: Font.Light
            font.family: "Courier"
            font.pixelSize: 19
        }
    }
}
