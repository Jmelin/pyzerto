# -*- coding: utf-8 -*-
'''Zerto alert object'''

from zertoobject import ZertoObject
from misc import parse_timestamp
import json


class Alert(ZertoObject):

    def __init__(self, **kwargs):
        self.values = kwargs
        self.vpgs = list([
            i['identifier'] for i in kwargs.get('AffectedVpgs', [])
        ])
        self.zorgs = list([
            i['identifier'] for i in kwargs.get('AffectedZorgs', [])
        ])
        self.help_identifier = kwargs.get('HelpIdentifier')
        self.site_identifier = (kwargs.get('Site') or {}).get('identifier')
        self.turned_on = parse_timestamp(kwargs['TurnedOn'])
        self.description = kwargs['Description']
        self.entity = kwargs.get('Entity')
        self.level = kwargs.get('Level')
        self.is_dismissed = kwargs.get('IsDismissed')

        with open('zerto_error_messages/zerto_error_messages.json', 'r') as errorfile:
            data = errorfile.read()
            error_data = json.loads(data)

            self.alert_name = error_data[""+ self.help_identifier]['Alert Name']
            self.alert_severity = error_data[""+ self.help_identifier]['Severity']
            self.alert_more_description = error_data[""+ self.help_identifier]['Alert Description']

    def __str__(self):

        return 'vpgs={0}, identifier={1}, alert_name={2}, description={3}, entity={4}, level={5}, dismissed={6}'.format(
            self.vpgs, self.help_identifier, self.alert_name, self.description, self.entity, self.level, self.is_dismissed)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4