from setuptools import find_packages
from setuptools import setup

packages = find_packages()

setup(
    author="somewheve",
    description="An easy use Event engine based on asyncio, just so so...",
    version="0.1",
    author_email='somewheve@gmail.com',
    packages=packages,
    name="async_event",
)
