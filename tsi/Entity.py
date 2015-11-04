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

from tsi.api_object import ApiObject


class Entity(ApiObject):

    def __init__(self,
                 cfg_attr_values=None,
                 entity_id=None,
                 entity_type_id=None,
                 name=None,
                 parent_entity_type_id=None,
                 parent_entity_id=None,
                 source_id=None
                 ):
        ApiObject.__init__(self)

        self._cfg_attr_values = cfg_attr_values
        self._entity_id = entity_id
        self._entity_type_id = entity_type_id
        self._name = name
        self._parent_entity_type_id=parent_entity_type_id
        self._parent_entity_id=parent_entity_id
        self._source_id = source_id
        self._tags = None

    @property
    def cfg_attr_values(self):
        return self._cfg_attr_values

    @property
    def entity_type_id(self):
        return self._entity_type_id

    @property
    def name(self):
        return self._name

    @property
    def source_id(self):
        return self._source_id

    @property
    def tags(self):
        return self._tags



# newEntity =  {
#     "entity_type_id": "APPLICATION",
#     "name": "Online Auction",
#     "tags": [
#         "app_id:online_auc"
#     ],
#     "cfg_attr_values": {},
#     "entity_id": "online_auc",
#     "source_id": "sample",
#     "cfg_attr_values":
#         {
#             "kpis":[
#                 {"entity_type_id":"TRANSACTION",
#                  "entity_type_name":"Transaction",
#                  "entity_id":"oa-appserver-1.bid_tx",
#                  "title":"Number of Requests",
#                  "application_id":"online_auc",
#                  "application_name":"Online Auction",
#                  "metric_name":"Number of Requests",
#                  "metric_uom":"#",
#                  "metric_id":"number_of_requests"},
#                 {"entity_type_id":"TRANSACTION",
#                  "entity_type_name":"Transaction",
#                  "entity_id":"oa-appserver-1.bid_tx",
#                  "title":"Request Response Time",
#                  "application_id":"online_auc",
#                  "application_name":"Online Auction",
#                  "metric_name":"Request Response Time",
#                  "metric_uom":"Seconds",
#                  "metric_id":"request_response_time"}
#             ]
#         }
# }
