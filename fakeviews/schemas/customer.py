from schemas.base import Schema, SchemaBase


class CustomerList(SchemaBase):

    @property
    def schema(self):
        return Schema(
            lambda: {
                'uuid': self._('uuid'),
                'name': self._('person.full_name'),
                'email': self._('person.email'),
                'phone': self._('person.telephone')
            }
        )