import sys

import PyQt5.uic
from PyQt5.QtWidgets import QWidget, QApplication


class LAUNCHER(QWidget):
    def __init__(self):
        super(LAUNCHER, self).__init__()
        self.app = QApplication(sys.argv)
        self.ui = PyQt5.uic.loadUi(r'E:\Anaconda\envs\launcher\main\launcher.ui')
        self.acceptDrops()

        self.ui.pushButton.clicked.connect(self.getLauncher)
        self.ui.show()
        self.app.exec()

    def getLauncher(self):
        getDropText: str = self.ui.textEdit.toPlainText()
        split = getDropText.split('file:///')
        del split[0]
        for item in split:
            if item.endswith('.py'):
                filePath = item[:-3]
                pyFullName = filePath + '.py'

                # write .bar
                batFullName = filePath + '.bat'
                batData = '''@echo off
python {}
pause'''.format(pyFullName)
                with open(batFullName, 'w') as file:
                    file.write(batData)

                # write .vbe
                vbeFullName = filePath + '.vbe'
                vbData = '''set ws=wscript.createobject("wscript.shell") 
ws.run "{} /start",0'''.format(batFullName)
                with open(vbeFullName, 'w') as vb:
                    vb.write(vbData)


app = QApplication(sys.argv)
myWin = LAUNCHER()
