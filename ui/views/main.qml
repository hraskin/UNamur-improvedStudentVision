import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Basic

ApplicationWindow {
    id: root
    visible: true
    width: 900
    height: 700
    minimumWidth: 800
    minimumHeight: height
    title: "ImprovedStudentVision"
    color: "#F4F4F4"

    FontLoader {
        id: luciole
        source: "police/Luciole-Regular.ttf"
    }

    property string fontName: luciole.name !== "" ? luciole.name : "sans-serif"

    Rectangle {
        anchors.fill: parent
        color: "#F4F4F4"

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 30
            spacing: 25

            Text {
                text: "🎯 Configuration d'ImprovedStudentVision"
                font.family: root.fontName
                font.pixelSize: 34
                font.bold: true
                color: "#202020"
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                Layout.topMargin: 10
            }

            Text {
                text: "Choisissez votre type de caméra et le modèle d'analyse adapté au tableau."
                font.family: root.fontName
                font.pixelSize: 20
                color: "#444"
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                Layout.maximumWidth: 600
            }

            Rectangle {
                Layout.preferredHeight: 180
                Layout.fillWidth: true
                Layout.maximumWidth: 600
                Layout.alignment: Qt.AlignHCenter
                radius: 12
                color: "#E0E0E0"
                border.color: "#B0B0B0"
                border.width: 1

                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 20
                    spacing: 16

                    Text {
                        text: "🎥 Sélection de la caméra"
                        font.family: root.fontName
                        font.pixelSize: 24
                        font.bold: true
                        color: "#222"
                        Layout.alignment: Qt.AlignHCenter
                    }

                    RowLayout {
                        spacing: 40
                        Layout.alignment: Qt.AlignHCenter

                        Button {
                            id: indexCameraBtn
                            text: "Caméra par index"
                            font.family: root.fontName
                            font.pixelSize: 18
                            background: Rectangle {
                                implicitWidth: 240
                                implicitHeight: 60
                                radius: 12
                                color: indexCameraBtn.down ? "#B39DDB" : "#D1C4E9"
                                border.color: "#7E57C2"
                                border.width: 2
                            }
                            onClicked: backend.want_index_camera()

                            MouseArea {
                                anchors.fill: parent
                                cursorShape: Qt.PointingHandCursor
                                enabled: true
                                onPressed: mouse.accepted = false
                            }
                        }

                        Button {
                            id: flowCameraBtn
                            text: "Caméra par flux"
                            font.family: root.fontName
                            font.pixelSize: 18
                            background: Rectangle {
                                implicitWidth: 240
                                implicitHeight: 60
                                radius: 12
                                color: flowCameraBtn.down ? "#80CBC4" : "#B2DFDB"
                                border.color: "#009688"
                                border.width: 2
                            }
                            onClicked: backend.want_flow_camera()

                            MouseArea {
                                anchors.fill: parent
                                cursorShape: Qt.PointingHandCursor
                                enabled: true
                                onPressed: mouse.accepted = false
                            }
                        }
                    }
                }
            }

            Rectangle {
                Layout.preferredHeight: 150
                Layout.fillWidth: true
                Layout.maximumWidth: 600
                Layout.alignment: Qt.AlignHCenter
                radius: 12
                color: "#E0E0E0"
                border.color: "#B0B0B0"
                border.width: 1

                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 20
                    spacing: 16

                    Text {
                        text: "🧠 Sélection du modèle d'analyse"
                        font.family: root.fontName
                        font.pixelSize: 24
                        font.bold: true
                        color: "#222"
                        Layout.alignment: Qt.AlignHCenter
                    }

                    ComboBox {
                        id: modelSelector
                        Layout.alignment: Qt.AlignHCenter
                        Layout.preferredWidth: 300
                        font.family: root.fontName
                        font.pixelSize: 18
                        model: [
                            "Reconnaissance de chiffres",
                            "Reconnaissance de lettres",
                            "Reconnaissance de symboles"
                        ]
                        onActivated: {
                            console.log("Modèle sélectionné :", modelSelector.currentText)
                            backend.set_analysis_model(modelSelector.currentIndex)
                        }

                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.PointingHandCursor
                            enabled: true
                            onPressed: mouse.accepted = false
                        }
                    }
                }
            }

            Button {
                id: startButton
                text: "Lancer l'analyse"
                font.family: root.fontName
                font.pixelSize: 20
                Layout.alignment: Qt.AlignHCenter
                Layout.preferredWidth: 300
                Layout.preferredHeight: 60
                background: Rectangle {
                    radius: 12
                    color: startButton.down ? "#81C784" : "#A5D6A7"
                    border.color: "#388E3C"
                    border.width: 2
                }
                onClicked: backend.start_analysis()

                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    enabled: true
                    onPressed: mouse.accepted = false
                }
            }

            Text {
                text: "© 2025 ImprovedStudentVision — Accessibilité avant tout"
                font.family: root.fontName
                font.pixelSize: 14
                color: "#777"
                horizontalAlignment: Text.AlignHCenter
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                Layout.bottomMargin: 10
                Layout.topMargin: 20
            }
        }
    }

    onClosing: backend.stop_application()
}