from setuptools import setup, find_packages

from feincms_jobs import get_version


setup(
    name = 'feincms-jobs',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'Django',
        'FeinCMS',
    ],
    version = get_version(),
    description = 'A FeinCMS Plugin for job listings.',
    author = 'Incuna Ltd',
    author_email = 'dev@incuna.com',
    url = 'http://github.com/incuna/feincms-jobs',
    long_description = open('README.markdown', 'r').read()
)
