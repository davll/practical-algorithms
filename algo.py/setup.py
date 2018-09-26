from setuptools import setup

setup(name='algo',
      version='0.1',
      description='Library of Algorithms',
      url='https://github.com/davll/progprac',
      author='David Lin',
      author_email='davll.xc@gmail.com',
      license='MIT',
      packages=['algo'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
