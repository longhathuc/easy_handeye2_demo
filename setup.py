import os
from glob import glob
from setuptools import setup

package_name = 'easy_handeye2_demo'

def files_in(dirpath):
    # include all files under dirpath (handles nested dirs)
    return [f for f in glob(os.path.join(dirpath, '**'), recursive=True) if os.path.isfile(f)]

setup(
    name=package_name,
    version='0.5.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Install launch/ (you already had this)
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*'))),

        # Install config/
        (os.path.join('share', package_name, 'config'), files_in('config')),

        # (optional) other resource dirs if you have them:
        # (os.path.join('share', package_name, 'rviz'), files_in('rviz')),
        # (os.path.join('share', package_name, 'urdf'), files_in('urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Marco Esposito',
    maintainer_email='esposito@imfusion.com',
    description='Playground for a hand-eye calibration with easy_handeye2, no hardware required.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tracking_simulator = easy_handeye2_demo.tracking_simulator:main'
        ],
    },
)
