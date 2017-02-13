'''Lisp interpreter test'''

import unittest

from interpreter import ContextualToken
from interpreter import RootScope
from interpreter import VarKeyword
from interpreter import Variable
from interpreter import Grammar

class ContextualTokenTest(unittest.TestCase):
    def setUp(self):
        self.contextual_token = ContextualToken()
        self.contextual_token_str_expectation = 'token'

    def test_contextual_token_instantiation(self):
        self.assertEqual(self.contextual_token.__class__,ContextualToken)

    def test_contextual_token_str(self):
        self.assertEqual(self.contextual_token.__str__(),self.contextual_token_str_expectation)

class RootScopeTest(unittest.TestCase):
    def setUp(self):
        self.root_scope = RootScope()
        self.root_scope_str_expectation = 'root_scope'

    def test_root_scope_instantiation(self):
        self.assertEqual(self.root_scope.__class__,RootScope)

    def test_root_scope_str(self):
        self.assertEqual(self.root_scope.__str__(),self.root_scope_str_expectation)

class VarKeywordTest(unittest.TestCase):
    def setUp(self):
        self.variable_keyword = VarKeyword()
        self.variable_keyword_str_expectation = 'var'

    def test_variable_keyword_instantiation(self):
        self.assertEqual(self.variable_keyword.__class__,VarKeyword)

    def test_variable_keyword_str(self):
        self.assertEqual(self.variable_keyword.__str__(),self.variable_keyword_str_expectation)

class VariableTest(unittest.TestCase):
    def setUp(self):
        self.contextual_token = ContextualToken()
        self.root_scope = RootScope()
        self.var_keyword = VarKeyword()
        self.variable = Variable()

    def test_variable_instantiation(self):
        self.assertEqual(self.variable.__class__,Variable)

    def test_variable_token_root_scope(self):
        self.assertEqual(self.variable.definition(self.contextual_token.__str__(),self.root_scope.__str__()),self.var_keyword.__str__())

class GrammarTest(unittest.TestCase):
    def setUp(self):
        self.gr = Grammar()
    
    def test_grammar_instantiation(self):
        self.assertEqual(self.gr.__class__,Grammar)

    def test_grammar_variable_definition_token_root_scope(self):
        self.assertEqual(self.gr.variable_definition('token','root_scope'),'var')

    def test_grammar_variable_definition_token_nested_scope(self):
        self.assertEqual(self.gr.variable_definition('token','nested_scope'),'let')

    def test_grammar_variable_definition_rule(self):
        self.assertEqual(self.gr.variable_definition(),'LEFT_HAND_ASSIGNMENT')

    def test_grammar_precedence_token(self):
        self.assertEqual(self.gr.precedence('token'),['(',')'])

    def test_grammar_precedence_rule(self):
        self.assertEqual(self.gr.precedence('rule'),'HIGH_ORDER_OPERATION')

    def test_grammar_operation_token(self):
        self.assertEqual(self.gr.operation('token','sum'),'+')
        self.assertEqual(self.gr.operation('rule','sum'),'SUM_ARGUMENTS_OF_THE_FUNCTION')

if __name__ == '__main__':
    unittest.main(verbosity=2)
