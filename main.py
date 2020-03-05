#!/usr/bin/python3
# -*- coding: utf-8 -*-
import PyQt5
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QSlider, QLabel, QLineEdit, QTextEdit, QGridLayout, \
    QRadioButton, QLCDNumber, QGraphicsView, QComboBox, QGraphicsScene, QGraphicsRectItem, QGraphicsPathItem, \
    QGraphicsEllipseItem, QGraphicsPolygonItem
from PyQt5.QtGui import QPainter, QColor, QPainterPath, QPen
from PyQt5.QtCore import Qt
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Инициализация элементов GUI

        radio_button_circle = QRadioButton('Круг')
        radio_button_circle.setChecked(True)
        radio_button_square = QRadioButton('Квадрат')
        radio_button_triangle = QRadioButton('Треугольник')

        combo_box_color = QComboBox()
        combo_box_color.addItems(['Белый', 'Черный', 'Зеленый', 'Синий', 'Красный'])

        label_rotate = QLabel('Поворот')
        label_size = QLabel('Размер')
        label_move_y = QLabel('Перемещение: ось Y')
        label_move_x = QLabel('Перемещение: ось X')

        horizontal_slider_rotate = QSlider(Qt.Horizontal, self)
        horizontal_slider_rotate.setMaximum(360)

        horizontal_slider_size = QSlider(Qt.Horizontal, self)
        horizontal_slider_size.setProperty("value", 50)

        horizontal_slider_move_x = QSlider(Qt.Horizontal, self)
        horizontal_slider_move_x.setMaximum(500)
        horizontal_slider_move_x.setProperty("value", 0)

        horizontal_slider_move_y = QSlider(Qt.Horizontal, self)
        horizontal_slider_move_y.setMaximum(500)
        horizontal_slider_move_y.setProperty("value", 0)

        lcd_number_rotate = QLCDNumber()
        lcd_number_rotate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        lcd_number_rotate.setProperty("intValue", 0)

        lcd_number_size = QLCDNumber()
        lcd_number_size.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        lcd_number_size.setProperty("intValue", 50)

        lcd_number_move_x = QLCDNumber()
        lcd_number_move_x.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        lcd_number_move_x.setProperty("intValue", 0)

        lcd_number_move_y = QLCDNumber()
        lcd_number_move_y.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        lcd_number_move_y.setProperty("intValue", 0)

        # Инициадизация графической сцены
        graphics_view = QGraphicsView()
        scene = QGraphicsScene()
        graphics_view.setScene(scene)

        # Применение варианта расположения элементов GUI
        grid = QGridLayout()
        grid.setSpacing(10)

        # Добавление элементов GUI
        grid.addWidget(radio_button_circle, 0, 0)
        grid.addWidget(label_rotate, 0, 1)
        grid.addWidget(horizontal_slider_rotate, 0, 2)
        grid.addWidget(lcd_number_rotate, 0, 3)

        grid.addWidget(radio_button_square, 1, 0)
        grid.addWidget(label_size, 1, 1)
        grid.addWidget(horizontal_slider_size, 1, 2)
        grid.addWidget(lcd_number_size, 1, 3)

        grid.addWidget(radio_button_triangle, 2, 0)
        grid.addWidget(label_move_x, 2, 1)
        grid.addWidget(horizontal_slider_move_x, 2, 2)
        grid.addWidget(lcd_number_move_x, 2, 3)

        grid.addWidget(combo_box_color, 3, 0)
        grid.addWidget(label_move_y, 3, 1)
        grid.addWidget(horizontal_slider_move_y, 3, 2)
        grid.addWidget(lcd_number_move_y, 3, 3)

        grid.addWidget(graphics_view, 4, 0, 4, 4)

        # Связь элементов GUI между собой
        horizontal_slider_size.valueChanged.connect(lcd_number_size.display)
        horizontal_slider_rotate.valueChanged.connect(lcd_number_rotate.display)
        horizontal_slider_move_x.valueChanged.connect(lcd_number_move_x.display)
        horizontal_slider_move_y.valueChanged.connect(lcd_number_move_y.display)

        def rotate():
            # получение значения со слайдера
            r = horizontal_slider_rotate.sliderPosition()
            # получение статуса радиокнопок и выполнение нужного действия
            if radio_button_circle.isChecked():
                circle1.rotate_circle(r)
            elif radio_button_square.isChecked():
                square1.rotate_square(r)
            elif radio_button_triangle.isChecked():
                triangle1.rotate_triangle(r)
            else:
                print('error')
            print('rotate: ', r)

        def move():
            # получение значения со слайдера
            m = horizontal_slider_move_x.sliderPosition()
            n = horizontal_slider_move_y.sliderPosition()
            # получение статуса радиокнопок и выполнение нужного действия
            if radio_button_circle.isChecked():
                circle1.move_circle(m, n)
            elif radio_button_square.isChecked():
                square1.move_square(m, n)
            elif radio_button_triangle.isChecked():
                triangle1.move_triangle(m, n)
            else:
                print('error')
            print('move: ', m, ' : ', n)

        def scale():
            # получение значения со слайдера
            s = horizontal_slider_size.sliderPosition()
            # получение статуса радиокнопок и выполнение нужного действия
            if radio_button_circle.isChecked():
                circle1.scale_circle(s)
            elif radio_button_square.isChecked():
                square1.scale_square(s)
            elif radio_button_triangle.isChecked():
                triangle1.scale_triangle(s)
            else:
                print('error')
            print('scale: ', s)

        # Отрисовка

        square1 = Square(0, 0, 250, 250)
        square1.draw_square(scene)

        circle1 = Сircle(0, 0, 250, 250)
        circle1.draw_circle(scene)

        triangle1 = Triangle(0, 0, 0, 250, 250, 250)
        triangle1.draw_triangle(scene)

        # Активация функций слайдерами
        horizontal_slider_rotate.valueChanged.connect(rotate)
        horizontal_slider_size.valueChanged.connect(scale)
        horizontal_slider_move_x.valueChanged.connect(move)
        horizontal_slider_move_y.valueChanged.connect(move)

        self.setLayout(grid)
        self.setGeometry(0, 0, 700, 700)
        self.setWindowTitle('Review')
        self.show()


class Square(QGraphicsView):

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.square = QGraphicsRectItem(self.x, self.y, self.a, self.b)

    def draw_square(self, scene):
        scene.addItem(self.square)

    def move_square(self, m, n):
        self.square.setPos(m, n)

    def rotate_square(self, r):
        self.square.setRotation(r)

    def scale_square(self, s):
        self.square.setScale((s + 50) / 100)


class Сircle(QGraphicsView):

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.circle = QGraphicsEllipseItem(self.x, self.y, self.w, self.h)

    def draw_circle(self, scene):
        scene.addItem(self.circle)

    def move_circle(self, m, n):
        self.circle.setPos(m, n)

    def rotate_circle(self, r):
        self.circle.setRotation(r)

    def scale_circle(self, s):
        self.circle.setScale((s + 50) / 100)

class Triangle(QGraphicsView):

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

        triangle = QtGui.QPolygonF(3)
        triangle[0] = QtCore.QPoint(self.x1, self.y1)
        triangle[1] = QtCore.QPoint(self.x2, self.y2)
        triangle[2] = QtCore.QPoint(self.x3, self.y3)
        self.triangle = QGraphicsPolygonItem(triangle)

    def draw_triangle(self, scene):
        scene.addItem(self.triangle)

    def move_triangle(self, m, n):
        self.triangle.setPos(m, n)

    def rotate_triangle(self, r):
        self.triangle.setRotation(r)

    def scale_triangle(self, s):
        self.triangle.setScale((s + 50) / 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
