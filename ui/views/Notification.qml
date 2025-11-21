import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    id: notification
    property real maxWidth: parent.width - 20
    width: Math.min(Math.max(notifText.paintedWidth + 40, parent.width / 3), maxWidth)
    height: Math.max(notifText.paintedHeight + 20, 50)
    color: "#E0E0E0"
    border.color: "#B0B0B0"
    border.width: 2
    radius: 12
    opacity: 0.95
    y: 40
    x: parent.width
    visible: false
    z: 10

    Rectangle {
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        width: 5
        color: "#7E57C2"
        radius: 2
    }

    Text {
        id: notifText
        anchors.centerIn: parent
        text: ""
        color: "#202020"
        font.pixelSize: 16
        wrapMode: Text.WordWrap
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    NumberAnimation {
        id: slideIn
        target: notification
        property: "x"
        duration: 300
        easing.type: Easing.OutCubic
    }

    Timer {
        id: hideTimer
        interval: 3000
        onTriggered: {
            slideIn.from = notification.x
            slideIn.to = notification.parent.width
            slideIn.start()
            notifText.text = ""
        }
    }

    function showMessage(msg) {
        notifText.text = msg
        notifText.forceLayout()
        width = Math.min(Math.max(notifText.paintedWidth + 40, parent.width / 3), maxWidth)
        height = Math.max(notifText.paintedHeight + 20, 50)

        x = parent.width
        visible = true
        slideIn.from = parent.width
        slideIn.to = parent.width - width
        slideIn.start()
        hideTimer.restart()
    }
}