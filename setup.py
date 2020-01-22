"""Slowest particle simulator on earth setup.

To install for development, using the commandline do:
    pip install -e /path/to/slowest_particle_simulator_on_earth
"""

from setuptools import setup

setup(name='slowest_particle_simulator_on_earth',
      version='0.0.0',
      description=('A very slow particle simulator for exploding nifti files.'),
      url='https://github.com/ofgulban/slowest-particle-simulator-on-earth',
      author='Omer Faruk Gulban',
      author_email="farukgulban@gmail.com",
      license='BSD-3-clause',
      packages=['slowest_particle_simulator_on_earth'],
      install_requires=['numpy>=1.17', 'matplotlib>=3.1', 'nibabel>=2.2'],
      keywords=['mri', 'nifti', 'particle', 'voxel', 'simulation', 'explosion'],
      zip_safe=True,
      entry_points={
        'console_scripts': [
            'slowest_particle_simulator_on_earth = slowest_particle_simulator_on_earth.__main__:main',
            ]},
      )
