from setuptools import setup

with open("README.rst", "r") as fh:
    long_desc = fh.read()

with open('src/factiva/core/__version__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

setup(
    name='factiva-core',
    version=version,
    description='Python package with root definitions and dictionaries, to support other functional packages.',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    author='Dow Jones Customer Engineers',
    author_email='customer.solutions@dowjones.com',
    # Warning: the folder 'factiva' should NOT have an __init__.py file to avoid conflicts with the same namespace across other packages
    package_dir={'': 'src'},
    packages=['factiva.core', 'factiva.helper', 'factiva.core.dicts', 'factiva.core.const', 'factiva.core.auth'],
    package_data={'': ['*.csv']},
    url='https://github.com/dowjones/factiva-core-python',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='news, news aggregator, risk, compliance, nlp, alternative data',
    python_requires='>=3.6',
    install_requires=['requests', 'pandas', 'numpy'],
)
