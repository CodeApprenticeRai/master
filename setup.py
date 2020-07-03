from setuptools import setup
from pip.req import parse_requirements


install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='master'.
    version='0.0.1',
    description="A web application for facilitating mastery of a defined skillset",
    author="Tare Gaskin",
    author_email="taregaskin@ufl.edu",
    packages=['master', 'app'],
    install_requires=reqs,
)
