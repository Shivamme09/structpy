from setuptools import setup, find_packages

setup (
		name = "structpy",
		version = "1.0.0",
		description = "Package implements all the data strucures",
		packages = find_packages(exclude=['tests']),
		author = "Mayank Chandravanshi",
		author_email = "mayank11195@gmail.com",
)