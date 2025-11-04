import random
import secrets
from datetime import datetime, timedelta

def generate_otp(length=6):
    """Generate a secure OTP of specified length."""
    # Using secrets for cryptographically strong random numbers
    return ''.join(secrets.choice('0123456789') for _ in range(length))

def format_otp_message(otp):
    """Format the OTP with a nice message."""
    return f"""
=== Secure OTP Generation ===
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Your OTP: {otp}
Valid for: 5 minutes
Expires at: {(datetime.now() + timedelta(minutes=5)).strftime('%H:%M:%S')}

Please don't share this OTP with anyone.
===============================
"""

def verify_otp(generated_otp, user_input):
    """Verify if the user-provided OTP matches the generated one."""
    return secrets.compare_digest(generated_otp, user_input)

if __name__ == "__main__":
    try:
        # Generate OTP
        print("\nGenerating secure OTP...")
        otp = generate_otp()
        
        # Display OTP with formatted message
        print(format_otp_message(otp))
        
        # Simulate OTP verification
        print("=== OTP Verification ===")
        user_input = input("Please enter the OTP: ")
        
        if verify_otp(otp, user_input):
            print("\n✓ OTP verified successfully!")
        else:
            print("\n✗ Invalid OTP. Please try again.")
            
    except Exception as e:
        print(f"\nError: {str(e)}")
