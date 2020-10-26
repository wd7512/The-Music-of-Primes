import os
import webbrowser
import time
while True:
    for i in range(5):
        if i==0:
            s='google.com'
        if i==1:
            s='brilliant.org'
        if i==2:
            s='https://track.ucas.com/Choices/Index/1'
        if i==3:
            s='https://mail.google.com/mail/u/1/?tab=wm#inbox/FMfcgxvzLNXbLPRgXVlJfczWHpjRNgzm'
        if i==4:
            s='https://sharepoint.bristolgrammarschool.org.uk/CookieAuth.dll?GetLogon?curl=Z2FslgZ2FStudentZ2FSLGPagesZ2FViewHomework.aspx&reason=0&formdir=3'
        if i==5:
            s='https://stackoverflow.com/'
        webbrowser.open(s)
    time.sleep(6)
    os.system('taskkill /im iexplore.exe')
    time.sleep(1)
    os.system('taskkill /im MicrosoftEdge.exe /t /f')
    time.sleep(10)
    os.system('taskkill /im iexplore.exe')
    time.sleep(1)
    os.system('taskkill /im MicrosoftEdge.exe /t /f')
    time.sleep(10)
