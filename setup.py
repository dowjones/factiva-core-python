from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_desc = fh.read()

setup(
    name='factiva-core',     # This is the name to be pip-installed
    version='0.0.1',
    description='Python package with root definitions and dictionaries, to support other functional packages.',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    author='Miguel Ballesteros',
    author_email='miguel.ballesteros@dowjones.com',
    # package_dir={'': 'factiva'},
    packages=find_packages(include=['factiva', 'factiva.*'], exclude=['test', 'docs']),  # Required
    # packages=['core'],
    url='https://github.com/dowjones/factiva-core-python',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='news, news aggregator, risk, compliance, nlp, alternative data',  # Optional

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.5',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['pandas>=1.0.3', 'fastavro>=0.23.0', 'requests>=2.23.0']  # Optional
    install_requires=['requests', 'pandas', 'numpy']  # Optional
)
