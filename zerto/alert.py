# -*- coding: utf-8 -*-
'''Zerto alert object'''

from zertoobject import ZertoObject
from misc import parse_timestamp


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

    def __str__(self):
        return 'vpgs={0}, alert_description={1}, help_identifier={2}, is_dismissed={3}, event_type={4}'.format(
            'self.vpgs', 'self.description', 'self.help_identifier', 'self.is_dismissed', 'self.level')


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
