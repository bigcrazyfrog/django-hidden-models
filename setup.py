import re

from setuptools import setup, find_packages


def get_version():
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")

    with open('hidden_models/__init__.py', 'r') as f:
        for line in f:
            match = version_re.match(line.strip())
            if match:
                return match.groups()[0]

    raise RuntimeError("Unable to find version string.")


setup(
    name='django-hidden-models',
    version=get_version(),
    use_scm_version={"version_scheme": "post-release"},
    author='Nikita Cibin',
    author_email='cibinnikita@gmail.com',
    description='Simply hiding a useless data from query results',
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    url='https://github.com/bigcrazyfrog/django-hidden-models',
    license="BSD",
    packages=find_packages(exclude=['tests*']),
    python_requires=">=3.8",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
    ],
    zip_safe=False,
    keywords=['django', 'hidden', 'hide', 'visible', 'models'],
    package_data={
        'model_utils': [
            'locale/*/LC_MESSAGES/django.po',
            'locale/*/LC_MESSAGES/django.mo',
            'py.typed',
        ],
    },
)
