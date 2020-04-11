# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ExportCustomJobList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, resource_type):
        """
        Initialize the ExportCustomJobList

        :param Version version: Version that contains the resource
        :param resource_type: The type of communication – Messages, Calls

        :returns: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobList
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobList
        """
        super(ExportCustomJobList, self).__init__(version)

        # Path Solution
        self._solution = {'resource_type': resource_type, }
        self._uri = '/Exports/{resource_type}/Jobs'.format(**self._solution)

    def stream(self, next_token=values.unset, previous_token=values.unset,
               limit=None, page_size=None):
        """
        Streams ExportCustomJobInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode next_token: The token for the next page of job results
        :param unicode previous_token: The token for the previous page of result
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            next_token=next_token,
            previous_token=previous_token,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, next_token=values.unset, previous_token=values.unset, limit=None,
             page_size=None):
        """
        Lists ExportCustomJobInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode next_token: The token for the next page of job results
        :param unicode previous_token: The token for the previous page of result
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance]
        """
        return list(self.stream(
            next_token=next_token,
            previous_token=previous_token,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, next_token=values.unset, previous_token=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param unicode next_token: The token for the next page of job results
        :param unicode previous_token: The token for the previous page of result
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ExportCustomJobInstance
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobPage
        """
        params = values.of({
            'NextToken': next_token,
            'PreviousToken': previous_token,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ExportCustomJobPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ExportCustomJobInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ExportCustomJobInstance
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ExportCustomJobPage(self._version, response, self._solution)

    def create(self, friendly_name=values.unset, start_day=values.unset,
               end_day=values.unset, webhook_url=values.unset,
               webhook_method=values.unset, email=values.unset):
        """
        Create a new ExportCustomJobInstance

        :param unicode friendly_name: The friendly_name
        :param unicode start_day: The start_day
        :param unicode end_day: The end_day
        :param unicode webhook_url: The webhook_url
        :param unicode webhook_method: The webhook_method
        :param unicode email: The email

        :returns: Newly created ExportCustomJobInstance
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'StartDay': start_day,
            'EndDay': end_day,
            'WebhookUrl': webhook_url,
            'WebhookMethod': webhook_method,
            'Email': email,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ExportCustomJobInstance(
            self._version,
            payload,
            resource_type=self._solution['resource_type'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.BulkExports.ExportCustomJobList>'


class ExportCustomJobPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the ExportCustomJobPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param resource_type: The type of communication – Messages, Calls

        :returns: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobPage
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobPage
        """
        super(ExportCustomJobPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ExportCustomJobInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance
        """
        return ExportCustomJobInstance(
            self._version,
            payload,
            resource_type=self._solution['resource_type'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.BulkExports.ExportCustomJobPage>'


class ExportCustomJobInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, resource_type):
        """
        Initialize the ExportCustomJobInstance

        :returns: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance
        :rtype: twilio.rest.preview.bulk_exports.export.export_custom_job.ExportCustomJobInstance
        """
        super(ExportCustomJobInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'friendly_name': payload.get('friendly_name'),
            'resource_type': payload.get('resource_type'),
            'start_day': payload.get('start_day'),
            'end_day': payload.get('end_day'),
            'webhook_url': payload.get('webhook_url'),
            'webhook_method': payload.get('webhook_method'),
            'email': payload.get('email'),
            'job_sid': payload.get('job_sid'),
            'details': payload.get('details'),
        }

        # Context
        self._context = None
        self._solution = {'resource_type': resource_type, }

    @property
    def friendly_name(self):
        """
        :returns: The friendly name specified when creating the job
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def resource_type(self):
        """
        :returns: The type of communication – Messages, Calls
        :rtype: unicode
        """
        return self._properties['resource_type']

    @property
    def start_day(self):
        """
        :returns: The start time for the export specified when creating the job
        :rtype: unicode
        """
        return self._properties['start_day']

    @property
    def end_day(self):
        """
        :returns: The end time for the export specified when creating the job
        :rtype: unicode
        """
        return self._properties['end_day']

    @property
    def webhook_url(self):
        """
        :returns: The optional webhook url called on completion
        :rtype: unicode
        """
        return self._properties['webhook_url']

    @property
    def webhook_method(self):
        """
        :returns: This is the method used to call the webhook
        :rtype: unicode
        """
        return self._properties['webhook_method']

    @property
    def email(self):
        """
        :returns: The optional email to send the completion notification to
        :rtype: unicode
        """
        return self._properties['email']

    @property
    def job_sid(self):
        """
        :returns: The job_sid returned when the export was created
        :rtype: unicode
        """
        return self._properties['job_sid']

    @property
    def details(self):
        """
        :returns: The details
        :rtype: dict
        """
        return self._properties['details']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.BulkExports.ExportCustomJobInstance>'
