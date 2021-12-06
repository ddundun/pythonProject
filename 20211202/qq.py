import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from bs4 import BeautifulSoup
from urllib import parse, request

form_class = uic.loadUiType("dmdkdkr.ui")[0]

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
        if (w1==None):
            QMessageBox.about(self,"경고","한국지역만 검색가능^^/이상한거 검색노노")
            # alert = QMessageBox(self)
            # alert.setText("한국지역만 검색가능/이상한거 검색ㄴㄴ")
            # alert.exec_()
        else:
            w1 = w1.get_text()
            n1 = n1.get_text()
            c1 = c1.get_text() #습도, 강수확률
            self.label_1.setText('현재날씨 '+w1)
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)

            # print(w1)
            # print(c1)
            n2= n1.split()
            # print(n2)
            w2 = w1.split()

            c2= c1.split()
            c3= c2[4:8]
            c4= ' '.join(c3)
            print(c4)


            self.label_7.setText(c4)
            self.label_7.setAlignment(QtCore.Qt.AlignCenter)


            n23 = (n2[0:11])
            n32 = n2[11:]
            # print(n32)
            n3= n2[3].split('온도')
            # print(n3)
            w3 = w2[2].split('온도')

            w4 = w3[1].split('°')

            if (int(w4[0]) <= 4):
                self.label_2.setText("패딩 추천")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                self.label_4.setPixmap(QPixmap("4.png"))
                self.show()

            elif (int(w4[0]) < 8):
                self.label_2.setText("코트 추천")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                pixmap = QPixmap("8.png")
                self.label_4.setPixmap(QPixmap(pixmap))

                self.show()

            elif (int(w4[0]) < 15):
                self.label_2.setText("자켓 추천")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                pixmap = QPixmap("8.png")
                self.label_4.setPixmap(QPixmap(pixmap))
                self.show()
            # elif ((w4[0])==' '):
            #     alert = QMessageBox(self)
            #     alert.setText("한국지역만 검색가능^^")
            #     alert.exec_()



if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()