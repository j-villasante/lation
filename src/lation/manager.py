from pprint import pprint
from subprocess import run
from json import loads
from typing import List, Dict

from lation.declarations import Declaration, Expression, Statement
from lation.errors import VariableNotFoundError, ExportDefaultNotFoundError, \
    ObjectNotFoundError

__all__ = ["Manager"]


class Variable:
    def __init__(self, declaration):
        self._declaration = declaration

    def _get_property_value(self, lang) -> Dict:
        for prop in self._declaration["init"]["properties"]:
            if prop["key"]["name"] == lang:
                return prop["value"]

    def get_value(self, lang: str) -> str:
        value = self._get_property_value(lang)
        return value["value"]

    def set_value(self, lang: str, new_value: str):
        value = self._get_property_value(lang)
        value["value"] = new_value
        value["raw"] = f"\'{new_value}\'"


class Text:
    def __init__(self):
        self._declarations = {}

    def add_declaration(self, lang: str, declaration: Dict):
        self._declarations[lang] = declaration

    def add_variable(self, lang: str, variable: Variable):
        self._declarations[lang] = variable

    def get_value(self, lang: str):
        declaration = self._declarations[lang]
        if isinstance(declaration, Variable):
            return declaration.get_value(lang)
        else:
            return declaration["value"]

    def set_value(self, lang: str, new_value: str):
        declaration = self._declarations[lang]
        if isinstance(declaration, Variable):
            declaration.set_value(lang, new_value)
        else:
            declaration["value"] = new_value
            declaration["raw"] = f"\'{new_value}\'"


class Topics:
    topics: Dict[str, Text]

    def __init__(self):
        self.topics = {}

    def has(self, key: str):
        return key in self.topics

    def get_value(self, key):
        return self.topics[key]

    def set_text(self, key: str, text: Text):
        self.topics[key] = text

    def set_variable(self, key: str, variable: Text):
        self.topics[key] = variable


class Manager:
    topics: Topics
    code: Dict

    def __init__(self, file_name) -> None:
        result = run(
            [
                "/home/josue/.nvm/versions/node/v10.10.0/bin/node",
                "./main.js",
                "read",
                f"--file={file_name}"
            ],
            capture_output=True)
        if result.returncode == 0:
            self.code = loads(result.stdout)
            self.topics = Topics()

            self._load()
        else:
            print(result.stderr)
            raise RuntimeError

    def _load(self):
        properties = self._get_export_properties()
        for prop in properties:
            lang = prop["key"]["name"]
            lines = prop["value"]["properties"]
            for line in lines:
                key = line["key"]["value"]
                value = line["value"]

                if value["type"] == Expression.LITERAL:
                    if self.topics.has(key):
                        self.topics.get_value(key).add_declaration(lang, value)
                    else:
                        text = Text()
                        text.add_declaration(lang, value)
                        self.topics.set_text(key, text)

    def _get_export_properties(self) -> Dict:
        declaration = self._get_export_declaration()
        if declaration["type"] == Expression.OBJECT_EXPRESSION:
            return declaration["properties"]
        raise ObjectNotFoundError()

    def _get_export_declaration(self) -> Dict:
        for body_item in self.code["body"]:
            if body_item["type"] == Declaration.EXPORT_DEFAULT_DECLARATION:
                return body_item["declaration"]
        raise ExportDefaultNotFoundError()

    def _get_variable_declaration(self, name: str) -> Variable:
        for body_item in self.code["body"]:
            if body_item["type"] == Statement.VARIABLE_DECLARATION:
                for declaration in body_item["declarations"]:
                    if declaration["id"]["name"] == name:
                        return Variable(declaration)
        raise VariableNotFoundError()
