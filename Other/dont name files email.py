import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("band.mishaps@gmail.com", "Ipad10thbday")
msg = "YOUR MESSAGE!"
server.sendmail("band.mishaps", "wwdennis.home@gmail.com", msg)
server.quit()
