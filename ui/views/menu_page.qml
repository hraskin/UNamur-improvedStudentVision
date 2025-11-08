import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Basic

Rectangle {
    id: menu
    anchors.fill: parent
    color: "#F4F4F4"

    property string selectedType: ""
    property var cameraList: []

    Connections {
        target: backend
        function onCameraListReady(cameras) {
            menu.cameraList = cameras
        }
    }

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
            Layout.preferredHeight: 220
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
                            color: menu.selectedType === "index" ? "#B39DDB" : "#D1C4E9"
                            border.color: "#7E57C2"
                            border.width: 2
                        }

                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.PointingHandCursor
                            enabled: true
                            onClicked: {
                                menu.selectedType = "index"
                                backend.want_camera("index")
                            }
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
                            color: menu.selectedType === "flow" ? "#80CBC4" : "#B2DFDB"
                            border.color: "#009688"
                            border.width: 2
                        }

                        MouseArea {
                            anchors.fill: parent
                            cursorShape: Qt.PointingHandCursor
                            enabled: true
                            onClicked: {
                                menu.selectedType = "flow"
                                backend.want_camera("flow")
                            }
                        }
                    }
                }

                Loader {
                    id: cameraLoader
                    Layout.alignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                    sourceComponent: menu.selectedType === "index" ? indexSelector :
                                     (menu.selectedType === "flow" ? flowInput : undefined)
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
                        backend.set_analysis_model(modelSelector.currentIndex)
                    }

                    MouseArea {
                        anchors.fill: parent
                        cursorShape: Qt.PointingHandCursor
                        enabled: true
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

            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor
                enabled: true

                onClicked: {
                    if (menu.selectedType === "flow") {
                        if (!cameraLoader.item.acceptableInput || cameraLoader.item.text.length === 0) {
                            cameraLoader.item.showError = true
                            cameraLoader.item.forceActiveFocus()
                            return
                        }
                        backend.start_analysis(cameraLoader.item.text)
                    }
                    else if (menu.selectedType === "index") {
                        if (cameraLoader.item.currentIndex < 0) {
                            return
                        }
                        backend.start_analysis(cameraLoader.item.currentIndex)
                    }
                    else {
                        return
                    }
                }
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

    Component {
        id: indexSelector
        ComboBox {
            id: cameraDropdown
            Layout.preferredWidth: 300
            model: menu.cameraList
            font.family: root.fontName
            font.pixelSize: 18
        }
    }

    Component {
        id: flowInput
        TextField {
            id: ipField
            Layout.preferredWidth: 300
            font.family: root.fontName
            font.pixelSize: 18
            placeholderText: "Entrez l'adresse IP du flux"
            inputMethodHints: Qt.ImhPreferNumbers

            property bool showError: false

            validator: RegularExpressionValidator {
                regularExpression: /^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$/
            }

            Rectangle {
                anchors.fill: parent
                color: "transparent"
                border.width: 2
                 border.color: (ipField.showError && (!ipField.acceptableInput || ipField.text.length === 0))
                          ? "#E53935"
                          : "transparent"
                z: 1
            }
        }
    }
}