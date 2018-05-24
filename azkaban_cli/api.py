# -*- coding: utf-8 -*-

"""
azkaban_cli.api

This module provides a set of requests for the Azkaban API
"""

import requests
import logging

def upload_request(session, host, session_id, project, zip_name, zip_path):
    """Upload request for the Azkaban API

    :param session: A requests session for creating the request
    :type session: requests.Session
    :param str host: Hostname where the request should go
    :param str session_id: An id that the user should have when is logged in
    :param str project: Project name on Azkaban
    :param str zip_name: Name that zip will receive
    :param str zip_path: Local path from zip that will be uploaded
    :return: The response from the request made
    :rtype: requests.Response
    :raises requests.exceptions.ConnectionError: if cannot connect to host
    """

    zip_file = open(zip_path, 'rb')

    response = session.post(
        host + '/manager',
        data={
            u'session.id': session_id,
            u'ajax': u'upload',
            u'project': project
        },
        files={
            u'file': (zip_name, zip_file, 'application/zip'),
        }
    )

    logging.debug("Response: \n%s", response.text)

    return response

def login_request(session, host, user, password):
    """Login request for the Azkaban API

    :param session: A requests session for creating the request
    :type session: requests.Session
    :param str host: Hostname where the request should go
    :param str user: The user name
    :param str password: The user password
    :return: The response from the request made
    :rtype: requests.Response
    :raises requests.exceptions.ConnectionError: if cannot connect to host
    """

    response = session.post(
        host,
        data={
            u'action': u'login',
            u'username': user,
            u'password': password
        }
    )

    logging.debug("Response: \n%s", response.text)

    return response

def schedule_request(session, host, session_id, project, flow, cron):
    """Schedule request for the Azkaban API

    :param session: A requests session for creating the request
    :type session: requests.Session
    :param str host: Hostname where the request should go
    :param str session_id: An id that the user should have when is logged in
    :param str project: Project name that contains the flow that will be scheduled on Azkaban
    :param str flow: Flow name to be scheduled on Azkaban
    :param str cron: Cron expression in quartz format used to schedule
    :return: The response from the request made
    :rtype: requests.Response
    :raises requests.exceptions.ConnectionError: if cannot connect to host
    """

    response = session.post(
        host + '/schedule',
        data={
            u'session.id': session_id,
            u'ajax': u'scheduleCronFlow',
            u'projectName': project,
            u'flow': flow,
            u'cronExpression': cron
        }
    )

    logging.debug("Response: \n%s", response.text)

    return response

#TODO: Add optional parameters
def execute_request(session, host, session_id, project, flow):
    """Execute request for the Azkaban API

    :param session: A requests session for creating the request
    :type session: requests.Session
    :param str host: Hostname where the request should go
    :param str session_id: An id that the user should have when is logged in
    :param str project: Project name that contains the flow that will be executed on Azkaban
    :param str flow: Flow name to be executed on Azkaban
    :return: The response from the request made
    :rtype: requests.Response
    :raises requests.exceptions.ConnectionError: if cannot connect to host
    """

    response = session.get(
        host + '/executor',
        params={
            u'session.id': session_id,
            u'ajax': 'executeFlow',
            u'project': project,
            u'flow': flow
        }
    )

    logging.debug("Response: \n%s", response.text)

    return response
