import unittest
from rules.new_rules.rules_2 import *
from rules.new_rules.helpers import get_data


class TestRules(unittest.TestCase):
    def test_rule_01(self):
        self.assertTrue(rule_01(get_data('../testdata/rule01W_OK_1.xml')))

        self.assertFalse(rule_01(get_data('../testdata/rule01W_fail.xml')))

    def test_rule_02(self):
        self.assertTrue(rule_02(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_02(get_data('../testdata/rule02W_fail.xml')))

    def test_rule_03(self):
        self.assertTrue(rule_03(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_03(get_data('../testdata/rule03W_idp_fail.xml')))

    def test_rule_04(self):
        self.assertTrue(rule_04(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_04(get_data('../testdata/rule03W_sp_fail.xml')))

    def test_rule_05(self):
        self.assertTrue(rule_05(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_05(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_06(self):
        self.assertTrue(rule_06(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_06(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_07(self):
        self.assertTrue(rule_07(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_07(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_11(self):
        self.assertTrue(rule_11(get_data('../testdata/rule11W_valid.xml')))

        self.assertFalse(rule_11(get_data('../testdata/rule11W_fail.xml')))

    def test_rule_12(self):
        self.assertTrue(rule_12(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_12(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_13(self):
        self.assertTrue(rule_13(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_13(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_14(self):
        self.assertTrue(rule_14(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_14(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_15(self):
        self.assertTrue(rule_15(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_15(get_data('../testdata/idp_incomplete.xml')))

    # TODO: Find out how the rule should work
    # def test_rule_16(self):
    #     self.assertTrue(rule_16(get_data('../testdata/rule16W_OK.xml')))
    #
    #     self.assertFalse(rule_16(get_data('../testdata/rule16W_fail.xml')))

    def test_rule_17(self):
        self.assertTrue(rule_17(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_17(get_data('../testdata/sp_invalid.xml')))

    def test_rule_19(self):
        self.assertTrue(rule_19(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_19(get_data('../testdata/rule19W_fail.xml')))

    def test_rule_20(self):
        self.assertTrue(rule_20(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_20(get_data('../testdata/rule19W_fail.xml')))

    def test_rule_21(self):
        self.assertTrue(rule_21(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_21(get_data('../testdata/rule19W_fail.xml')))

    def test_rule_22(self):
        self.assertTrue(rule_22(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_22(get_data('../testdata/rule22E_fail.xml')))

    def test_rule_23(self):
        self.assertTrue(rule_23(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_23(get_data('../testdata/rule23E_fail.xml')))

    def test_rule_24(self):
        self.assertTrue(rule_24(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_24(get_data('../testdata/rule24E_fail.xml')))

    def test_rule_25(self):
        self.assertTrue(rule_25(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_25(get_data('../testdata/rule25W_fail.xml')))

    def test_rule_26(self):
        self.assertTrue(rule_26(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_26(get_data('../testdata/rule26W_fail.xml')))

    def test_rule_27(self):
        self.assertTrue(rule_27(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_27(get_data('../testdata/rule27E_fail.xml')))

    def test_rule_28(self):
        self.assertTrue(rule_28(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_28(get_data('../testdata/rule28E_fail.xml')))

    def test_rule_29(self):
        self.assertTrue(rule_29(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_29(get_data('../testdata/rule29E_fail.xml')))

    def test_rule_30(self):
        self.assertTrue(rule_30(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_30(get_data('../testdata/rule30W_fail.xml')))

    def test_rule_31(self):
        self.assertTrue(rule_31(get_data('../testdata/sp_valid.xml')))

        self.assertFalse(rule_31(get_data('../testdata/rule31W_fail.xml')))

    def test_rule_32(self):
        self.assertTrue(rule_32(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_32(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_33(self):
        self.assertTrue(rule_33(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_33(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_34(self):
        self.assertTrue(rule_34(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_34(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_35(self):
        self.assertTrue(rule_35(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_35(get_data('../testdata/rule35W_fail.xml')))

    def test_rule_36(self):
        self.assertTrue(rule_36(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_36(get_data('../testdata/rule36E_fail.xml')))

    def test_rule_37(self):
        self.assertTrue(rule_37(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_37(get_data('../testdata/idp_incomplete.xml')))

    def test_rule_38(self):
        self.assertTrue(rule_38(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_38(get_data('../testdata/rule38E_fail.xml')))

    def test_rule_39(self):
        self.assertTrue(rule_39(get_data('../testdata/idp_valid.xml')))

        self.assertFalse(rule_39(get_data('../testdata/rule39E_fail.xml')))

    def test_rule_40(self):
        self.assertTrue(rule_40(get_data('../testdata/rule40E_OK.xml')))

        self.assertFalse(rule_40(get_data('../testdata/rule40E_fail.xml')))