'''Lisp interpreter test'''

import os
import unittest

from interpreter import VARIABLE_RULE_PARAMETER_OP
from interpreter import PRECEDENCE_RULE_PARAMETER_OP
from interpreter import SUM_OPERATION_PARAMETER_OP
from interpreter import SUB_OPERATION_PARAMETER_OP
from interpreter import MUL_OPERATION_PARAMETER_OP
from interpreter import DIV_OPERATION_PARAMETER_OP
from interpreter import MOD_OPERATION_PARAMETER_OP

from interpreter import Scope
from interpreter import ContextualToken
from interpreter import DefinitionToken
from interpreter import ContextualRule
from interpreter import RootScope
from interpreter import NestedScope
from interpreter import VarKeyword
from interpreter import LetKeyword
from interpreter import SumKeyword
from interpreter import SubKeyword
from interpreter import MulKeyword
from interpreter import DivKeyword
from interpreter import ModKeyword
from interpreter import DefinitionKeyword
from interpreter import Definition
from interpreter import PrecedenceDelimiters
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

class DefinitionTokenTest(unittest.TestCase):
    def setUp(self):
        self.definition_token = DefinitionToken()
        self.definition_token_str_expectation = DefinitionToken().__str__()

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

class SubKeywordTest(unittest.TestCase):
    def setUp(self):
        self.sub_keyword = SubKeyword()
        self.sub_keyword_str_expectation = SubKeyword().__str__()

    def test_sub_keyword_instantiation(self):
        self.assertEqual(self.sub_keyword.__class__,SubKeyword)

class SumKeywordTest(unittest.TestCase):
    def setUp(self):
        self.sum_keyword = SumKeyword()
        self.sum_keyword_str_expectation = SumKeyword().__str__()

    def test_sum_keyword_instantiation(self):
        self.assertEqual(self.sum_keyword.__class__,SumKeyword)

    def test_sum_keyword_str(self):
        self.assertEqual(self.sum_keyword.__str__(),self.sum_keyword_str_expectation)

class DivKeywordTest(unittest.TestCase):
    def setUp(self):
        self.div_keyword = DivKeyword()
        self.div_keyword_str_expectation = DivKeyword().__str__()

    def test_div_keyword_instantiation(self):
        self.assertEqual(self.div_keyword.__class__,DivKeyword)

    def test_div_keyword_str(self):
        self.assertEqual(self.div_keyword.__str__(),self.div_keyword_str_expectation)

class ModKeywordTest(unittest.TestCase):
    def setUp(self):
        self.mod_keyword = ModKeyword()
        self.mod_keyword_str_expectation = ModKeyword().__str__()

    def test_mod_keyword_instantiation(self):
        self.assertEqual(self.mod_keyword.__class__,ModKeyword)

    def test_mod_keyword_str(self):
        self.assertEqual(self.mod_keyword.__str__(),self.mod_keyword_str_expectation)

class DefinitionKeywordTest(unittest.TestCase):
    def setUp(self):
        self.definition_keyword = DefinitionKeyword()
        self.definition_keyword_str_expectation = DefinitionKeyword().__str__()

    def test_definition_keyword_instantiation(self):
        self.assertEqual(self.definition_keyword.__class__,DefinitionKeyword)

    def test_definition_keyword_str(self):
        self.assertEqual(self.definition_keyword.__str__(),self.definition_keyword_str_expectation)
    

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

class DefinitionTest(unittest.TestCase):
    def setUp(self):
        self.contextual_token = ContextualToken()
        self.root_scope = RootScope()
        self.definition_keyword = DefinitionKeyword()
        self.definition = Definition()

    def test_definition_instantiation(self):
        self.assertEqual(self.definition.__class__,Definition)

class PrecedenceDelimitersTest(unittest.TestCase):
    def setUp(self):
        self.precedence_delimiters = PrecedenceDelimiters()

    def test_precedence_delimiters_instantiation(self):
        self.assertEqual(self.precedence_delimiters.__class__,PrecedenceDelimiters)

    def test_precedence_delimiters_meta(self):
        self.assertEqual(self.precedence_delimiters.__meta__(),['(',')'])

class GrammarTest(unittest.TestCase):
    def setUp(self):
        self.contextual_token_str = ContextualToken().__str__()
        self.definition_token_str = DefinitionToken().__str__()
        self.root_scope_str = RootScope().__str__()
        self.contextual_rule_str = ContextualRule().__str__()
        self.nested_scope_str = NestedScope().__str__()
        self.let_keyword_str = LetKeyword().__str__()
        self.var_keyword_str = VarKeyword().__str__()
        self.sum_keyword_str = SumKeyword().__str__()
        self.sub_keyword_str = SubKeyword().__str__()
        self.mul_keyword_str = MulKeyword().__str__()
        self.div_keyword_str = DivKeyword().__str__()
        self.mod_keyword_str = ModKeyword().__str__()
        self.definition_keyword_str = DefinitionKeyword().__str__()
        self.precedence_delimiters_meta = PrecedenceDelimiters().__meta__()
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
        self.assertEqual(self.gr.precedence(self.contextual_token_str),self.precedence_delimiters_meta)

    def test_grammar_precedence_rule(self):
        self.assertEqual(self.gr.precedence(self.contextual_rule_str),PRECEDENCE_RULE_PARAMETER_OP)

    def test_grammar_operation_token(self):
        self.assertEqual(self.gr.operation(self.contextual_token_str,self.sum_keyword_str),'+')
        self.assertEqual(self.gr.operation(self.contextual_rule_str,self.sum_keyword_str),SUM_OPERATION_PARAMETER_OP)
        self.assertEqual(self.gr.operation(self.contextual_token_str,self.sub_keyword_str),'-')
        self.assertEqual(self.gr.operation(self.contextual_rule_str,self.sub_keyword_str),SUB_OPERATION_PARAMETER_OP)
        self.assertEqual(self.gr.operation(self.contextual_token_str,self.mul_keyword_str),'*')
        self.assertEqual(self.gr.operation(self.contextual_rule_str,self.mul_keyword_str),MUL_OPERATION_PARAMETER_OP)
        self.assertEqual(self.gr.operation(self.contextual_token_str,self.div_keyword_str),'/')
        self.assertEqual(self.gr.operation(self.contextual_rule_str,self.div_keyword_str),DIV_OPERATION_PARAMETER_OP)
        self.assertEqual(self.gr.operation(self.contextual_token_str,self.mod_keyword_str),'%')
        self.assertEqual(self.gr.operation(self.contextual_rule_str,self.mod_keyword_str),MOD_OPERATION_PARAMETER_OP)

    def test_grammar_definition_token(self):
        self.assertEqual(self.gr.definition(self.contextual_token_str,self.definition_keyword_str),'def')

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
