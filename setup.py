from setuptools import setup

setup(
    name='Laffka',
    version='1.00',
    long_description='Laffkastop developed with tor in mind.',
    packages=['laffka'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask','requests','Flask-APScheduler','Flask-WTF','bitmerchant','Flask-Login','Flask-Session','waitress']
)