import smtplib
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login("python7512@outlook.com", "Baobab7512")
msg = "YOUR MESSAGE!"
server.sendmail("python7512@outlook.com", "python7512@outlook.com", msg)
server.quit()
