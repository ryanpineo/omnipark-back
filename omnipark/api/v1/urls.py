from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

# Login
from .login.views import LoginViewSet  # noqa

router.register(r'login', LoginViewSet, base_name='login')

# Parking
from .parking.views import SpotsViewSet, BookingsViewSet  # noqa

router.register(r'spots', SpotsViewSet, base_name='spots')
router.register(r'bookings', BookingsViewSet, base_name='bookings')
