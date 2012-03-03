from distutils.core import setup

__version__ = '0.1'

setup(name='s3grep',
      version=__version__,
      description='Parallelized grep for Amazon S3',
      license='MIT',
      author='Barnaby Gray',
      author_email='barnaby@pickle.me.uk',
      url='http://github.com/barnybug/s3grep/',
      requires=['boto'],
      scripts=['s3grep'],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
      )
