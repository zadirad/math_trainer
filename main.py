import os
import sys
import sqlite3

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QCheckBox


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.count = 0

    def init_ui(self):
        self.setGeometry(50, 50, 700, 450)
        self.setWindowTitle('Тест')
        self.setStyleSheet('background-color: rgb(211, 211, 211);')

        btn_back = QPushButton('Назад', self)
        btn_back.setStyleSheet('background-color: rgb(255, 150, 150); '
                               'border-style: outset; '
                               'border-width: 1px; '
                               'border-radius: 5px; '
                               'border-color: black; '
                               'padding: 1px;')
        btn_back.resize(150, 50)
        btn_back.move(530, 380)
        btn_back.clicked.connect(self.back_main)

        btn_score = QPushButton('Узнать результат', self)
        btn_score.setStyleSheet('background-color: rgb(144, 251, 144); '
                                'border-style: outset; '
                                'border-width: 1px; '
                                'border-radius: 5px; '
                                'border-color: black; '
                                'padding: 1px;')
        btn_score.resize(150, 50)
        btn_score.move(200, 300)
        btn_score.clicked.connect(self.check)

        self.total = QLabel(self)
        self.total.move(150, 350)
        self.total.hide()

        self.ch_1 = QCheckBox(self)
        self.ch_1.move(300, 50)

        self.ch_2 = QCheckBox(self)
        self.ch_2.move(400, 50)

        self.ch_3 = QCheckBox(self)
        self.ch_3.move(500, 50)

        self.ch_4 = QCheckBox(self)
        self.ch_4.move(300, 80)

        self.ch_5 = QCheckBox(self)
        self.ch_5.move(400, 80)

        self.ch_6 = QCheckBox(self)
        self.ch_6.move(500, 80)

        self.ch_7 = QCheckBox(self)
        self.ch_7.move(300, 110)

        self.ch_8 = QCheckBox(self)
        self.ch_8.move(400, 110)

        self.ch_9 = QCheckBox(self)
        self.ch_9.move(500, 110)

        self.ch_10 = QCheckBox(self)
        self.ch_10.move(300, 140)

        self.ch_11 = QCheckBox(self)
        self.ch_11.move(400, 140)

        self.ch_12 = QCheckBox(self)
        self.ch_12.move(500, 140)

        self.ch_13 = QCheckBox(self)
        self.ch_13.move(300, 170)

        self.ch_14 = QCheckBox(self)
        self.ch_14.move(400, 170)

        self.ch_15 = QCheckBox(self)
        self.ch_15.move(500, 170)

        #
        con = sqlite3.connect("quest.db")
        cur = con.cursor()
        questions = cur.execute(f"""SELECT * FROM questions """).fetchall()
        print(questions)
        con.commit()
        self.hide()

        # сами вопросы

        self.q0 = QLabel(self)
        self.q1 = QLabel(self)
        self.q2 = QLabel(self)
        self.q3 = QLabel(self)
        self.q4 = QLabel(self)
        self.q5 = QLabel(self)
        self.q0.setText('Ответьте на 5 вопросов')
        self.q0.move(200, 10)
        self.q1.setText('1) ' + str(questions[0][0]))
        self.q1.move(10, 50)
        self.q2.setText('2) ' + str(questions[0][1]))
        self.q2.move(10, 80)
        self.q3.setText('3) ' + str(questions[0][2]))
        self.q3.move(10, 110)
        self.q4.setText('4) ' + str(questions[0][3]))
        self.q4.move(10, 140)
        self.q5.setText('5) ' + str(questions[0][4]))
        self.q5.move(10, 170)

        # ответы на вопросы

        self.ans1 = QLabel(self)
        self.ans1.move(320, 50)
        self.ans1.setText('c^3-6*a*c')

        self.ans2 = QLabel(self)
        self.ans2.move(420, 50)
        self.ans2.setText('b^2-4*a*c')

        self.ans3 = QLabel(self)
        self.ans3.move(520, 50)
        self.ans3.setText('80*a*d-b')

        self.ans4 = QLabel(self)
        self.ans4.move(320, 80)
        self.ans4.setText('(-1; 0.2)')

        self.ans5 = QLabel(self)
        self.ans5.move(420, 80)
        self.ans5.setText('(-2; 0.5)')

        self.ans6 = QLabel(self)
        self.ans6.move(520, 80)
        self.ans6.setText('(1; -0.2)')

        self.ans7 = QLabel(self)
        self.ans7.move(320, 110)
        self.ans7.setText('1.065')

        self.ans8 = QLabel(self)
        self.ans8.move(420, 110)
        self.ans8.setText('2.02')

        self.ans9 = QLabel(self)
        self.ans9.move(520, 110)
        self.ans9.setText('3.1')

        self.ans10 = QLabel(self)
        self.ans10.move(320, 140)
        self.ans10.setText('-1.5, 1')

        self.ans11 = QLabel(self)
        self.ans11.move(420, 140)
        self.ans11.setText('-1.1, 2')

        self.ans12 = QLabel(self)
        self.ans12.move(520, 140)
        self.ans12.setText('-1.1, 1')

        self.ans13 = QLabel(self)
        self.ans13.move(320, 170)
        self.ans13.setText('3.4')

        self.ans14 = QLabel(self)
        self.ans14.move(420, 170)
        self.ans14.setText('1.8')

        self.ans15 = QLabel(self)
        self.ans15.move(520, 170)
        self.ans15.setText('2.6')

    def check(self):
        self.count = 0
        if self.ch_2.isChecked() is True:
            self.count += 1
        if self.ch_4.isChecked() is True:
            self.count += 1
        if self.ch_8.isChecked() is True:
            self.count += 1
        if self.ch_12.isChecked() is True:
            self.count += 1
        if self.ch_15.isChecked() is True:
            self.count += 1
        self.total.setText(f'Вы ответили верно на {self.count} из 5 вопросов')
        self.total.show()

    def back_main(self):
        ex.show()
        self.total.hide()
        self.hide()


def instruct():
    os.startfile('TEORIA.docx')


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.pixmap = None
        self.main_label = None
        self.name_label = None
        self.name_box = None
        self.image = None
        self.init_ui()

    def init_ui(self):
        self.setGeometry(50, 50, 700, 450)
        self.setWindowTitle('Главное окно')
        self.setStyleSheet('background-color: rgb(211, 211, 211);')
        # Создаем кнопки
        # Настраиваем кнопки
        btn1 = QPushButton('Теория', self)
        btn1.setStyleSheet('background-color: rgb(255, 218, 185); '
                           'border-style: outset; '
                           'border-width: 1px; '
                           'border-radius: 5px; '
                           'border-color: black; '
                           'padding: 1px;')

        btn2 = QPushButton('Тест', self)
        btn2.setStyleSheet('background-color: rgb(200, 230, 185); '
                           'border-style: outset; '
                           'border-width: 1px; '
                           'border-radius: 5px; '
                           'border-color: black; '
                           'padding: 1px;')

        btn3 = QPushButton('Выход', self)
        btn3.setStyleSheet('background-color: rgb(250, 128, 114); '
                           'border-style: outset; '
                           'border-width: 1px; '
                           'border-radius: 5px; '
                           'border-color: black; '
                           'padding: 1px;')

        # Изменяем размер кнопки. Теперь он 150 на 50 пикселей
        btn1.resize(150, 50)
        btn2.resize(150, 50)
        btn3.resize(150, 50)

        # Размещаем кнопку на родительском виджете по своим местам
        btn1.move(500, 150)
        btn2.move(500, 250)
        btn3.move(500, 350)

        # Подключаем наши кнопки к их функциям
        btn2.clicked.connect(self.test_come)
        btn3.clicked.connect(self.inc_click)
        btn1.clicked.connect(instruct)

        self.pixmap = QPixmap('project.jpg')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(20, 50)
        self.image.resize(450, 400)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

        self.main_label = QLabel(self)
        self.main_label.setText("Проект 'Математический тренажер' выполнен Захаровым Дмитрием")
        self.main_label.setStyleSheet('font: 100 9pt "MS Shell Dlg 2";')
        self.main_label.move(10, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Введите свое имя")
        self.name_label.move(500, 70)

        self.name_box = QLineEdit(self)
        self.name_box.move(500, 20)
        self.name_box.resize(150, 40)

    def inc_click(self):
        count = eval(self.name_box.text())
        # В QLCDNumber для отображения данных используется метод display()
        self.name_box.display(count)

    def test_come(self):
        ex_test.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex_test = Test()
    ex.show()
    sys.exit(app.exec())
