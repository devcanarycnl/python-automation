import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_email(sender_email, app_password, receiver_email, subject, message):
    print("\n=== Email Sending Process Started ===")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Create message container
        print("\nPreparing email...")
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(message, 'plain'))

        # Create SMTP session
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS
        
        # Login to server
        print("Logging into Gmail...")
        server.login(sender_email, app_password)
        
        # Send email
        print("Sending email...")
        server.send_message(msg)
        
        print("\n✓ Email sent successfully!")
        
    except smtplib.SMTPAuthenticationError:
        print("\n✗ Error: Authentication failed!")
        print("Please make sure you're using an App Password, not your regular Gmail password.")
        print("To generate an App Password:")
        print("1. Go to your Google Account settings")
        print("2. Enable 2-Step Verification if not already enabled")
        print("3. Go to Security > App Passwords")
        print("4. Generate a new App Password for 'Mail'")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        
    finally:
        try:
            print("\nClosing SMTP connection...")
            server.quit()
        except:
            pass
        print("=== Process Complete ===")

if __name__ == "__main__":
    # Email configuration
    sender_email = "your.email@gmail.com"  # Replace with your Gmail
    app_password = "your-app-password"      # Replace with your App Password
    receiver_email = "recipient@email.com"  # Replace with recipient's email
    
    # Email content
    subject = "Test Email from Python"
    message = """
    Hello!
    
    This is a test email sent from Python.
    
    Best regards,
    Python Script
    """
    
    # Send the email
    send_email(sender_email, app_password, receiver_email, subject, message)
