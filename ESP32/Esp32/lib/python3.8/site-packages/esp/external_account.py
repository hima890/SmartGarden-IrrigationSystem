import uuid
import json

from .resource import (ESPResource,
					   POST_REQUEST,
					   DELETE_REQUEST,
					   GET_REQUEST,
					   PATCH_REQUEST)
from .sdk import make_endpoint

class ExternalAccount(ESPResource):

        # Note that this will not actually show the endpoint URL itself..it is
        # displayed only upon creation. This helps determine whether one exists
	def show_ua_endpoint(self):
		endpoint = make_endpoint('/'.join([ExternalAccount._resource_path(self.id_),'user_attribution', 'channel']))
		serialized = json.dumps({'data': {'type': 'channel'}})
		response = self._make_request(endpoint, GET_REQUEST, data=serialized)
		data = response.json()
		if response.status_code != 200:
			return response
		return data

	def create_ua_endpoint(self):
		endpoint = make_endpoint('/'.join([ExternalAccount._resource_path(self.id_),'user_attribution', 'channel']))
		serialized = json.dumps({'data': {'type': 'channel'}})
		response = self._make_request(endpoint, POST_REQUEST, data=serialized)
		data = response.json()
		if response.status_code != 200:
			return response
		return data

	def destroy_ua_endpoint(self):
		endpoint = make_endpoint('/'.join([ExternalAccount._resource_path(self.id_),'user_attribution', 'channel']))
		serialized = json.dumps({'data': {'type': 'channel'}})
		response = self._make_request(endpoint, DELETE_REQUEST, data=serialized)
		data = response.json()
		if response.status_code != 200:
			return response
		return data

	def update_cloudtrail_name(self, cloudtrail_name):
		endpoint = make_endpoint('/'.join([ExternalAccount._resource_path(self.id_),'user_attribution']))
		serialized = json.dumps({'data': {'type': 'external_accounts', 'attributes': {'cloudtrail_name': cloudtrail_name}}})
		response = self._make_request(endpoint, PATCH_REQUEST, data=serialized)
		data = response.json()
		if response.status_code != 200:
			return response
		return data

	@classmethod
	def create(cls, **kwargs):
		if 'external_id' not in kwargs:
			kwargs['external_id'] = str(uuid.uuid4())
		return super(ExternalAccount, cls).create(**kwargs)
