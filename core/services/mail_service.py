import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class MailService:
    @staticmethod
    def register_mail_sender(id, to):
        template = get_template('register_mail.html')
        html_content = template.render({"id": id})
        msg = EmailMultiAlternatives('hi', 'You are registered', os.environ.get('EMAIL_HOST_USER'), [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @staticmethod
    def change_password_mail_sender(id, to):
        template = get_template('change_password_mail.html')
        html_content = template.render({"id": id})
        msg = EmailMultiAlternatives('hi', os.environ.get('EMAIL_HOST_USER'), [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
