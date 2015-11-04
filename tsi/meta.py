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

from api_object import ApiObject


class Meta(ApiObject):

    def __init__(self, attributes=None, id=None, metrics=None, name=None):
        ApiObject.__init__(self)
        self._attributes = attributes
        self._id = id
        self._metrics = metrics
        self._name = name

    @property
    def attributes(self):
        return self._attributes

    @property
    def id(self):
        return self._id

    @property
    def metrics(self):
        return self._metrics

    @property
    def name(self):
        return self._name
