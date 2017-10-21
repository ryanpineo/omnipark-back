from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)


# Login
from .login.views import LoginViewSet  # noqa

router.register(r'login', LoginViewSet, base_name='login')
