from setuptools import setup

__version__ = '0.2'

setup(name='s3grep',
      version=__version__,
      description='Parallelized grep for Amazon S3',
      license='MIT',
      author='Barnaby Gray',
      author_email='barnaby@pickle.me.uk',
      url='http://loads.pickle.me.uk/s3grep/',
      install_requires=['boto'],
      scripts=['s3grep'],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
      )
