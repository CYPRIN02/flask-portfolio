from flask import current_app
from flask_mail import Message
#from app import mail
from app.models import Message as MessageModel

def send_contact_notification(form_data):
    """
    Send email notification for new contact form submission
    """
    try:
        # Create message object
        message = MessageModel.create(
            name=form_data['name'],
            email=form_data['email'],
            subject=form_data['subject'],
            content=form_data['message']
        )
        
        # Prepare email
        email = Message(
            subject=f"New Contact: {message['subject']}",
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=[current_app.config['ADMIN_EMAIL']],
            body=MessageModel.format_for_email(message)
        )
        
        # Send email
        #mail.send(email)
        current_app.extensions['mail'].send(email)
        current_app.logger.info("Contact notification email sent")
        return True
        
    except Exception as e:
        current_app.logger.error(f"Error sending notification: {str(e)}")
        return False