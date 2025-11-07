import QtQuick
import QtQuick.Controls

Rectangle {
    id: camView
    anchors.fill: parent
    color: "black"

    Image {
        id: cameraFeed
        anchors.fill: parent
        fillMode: Image.PreserveAspectFit
        source: "image://camera/live"
    }

    Connections {
        target: backend
        function onFrameUpdated() {
            cameraFeed.source = "image://camera/live?" + Date.now()
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
}
