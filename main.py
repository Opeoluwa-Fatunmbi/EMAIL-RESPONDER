import smtplib
from email.mime.text import MIMEText

# Your email credentials
email = "youremail@example.com"
password = "yourpassword"

# The message to be sent
message = MIMEText("Thank you for your email. I am currently out of office and will get back to you as soon as possible.")

# Connect to the email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)

# Send the email
server.sendmail(email, sender, message.as_string())

# Disconnect from the email server
server.quit()
