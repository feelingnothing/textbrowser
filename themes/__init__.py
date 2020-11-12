from PyQt5.QtCore import QFile, QTextStream


def getTheme(theme: str):
    file = QFile(f":/{theme}.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    return stream.readAll()
