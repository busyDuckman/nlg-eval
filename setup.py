#!/usr/bin/env python2.7

from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt', session=False)
# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='nlg-eval',
      version='1.0',
      description='Wrapper for multiple NLG evaluation methods and metrics',
      author='Shikhar Sharma, Hannes Schulz',
      author_email='shikhar.sharma@microsoft.com, hannes.schulz@microsoft.com',
      url='http://github.com/Maluuba/nlg-eval',
      packages=['nlgeval'],
      scripts=['bin/nlg-eval'],
      install_requires=reqs)

