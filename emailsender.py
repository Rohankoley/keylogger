import smtplib
import ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "faltuuse7734@gmail.com"  
    password = "bqow dbif biee bwhi" 
    receiver_email = "rohankoley91@gmail.com" 

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
