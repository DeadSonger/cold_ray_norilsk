import os
from PyQt5 import QtWidgets, QtGui, QtCore

import cold_ray_norilsk.src.application.locs.languages as languages

from cold_ray_norilsk.src.application.design import Design


QtCore.QCoreApplication.setOrganizationName("bestgameeveruveseen")
QtCore.QCoreApplication.setOrganizationDomain("bestgameeveruveseen.org")
QtCore.QCoreApplication.setApplicationName("Cold Ray Norilsk")


class MyApp(QtWidgets.QMainWindow, Design):
    """MyApp is the main class for handling and displaying the UI."""

    def __init__(self):
        """Initialize the application.

        We setup all the needed ui in this method, then set locale, retranslate all the texts
        to this locale, and connect callbacks to slots
        """
        super().__init__()
        self.resize(640, 480)
        self.setup_ui(self)
        self.set_default_locale()
        self.retranslate_ui()
        self.connect_callbacks()

        self.setWindowTitle("Game")
        self.setWindowIcon(QtGui.QIcon(":icon.png"))

    def connect_callbacks(self):
        """Connect callbacks to slots."""
        self.settings_button.clicked.connect(self.setup_settings)
        self.back_button.clicked.connect(self.setup_main)
        self.exit_button.clicked.connect(self.exit)
        self.language_switch.currentIndexChanged.connect(self.change_func)

    def changeEvent(self, event):
        """Retranslate UI if application language changes.

        Overriden method that will call retranslate texts if
        the event QtCore.QEvent.LanguageChange occurs.

        :param event: happened event
        :return: None
        """
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslate_ui()
        super().changeEvent(event)

    def exit(self):
        self.close()

    def retranslate_ui(self):
        """Retranslate all the ui texts.

        All the texts of each element has to be set here
        """
        self.start_button.setText(QtWidgets.QApplication.translate("Design", "Start"))
        self.settings_button.setText(QtWidgets.QApplication.translate("Design", "Settings"))
        self.exit_button.setText(QtWidgets.QApplication.translate("Design", "Suicide"))
        self.back_button.setText(QtWidgets.QApplication.translate("Design", "Back"))

    def set_default_locale(self):
        """Determine user LANG according to LANG environment variable."""
        if os.environ.get("LANG"):
            prefix = os.environ.get("LANG").split("_")[0]
            if prefix in languages.codes and prefix != "en":
                self.language_switch.setCurrentIndex(languages.codes.index(prefix))
                self.change_func(languages.codes.index(prefix))
        else:
            self.language_switch.setCurrentIndex(languages.codes.index("en"))
            self.change_func(languages.codes.index("en"))


def start_application():
    app = QtWidgets.QApplication([])
    win = MyApp()
    win.show()
    app.exec()
