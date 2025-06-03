import importlib
import inspect
import pathlib

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet

# Set up a router
router = DefaultRouter()

# Path to this directory
base_path = pathlib.Path(__file__).parent

# Look for files like ch_1_1.py, ch_1_2.py, etc.
for file in base_path.glob("ch_2_*.py"):
    module_name = file.stem
    module_path = f"{__package__}.{module_name}"

    # Import the module dynamically
    module = importlib.import_module(module_path)

    # Look for a class like challenge_2_1_ViewSet
    expected_class_name = (
        f"challenge_{module_name.split('_')[1]}_{module_name.split('_')[2]}_ViewSet"
    )

    for name, cls in inspect.getmembers(module, inspect.isclass):
        if (
            name == expected_class_name
            and issubclass(cls, ViewSet)
            and cls.__module__ == module.__name__
        ):
            router.register(
                rf"{name.lower().replace('viewset', '')}", cls, basename=name.lower()
            )

urlpatterns = [
    path("api/", include(router.urls)),
]
