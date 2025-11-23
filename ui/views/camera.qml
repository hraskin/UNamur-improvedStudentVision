import QtQuick
import QtQuick.Controls

Rectangle {
    id: camView
    anchors.fill: parent
    color: "black"

    Connections {
        target: backend
        function onFrameUpdated() {
            cameraFeed.source = "image://camera/live?" + Date.now()
        }
    }

    Image {
            id: cameraFeed
            anchors.fill: parent
            fillMode: Image.PreserveAspectFit
            source: "image://camera/live"
        

        MouseArea {
            anchors.fill: parent
            onClicked: {
                backend.zoom(mouseX, mouseY)
            }
        }
    }

    

    Button {
        id: backBtn
        text: "⬅ Retour"
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.margins: 20
        onClicked: backend.return_to_menu()
    }

    Button {
        id: screen
        text: "screen"
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.margins: 40
        onClicked: backend.screen()
    }

    
    Slider {
        id: slider
        value: 1
        from: 0
        to: 10
        anchors.bottom: camView.bottom
        anchors.horizontalCenter: camView.horizontalCenter

        background: Rectangle {
            x: slider.leftPadding
            y: slider.topPadding + slider.availableHeight / 2 - height / 2
            implicitWidth: 200
            implicitHeight: 4
            width: slider.availableWidth
            height: implicitHeight
            radius: 2
            color: "#bdbebf"

            Rectangle {
                width: slider.visualPosition * parent.width
                height: parent.height
                color: "#21be2b"
                radius: 2
            }
        }

        handle: Rectangle {
            x: slider.leftPadding + slider.visualPosition * (slider.availableWidth - width)
            y: slider.topPadding + slider.availableHeight / 2 - height / 2
            implicitWidth: 26
            implicitHeight: 26
            radius: 13
            color: slider.pressed ? "#f0f0f0" : "#f6f6f6"
            border.color: "#bdbebf"
        }

        onMoved: {
            backend.set_zoom(slider.value)
        }

    }
}
