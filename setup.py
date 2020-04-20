from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_desc = fh.read()

setup(
    name='factiva-core',
    version='0.0.2',
    description='Python package with root definitions and dictionaries, to support other functional packages.',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    author='Miguel Ballesteros',
    author_email='miguel.ballesteros@dowjones.com',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={'': ['*.csv']},
    url='https://github.com/dowjones/factiva-core-python',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'Topic :: Office/Business :: News/Diary',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='news, news aggregator, risk, compliance, nlp, alternative data',
    python_requires='>=3.5',
    install_requires=['requests', 'pandas', 'numpy']
)
