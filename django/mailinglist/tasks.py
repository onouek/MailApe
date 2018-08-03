from celery import shared_task

from mailinglist import emails


@shared_task
def send_confirmation_email_to_subscriber(subscriber_id):
    from mailinglist.models import Subscriber
    subscriber = Subscriber.objects.get(id=subscriber_id)
    emails.send_confirmation_email(subscriber)

@shared_task
def send_subscriber_message(subscriber_message_id):
    from mailinglist.models import SubscriberMessage
    subscriber_message = SubscriberMessage.objects.get(
        id=subscriber_message_id)
    emails.send_subscriber_message(subscriber_message)