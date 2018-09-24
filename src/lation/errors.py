__all__ = [
    "VariableNotFoundError",
    "ExportDefaultNotFoundError",
    "ObjectNotFoundError",
]


class VariableNotFoundError(BaseException):
    pass


class ExportDefaultNotFoundError(BaseException):
    pass


class ObjectNotFoundError(BaseException):
    pass
