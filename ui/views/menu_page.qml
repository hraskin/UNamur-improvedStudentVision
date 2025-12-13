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
            text: "Configuration d'ImprovedBoardVision"
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
            font.pixelSize: 24
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
                    text: "Sélection de la caméra"
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
                        font.pixelSize: 24
                        contentItem: Text {
                            text: flowCameraBtn.text
                            font: flowCameraBtn.font
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            color: "#FFFFFF"
                        }
                        background: Rectangle {
                            implicitWidth: 240
                            implicitHeight: 60
                            radius: 12
                            color: menu.selectedType === "index" ? "#2962FF" : "#2E2E2E"
                            border.color: "#ff0000"
                            border.width: 3
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
                        contentItem: Text {
                            text: flowCameraBtn.text
                            font: flowCameraBtn.font
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            color: "#FFFFFF"
                        }
                        font.family: root.fontName
                        font.pixelSize: 24
                        background: Rectangle {
                            implicitWidth: 240
                            implicitHeight: 60
                            radius: 12
                            color: menu.selectedType === "flow" ? "#2962FF" : "#2E2E2E"
                            border.color: "#ff0000"
                            border.width: 3
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
                    text: "Sélection du modèle d'analyse"
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
                    font.pixelSize: 24
                    model: [
                        "Zoom",
                        "Edge",
                        "Zoom + edge"
                    ]

                    onActivated: {
                            if (currentIndex === 0) {//Zoom
                                backend.zoom_on(true)
                                backend.edge_on(false)
                            }
                            else if (currentIndex === 1) {// Edge
                                backend.zoom_on(false)
                                backend.edge_on(true)
                            }
                            else if (currentIndex === 2) {// Zoom + Edge
                                backend.zoom_on(true)
                                backend.edge_on(true)
                            }

                    }

                    background: Rectangle {
                        implicitHeight: 40
                        color: "#FFFFFF"
                        border.color: modelSelector.activeFocus ? "#ff0000" : "#B0B0B0"
                        border.width: 2
                        radius: 8
                    }

                    contentItem: Text {
                        text: modelSelector.displayText
                        font: modelSelector.font
                        color: "#333333"
                        verticalAlignment: Text.AlignVCenter
                        leftPadding: 10
                        rightPadding: 10
                    }

                    indicator: Canvas {
                        x: modelSelector.width - width - 10
                        y: modelSelector.topPadding + (modelSelector.availableHeight - height) / 2
                        width: 12
                        height: 8
                        contextType: "2d"

                        onPaint: {
                            context.reset();
                            context.moveTo(0, 0);
                            context.lineTo(width, 0);
                            context.lineTo(width / 2, height);
                            context.closePath();
                            context.fillStyle = "#333333";
                            context.fill();
                        }
                    }

                    popup: Popup {
                        y: modelSelector.height
                        width: modelSelector.width
                        implicitHeight: contentItem.implicitHeight
                        padding: 1

                        background: Rectangle {
                            color: "#FFFFFF"
                            border.color: "#B0B0B0"
                            border.width: 2
                            radius: 8
                        }

                        contentItem: ListView {
                            clip: true
                            implicitHeight: contentHeight
                            model: modelSelector.popup.visible ? modelSelector.delegateModel : null
                            currentIndex: modelSelector.highlightedIndex

                            delegate: ItemDelegate {
                                width: modelSelector.width
                                height: 40

                                contentItem: Text {
                                    text: modelData
                                    color: "#333333"
                                    font: modelSelector.font
                                    verticalAlignment: Text.AlignVCenter
                                    leftPadding: 10
                                }

                                background: Rectangle {
                                    color: highlighted ? "#E8E8E8" : (index % 2 === 0 ? "#E0E0E0E0" : "#FFFFFF")
                                }
                            }

                            ScrollIndicator.vertical: ScrollIndicator {
                                active: true
                                background: Rectangle {
                                    color: "#F0F0F0"
                                    radius: 4
                                }
                                contentItem: Rectangle {
                                    color: "#C0C0C0"
                                    radius: 4
                                }
                            }
                        }
                    }
                }
            }
        }

       Button {
            id: startButton
            text: "Lancer l'analyse"
            font.family: root.fontName
            font.pixelSize: 24
            hoverEnabled: true

            Layout.alignment: Qt.AlignHCenter
            Layout.preferredWidth: 300
            Layout.preferredHeight: 60

            contentItem: Text {
                text: startButton.text
                font: startButton.font

                color: startButton.hovered ? "white" :
                       "black"

                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
                radius: 12
                border.width: 3
                border.color: "#ff0000"

                color: startButton.hovered ? "black" : "white"
            }





            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onClicked: {
                    if (menu.selectedType !== "flow") {
                        menu.selectedType = "flow"
                        backend.want_camera("flow")
                    }
                }
            }
            MouseArea {
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

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
                }
            }

        }

        Text {
            text: "© 2025 ImprovedBoardVision - Accessibilité avant tout"
            font.family: root.fontName
            font.pixelSize: 18
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
            font.pixelSize: 24

            background: Rectangle {
                implicitHeight: 40
                color: "#FFFFFF"
                border.color: cameraDropdown.activeFocus ? "#ff0000" : "#B0B0B0"
                border.width: 2
                radius: 8

            }

            contentItem: Text {
                text: cameraDropdown.displayText
                font.pixelSize: 24
                font.family: root.fontName
                color: "#333333"
                verticalAlignment: Text.AlignVCenter
                leftPadding: 10
                rightPadding: 10
            }

            indicator: Canvas {
                x: cameraDropdown.width - width - 10
                y: cameraDropdown.topPadding + (cameraDropdown.availableHeight - height) / 2
                width: 12
                height: 8
                contextType: "2d"

                onPaint: {
                    context.reset();
                    context.moveTo(0, 0);
                    context.lineTo(width, 0);
                    context.lineTo(width / 2, height);
                    context.closePath();
                    context.fillStyle = "#333333";
                    context.fill();
                }
            }

            popup: Popup {
                y: cameraDropdown.height
                width: cameraDropdown.width
                implicitHeight: contentItem.implicitHeight
                padding: 1

                background: Rectangle {
                    color: "#FFFFFF"
                    border.color: "#B0B0B0"
                    border.width: 2
                    radius: 8
                }

                contentItem: ListView {
                    clip: true
                    implicitHeight: contentHeight
                    model: cameraDropdown.popup.visible ? cameraDropdown.delegateModel : null
                    currentIndex: cameraDropdown.highlightedIndex

                    delegate: ItemDelegate {
                        width: cameraDropdown.width
                        height: 40

                        contentItem: Text {
                            text: modelData
                            color: "#333333"
                            font: cameraDropdown.font
                            verticalAlignment: Text.AlignVCenter
                            leftPadding: 10
                        }

                        background: Rectangle {
                            color: highlighted ? "#E8E8E8" : "transparent"
                        }
                    }

                    ScrollIndicator.vertical: ScrollIndicator {
                        active: true
                        background: Rectangle {
                            color: "#F0F0F0"
                            radius: 4
                        }
                        contentItem: Rectangle {
                            color: "#C0C0C0"
                            radius: 4
                        }
                    }
                }
            }
        }
    }

    Component {
        id: flowInput
        TextField {
            id: ipField
            Layout.preferredWidth: 300
            font.family: root.fontName
            font.pixelSize: 24
            placeholderText: "Entrez l'adresse IP du flux"
            placeholderTextColor: "#333333"
            color: "#333333"
            inputMethodHints: Qt.ImhPreferNumbers

            property bool showError: false

            background: Rectangle {
                implicitHeight: 40
                color: "#FFFFFF"
                border.color: {
                    if (ipField.showError && (!ipField.acceptableInput || ipField.text.length === 0))
                        return "#E53935"
                    else if (ipField.activeFocus)
                        return "#ff0000"
                    else
                        return "#B0B0B0"
                }
                border.width: 2
                radius: 8
            }

            validator: RegularExpressionValidator {
                regularExpression: /^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$/
            }
        }
    }
}