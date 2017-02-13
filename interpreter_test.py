'''Lisp interpreter test'''

import unittest

from interpreter import VARIABLE_RULE_PARAMETER_OP
from interpreter import PRECEDENCE_RULE_PARAMETER_OP

from interpreter import Scope
from interpreter import ContextualToken
from interpreter import ContextualRule
from interpreter import RootScope
from interpreter import NestedScope
from interpreter import VarKeyword
from interpreter import LetKeyword
from interpreter import Variable
from interpreter import Grammar

class ScopeTest(unittest.TestCase):
    def setUp(self):
        self.scope = Scope()

    def test_scope_instantiation(self):
        self.assertEqual(self.scope.__class__,Scope)

class ContextualTokenTest(unittest.TestCase):
    def setUp(self):
        self.contextual_token = ContextualToken()
        self.contextual_token_str_expectation = ContextualToken().__str__()

    def test_contextual_token_instantiation(self):
        self.assertEqual(self.contextual_token.__class__,ContextualToken)

    def test_contextual_token_str(self):
        self.assertEqual(self.contextual_token.__str__(),self.contextual_token_str_expectation)

class ContextualRuleTest(unittest.TestCase):
    def setUp(self):
        self.contextual_rule = ContextualRule()
        self.contextual_rule_str_expecation = ContextualRule().__str__()

    def test_contextual_rule_instantiation(self):
        self.assertEqual(self.contextual_rule.__class__,ContextualRule)

class RootScopeTest(unittest.TestCase):
    def setUp(self):
        self.root_scope = RootScope()
        self.root_scope_str_expectation = RootScope().__str__()

    def test_root_scope_instantiation(self):
        self.assertEqual(self.root_scope.__class__,RootScope)

    def test_root_scope_str(self):
        self.assertEqual(self.root_scope.__str__(),self.root_scope_str_expectation)

class NestedScopeTest(unittest.TestCase):
    def setUp(self):
        self.nested_scope = NestedScope()
        self.nested_scope_str_expectation = NestedScope().__str__()

    def test_nested_scope_instantiation(self):
        self.assertEqual(self.nested_scope.__class__,NestedScope)

    def test_nested_scope_str(self):
        self.assertEqual(self.nested_scope.__str__(),self.nested_scope_str_expectation)

class VarKeywordTest(unittest.TestCase):
    def setUp(self):
        self.var_keyword = VarKeyword()
        self.var_keyword_str_expectation = VarKeyword().__str__()

    def test_variable_keyword_instantiation(self):
        self.assertEqual(self.var_keyword.__class__,VarKeyword)

    def test_variable_keyword_str(self):
        self.assertEqual(self.var_keyword.__str__(),self.var_keyword_str_expectation)

class LetKeywordTest(unittest.TestCase):
    def setUp(self):
        self.let_keyword = LetKeyword()
        self.let_keyword_str_expectation = LetKeyword().__str__()

    def test_let_keyword_instantiation(self):
        self.assertEqual(self.let_keyword.__class__,LetKeyword)

    def test_let_keyword_str(self):
        self.assertEqual(self.let_keyword.__str__(),self.let_keyword_str_expectation)

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
        self.contextual_token_str = ContextualToken().__str__()
        self.root_scope_str = RootScope().__str__()
        self.contextual_rule_str = ContextualRule().__str__()
        self.nested_scope_str = NestedScope().__str__()
        self.let_keyword_str = LetKeyword().__str__()
        self.var_keyword_str = VarKeyword().__str__()
        self.gr = Grammar()
    
    def test_grammar_instantiation(self):
        self.assertEqual(self.gr.__class__,Grammar)

    def test_grammar_variable_definition_token_root_scope(self):
        self.assertEqual(self.gr.variable_definition(self.contextual_token_str,self.root_scope_str),self.var_keyword_str)

    def test_grammar_variable_definition_token_nested_scope(self):
        self.assertEqual(self.gr.variable_definition(self.contextual_token_str,self.nested_scope_str),self.let_keyword_str)

    def test_grammar_variable_definition_rule(self):
        self.assertEqual(self.gr.variable_definition(),VARIABLE_RULE_PARAMETER_OP)

    def test_grammar_precedence_token(self):
        self.assertEqual(self.gr.precedence(ContextualToken().__str__()),['(',')'])

    def test_grammar_precedence_rule(self):
        self.assertEqual(self.gr.precedence(self.contextual_rule_str),PRECEDENCE_RULE_PARAMETER_OP)

    def test_grammar_operation_token(self):
        self.assertEqual(self.gr.operation(self.contextual_token_str,'sum'),'+')
        self.assertEqual(self.gr.operation(self.contextual_rule_str,'sum'),'SUM_ARGUMENTS_OF_THE_FUNCTION')

if __name__ == '__main__':
    unittest.main(verbosity=2)
