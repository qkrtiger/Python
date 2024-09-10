import sys
import time
import threading
import requests
import configparser
from PyQt5.QtCore import QThread, QTimer, pyqtSignal
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.keep_running = True
        
        # 타이머 생성
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer3 = QTimer(self)

        # 타이머 타임아웃 시 쓰레드 다시 실행
        self.timer1.timeout.connect(self.start_get_receipt_data)
        self.timer2.timeout.connect(self.start_RQpdf_thread)
        self.timer3.timeout.connect(self.start_is_data_thread)

    def setupUi(self):
        # Setup the UI (pseudo-code)
        pass
    
    def stop_thread(self):
        """스레드를 종료하는 메서드"""
        self.keep_running = False

    def pushbutton2_handler(self):        
        # 쓰레드1 시작
        self.start_get_receipt_data()
        # 쓰레드2 시작
        self.start_RQpdf_thread()
        # 쓰레드3 시작
        self.start_is_data_thread()
        
        
    def start1(self):
        print('1번 쓰레드 시작')
        time.sleep(5)

    # 쓰레드 1 실행 함수
    def run_rq_thread(self):
        # self.rq_thread = jupsu.StartGetRQDataThread(self.csi_id, self.csi_pw)
        self.rq_thread = self.start1()
        self.rq_thread.log_signal1.connect(self.log)
        self.rq_thread.start()
        self.rq_thread.finished.connect(self.on_thread_finished1)

    # 쓰레드 2 실행 함수
    def run_rqpdf_thread(self):
        self.rq_pdf_thread = docu.StartGetRQPDFThread(self.csi_id, self.csi_pw)
        self.rq_pdf_thread.start()
        self.rq_pdf_thread.finished.connect(self.on_thread_finished2)
        
    # 쓰레드 3 실행 함수
    def run_is_thread(self):
        self.is_pdf_thread = docu.StartGetISDataThread(self.csi_id, self.csi_pw)
        self.is_pdf_thread.start()
        self.is_pdf_thread.finished.connect(self.on_thread_finished3)

    # 쓰레드 1 시작
    def start_get_receipt_data(self):
        print('1번 쓰레드 시작')
        self.csi_id = get_term('csi_id')
        self.csi_pw = get_term('csi_pw')
        
        thread1 = threading.Thread(target=self.run_rq_thread)
        thread1.start()

    # 쓰레드 2 시작
    def start_RQpdf_thread(self):
        print('2번 쓰레드 시작')
        self.csi_id = get_term('csi_id')
        self.csi_pw = get_term('csi_pw')
        
        thread2 = threading.Thread(target=self.run_rqpdf_thread)
        thread2.start()
        
    # 쓰레드 3 시작
    def start_is_data_thread(self):
        print('3번 쓰레드 시작')
        self.csi_id = get_term('csi_id')
        self.csi_pw = get_term('csi_pw')
        
        thread3 = threading.Thread(target=self.run_is_thread)
        thread3.start()

    # 쓰레드 1 종료 후 타이머 작동
    def on_thread_finished1(self):
        print('1번 쓰레드 종료, 5분 후 다시 시작')
        self.timer1.start(300000)  # 5분 후 재시작 (300,000ms)

    # 쓰레드 2 종료 후 타이머 작동
    def on_thread_finished2(self):
        print('2번 쓰레드 종료, 3분 후 다시 시작')
        self.timer2.start(180000)  # 3분 후 재시작 (180,000ms)

    # 쓰레드 3 종료 후 타이머 작동
    def on_thread_finished3(self):
        print('3번 쓰레드 종료, 10분 후 다시 시작')
        self.timer3.start(600000)  # 10분 후 재시작 (600,000ms)

    def log(self, message):
        print(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
