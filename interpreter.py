'''List intepreter'''

VARIABLE_DEFINITION_ROOT_SCOPE = 'var'
VARIABLE_DEFINITION_NESTED_SCOPE = 'let'
VARIABLE_RULE_PARAMETER_OP = 'LEFT_HAND_ASSIGNMENT'
PRECEDENCE_RULE_PARAMETER_OP = 'HIGH_ORDER_OPERATION'
DEFAULT_VARIABLE_KIND_RULESET = 'rule'
DEFAULT_VARIABLE_ASSESMENT = 'root_scope'
DEFAULT_PRECEDENCE_KIND_RULESET = 'rule'
DEFAULT_OPERATION_KIND_RULESET = 'rule'
DEFAULT_ASSESMENT_UNSET_VALUE = None

class Scope(object):
    pass

class ContextualToken(object):
    def __init__(self):
        self.key_name = 'token'

    def __str__(self):
        return self.key_name

class ContextualRule(object):
    def __init__(self):
        self.key_name = 'rule'

    def __str__(self):
        return self.key_name

class RootScope(object):
    def __init__(self):
        self.key_name = 'root_scope'

    def __str__(self):
        return self.key_name

class NestedScope(object):
    def __init__(self):
        self.key_name = 'nested_scope'

    def __str__(self):
        return self.key_name
    
class VarKeyword(object):
    def __init__(self):
        self.assignment_key_name = 'var'

    def __str__(self):
        return self.assignment_key_name

class LetKeyword(object):
    def __init__(self):
        self.assignment_key_name = 'let'

    def __str__(self):
        return self.assignment_key_name
        
class Variable(object):
    def __init__(self):
        self._definition = {
            ContextualToken().__str__(): {
                RootScope().__str__(): VARIABLE_DEFINITION_ROOT_SCOPE,
                'nested_scope': VARIABLE_DEFINITION_NESTED_SCOPE,
            },
            'rule': VARIABLE_RULE_PARAMETER_OP,
        }

    def definition(self,kind=DEFAULT_VARIABLE_KIND_RULESET,assesment=DEFAULT_ASSESMENT_UNSET_VALUE):
        if kind == ContextualToken().__str__():
            return self._definition[kind][assesment or DEFAULT_VARIABLE_ASSESMENT]
        else:
            return self._definition[kind]

class Grammar(object):
    def __init__(self):
        self._variable_definition = {
            'token': {
                'root_scope': VARIABLE_DEFINITION_ROOT_SCOPE,
                'nested_scope': VARIABLE_DEFINITION_NESTED_SCOPE,
            },
            'rule': VARIABLE_RULE_PARAMETER_OP,
        }
        self._precedence_definition = {
            'token': ['(',')'],
            'rule': PRECEDENCE_RULE_PARAMETER_OP,
        }
        self._operation_definition = {
            'token': {
                'sum': '+'
            },
            'rule': {
                'sum': 'SUM_ARGUMENTS_OF_THE_FUNCTION'
            }
        }

    def variable_definition(self,kind=DEFAULT_VARIABLE_KIND_RULESET,assesment=DEFAULT_ASSESMENT_UNSET_VALUE):
        return Variable().definition(kind,assesment)
        #if kind == 'token':
        #    return self._variable_definition[kind][assesment or DEFAULT_VARIABLE_ASSESMENT]
        #else:
        #    return self._variable_definition[kind]

    def precedence(self,kind=DEFAULT_PRECEDENCE_KIND_RULESET):
        return self._precedence_definition[kind]

    def operation(self,kind=DEFAULT_OPERATION_KIND_RULESET,assesment=DEFAULT_ASSESMENT_UNSET_VALUE):
        return self._operation_definition[kind][assesment or DEFAULT_OPERATION_ASSESMENT]

