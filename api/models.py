from django.db import models


SOCIAL_NETWORK_CHOISES = [
    ('vk', 'VKontacte'),
    ('google', 'Google'),
    ('yandex', 'Yandex'),
]

LOGIN_STAGES = [
    (1, 'request_created'),
    (2, 'login_started'),
    (3, 'login_completed'),
]


class LoginRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    social_network = models.CharField(choices=SOCIAL_NETWORK_CHOISES, max_length=20)
    stage = models.CharField(choices=LOGIN_STAGES, max_length=30)

    class Meta:
        ordering = ('created',)

