from IPy import IP

from django.db import models

from netfields.managers import NET_OPERATORS, NET_TEXT_OPERATORS
from netfields.forms import NetAddressFormField, MACAddressFormField

class _BaseField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = self.max_length
        super(_BaseField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

    def db_type(self, connection):
        engine = connection.settings_dict['ENGINE']
        if engine == 'django.db.backends.postgresql_psycopg2':
            return self.db_pg_type

        return super(_BaseField, self).db_type(connection)

    def formfield(self, **kwargs):
        defaults = {'form_class': self.form_class}
        defaults.update(kwargs)
        return super(_BaseField, self).formfield(**defaults)


class _NetAddressField(_BaseField):
    empty_strings_allowed = False
    form_class = NetAddressFormField
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if not value:
            return value

        return IP(value)

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
    db_pg_type = 'inet'
    max_length = 39


class CidrAddressField(_NetAddressField):
    description = "PostgreSQL CIDR field"
    db_pg_type = 'cidr'
    max_length = 43


class MACAddressField(_BaseField):
    description = "PostgreSQL MACADDR field"
    db_pg_type = 'macaddr'
    form_class = MACAddressFormField
    max_length = 17
