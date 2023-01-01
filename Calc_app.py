#Main file that runs the application

from PyQt5 import uic, QtWidgets
Form, _ = uic.loadUiType("calcu.ui")

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.Type1)
        self.pushButton_2.clicked.connect(self.Type2)
        self.pushButton_3.clicked.connect(self.Type3)
        self.pushButton_4.clicked.connect(self.Type4)
        self.pushButton_5.clicked.connect(self.Type5)
        self.pushButton_6.clicked.connect(self.Type6)
        self.pushButton_7.clicked.connect(self.Type7)
        self.pushButton_8.clicked.connect(self.Type8)
        self.pushButton_9.clicked.connect(self.Type9)
        self.pushButton_0.clicked.connect(self.Type0)
        self.pushButton_11.clicked.connect(self.plus)
        self.pushButton_12.clicked.connect(self.minus)
        self.pushButton_13.clicked.connect(self.div)
        self.pushButton_14.clicked.connect(self.mul)
        self.pushButton_15.clicked.connect(self.eval)
        self.pushButton_del.clicked.connect(self.delete)
        self.pushButton_backspace.clicked.connect(self.backspace)
        self.pushButton_point.clicked.connect(self.point)
        self.stroka = ''
        
    def Type1(self):
        self.stroka = self.stroka + '1'
        self.textEdit.setText(self.stroka)
        
    def Type2(self):
        self.stroka = self.stroka + '2'
        self.textEdit.setText(self.stroka)
        
    def Type3(self):
        self.stroka = self.stroka + '3'
        self.textEdit.setText(self.stroka)
        
    def Type4(self):
        self.stroka = self.stroka + '4'
        self.textEdit.setText(self.stroka)
        
    def Type5(self):
        self.stroka = self.stroka + '5'
        self.textEdit.setText(self.stroka)
        
    def Type6(self):
        self.stroka = self.stroka + '6'
        self.textEdit.setText(self.stroka)
        
    def Type7(self):
        self.stroka = self.stroka + '7'
        self.textEdit.setText(self.stroka)
        
    def Type8(self):
        self.stroka = self.stroka + '8'
        self.textEdit.setText(self.stroka)
        
    def Type9(self):
        self.stroka = self.stroka + '9'
        self.textEdit.setText(self.stroka)
        
    def Type0(self):
         self.stroka = self.stroka + '0'
         self.textEdit.setText(self.stroka)

    def plus(self):
         self.stroka = self.stroka + ' + '
         self.textEdit.setText(self.stroka)
         
    def minus(self):
         self.stroka = self.stroka + ' - '
         self.textEdit.setText(self.stroka)
         
    def div(self):
         self.stroka = self.stroka + ' / '
         self.textEdit.setText(self.stroka)
    
    def mul(self):
         self.stroka = self.stroka + ' * '
         self.textEdit.setText(self.stroka)
    
    def point(self):
        if len(self.stroka) == 0 or self.stroka[len(self.stroka)-1] == ' ':
            self.stroka = self.stroka + '0.'
        else:
            self.stroka = self.stroka + '.'
        self.textEdit.setText(self.stroka)
         
    def eval(self):
         a,znak,b = self.stroka.split()
         a,b = map(float, (a,b))
         if znak == '+':
             c = a + b
         elif znak == '-':
             c = a - b
         elif znak == '*':
             c = a * b
         elif znak == '/':
             c = a / b
         self.textEdit.setText(str(c))
         stroka = ''
         
    def delete(self):
         self.stroka = ''
         self.textEdit.setText(self.stroka)
    
    def backspace(self):
         if len(self.stroka) == 0:
             self.stroka = ''
         elif self.stroka[len(self.stroka)-1] == ' ':
             self.stroka = self.stroka[0:len(self.stroka) - 3]
         else:
             self.stroka = self.stroka[0:len(self.stroka) - 1]
         self.textEdit.setText(self.stroka)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())