from setuptools import setup,find_packages
#import versioneer

setup(
    author_email = "e.tuidhana@yandex.ru",
    description = "Laffka torshop",
    license = "BSD",
    name='laffka',
    version='1.01',
    long_description='Laffkashop developed with tor in mind.',
    packages=find_packages(exclude='__pycharm__'),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask','requests','Flask-APScheduler','Flask-WTF','bitmerchant','Flask-Login','Flask-Session','waitress']
)