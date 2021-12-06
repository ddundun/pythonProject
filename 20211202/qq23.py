import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from bs4 import BeautifulSoup
from urllib import parse, request

form_class = uic.loadUiType("untitled.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('images/2.png'))
        self.setupUi(self)
        self.searchbtn.clicked.connect(self.searchfn)

    def searchfn(self):

        d = (self.lineEdit.text())
        d += "날씨"
        d = parse.quote(d)
        URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + d

        source = request.urlopen(URL)
        soup = BeautifulSoup(source.read(), 'html.parser')

        w1 = soup.find("div", {"class": "weather_graphic"})
        c1 = soup.find("div", {"class": "temperature_info"})
        n1 = soup.find("ul", {"class": "weather_info_list"})
        m1 = soup.find("ul",{"class": "today_chart_list"})

        # print(t2)
        if (w1==None):
            QMessageBox.about(self,"경고","한국지역만 검색가능^^/이상한거 검색노노")

            # alert = QMessageBox(self)
            # alert.setText("한국지역만 검색가능/이상한거 검색ㄴㄴ")
            # alert.exec_()
        else:
            t1 = soup.find("dl",{"class":"info"})
            t2 = t1.find('dd').text.strip()
            t2 = t2.split()
            t2 = t2[:3]
            t2 = ' '.join(t2)
            w1 = w1.get_text()
            n1 = n1.get_text()
            c1 = c1.get_text() #습도, 강수확률
            m1 = m1.get_text()
            self.label_1.setText('현재날씨 '+w1)
            self.label_1.adjustSize()
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)


            self.label_6.setText(t2+'기준')
            self.label_6.adjustSize()
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            # print(m1)
            # # print(w1)
            # # print(c1)
            n2= n1.split()
            # # print(n2)
            w2 = w1.split()
            #
            c2= c1.split()
            c3= c2[4:8]
            c4= ' '.join(c3)
            # print(c4)
            m1 = m1.split()
            m1= m1[:4]
            m2= ' '.join(m1)

            # print(m1[1])
            # print(m2)
            self.label_3.setText(c4)
            self.label_3.adjustSize()
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)


            self.label_5.setText(m2)
            self.label_5.adjustSize()
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)

            # n23 = (n2[0:11])
            # n32 = n2[11:]
            # print(n32)
            # print(w2)
            # n3= n2[3].split('온도')
            # print(n3)
            w3 = w2[2].split('온도')

            w4 = w3[1].split('°')
            if(w2[0]=='맑음'):
                pixmap = QPixmap("3.png")
                self.label_4.setPixmap(QPixmap(pixmap))
                self.label_4.adjustSize()

                self.show()
            elif(w2[0]=='구름많음'):
                pixmap = QPixmap("1.png")
                self.label_4.setPixmap(QPixmap(pixmap))
                self.label_4.adjustSize()

            if(m1[1]=='나쁨'or m1[3]=='나쁨'):
                self.label.setText("마스크끼세용")
                self.label.adjustSize()
                self.label.setAlignment(QtCore.Qt.AlignCenter)
            else:
                self.label.setText("신선한공기마십시당")
                self.label.adjustSize()
                self.label.setAlignment(QtCore.Qt.AlignCenter)



            if (int(w4[0]) <= 4):
                self.label_2.setText("패딩 추천")
                self.label_2.adjustSize()
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                self.label_c.setPixmap(QPixmap("4.png"))
                self.label_c.adjustSize()
                self.show()

            elif (int(w4[0]) < 8):
                self.label_2.setText("코트 추천")
                self.label_2.adjustSize()
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                pixmap = QPixmap("8.png")
                self.label_c.setPixmap(QPixmap(pixmap))
                self.label_c.adjustSize()

                self.show()

            elif (int(w4[0]) < 15):
                self.label_2.setText("자켓 추천")
                self.label_2.adjustSize()
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                pixmap = QPixmap("9.png")
                self.label_c.setPixmap(QPixmap(pixmap))
                self.label_c.adjustSize()
                self.show()



if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()