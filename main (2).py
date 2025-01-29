import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>order</class>
 <widget class="QMainWindow" name="order">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Order</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="choice1">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}
</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="choice2">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="choice3">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="choice4">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="finish">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>392</y>
      <width>271</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>СДЕЛАТЬ ЗАКАЗ</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="Choices"/>
 </buttongroups>
</ui>
"""


class Order(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.Choices.buttonClicked.connect(self.choice)
        self.finish.clicked.connect(self.run)

    def choice(self, btn):
        drink, ok_pressed = QInputDialog.getItem(
            self, "Выбор", "Выберите ваш напиток",
            ("Газированная вода", "Мятный сироп", "Апельсиновый сок", "Лимонад “Мятный”", "Лимонад “Заводной апельсин”"
             , "Лимонад ‘Тройной”"), 1, False)
        if ok_pressed:
            btn.setText(drink)

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Order()
    ex.show()
    sys.exit(app.exec())
