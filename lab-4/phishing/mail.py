import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email server details (for example, Gmail's SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "nurssafranbolu@gmail.com"
sender_password = "my_password"     # Replace with your email password or app-specific password
receiver_email = "nurstunguch@gmail.com"
app_password = "my_app_password"  # Replace with your app-specific password if using Gmail


# HTML email content
subject = "Instagram Login Required"

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Attach the body with the HTML content
# Read HTML from an external file
html_file_path = "email-template.html"  # Path to your HTML file

try:
    with open(html_file_path, "r", encoding="utf-8") as file:
        body = file.read()
except FileNotFoundError:
    print(f"Error: {html_file_path} not found")
    exit()

# ... rest of your code ...

# Attach the body with the HTML content (same as before)
message.attach(MIMEText(body, "html"))


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
