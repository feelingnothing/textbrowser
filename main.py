from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence

from collections import namedtuple
from functools import partial
from settings import BASE_DIR
from ui import Ui, Settings

import shutil
import json
import sys
import os


class Browser(Ui):
    def __init__(self):
        super(Browser, self).__init__()
        self.current_file = getattr(self, 'current_file', None)
        self.ask_file = partial(QFileDialog.getOpenFileName, self, 'Choose file', '',
                                'All files (*.*)')
        self.settings = getattr(self, 'current_file', None)
        self._init_settings()
        self.current_theme = self.settings.theme
        self.set_theme(self.current_theme)
        self._init_shortcuts()
        self._init_triggers()
        self._change_status()
        self.text.textChanged.connect(self._change_status)
        self.text.cursorPositionChanged.connect(self._change_status)

    def _change_status(self):
        c = self.text.textCursor()
        row = c.blockNumber()
        col = c.columnNumber()
        length = len(self.text.toPlainText())
        self.statusbar.showMessage(
            f"'{self.current_file.split(os.sep)[-1]}'\n{length}\t({row}:{col})", -1)

    def _init_settings(self):
        if self.settings:
            return
        path = os.path.join(BASE_DIR, 'settings.json')
        if os.path.isfile(path) and os.stat(path).st_size != 0:
            settings = json.load(open(path))
        else:
            shutil.copy(
                os.path.join(BASE_DIR, 'default_settings.json'),
                path)
            settings = json.load(open(path))
        self.settings = namedtuple('settings', settings.keys())(**settings)
        if self.settings.current_file:
            self.current_file = self.settings.current_file
            self._open_file(self.settings.current_file)

    def _init_shortcuts(self):
        save = QShortcut(QKeySequence('Ctrl+S'), self)
        save.activated.connect(self._save_file)
        new = QShortcut(QKeySequence('Ctrl+N'), self)
        new.activated.connect(self._new_file)
        open_ = QShortcut(QKeySequence('Ctrl+O'), self)
        open_.activated.connect(self._open_file)

    def _init_triggers(self):
        self.save_file.triggered.connect(self._save_file)
        self.new_file.triggered.connect(self._new_file)
        self.open_file.triggered.connect(self._open_file)
        self.settings_act.triggered.connect(self._settings)
        self.exit.triggered.connect(self._exit)
        self.closeEvent = self._exit

    def _settings(self):
        super(Browser, self).hide()
        self.m = Settings(self)
        self.m.show()

    def _exit(self, event=None):
        if self.text.toPlainText():
            self._save_file()
            data = self.settings._asdict()
            data['current_file'] = self.current_file
            with open(os.path.join(BASE_DIR, 'settings.json'), 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        if event:
            event.accept()
        else:
            super(Browser, self).close()

    def _open_file(self, path=None):
        path, _ = self.ask_file() if not path else (path, None)
        if self.current_file and not path:
            self._save_file()
        if os.path.isfile(path):
            self.current_file = path
        else:
            self.current_file = None
            return
        with open(path, 'r+', encoding=self.settings.encoding) as f:
            self.text.setText(f.read())

    def _new_file(self):
        if self.current_file:
            self._save_file()
        self.text.setText('')
        self.current_file = None

    def _save_file(self):
        if self.current_file is None:
            path, _ = self.ask_file()
            if path:
                if os.stat(path).st_size != 0:
                    answer = QMessageBox.question(self, 'This file is not empty.',
                                                  'Are you sure you want to save in this file?',
                                                  QMessageBox.Yes | QMessageBox.No)
                    if answer == QMessageBox.No:
                        return
                self.current_file = path
            else:
                return
        with open(self.current_file, 'w', encoding=self.settings.encoding) as f:
            f.write(self.text.toPlainText())


def main():
    app = QApplication(sys.argv)
    m = Browser()
    m.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
