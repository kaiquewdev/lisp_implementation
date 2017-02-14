'''List intepreter'''

# Essential Representations
TOKEN = 'token'
SUM = 'sum'
RULE = 'rule'
ROOT_SCOPE = 'root_scope'
NESTED_SCOPE = 'nested_scope'
VAR = 'var'
LET = 'let'
# Variable
VARIABLE_DEFINITION_ROOT_SCOPE = 'var'
VARIABLE_DEFINITION_NESTED_SCOPE = 'let'
VARIABLE_RULE_PARAMETER_OP = 'LEFT_HAND_ASSIGNMENT'
DEFAULT_VARIABLE_KIND_RULESET = 'rule'
DEFAULT_VARIABLE_ASSESMENT = 'root_scope'
# Precedence
PRECEDENCE_RULE_PARAMETER_OP = 'HIGH_ORDER_OPERATION'
DEFAULT_PRECEDENCE_KIND_RULESET = 'rule'
DEFAULT_OPERATION_KIND_RULESET = 'rule'
DEFAULT_ASSESMENT_UNSET_VALUE = None
# Operation
SUM_OPERATION_PARAMETER_OP = 'SUM_ARGUMENTS_OF_THE_FUNCTION'

class Scope(object):
    pass

class ContextualToken(object):
    def __init__(self):
        self.key_name = TOKEN

    def __str__(self):
        return self.key_name

class ContextualSumToken(ContextualToken):
    def __init__(self):
        self.key_name = SUM
    
class ContextualRule(object):
    def __init__(self):
        self.key_name = RULE

    def __str__(self):
        return self.key_name

class Identifier(object):
    def __init__(self):
        self.key_name = None

    def __str__(self):
        return self.key_name

class Keyword(object):
    def __init__(self):
        self.assignment_key_name = None

    def __str__(self):
        return self.assigment_key_name
    
class RootScope(Identifier):
    def __init__(self):
        self.key_name = ROOT_SCOPE

class NestedScope(Identifier):
    def __init__(self):
        self.key_name = NESTED_SCOPE

class Rule(Identifier):
    def __init__(self):
        self.key_name = RULE
    
class VarKeyword(Keyword):
    def __init__(self):
        self.assignment_key_name = VAR

    def __str__(self):
        return self.assignment_key_name

class LetKeyword(object):
    def __init__(self):
        self.assignment_key_name = LET

    def __str__(self):
        return self.assignment_key_name

class SumKeyword(Identifier):
    def __init__(self):
        self.key_name = SUM

class Variable(object):
    def __init__(self):
        self._contextual_token_str = ContextualToken().__str__()
        self._root_scope_str = RootScope().__str__()
        self._nested_scope_str = NestedScope().__str__()
        self._rule_str = Rule().__str__()
        self._definition = {
            self._contextual_token_str: {
                self._root_scope_str: VARIABLE_DEFINITION_ROOT_SCOPE,
                self._nested_scope_str: VARIABLE_DEFINITION_NESTED_SCOPE,
            },
            self._rule_str: VARIABLE_RULE_PARAMETER_OP,
        }

    def definition(self,kind=DEFAULT_VARIABLE_KIND_RULESET,assesment=DEFAULT_ASSESMENT_UNSET_VALUE,is_token=lambda k,t:k==t):
        if is_token(kind,self._contextual_token_str):
            return self._definition[kind][assesment or DEFAULT_VARIABLE_ASSESMENT]
        else:
            return self._definition[kind]

class Grammar(object):
    def __init__(self):
        self._variable_definition = {
            ContextualToken().__str__(): {
                RootScope().__str__(): VARIABLE_DEFINITION_ROOT_SCOPE,
                NestedScope().__str__(): VARIABLE_DEFINITION_NESTED_SCOPE,
            },
            Rule().__str__(): VARIABLE_RULE_PARAMETER_OP,
        }
        self._precedence_definition = {
            ContextualToken().__str__(): ['(',')'],
            Rule().__str__(): PRECEDENCE_RULE_PARAMETER_OP,
        }
        self._operation_definition = {
            ContextualToken().__str__(): {
                SumKeyword().__str__(): '+'
            },
            Rule().__str__(): {
                SumKeyword().__str__(): SUM_OPERATION_PARAMETER_OP
            }
        }

    def variable_definition(self,kind=DEFAULT_VARIABLE_KIND_RULESET,assesment=DEFAULT_ASSESMENT_UNSET_VALUE,variable=Variable()):
        return variable.definition(kind,assesment)

    def precedence(self,kind=DEFAULT_PRECEDENCE_KIND_RULESET):
        return self._precedence_definition[kind]

    def operation(self,kind=DEFAULT_OPERATION_KIND_RULESET,assesment=DEFAULT_ASSESMENT_UNSET_VALUE):
        return self._operation_definition[kind][assesment or DEFAULT_OPERATION_ASSESMENT]
