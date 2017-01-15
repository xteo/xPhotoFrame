import QtQuick 2.6

Rectangle {

    width: 640
    height: 960
    color: "#000000"

    MouseArea {
        id: mouseArea
        y: 0
        enabled: true

        Image {
            id: mainImage
            x: 0
            y: 0
            width: 640
            height: 640
            fillMode: Image.PreserveAspectFit
            source: imageUrl
        }

        Rectangle {
            id: rectangle1
            x: 0
            y: 640
            width: 640
            height: 147
            color: "#ffffff"
        }

        Row {
            id: commentRow
            x: 8
            y: 644
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
            y: 777
            width: 640
            height: 201
            color: "#383839"

            Text {
                id: sign
                x: 241
                y: 161
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
            y: 667
            width: 624
            height: 104
            text: commentText
            wrapMode: Text.WordWrap
            font.pixelSize: 18
        }
    }
}
