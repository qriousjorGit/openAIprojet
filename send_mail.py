import smtplib

OWN_EMAIL = "ielts.trainer.2010@gmail.com"
OWN_PASSWORD = "uedjbbmhtbmbdfyn"


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

# send_email("joe", "qriousjo@yahoo.com", "2343", "just a test message")