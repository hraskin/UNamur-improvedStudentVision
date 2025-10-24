import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    visible: true
    width: 400
    height: 200
    minimumWidth: width
    minimumHeight: height
    maximumWidth: width
    maximumHeight: height
    title: "Main Window"

    Rectangle {
        anchors.fill: parent
        color: "#031D38"

        ColumnLayout {
            anchors.centerIn: parent
            spacing: 20
            width: parent.width * 0.9

            Text {
                text: "Test"
                color: "#FCFCFC"
                font.pixelSize: 16
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                Layout.alignment: Qt.AlignHCenter
            }

        }
    }
}