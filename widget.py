#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 SRE

import os
import sys

sys.dont_write_bytecode = True  # noqa: E402
sys.path.insert(0, os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..')))  # noqa: E402

from PySide6.QtUiTools import loadUiType

from PySide6.QtCore import (
     QCoreApplication,
     Signal,
     Slot,
     Qt
     )

from PySide6.QtWidgets import (
     QApplication
     )

UIFilename = "form.ui"
Form, Base = loadUiType(os.path.join(sys.path[1], UIFilename))

def check_str(string, base):
    characters = "0123456789ABCDEF"
    characters = characters[:base]
    string = string.upper()
    out = ""

    for char in string:
        if char != ' ' and char in characters:
            out += char
        else:
            return None

    return out

class Widget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.in_base = 10
        self.out_base = 10
        self.prefix = ""

    @Slot()
    def on_btnFormatieren_clicked(self):

        res = check_str(self.txtEinZahl.toPlainText(), self.in_base)

        if res == None:
            print("Fehler")
            return

        res = int(self.prefix + res, 0)

        if self.out_base == 2:    res = bin(res)[2:]
        elif self.out_base == 8:  res = oct(res)[2:]
        elif self.out_base == 10: res = str(res)
        elif self.out_base == 16: res = hex(res)[2:]

        self.txtAusZahl.setText(res)

    @Slot()
    def on_btnLeer_clicked(self):
        self.txtEinZahl.setText("")


    ####### Change the input base #######

    @Slot()
    def on_optBinE_clicked(self):
        self.in_base = 2
        self.prefix = "0b"
        self.on_btnFormatieren_clicked()

    @Slot()
    def on_optDezE_clicked(self):
        self.in_base = 10
        self.prefix = ""
        self.on_btnFormatieren_clicked()

    @Slot()
    def on_optHexE_clicked(self):
        self.in_base = 16
        self.prefix = "0x"
        self.on_btnFormatieren_clicked()

    @Slot()
    def on_optOctE_clicked(self):
        self.in_base = 8
        self.prefix = "0o"
        self.on_btnFormatieren_clicked()


    ####### Change the output base #######

    @Slot()
    def on_optBinA_clicked(self):
        self.out_base = 2
        self.on_btnFormatieren_clicked()

    @Slot()
    def on_optDezA_clicked(self):
        self.out_base = 10
        self.on_btnFormatieren_clicked()

    @Slot()
    def on_optHexA_clicked(self):
        self.out_base = 16
        self.on_btnFormatieren_clicked()

    @Slot()
    def on_optOctA_clicked(self):
        self.out_base = 8
        self.on_btnFormatieren_clicked()



if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    os.chdir(sys.path[1])
    widget = Widget()
    widget.show()

    sys.exit(app.exec())
