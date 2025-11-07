import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root
    visible: true
    width: 800
    height: 600
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
            anchors.centerIn: parent
            spacing: 32
            width: parent.width * 0.7

            Text {
                text: "🎯 Configuration d'ImprovedStudentVision"
                font.family: root.fontName
                font.pixelSize: 34
                font.bold: true
                color: "#202020"
                horizontalAlignment: Text.AlignHCenter
                wrapMode: Text.WordWrap
                Layout.alignment: Qt.AlignHCenter
            }

            Text {
                text: "Choisissez votre type de caméra et le modèle d'analyse adapté au tableau."
                font.family: root.fontName
                font.pixelSize: 20
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
                height: 180

                ColumnLayout {
                    anchors.centerIn: parent
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
                            text: "Caméra par index"
                            font.family: root.fontName
                            font.pixelSize: 18
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
                            font.family: root.fontName
                            font.pixelSize: 18
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

            Rectangle {
                width: parent.width
                radius: 12
                color: "#E0E0E0"
                border.color: "#B0B0B0"
                border.width: 1
                Layout.alignment: Qt.AlignHCenter
                Layout.fillWidth: true
                height: 150

                ColumnLayout {
                    anchors.centerIn: parent
                    spacing: 16

                    Text {
                        text: " Sélection du modèle d'analyse"
                        font.family: root.fontName
                        font.pixelSize: 24
                        font.bold: true
                        color: "#222"
                        Layout.alignment: Qt.AlignHCenter
                    }

                    ComboBox {
                        id: modelSelector
                        Layout.alignment: Qt.AlignHCenter
                        width: 300
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
                    }
                }
            }

            Button {
                text: "Lancer l'analyse"
                font.family: root.fontName
                font.pixelSize: 20
                Layout.alignment: Qt.AlignHCenter
                background: Rectangle {
                    implicitWidth: 300
                    implicitHeight: 60
                    radius: 12
                    color: control.down ? "#81C784" : "#A5D6A7"
                    border.color: "#388E3C"
                    border.width: 2
                }
                onClicked: backend.start_analysis()
            }

            Text {
                text: "© 2025 ImprovedStudentVision — Accessibilité avant tout"
                font.family: root.fontName
                font.pixelSize: 14
                color: "#777"
                horizontalAlignment: Text.AlignHCenter
                Layout.alignment: Qt.AlignHCenter
            }
        }
    }

    onClosing: backend.stop_application()
}
