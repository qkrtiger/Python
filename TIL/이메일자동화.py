import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# 이메일 설정
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'

# 수신자 이메일 주소와 보고서 내용
RECIPIENT_EMAIL = 'recipient_email@example.com'
SUBJECT = 'Daily Report'
BODY = 'This is the daily report content.'

def send_email():
    # 이메일 메시지 생성
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = SUBJECT
    
    # 이메일 본문 추가
    msg.attach(MIMEText(BODY, 'plain'))
    
    # 이메일 전송
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print(f"Email sent to {RECIPIENT_EMAIL}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# 스케줄링: 매일 특정 시간에 이메일 전송
schedule.every().day.at("09:00").do(send_email)  # 09:00에 이메일 전송

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
