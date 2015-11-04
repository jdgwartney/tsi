#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from distutils.core import setup

setup(
    name='tsi',
    version='0.1.0',
    url="http://www.bmc.com",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['tsi', ],
    scripts=[
        'bin/tsi-cli',
    ],
    package_data={'tsi': ['templates/*']},
    license='LICENSE.txt',
    description='Command line tools for TrueSight Intelligence',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
    ],
)
