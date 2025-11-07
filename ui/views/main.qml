import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Basic

ApplicationWindow {
    id: root
    visible: true
    visibility: ApplicationWindow.Maximized
    minimumWidth: 800
    minimumHeight: 700
    title: "ImprovedStudentVision"
    color: "#F4F4F4"

    FontLoader {
        id: luciole
        source: "police/Luciole-Regular.ttf"
    }

    property string fontName: luciole.name !== "" ? luciole.name : "sans-serif"
    property string currentView: "menu"
    property bool frameUpdated: false

    Loader {
        id: viewLoader
        anchors.fill: parent
        active: true
        source: currentView === "menu" ? "menu_page.qml" : "camera.qml"
    }

    onClosing: backend.stop_application()
}