from enum import Enum

__all__ = [
    "Main",
    "Expression",
    "Declaration",
    "Statement"
]


class Type(Enum):
    def __eq__(self, o: object) -> bool:
        if type(o) == str:
            return self.value == o
        else:
            return Enum.__eq__(o)


class Main(Type):
    PROGRAM = "Program"


class Expression(Type):
    THIS_EXPRESSION = "ThisExpression"
    IDENTIFIER = "Identifier"
    LITERAL = "Literal"
    ARRAY_EXPRESSION = "ArrayExpression"
    OBJECT_EXPRESSION = "ObjectExpression"
    FUNCTION_EXPRESSION = "FunctionExpression"
    ARROW_FUNCTION_EXPRESSION = "ArrowFunctionExpression"
    CLASS_EXPRESSION = "ClassExpression"
    TAGGED_TEMPLATE_EXPRESSION = "TaggedTemplateExpression"
    MEMBER_EXPRESSION = "MemberExpression"
    SUPER = "Super"
    META_PROPERTY = "MetaProperty"
    NEW_EXPRESSION = "NewExpression"
    CALL_EXPRESSION = "CallExpression"
    UPDATE_EXPRESSION = "UpdateExpression"
    AWAIT_EXPRESSION = "AwaitExpression"
    UNARY_EXPRESSION = "UnaryExpression"
    BINARY_EXPRESSION = "BinaryExpression"
    LOGICAL_EXPRESSION = "LogicalExpression"
    CONDITIONAL_EXPRESSION = "ConditionalExpression"
    YIELD_EXPRESSION = "YieldExpression"
    ASSIGNMENT_EXPRESSION = "AssignmentExpression"
    SEQUENCE_EXPRESSION = "SequenceExpression"


class Declaration(Type):
    EXPORT_ALL_DECLARATION = "ExportAllDeclaration"
    EXPORT_DEFAULT_DECLARATION = "ExportDefaultDeclaration"
    EXPORT_NAMED_DECLARATION = "ExportNamedDeclaration"

class Statement(Type):
    BLOCK_STATEMENT = "BlockStatement"
    BREAK_STATEMENT = "BreakStatement"
    CONTINUE_STATEMENT = "ContinueStatement"
    DEBUGGER_STATEMENT = "DebuggerStatement"
    DO_WHILE_STATEMENT = "DoWhileStatement"
    EMPTY_STATEMENT = "EmptyStatement"
    EXPRESSION_STATEMENT = "ExpressionStatement"
    FOR_STATEMENT = "ForStatement"
    FOR_IN_STATEMENT = "ForInStatement"
    FOR_OF_STATEMENT = "ForOfStatement"
    FUNCTION_DECLARATION = "FunctionDeclaration"
    IF_STATEMENT = "IfStatement"
    LABELED_STATEMENT = "LabeledStatement"
    RETURN_STATEMENT = "ReturnStatement"
    SWITCH_STATEMENT = "SwitchStatement"
    THROW_STATEMENT = "ThrowStatement"
    TRY_STATEMENT = "TryStatement"
    VARIABLE_DECLARATION = "VariableDeclaration"
    WHILE_STATEMENT = "WhileStatement"
    WITH_STATEMENT = "WithStatement"
