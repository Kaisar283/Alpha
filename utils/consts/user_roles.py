from django.db import models


class CustomUserRolesChoices(models.TextChoices):
    ADMIN = 'Administrator', 'Администратор'
    EDITOR = 'Editor', 'Редактор'
    CONTRIBUTOR = 'Contributor', 'Участник'
    USER = 'user', 'Пользователь'