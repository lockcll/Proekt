from PySide6 import QtCore, QtWidgets, QtGui
import random
import sys
def gomenu():
    menu = Main()
    switch.addWidget(menu)
    switch.setCurrentIndex(switch.currentIndex() + 1)
class Main(QtWidgets.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle('Игра Ним')
        start = QtWidgets.QPushButton('Начать игру', self)
        rules = QtWidgets.QPushButton('Правила', self)
        setting = QtWidgets.QPushButton('Настройки', self)
        exitgame = QtWidgets.QPushButton('Выход', self)
        zastav = QtWidgets.QLabel('  Ним', self)
        zastav.setFont(QtGui.QFont('Arial', 50))
        zastav.setFixedSize(250, 50)
        zastav.move(455, 50)
        menu = QtWidgets.QGridLayout()
        menu.addWidget(start, 1, 0)
        menu.addWidget(rules, 3, 0)
        menu.addWidget(setting, 2, 0)
        menu.addWidget(exitgame, 4, 0)
        menu.addWidget(zastav, 0, 0)
        start.setFixedSize(200, 100)
        start.setFont(QtGui.QFont('Arial', 25))
        setting.setFixedSize(200, 100)
        setting.setFont(QtGui.QFont('Arial', 25))
        exitgame.setFixedSize(200, 100)
        exitgame.setFont(QtGui.QFont('Arial', 25))
        rules.setFixedSize(200, 100)
        rules.setFont(QtGui.QFont('Arial', 25))
        exitgame.clicked.connect(sys.exit)
        self.setStyleSheet("background-color: green")
        exitgame.setStyleSheet("background-color: red; color: white")
        start.setStyleSheet("background-color: red; color: white")
        setting.setStyleSheet("background-color: red; color: white")
        rules.setStyleSheet("background-color: red; color: white")
        rules.clicked.connect(self.gorule)
        setting.clicked.connect(self.gosetting)
        start.clicked.connect(self.gogame)
        self.setLayout(menu)

    def gorule(self):
        rule = rules()
        switch.addWidget(rule)
        switch.setCurrentIndex(switch.currentIndex() + 1)

    def gogame(self):
        game = Game()
        switch.addWidget(game)
        switch.setCurrentIndex(switch.currentIndex() + 1)
    def gosetting(self):
        setting = Setting()
        switch.addWidget(setting)
        switch.setCurrentIndex(switch.currentIndex() + 1)
class Setting(QtWidgets.QWidget):
    def __init__(self):
        super(Setting, self).__init__()
        set = QtWidgets.QGridLayout()
        pr = QtWidgets.QLabel('Выбор противника')
        dif = QtWidgets.QLabel('Выбор сложности')
        xod = QtWidgets.QLabel('Первым ходит')
        self.pro = QtWidgets.QComboBox()
        self.diff = QtWidgets.QComboBox()
        self.xxod = QtWidgets.QComboBox()
        self.pro.addItems(['Компьютер', 'Игрок'])
        self.diff.addItems(['Легкая', 'Средняя', 'Сложная'])
        self.xxod.addItems(['Игрок', 'Компьютер'])
        if Setting.protiv == 0:
            self.pro.setCurrentIndex(0)
        if Setting.protiv == 1:
            self.pro.setCurrentIndex(1)
        if Setting.flxod == 1:
            self.xxod.setCurrentIndex(0)
        if Setting.flxod == 2:
            self.xxod.setCurrentIndex(1)
        if Setting.sloj == 1:
            self.diff.setCurrentIndex(0)
        if Setting.sloj == 2:
            self.diff.setCurrentIndex(1)
        if Setting.sloj == 3:
            self.diff.setCurrentIndex(2)
        back = QtWidgets.QPushButton('В меню', self)
        back.clicked.connect(gomenu)
        back.setStyleSheet("background-color: red; color: white")
        pr.setFont(QtGui.QFont('Arial', 15))
        dif.setFont(QtGui.QFont('Arial', 15))
        xod.setFont(QtGui.QFont('Arial', 15))
        self.pro.setFont(QtGui.QFont('Arial', 15))
        self.xxod.setFont(QtGui.QFont('Arial', 15))
        self.diff.setFont(QtGui.QFont('Arial', 15))
        set.addWidget(pr, 0, 0)
        set.addWidget(self.pro, 0, 1)
        set.addWidget(dif, 1, 0)
        set.addWidget(self.diff, 1, 1)
        set.addWidget(xod, 2, 0)
        set.addWidget(self.xxod, 2, 1)
        self.pro.setStyleSheet('border-style: solid; border-width: 3px; border-color: black; background-color: red')
        pr.setStyleSheet('border-style: solid; border-width: 3px; border-color: black; background-color: red')
        dif.setStyleSheet('border-style: solid; border-width: 3px; border-color: black; background-color: red')
        self.diff.setStyleSheet('border-style: solid; border-width: 3px; border-color: black; background-color: red')
        xod.setStyleSheet('border-style: solid; border-width: 3px; border-color: black; background-color: red')
        self.xxod.setStyleSheet('border-style: solid; border-width: 3px; border-color: black; background-color: red')
        self.setLayout(set)
        self.xxod.activated.connect(self.xod)
        self.pro.activated.connect(self.pr)
        self.diff.activated.connect(self.sl)
    def pr(self):
        if self.pro.currentText() == 'Компьютер':
            Setting.protiv = 0
        if self.pro.currentText() == 'Игрок':
            Setting.protiv = 1

    def xod(self):
        if self.xxod.currentText() == 'Игрок':
            Setting.flxod = 1
        if self.xxod.currentText() == 'Компьютер':
            Setting.flxod = 2
    def sl(self):
        if self.diff.currentText() == 'Легкая':
            Setting.sloj = 1
        if self.diff.currentText() == 'Средняя':
            Setting.sloj = 2
        if self.diff.currentText() == 'Сложная':
            Setting.sloj = 3
class Game(QtWidgets.QWidget):
    def __init__(self):
        super(Game, self).__init__()
        def vklu():
            vkl = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                   self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                   self.el4_6, self.el4_7]
            for a in vkl:
                a.setEnabled(True)
            self.men.setEnabled(True)
        field = self.field1()
        self.flag = True
        self.count1 = 1
        self.count2 = 3
        self.count3 = 5
        self.count4 = 7
        self.count = 4
        self.end = 0
        self.men = QtWidgets.QPushButton('В меню' ,self)
        self.men.setStyleSheet("background-color: red; color: white")
        self.men.clicked.connect(gomenu)
        Game.winer = QtWidgets.QLabel(self)
        Game.winer.hide()
        Game.winer.setFont(QtGui.QFont('Arial', 50))
        Game.winer.setStyleSheet("color: yellow")
        Game.nac = Setting.flxod
        vs = QtWidgets.QLabel(self)
        vs.setFont(QtGui.QFont('Arial', 15))
        vs.setStyleSheet("color: white")
        self.xod = QtWidgets.QLabel(self)
        self.xod.setFont(QtGui.QFont('Arial', 15))
        self.xod.setStyleSheet("color: white")
        if Setting.protiv == 0:
            vs.setText('Режим: игрок против компьютера')
        else:
            vs.setText('Режим: игрок против игрока')
            self.xod.setText('Ход игрока 1')
            Game.xodi = 1
        if Game.nac == 1 and Setting.protiv == 0:
            self.xod.setText('Ход игрока')
        if Game.nac == 2 and Setting.protiv == 0:
            self.xod.setText('Ход компьютера')
            self.men.setEnabled(False)
            vkl = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                      self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                      self.el4_6, self.el4_7]
            for a in vkl:
                a.setEnabled(False)
            QtCore.QTimer.singleShot(1000, self.xorf1)
            QtCore.QTimer.singleShot(1001, vklu)
        vs.adjustSize()
        nad = QtWidgets.QGridLayout()
        nad.addWidget(self.men, 0, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        nad.addWidget(vs, 0, 0, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        nad.addWidget(self.xod, 0, 0, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        game = QtWidgets.QGridLayout()
        game.addLayout(nad, 0, 0)
        game.addLayout(field, 1, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(game)
    def field1(self):
        field = QtWidgets.QGridLayout()
        self.el1_1 = QtWidgets.QPushButton()

        def vklu():
            vkl = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                   self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                   self.el4_6, self.el4_7]
            for a in vkl:
                a.setEnabled(True)
            self.men.setEnabled(True)
        def xodit():
            if Game.nac == 1 and self.count != 0:
                Game.nac = 2
                self.men.setEnabled(False)
                self.xod.setText('Ход компьютера')
                vkl = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                          self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                          self.el4_6, self.el4_7]
                for a in vkl:
                    a.setEnabled(False)
                QtCore.QTimer.singleShot(1000, self.xorf1)
                QtCore.QTimer.singleShot(1001, vklu)
            elif Game.nac == 2 and self.count != 0:
                Game.nac = 1
                self.xod.setText('Ход игрока')
            if self.count == 0 and Game.nac == 1:
                field.addWidget(Game.winer, 4, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
                Game.winer.show()
                self.xod.setText('')
                Game.winer.setText('Победил игрок')
            elif self.count == 0 and Game.nac == 2:
                field.addWidget(Game.winer, 4, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
                Game.winer.show()
                self.xod.setText('')
                Game.winer.setText('Победил компьютер')
        def igroki():
            if Game.xodi == 1:
                Game.xodi = 2
                self.xod.setText('Ход игрока 2')
            else:
                Game.xodi = 1
                self.xod.setText('Ход игрока 1')
            if self.count == 0 and Game.xodi == 1:
                field.addWidget(Game.winer, 4, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
                Game.winer.show()
                self.xod.setText('')
                Game.winer.setText('Победил игрок 2')
            elif self.count == 0 and Game.xodi == 2:
                field.addWidget(Game.winer, 4, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
                Game.winer.show()
                self.xod.setText('')
                Game.winer.setText('Победил игрок 1')
        def vibor():
            if Setting.protiv == 0:
                xodit()
            else:
                igroki()

        def el11enter(q):
            self.el1_1.setIcon(QtGui.QIcon('monetka2.png'))
        def el11leave(q):
            self.el1_1.setIcon(QtGui.QIcon('monetka.png'))
        def el21enter(q):
            self.el2_1.setIcon(QtGui.QIcon('monetka2.png'))
            self.el2_2.setIcon(QtGui.QIcon('monetka2.png'))
            self.el2_3.setIcon(QtGui.QIcon('monetka2.png'))
        def el21leave(q):
            self.el2_1.setIcon(QtGui.QIcon('monetka.png'))
            self.el2_2.setIcon(QtGui.QIcon('monetka.png'))
            self.el2_3.setIcon(QtGui.QIcon('monetka.png'))
        def el22enter(q):
            self.el2_2.setIcon(QtGui.QIcon('monetka2.png'))
            self.el2_3.setIcon(QtGui.QIcon('monetka2.png'))
        def el22leave(q):
            self.el2_2.setIcon(QtGui.QIcon('monetka.png'))
            self.el2_3.setIcon(QtGui.QIcon('monetka.png'))
        def el23enter(q):
            self.el2_3.setIcon(QtGui.QIcon('monetka2.png'))
        def el23leave(q):
            self.el2_3.setIcon(QtGui.QIcon('monetka.png'))
        def el31enter(q):
            self.el3_1.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_2.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_3.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka2.png'))
        def el31leave(q):
            self.el3_1.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_2.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_3.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka.png'))
        def el32enter(q):
            self.el3_2.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_3.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka2.png'))
        def el32leave(q):
            self.el3_2.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_3.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka.png'))
        def el33enter(q):
            self.el3_3.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka2.png'))
        def el33leave(q):
            self.el3_3.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka.png'))
        def el34enter(q):
            self.el3_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka2.png'))
        def el34leave(q):
            self.el3_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el3_5.setIcon(QtGui.QIcon('monetka.png'))
        def el35enter(q):
            self.el3_5.setIcon(QtGui.QIcon('monetka2.png'))
        def el35leave(q):
            self.el3_5.setIcon(QtGui.QIcon('monetka.png'))
        def el41enter(q):
            self.el4_1.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_2.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_3.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el41leave(q):
            self.el4_1.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_2.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_3.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def el42enter(q):
            self.el4_2.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_3.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el42leave(q):
            self.el4_2.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_3.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def el43enter(q):
            self.el4_3.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el43leave(q):
            self.el4_3.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def el44enter(q):
            self.el4_4.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el44leave(q):
            self.el4_4.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_5.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def el45enter(q):
            self.el4_5.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el45leave(q):
            self.el4_5.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def el46enter(q):
            self.el4_6.setIcon(QtGui.QIcon('monetka2.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el46leave(q):
            self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def el47enter(q):
            self.el4_7.setIcon(QtGui.QIcon('monetka2.png'))
        def el47leave(q):
            self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        def click11():
            self.count1 -=1
            self.count -= 1
            self.el1_1.hide()
            vibor()


        def clik21():
            if self.count2 == 3:
                self.count2 -= 3
                self.count -=1
                self.el2_1.hide()
                self.el2_2.hide()
                self.el2_3.hide()
                vibor()

            elif self.count2 == 2:
                self.count2 -=2
                self.count -= 1
                self.el2_1.hide()
                self.el2_2.hide()
                vibor()
            elif self.count2 == 1:
                self.count2 -=1
                self.count -= 1
                self.el2_1.hide()
                vibor()
        def click22():
            if self.count2 == 3:
                self.count2 -= 2
                self.el2_2.hide()
                self.el2_3.hide()
                vibor()
            elif self.count2 == 2:
                self.count2 -= 1
                self.el2_2.hide()
                vibor()
        def click23():
            self.count2 -= 1
            self.el2_3.hide()
            vibor()
        def click31():
            if self.count3 == 5:
                self.count3 -= 5
                self.count -= 1
                self.el3_5.hide()
                self.el3_1.hide()
                self.el3_2.hide()
                self.el3_4.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 4:
                self.count3 -= 4
                self.el3_1.hide()
                self.count -= 1
                self.el3_2.hide()
                self.el3_4.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 3:
                self.count3 -= 3
                self.el3_1.hide()
                self.count -= 1
                self.el3_2.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 2:
                self.count3 -= 2
                self.el3_1.hide()
                self.el3_2.hide()
                self.count -= 1
                vibor()
            elif self.count3 == 1:
                self.count3 -= 1
                self.el3_1.hide()
                self.count -= 1
                vibor()
        def click32():
            if self.count3 == 5:
                self.count3 -= 4
                self.el3_5.hide()
                self.el3_2.hide()
                self.el3_4.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 4:
                self.count3 -= 3
                self.el3_2.hide()
                self.el3_4.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 3:
                self.count3 -= 2
                self.el3_2.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 2:
                self.count3 -= 1
                self.el3_2.hide()
                vibor()

        def click33():
            if self.count3 == 5:
                self.count3 -= 3
                self.el3_5.hide()
                self.el3_4.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 4:
                self.count3 -= 2
                self.el3_4.hide()
                self.el3_3.hide()
                vibor()
            elif self.count3 == 3:
                self.count3 -= 1
                self.el3_3.hide()
                vibor()
        def click34():
            if self.count3 == 5:
                self.count3 -= 2
                self.el3_5.hide()
                self.el3_4.hide()
                vibor()

            elif self.count3 == 4:
                self.count3 -= 1
                self.el3_4.hide()
                vibor()

        def click35():
            if self.count3 == 5:
                self.count3 -= 1
                self.el3_5.hide()
                vibor()

        def click41():
            if self.count4 == 7:
                self.count4 -= 7
                self.count -= 1
                self.el4_1.hide()
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                self.el4_7.hide()
                vibor()

            elif self.count4 == 6:
                self.count4 -= 6
                self.count -= 1
                self.el4_1.hide()
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                vibor()

            elif self.count4 == 5:
                self.count4 -= 5
                self.count -= 1
                self.el4_1.hide()
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                vibor()

            elif self.count4 == 4:
                self.count4 -= 4
                self.count -= 1
                self.el4_1.hide()
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                vibor()
            elif self.count4 == 3:
                self.count4 -= 3
                self.count -= 1
                self.el4_1.hide()
                self.el4_2.hide()
                self.el4_3.hide()
                vibor()
            elif self.count4 == 2:
                self.count4 -= 2
                self.count -= 1
                self.el4_1.hide()
                self.el4_2.hide()
                vibor()
            elif self.count4 == 1:
                self.count4 -= 1
                self.count -= 1
                self.el4_1.hide()
                vibor()
        def click42():
            if self.count4 == 7:
                self.count4 -= 6
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                self.el4_7.hide()
                vibor()
            elif self.count4 == 6:
                self.count4 -= 5
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                vibor()
            elif self.count4 == 5:
                self.count4 -= 4
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                vibor()
            elif self.count4 == 4:
                self.count4 -= 3
                self.el4_2.hide()
                self.el4_3.hide()
                self.el4_4.hide()
                vibor()
            elif self.count4 == 3:
                self.count4 -= 2
                self.el4_2.hide()
                self.el4_3.hide()
                vibor()
            elif self.count4 == 2:
                self.count4 -= 1
                self.el4_2.hide()
                vibor()

        def click43():
            if self.count4 == 7:
                self.count4 -= 5
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                self.el4_7.hide()
                vibor()
            elif self.count4 == 6:
                self.count4 -= 4
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                vibor()
            elif self.count4 == 5:
                self.count4 -= 3
                self.el4_3.hide()
                self.el4_4.hide()
                self.el4_5.hide()
                vibor()
            elif self.count4 == 4:
                self.count4 -= 2
                self.el4_3.hide()
                self.el4_4.hide()
                vibor()
            elif self.count4 == 3:
                self.count4 -= 1
                self.el4_3.hide()
                vibor()
        def click44():
            if self.count4 == 7:
                self.count4 -= 4
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                self.el4_7.hide()
                vibor()
            elif self.count4 == 6:
                self.count4 -= 3
                self.el4_4.hide()
                self.el4_5.hide()
                self.el4_6.hide()
                vibor()
            elif self.count4 == 5:
                self.count4 -= 2
                self.el4_4.hide()
                self.el4_5.hide()
                vibor()
            elif self.count4 == 4:
                self.count4 -= 1
                self.el4_4.hide()
                vibor()
        def click45():
            if self.count4 == 7:
                self.count4 -= 3
                self.el4_5.hide()
                self.el4_6.hide()
                self.el4_7.hide()
                vibor()
            elif self.count4 == 6:
                self.count4 -= 2
                self.el4_5.hide()
                self.el4_6.hide()
                vibor()

            elif self.count4 == 5:
                self.count4 -= 1
                self.el4_5.hide()
                vibor()


        def click46():
            if self.count4 == 7:
                self.count4 -= 2
                self.el4_6.hide()
                self.el4_7.hide()
                vibor()
            elif self.count4 == 6:
                self.count4 -= 1
                self.el4_6.hide()
                vibor()
        def click47():
            if self.count4 == 7:
                self.count4 -= 1
                self.el4_7.hide()
                vibor()

        self.el1_1.setFixedSize(100, 100)
        self.el1_1.setIconSize(QtCore.QSize(95, 95))
        self.el1_1.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el1_1.setIcon(QtGui.QIcon('monetka.png'))
        self.el1_1.enterEvent = el11enter
        self.el1_1.leaveEvent = el11leave
        self.el1_1.clicked.connect(click11)
        field.addWidget(self.el1_1, 0, 1)
        self.el2_1 = QtWidgets.QPushButton()
        self.el2_1.setFixedSize(100, 100)
        self.el2_1.setIconSize(QtCore.QSize(95, 95))
        self.el2_1.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el2_1.setIcon(QtGui.QIcon('monetka.png'))
        self.el2_1.enterEvent = el21enter
        self.el2_1.leaveEvent = el21leave
        field.addWidget(self.el2_1, 1, 1)
        self.el2_2 = QtWidgets.QPushButton()
        self.el2_2.setFixedSize(100, 100)
        self.el2_2.setIconSize(QtCore.QSize(95, 95))
        self.el2_2.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el2_2.setIcon(QtGui.QIcon('monetka.png'))
        self.el2_2.enterEvent = el22enter
        self.el2_2.leaveEvent = el22leave
        self.el2_2.clicked.connect(click22)
        field.addWidget(self.el2_2, 1, 2)
        self.el2_3 = QtWidgets.QPushButton()
        self.el2_3.setFixedSize(100, 100)
        self.el2_3.setIconSize(QtCore.QSize(95, 95))
        self.el2_3.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el2_3.setIcon(QtGui.QIcon('monetka.png'))
        self.el2_3.enterEvent = el23enter
        self.el2_3.leaveEvent = el23leave
        self.el2_3.clicked.connect(click23)
        self.el2_1.clicked.connect(clik21)
        field.addWidget(self.el2_3, 1, 3)
        self.el3_1 = QtWidgets.QPushButton()
        self.el3_1.setFixedSize(100, 100)
        self.el3_1.setIconSize(QtCore.QSize(95, 95))
        self.el3_1.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el3_1.setIcon(QtGui.QIcon('monetka.png'))
        self.el3_1.enterEvent = el31enter
        self.el3_1.leaveEvent = el31leave
        field.addWidget(self.el3_1, 2, 1)
        self.el3_2 = QtWidgets.QPushButton()
        self.el3_2.setFixedSize(100, 100)
        self.el3_2.setIconSize(QtCore.QSize(95, 95))
        self.el3_2.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el3_2.setIcon(QtGui.QIcon('monetka.png'))
        self.el3_2.enterEvent = el32enter
        self.el3_2.leaveEvent = el32leave
        field.addWidget(self.el3_2, 2, 2)
        self.el3_3 = QtWidgets.QPushButton()
        self.el3_3.setFixedSize(100, 100)
        self.el3_3.setIconSize(QtCore.QSize(95, 95))
        self.el3_3.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el3_3.setIcon(QtGui.QIcon('monetka.png'))
        self.el3_3.enterEvent = el33enter
        self.el3_3.leaveEvent = el33leave
        field.addWidget(self.el3_3, 2, 3)
        self.el3_4 = QtWidgets.QPushButton()
        self.el3_4.setFixedSize(100, 100)
        self.el3_4.setIconSize(QtCore.QSize(95, 95))
        self.el3_4.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el3_4.setIcon(QtGui.QIcon('monetka.png'))
        self.el3_4.enterEvent = el34enter
        self.el3_4.leaveEvent = el34leave
        field.addWidget(self.el3_4, 2, 4)
        self.el3_5 = QtWidgets.QPushButton()
        self.el3_5.setFixedSize(100, 100)
        self.el3_5.setIconSize(QtCore.QSize(95, 95))
        self.el3_5.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el3_5.setIcon(QtGui.QIcon('monetka.png'))
        self.el3_5.enterEvent = el35enter
        self.el3_5.leaveEvent = el35leave
        field.addWidget(self.el3_5, 2, 5)
        self.el3_1.clicked.connect(click31)
        self.el3_2.clicked.connect(click32)
        self.el3_3.clicked.connect(click33)
        self.el3_4.clicked.connect(click34)
        self.el3_5.clicked.connect(click35)
        self.el4_1 = QtWidgets.QPushButton()
        self.el4_1.setFixedSize(100, 100)
        self.el4_1.setIconSize(QtCore.QSize(95, 95))
        self.el4_1.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_1.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_1.enterEvent = el41enter
        self.el4_1.leaveEvent = el41leave
        field.addWidget(self.el4_1, 3, 1)
        self.el4_2 = QtWidgets.QPushButton()
        self.el4_2.setFixedSize(100, 100)
        self.el4_2.setIconSize(QtCore.QSize(95, 95))
        self.el4_2.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_2.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_2.enterEvent = el42enter
        self.el4_2.leaveEvent = el42leave
        field.addWidget(self.el4_2, 3, 2)
        self.el4_3 = QtWidgets.QPushButton()
        self.el4_3.setFixedSize(100, 100)
        self.el4_3.setIconSize(QtCore.QSize(95, 95))
        self.el4_3.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_3.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_3.enterEvent = el43enter
        self.el4_3.leaveEvent = el43leave
        field.addWidget(self.el4_3, 3, 3)
        self.el4_4 = QtWidgets.QPushButton()
        self.el4_4.setFixedSize(100, 100)
        self.el4_4.setIconSize(QtCore.QSize(95, 95))
        self.el4_4.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_4.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_4.enterEvent = el44enter
        self.el4_4.leaveEvent = el44leave
        field.addWidget(self.el4_4, 3, 4)
        self.el4_5 = QtWidgets.QPushButton()
        self.el4_5.setFixedSize(100, 100)
        self.el4_5.setIconSize(QtCore.QSize(95, 95))
        self.el4_5.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_5.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_5.enterEvent = el45enter
        self.el4_5.leaveEvent = el45leave
        field.addWidget(self.el4_5, 3, 5)
        self.el4_6 = QtWidgets.QPushButton()
        self.el4_6.setFixedSize(100, 100)
        self.el4_6.setIconSize(QtCore.QSize(95, 95))
        self.el4_6.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_6.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_6.enterEvent = el46enter
        self.el4_6.leaveEvent = el46leave
        field.addWidget(self.el4_6, 3, 6)
        self.el4_7 = QtWidgets.QPushButton()
        self.el4_7.setFixedSize(100, 100)
        self.el4_7.setIconSize(QtCore.QSize(95, 95))
        self.el4_7.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.el4_7.setIcon(QtGui.QIcon('monetka.png'))
        self.el4_7.enterEvent = el47enter
        self.el4_7.leaveEvent = el47leave
        self.el4_1.clicked.connect(click41)
        self.el4_2.clicked.connect(click42)
        self.el4_3.clicked.connect(click43)
        self.el4_4.clicked.connect(click44)
        self.el4_5.clicked.connect(click45)
        self.el4_6.clicked.connect(click46)
        self.el4_7.clicked.connect(click47)
        field.addWidget(self.el4_7, 3, 7)
        return field
    def xorf1(self):
        c = 0
        b = 0
        if self.count != 1 and self.count1 ^ self.count2 ^ self.count3 ^ self.count4 == 0:
            c = 1
            while b == 0:
                ran_el = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                          self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                          self.el4_6, self.el4_7]
                a = random.choice(ran_el)
                if a.isHidden() == False:
                    a.setEnabled(True)
                    a.click()
                    b = 1
        if Setting.sloj == 1 and self.count != 1:
            sll = random.randint(1,100000000)
            if sll > 40000000 and c == 0:
                c = 1
                b = 0
                while b == 0:
                    ran_el = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                              self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                              self.el4_6, self.el4_7]
                    a = random.choice(ran_el)
                    if a.isHidden() == False:
                        a.setEnabled(True)
                        a.click()
                        b = 1
        if Setting.sloj == 2 and self.count != 1:
            sll = random.randint(1,100000000)
            if sll > 60000000 and c == 0 :
                c = 1
                b = 0
                while b == 0:
                    ran_el = [self.el1_1, self.el2_1, self.el2_2, self.el2_3, self.el3_1, self.el3_2, self.el3_3,
                              self.el3_4, self.el3_5, self.el4_1, self.el4_2, self.el4_3, self.el4_4, self.el4_5,
                              self.el4_6, self.el4_7]
                    a = random.choice(ran_el)
                    if a.isHidden() == False:
                        a.setEnabled(True)
                        a.click()
                        b = 1
        c1 = self.count1
        c2 = self.count2
        c3 = self.count3
        c4 = self.count4
        if c == 0:
            if c1 != 0:
                while c1 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                    c1 -= 1
                    b = 1
            if c1 ^ c2 ^ c3 ^ c4 != 0:
                c1 = self.count1
            if c2 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                while c2 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                    c2 -= 1
                    b = 2
            if c1 ^ c2 ^ c3 ^ c4 != 0:
                c2 = self.count2
            if c3 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                while c3 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                    c3 -= 1
                    b = 3
            if c1 ^ c2 ^ c3 ^ c4 != 0:
                c3 = self.count3
            if c4 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                while c4 != 0 and c1 ^ c2 ^ c3 ^ c4 != 0:
                    c4 -= 1
                    b = 4
        if c == 0:
            if b == 1 :
                self.el1_1.setEnabled(True)
                self.el1_1.click()
            if b == 2:
                if c2 == 2:
                    self.el2_3.setEnabled(True)
                    self.el2_3.click()
                if c2 == 1:
                    self.el2_2.setEnabled(True)
                    self.el2_2.click()
                if c2 == 0:
                    self.el2_1.setEnabled(True)
                    self.el2_1.click()
            if b == 3:
                if c3 == 4:
                    self.el3_5.setEnabled(True)
                    self.el3_5.click()
                elif c3 == 3:
                    self.el3_4.setEnabled(True)
                    self.el3_4.click()
                elif c3 == 2:
                    self.el3_3.setEnabled(True)
                    self.el3_3.click()
                elif c3 == 1:
                    self.el3_2.setEnabled(True)
                    self.el3_2.click()
                elif c3 == 0:
                    self.el3_1.setEnabled(True)
                    self.el3_1.click()
            if b == 4:
                if c4 == 6:
                    self.el4_7.setEnabled(True)
                    self.el4_7.click()
                elif c4 == 5:
                    self.el4_6.setEnabled(True)
                    self.el4_6.click()
                elif c4 == 4:
                    self.el4_5.setEnabled(True)
                    self.el4_5.click()
                elif c4 == 3:
                    self.el4_4.setEnabled(True)
                    self.el4_4.click()
                elif c4 == 2:
                    self.el4_3.setEnabled(True)
                    self.el4_3.click()
                elif c4 == 1:
                    self.el4_2.setEnabled(True)
                    self.el4_2.click()
                elif c4 == 0:
                    self.el4_1.setEnabled(True)
                    self.el4_1.click()
            if self.count == 1:
                if c1 > 0:
                    self.el1_1.setEnabled(True)
                    self.el1_1.click()
                elif c2 > 0:
                    self.el2_1.setEnabled(True)
                    self.el2_1.click()
                elif c3 > 0:
                    self.el3_1.setEnabled(True)
                    self.el3_1.click()
                elif c4 > 0:
                    self.el4_1.setEnabled(True)
                    self.el4_1.click()
class rules(QtWidgets.QWidget):
    def __init__(self):
        super(rules, self).__init__()
        self.setWindowTitle('Правила')
        rule = ('Два игрока по очереди берут предметы, распределенные на несколько групп.За один ход может быть взято любое количество предметов (большее нуля) из одной группы.Выигрывает игрок, взявший последний предмет.')
        rules1 = QtWidgets.QLabel(rule, self)
        rules1.setStyleSheet("color: white")
        Q = QtWidgets.QGridLayout()
        Q.addWidget(rules1, 0, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft.AlignTop)
        rules1.setFont(QtGui.QFont('Arial', 20))
        rules1.setWordWrap(True)
        back = QtWidgets.QPushButton('Назад', self)
        back.setFixedSize(200, 100)
        back.setFont(QtGui.QFont('Arial', 25))
        Q.addWidget(back, 1, 0, alignment=QtCore.Qt.AlignmentFlag.AlignBottom.AlignCenter)
        back.setStyleSheet("background-color: red; color: white")
        back.clicked.connect(gomenu)
        self.setLayout(Q)
app = QtWidgets.QApplication([])
switch = QtWidgets.QStackedWidget()
menu = Main()
switch.addWidget(menu)
switch.setStyleSheet("background-color: green")
switch.setWindowTitle('Игра Ним')
switch.setMinimumSize(1000, 550)
Setting.flxod = 1
Setting.protiv = 0
Setting.sloj = 1
switch.show()
app.exec()