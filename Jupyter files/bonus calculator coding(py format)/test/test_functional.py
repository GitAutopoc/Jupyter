import unittest
from employee_bonus import BonusCalculator
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_return_type_none(self):
        obj=BonusCalculator.calculate_bonus({"id":101,"dob":"1999-4-2"},{"id":101,"salary":8000})
        test_obj = TestUtils()
        if type(obj)!=type(None):
            test_obj.yakshaAssert("TestReturnTypeNone", True, "functional")
            print("TestReturnTypeNone = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeNone", False, "functional")
            print("TestReturnTypeNone = Failed")

    def test_return_type_dict(self):
        obj=BonusCalculator.calculate_bonus({"id":101,"dob":"1999-4-2"},{"id":101,"salary":8000})
        test_obj = TestUtils()
        if type(obj)==type({}):
            test_obj.yakshaAssert("TestReturnTypeDict", True, "functional")
            print("TestReturnTypeDict = Passed")
        else:
            test_obj.yakshaAssert("TestReturnTypeDict", False, "functional")
            print("TestReturnTypeDict = Failed")

    def test_result(self):
        obj=BonusCalculator.calculate_bonus({"id":101,"dob":"1999-4-2"},{"id":101,"salary":25000})
        test_obj = TestUtils()
        if type(obj)!=type(None):
            if obj['salary']==25200:
                test_obj.yakshaAssert("TestResult", True, "functional")
                print("TestResult = Passed")
            else:
                test_obj.yakshaAssert("TestResult", False, "functional")
                print("TestResult = Failed")
        else:
            test_obj.yakshaAssert("TestResult", False, "functional")
            print("TestResult = Failed")
