class PythonType(object):
    def to_python(self, value):
        if not value:
            return value

        if isinstance(value, self.python_instances):
            return value

        return self.python_type(value)
