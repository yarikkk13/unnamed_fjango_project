from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class MailService:
    @staticmethod
    def register_mail_sender(username, to):
        template = get_template('register_mail.html')
        html_content = template.render({"username": username})
        msg = EmailMultiAlternatives('hi', 'Вы зарегитрировались', 'yar.mag.adm@gmail.com', [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
