from PyQt5.QtCore import Qt as _qt
from PyQt5.QtGui import QIcon as _icon
from PyQt5.QtWidgets import QWidget as _widget
from PyQt5.QtWidgets import QMainWindow as _mainwindow

from themes import getTheme
import ui.breeze_resources
from ui.ui import Ui_main as _Ui
from ui.settings import Ui_Form
from settings import ENCODINGS


class Ui(_mainwindow, _Ui):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowFlags(_qt.FramelessWindowHint)
        self._max_normal, self._moving, self._offset = False, False, False
        self.current_theme = 'dark'
        self.set_theme(self.current_theme)
        self.setupUi(self)
        self._init_gui()

    def _init_gui(self):
        file = self.menubar.addMenu('File')
        self.new_file = file.addAction('New')
        self.save_file = file.addAction('Save')
        self.open_file = file.addAction('Open')
        self.exit = file.addAction('Exit')
        preferences = self.menubar.addMenu('Preferences')
        self.settings_act = preferences.addAction('Settings')
        self.close.clicked.connect(super().close)
        self.close.setIcon(_icon('img/close.png'))
        self.hide.setIcon(_icon('img/hide.png'))
        self.hide.clicked.connect(super(Ui, self).showMinimized)
        self.minimize.clicked.connect(self._show_max_store)
        self.minimize.setIcon(_icon('img/maximize.png'))

    def set_theme(self, theme):
        self.setStyleSheet(getTheme(theme))

    def _show_max_store(self):
        if self._max_normal:
            self.showNormal()
            self._max_normal = False
            self.minimize.setIcon(_icon('img/maximize.png'))
        else:
            self.showMaximized()
            self._max_normal = True
            self.minimize.setIcon(_icon('img/minimize.png'))

    def mousePressEvent(self, event):
        if event.button() == _qt.LeftButton:
            self._moving = True
            self._offset = event.pos()

    def mouseMoveEvent(self, event):
        if self._moving:
            self.move(event.globalPos() - self._offset)


class Settings(_widget, Ui_Form):
    def __init__(self, parent):
        super(Settings, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(_qt.FramelessWindowHint)
        self.setWindowTitle('Settings')
        self._max_normal, self._moving, self._offset = False, False, False
        self._parent = parent
        self.settings = parent.settings
        self.save.clicked.connect(self._save)
        self._init_gui()

    def _show_max_store(self):
        if self._max_normal:
            self.showNormal()
            self._max_normal = False
            self.minimize.setIcon(_icon('img/maximize.png'))
        else:
            self.showMaximized()
            self._max_normal = True
            self.minimize.setIcon(_icon('img/minimize.png'))

    def set_theme(self, theme):
        self.setStyleSheet(getTheme(theme))

    def _init_gui(self):
        self.encoding.addItems(ENCODINGS)
        self.theme.addItems(['dark', 'light'])
        self.theme.setCurrentText(self.settings.theme)
        self.set_theme(self.settings.theme)
        self.close.clicked.connect(super().close)
        self.close.setIcon(_icon('img/close.png'))
        self.hide.clicked.connect(super(Settings, self).showMinimized)
        self.minimize.clicked.connect(self._show_max_store)
        self.minimize.setIcon(_icon('img/maximize.png'))
        self.hide.setIcon(_icon('img/hide.png'))

    def _save(self):
        theme = self.theme.currentText()
        encoding = self.encoding.currentText()
        self.set_theme(theme)
        self._parent.set_theme(theme)
        self.settings = self.settings._replace(theme=theme, encoding=encoding)
        if self._max_normal:
            self.minimize.setIcon(_icon('img/maximize.png'))
        else:
            self.minimize.setIcon(_icon('img/minimize.png'))

    def closeEvent(self, event):
        super(type(self._parent), self._parent).show()
        self._parent.set_theme(self.theme.currentText())
        self._parent.settings = self.settings
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == _qt.LeftButton:
            self._moving = True
            self._offset = event.pos()

    def mouseMoveEvent(self, event):
        if self._moving:
            self.move(event.globalPos() - self._offset)
