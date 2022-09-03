from setuptools import setup, find_packages

setup(
    name='pydtc',
    version='0.2.1',
    packages=find_packages(),
    url='https://github.com/Queeq/pydtc',
    license='MIT',
    author='queeq',
    author_email='queeq@pm.me',
    description='Very basic Python realization of Data and Trading Communications (DTC) Protocol: '
                'http://dtcprotocol.org/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
    ],
    keywords='dtc protocol trading',
    install_requires=['tqdm', 'protobuf', 'pandas', 'python-dateutil']
)
