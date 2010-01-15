APP_NAME = 'divioadmin'
DESCRIPTION = "django admin modifications for the divio theme"

from setuptools import setup, find_packages
import os

version = __import__(APP_NAME).__version__

media_files = []
for dir in ['%s/media' % APP_NAME,'%s/templates' % APP_NAME]:
    for dirpath, dirnames, filenames in os.walk(dir):
        media_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
    'setuptools',
]

setup(
    name = "django-%s"  % APP_NAME,
    version = version,
    url = 'http://github.com/divio/django-%s' % APP_NAME,
    license = 'BSD',
    platforms=['OS Independent'],
    description = DESCRIPTION,
    long_description = read('README'),
    author = 'Divio GmbH',
    author_email = 'developers@divio.ch',
    packages=find_packages(),
    install_requires = install_requires,
    package_data={
        '': ['*.txt', '*.rst',],
    },
    package_dir = {
        APP_NAME:APP_NAME,
    },
    data_files = media_files,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
