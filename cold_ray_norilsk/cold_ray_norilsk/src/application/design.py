from PyQt5 import QtCore, QtWidgets, QtGui
import resources

from os.path import join
from cold_ray_norilsk.cold_ray_norilsk.data import styles
from cold_ray_norilsk.cold_ray_norilsk.src.application.locs import languages


class Design(object):
    def __init__(self):
        self.window = None
        self.main_widget = None
        self.m_layout = None
        self.start_button = None
        self.settings_button = None
        self.exit_button = None
        self.back_button = None
        self.v_layout = None
        self.s_layout = None
        self.main_menu = None
        self.language_switch = None
        self.settings_menu = None
        self.trans = None

    def setup_ui(self, main_window: QtWidgets.QWidget):
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.window = main_window

        self.main_widget = QtWidgets.QWidget(self.window)
        self.main_widget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.main_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_widget.setObjectName("main menu")

        self.m_layout = QtWidgets.QGridLayout(self.main_widget)

        self.main_menu = QtWidgets.QWidget(self.main_widget)
        self.main_menu.setMaximumSize(QtCore.QSize(1920, 1080))
        self.main_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_menu.setObjectName("main menu")

        self.settings_menu = QtWidgets.QWidget(self.main_widget)
        self.settings_menu.setMaximumSize(QtCore.QSize(1920, 1080))
        self.settings_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_menu.setObjectName("settings menu")

        self.m_layout.addWidget(self.main_menu)
        self.m_layout.addWidget(self.settings_menu)

        self.start_button = self.make_evil(QtWidgets.QPushButton())
        self.start_button.setSizePolicy(size_policy)
        self.settings_button = self.make_evil(QtWidgets.QPushButton())
        self.exit_button = self.make_evil(QtWidgets.QPushButton())

        self.language_switch = QtWidgets.QComboBox()
        self.language_switch.setSizePolicy(size_policy)
        options = ([(src, 'en-' + code) for src, code in zip(languages.langs, languages.codes)])
        for i, (text, lang) in enumerate(options):
            self.language_switch.addItem(text)
            if text != "english":
                self.language_switch.setItemData(i, lang)
            else:
                self.language_switch.setItemData(i, '')

        self.back_button = self.make_evil(QtWidgets.QPushButton())
        self.back_button.setSizePolicy(size_policy)

        self.v_layout = QtWidgets.QGridLayout(self.main_menu)
        self.v_layout.addItem(spacer_item, 0, 0)
        self.v_layout.addWidget(self.start_button, 1, 0)
        self.v_layout.addWidget(self.settings_button, 2, 0)
        self.v_layout.addWidget(self.exit_button, 3, 0)
        self.v_layout.addItem(spacer_item, 4, 0)

        self.s_layout = QtWidgets.QGridLayout(self.settings_menu)
        self.s_layout.addItem(spacer_item, 0, 0)
        self.s_layout.addWidget(self.language_switch, 1, 0)
        self.s_layout.addItem(spacer_item, 2, 0)
        self.s_layout.addWidget(self.back_button, 3, 0)
        self.s_layout.addItem(spacer_item, 2, 0)
        self.settings_menu.hide()

        self.trans = QtCore.QTranslator(self.main_widget)
        self.window.setCentralWidget(self.main_widget)

    def setup_settings(self):
        self.main_menu.hide()
        self.settings_menu.show()

    def setup_main(self):
        self.settings_menu.hide()
        self.main_menu.show()

    @QtCore.pyqtSlot(int)
    def change_func(self, index):
        data = self.language_switch.itemData(index)
        if data:
            self.trans.load(data, join("cold_ray_norilsk", "cold_ray_norilsk", "src", "application", "locs"))
            QtWidgets.QApplication.instance().installTranslator(self.trans)
        else:
            QtWidgets.QApplication.instance().removeTranslator(self.trans)

    @staticmethod
    def make_evil(widget: QtWidgets.QWidget):
        widget.setStyleSheet(styles.button_style)
        return widget
