from django.conf import settings
from django.core.mail import send_mail

from posting.models import Letter


def send_posting_email(letter_item: Letter):
    print(letter_item.topic_letter)
    print(letter_item.body_letter)



    # send_mail(
    #     'Рассылка',
    #     f'{letter_item.topic_letter} ({letter_item.body_letter})',
    #     settings.EMAIL_HOST_USER,
    #     [letter_item.clients]
    #
    # )

# response = send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[self.user.email],
#             fail_silently=False
#         )
# print(response)
