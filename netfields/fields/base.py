from django.db import models

from netfields.managers import NET_OPERATORS, NET_TEXT_OPERATORS


class _BaseNetField(object):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = self.max_length
        super(_BaseNetField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': self.form_class}
        defaults.update(kwargs)
        return super(_BaseNetField, self).formfield(**defaults)


class _NetAddressField(_BaseNetField, models.Field):
    empty_strings_allowed = False

    def get_prep_lookup(self, lookup_type, value):
        if not value:
            return None

        if (lookup_type in NET_OPERATORS and
                NET_OPERATORS[lookup_type] not in NET_TEXT_OPERATORS):
            return self.get_prep_value(value)

        return super(_NetAddressField, self).get_prep_lookup(
            lookup_type, value)

    def get_prep_value(self, value):
        if not value:
            return None

        return unicode(self.to_python(value))

    def get_db_prep_lookup(self, lookup_type, value, connection,
                           prepared=False):
        if not value:
            return []

        if (lookup_type in NET_OPERATORS and
                NET_OPERATORS[lookup_type] not in NET_TEXT_OPERATORS):
            return [value] if prepared else [self.get_prep_value(value)]

        return super(_NetAddressField, self).get_db_prep_lookup(
            lookup_type, value, connection=connection, prepared=prepared)


class InetAddressField(_NetAddressField):
    description = "PostgreSQL INET field"
    max_length = 39
    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        return 'inet'


class CidrAddressField(_NetAddressField):
    description = "PostgreSQL CIDR field"
    max_length = 43
    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        return 'cidr'


class MACAddressField(_BaseNetField, models.Field):
    description = "PostgreSQL MACADDR field"
    max_length = 17

    def db_type(self, connection):
        return 'macaddr'
