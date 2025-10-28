import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root
    visible: true
    visibility: Window.Maximized
    title: "ImprovedStudentVision"
    color: "#F4F4F4"

    FontLoader {
        id: luciole
        source: "police/Luciole-Regular.ttf"
        onStatusChanged: {
            console.log("Luciole status:", status, "font name:", name)
            if (status === FontLoader.Error)
                console.warn("Impossible de charger Luciole")
        }
    }

Rectangle {
        anchors.fill: parent
        color: "#F4F4F4"

        ColumnLayout {
            anchors.centerIn: parent
            spacing: 32
            width: parent.width * 0.7

            Text {
                text: "Bienvenue dans ImprovedStudentVision"
                font.family: luciole.name
                font.pixelSize: 36
                font.bold: true
                color: "#202020"
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                Layout.alignment: Qt.AlignHCenter
            }

            Text {
                text: "Cette application aide à améliorer la lisibilité. Sélectionnez une caméra pour commencer."
                font.family: luciole.name
                font.pixelSize: 22
                color: "#444"
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                Layout.alignment: Qt.AlignHCenter
            }

            Rectangle {
                width: parent.width
                radius: 12
                color: "#E0E0E0"
                border.color: "#B0B0B0"
                border.width: 1
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                height: 200

                ColumnLayout {
                    anchors.centerIn: parent
                    spacing: 20

                    Text {
                        text: "Choisissez la caméra"
                        font.family: luciole.name
                        font.bold: true
                        font.pixelSize: 24
                        color: "#222"
                        Layout.alignment: Qt.AlignHCenter
                    }

                    RowLayout {
                        spacing: 40
                        Layout.alignment: Qt.AlignHCenter

                        Button {
                            text: "Caméra par index"
                            font.family: luciole.name
                            font.pixelSize: 20
                            background: Rectangle {
                                implicitWidth: 240
                                implicitHeight: 60
                                radius: 12
                                color: control.down ? "#B39DDB" : "#D1C4E9"
                                border.color: "#7E57C2"
                                border.width: 2
                            }
                            onClicked: backend.want_index_camera()
                        }

                        Button {
                            text: "Caméra par flux"
                            font.family: luciole.name
                            font.pixelSize: 20
                            background: Rectangle {
                                implicitWidth: 240
                                implicitHeight: 60
                                radius: 12
                                color: control.down ? "#80CBC4" : "#B2DFDB"
                                border.color: "#009688"
                                border.width: 2
                            }
                            onClicked: backend.want_flow_camera()
                        }
                    }
                }
            }

            Text {
                text: "© 2025 ImprovedStudentVision : Accessibilité avant tout by Mallory Bouchard, Robin Delvaux, Simon Karler and Hugo Raskin "
                font.family: luciole.name
                font.pixelSize: 16
                color: "#666"
                horizontalAlignment: Text.AlignHCenter
                Layout.alignment: Qt.AlignHCenter
            }
        }
    }

    onClosing: {
        backend.stop_application()
    }
}