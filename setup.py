from setuptools import setup

requirements = ['networkx>=1.9', 'scipy>=0.15', 'numpy>=1.9.1']

setup(
    name='Spanning-centrality',
    install_requires=requirements,
    packages=['spanning-centrality'],
    test_suite='nose.collector',
    tests_require=['nose']
)
