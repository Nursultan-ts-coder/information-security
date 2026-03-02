from email.message import EmailMessage
import smtplib


# Email server details (for example, Gmail's SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "nurssafranbolu@gmail.com"
sender_password = "my_password"     # Replace with your email password or app-specific password
receiver_email = "nurstunguch@gmail.com"
app_password = "my_app_password"  # Replace with your app-specific password if using Gmail

# HTML email content
subject = "Daily report"

# Set up the MIME
message = EmailMessage()
message.set_content("This is a daily report email.")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


   

# Send the email
try:
   # Establish a secure session with the server
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()  # Secure the connection
   server.login(sender_email, app_password)  # Log into the email server
   text = message.as_string()
   server.sendmail(sender_email, receiver_email, text)  # Send the email
   print("Email sent successfully!")
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()  # Close the connection
