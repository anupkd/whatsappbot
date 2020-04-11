# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.ip_messaging.v1.service.user.user_channel import UserChannelList


class UserList(ListResource):
    """  """

    def __init__(self, version, service_sid):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.chat.v1.service.user.UserList
        :rtype: twilio.rest.chat.v1.service.user.UserList
        """
        super(UserList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Users'.format(**self._solution)

    def create(self, identity, role_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset):
        """
        Create a new UserInstance

        :param unicode identity: The `identity` value that identifies the new resource's User
        :param unicode role_sid: The SID of the Role assigned to this user
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param unicode friendly_name: A string to describe the new resource

        :returns: Newly created UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        data = values.of({
            'Identity': identity,
            'RoleSid': role_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return UserInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.user.UserInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UserPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a UserContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v1.service.user.UserContext
        :rtype: twilio.rest.chat.v1.service.user.UserContext
        """
        return UserContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a UserContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v1.service.user.UserContext
        :rtype: twilio.rest.chat.v1.service.user.UserContext
        """
        return UserContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.UserList>'


class UserPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with

        :returns: twilio.rest.chat.v1.service.user.UserPage
        :rtype: twilio.rest.chat.v1.service.user.UserPage
        """
        super(UserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v1.service.user.UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        return UserInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.UserPage>'


class UserContext(InstanceContext):
    """  """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the resource from
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v1.service.user.UserContext
        :rtype: twilio.rest.chat.v1.service.user.UserContext
        """
        super(UserContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Users/{sid}'.format(**self._solution)

        # Dependents
        self._user_channels = None

    def fetch(self):
        """
        Fetch a UserInstance

        :returns: Fetched UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the UserInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, role_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset):
        """
        Update the UserInstance

        :param unicode role_sid: The SID id of the Role assigned to this user
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param unicode friendly_name: A string to describe the resource

        :returns: Updated UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        data = values.of({'RoleSid': role_sid, 'Attributes': attributes, 'FriendlyName': friendly_name, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return UserInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def user_channels(self):
        """
        Access the user_channels

        :returns: twilio.rest.chat.v1.service.user.user_channel.UserChannelList
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelList
        """
        if self._user_channels is None:
            self._user_channels = UserChannelList(
                self._version,
                service_sid=self._solution['service_sid'],
                user_sid=self._solution['sid'],
            )
        return self._user_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.UserContext {}>'.format(context)


class UserInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the UserInstance

        :returns: twilio.rest.chat.v1.service.user.UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        super(UserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'attributes': payload.get('attributes'),
            'friendly_name': payload.get('friendly_name'),
            'role_sid': payload.get('role_sid'),
            'identity': payload.get('identity'),
            'is_online': payload.get('is_online'),
            'is_notifiable': payload.get('is_notifiable'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'joined_channels_count': deserialize.integer(payload.get('joined_channels_count')),
            'links': payload.get('links'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def role_sid(self):
        """
        :returns: The SID of the assigned to the user
        :rtype: unicode
        """
        return self._properties['role_sid']

    @property
    def identity(self):
        """
        :returns: The string that identifies the resource's User
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def is_online(self):
        """
        :returns: Whether the User is actively connected to the Service instance and online
        :rtype: bool
        """
        return self._properties['is_online']

    @property
    def is_notifiable(self):
        """
        :returns: Whether the User has a potentially valid Push Notification registration for the Service instance
        :rtype: bool
        """
        return self._properties['is_notifiable']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def joined_channels_count(self):
        """
        :returns: The number of Channels this User is a Member of
        :rtype: unicode
        """
        return self._properties['joined_channels_count']

    @property
    def links(self):
        """
        :returns: The absolute URLs of the Channel and Binding resources related to the user
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def url(self):
        """
        :returns: The absolute URL of the User resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a UserInstance

        :returns: Fetched UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the UserInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, role_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset):
        """
        Update the UserInstance

        :param unicode role_sid: The SID id of the Role assigned to this user
        :param unicode attributes: A valid JSON string that contains application-specific data
        :param unicode friendly_name: A string to describe the resource

        :returns: Updated UserInstance
        :rtype: twilio.rest.chat.v1.service.user.UserInstance
        """
        return self._proxy.update(role_sid=role_sid, attributes=attributes, friendly_name=friendly_name, )

    @property
    def user_channels(self):
        """
        Access the user_channels

        :returns: twilio.rest.chat.v1.service.user.user_channel.UserChannelList
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelList
        """
        return self._proxy.user_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.UserInstance {}>'.format(context)
