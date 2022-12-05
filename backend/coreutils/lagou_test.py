from django.contrib.auth import get_user_model


class LagouTestUtils:
    @staticmethod
    def create_test_superuser():
        """
        Override this method to return an instance of your custom user model
        """
        user_model = get_user_model()
        # Create a user
        user_data = {
            user_model.USERNAME_FIELD: 'test@email.com',
            'email': 'test@email.com',
            'password': 'password'
        }

        for field in user_model.REQUIRED_FIELDS:
            if field not in user_data:
                user_data[field] = field

        return user_model.objects.create_superuser(**user_data)

    @staticmethod
    def create_user(username, email=None, password=None, **kwargs):
        # wrapper for get_user_model().objects.create_user that works
        # interchangeably for user models with and without a username field

        user_model = get_user_model()
        kwargs["email"] = email or "%s@test.com" % username
        kwargs["password"] = password
        if user_model.USERNAME_FIELD != "email":
            kwargs[user_model.USERNAME_FIELD] = username

        return user_model.objects.create_user(**kwargs)

    @staticmethod
    def create_superuser(username, email=None, password=None, **kwargs):
        # wrapper for get_user_model().objects.create_user that works
        # interchangeably for user models with and without a username field

        user_model = get_user_model()

        kwargs["email"] = email or "%s@example.com" % username
        kwargs["password"] = password
        if user_model.USERNAME_FIELD != "email":
            kwargs[user_model.USERNAME_FIELD] = username

        return user_model.objects.create_superuser(**kwargs)
