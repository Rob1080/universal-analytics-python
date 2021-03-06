from setuptools import setup

try:
    long_description=open('DESCRIPTION.rst', 'rt').read()
except Exception:
    long_description="Universal Analytics in Python; an implementation of Google's Universal Analytics Measurement Protocol"

setup(
    name = "universal-analytics-python",
    description = "Universal Analytics Python Module",
    long_description = long_description,

    version = "0.1",

    author = 'Sam Briesemeister',
    author_email = 'opensource@analyticspros.com',

    url = 'https://github.com/analytics-pros/universal-analytics-python',

    license = 'BSD',
    packages = ["UniversalAnalytics"],

    zip_safe = True,
)
