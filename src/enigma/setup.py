from setuptools import setup, find_packages


setup(
    name="enigmapython",
    version="0.1.0",
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['enigmapython'],  # ['*'] by default
    ),
    long_description=open('./enigmapython/README.txt').read(),
    long_description_content_type='text/markdown'
)