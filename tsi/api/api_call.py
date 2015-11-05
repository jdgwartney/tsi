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

import json
import requests
import urllib
import logging


class ApiCall(object):
    def __init__(self, **kwargs):
        """
        :param kwargs
        :return: returns nothing

        :Example:

        """
        self._methods = {"DELETE": self._do_delete,
                         "GET": self._do_get,
                         "POST": self._do_post,
                         "PUT": self._do_put}
        self._auth_methods = ['basic']
        self._schemes = ["http", "https"]

        # All member variables related to REST CALL
        self._auth = None
        self._data = None
        self._headers = None
        self._host = None
        self._user = None
        self._method = None
        self._password = None
        self._path = None
        self._query_parameters = None
        self._scheme = None
        self._url = None

        # Stores api result
        self._api_result = None

        # Sets the log level
        self._logLevel = None


    #
    # data
    #

    @property
    def data(self):
        """
        Value of the HTTP payload
        :return:
        """
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    #
    # headers
    #

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers
    #
    # method
    #

    @property
    def method(self):
        """
        """
        return self._method

    @method.setter
    def method(self, value):
        """
        Before assigning the value validate that is in one of the
        HTTP methods we implement
        """
        keys = self._methods.keys()
        if value not in keys:
            raise AttributeError("Method value not in " + str(keys))
        else:
            self._method = value

    #
    # path
    #

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def query_parameters(self):
        return self._url_parameters

    #
    #
    @query_parameters.setter
    def query_parameters(self, value):
        self._query_parameters = value

    @query_parameters.setter
    def query_parameters(self, url_parameters):
        self._query_parameters = url_parameters

    def _query_parameters(self):
        """
        Encode URL parameters
        """
        url_parameters = ''
        if self._url_parameters is not None:
            url_parameters = '?' + urllib.urlencode(self._url_parameters)
        return url_parameters

    def get_api_parameters(self):
        pass

    def _do_get(self):
        """
        HTTP Get Request
        """
        return requests.get(self._url, data=self._data, headers=self._headers, auth=(self._email, self._api_token))

    def _do_delete(self):
        """
        HTTP Delete Request
        """
        return requests.delete(self._url, data=self._data, headers=self._headers, auth=(self._email, self._api_token))

    def _do_post(self):
        """
        HTTP Post Request
        """
        return requests.post(self._url, data=self._data, headers=self._headers, auth=(self._email, self._api_token))

    def _do_put(self):
        """
        HTTP Put Request
        """
        return requests.put(self._url, data=self._data, headers=self._headers, auth=(self._email, self._api_token))

    def _call_api(self):
        """
        Make an API call to get the metric definition
        """

        self._url = "{0}://{1}/{2}{3}".format(self._scheme, self._api_host, self._path, self._query_parameters())
        if self._headers is not None:
            logging.debug(self._headers)
        if self._data is not None:
            logging.debug(self._data)
        if len(self._get_url_parameters()) > 0:
            logging.debug(self._get_url_parameters())

        result = self._methods[self._method]()
        self._api_result = result
        self._status_code = result.status_code

    def handle_api_results(self, status_code, results):
        result = None
        # Only process if we get HTTP result of 200
        if self._api_result.status_code == requests.codes.ok:
            result = json.loads(self._api_result.text)
        return result

    def api_call(self):
        self.get_api_parameters()
        self._call_api()
        return self.handle_api_results(self._api_result, self._status_code)

