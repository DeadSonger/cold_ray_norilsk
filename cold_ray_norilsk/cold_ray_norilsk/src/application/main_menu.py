from PyQt5 import QtWidgets, QtGui, QtCore
import cold_ray_norilsk.src.application.resources

from cold_ray_norilsk.src.application.design import Design


QtCore.QCoreApplication.setOrganizationName("bestgameeveruveseen")
QtCore.QCoreApplication.setOrganizationDomain("bestgameeveruveseen.org")
QtCore.QCoreApplication.setApplicationName("Cold Ray Norilsk")


class MyApp(QtWidgets.QMainWindow, Design):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setup_ui(self)
        self.retranslate_ui()
        self.connect_callbacks()

        self.setWindowTitle("Game")
        self.setWindowIcon(QtGui.QIcon(":icon.png"))

    def connect_callbacks(self):
        self.settings_button.clicked.connect(self.setup_settings)
        self.back_button.clicked.connect(self.setup_main)
        self.exit_button.clicked.connect(self.exit)
        self.language_switch.currentIndexChanged.connect(self.change_func)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslate_ui()
        super().changeEvent(event)

    def exit(self):
        self.close()

    def retranslate_ui(self):
        self.start_button.setText(QtWidgets.QApplication.translate("Design", "Start"))
        self.settings_button.setText(QtWidgets.QApplication.translate("Design", "Settings"))
        self.exit_button.setText(QtWidgets.QApplication.translate("Design", "Suicide"))
        self.back_button.setText(QtWidgets.QApplication.translate("Design", "Back"))


def start_application():
    app = QtWidgets.QApplication([])
    win = MyApp()
    win.show()
    app.exec()