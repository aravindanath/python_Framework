import unittest

from  tests.home.home_tests import HomeTest
from tests.login.login_tests import LoginTests
from tests.login.createAcount_tests import CreateAccountTests
from tests.address.address_tests import AddressTests


# Get all test from the test class

tc1 =  unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 =  unittest.TestLoader().loadTestsFromTestCase(HomeTest)
tc3 =  unittest.TestLoader().loadTestsFromTestCase(AddressTests)
tc4 =  unittest.TestLoader().loadTestsFromTestCase(CreateAccountTests)

# Create test suite

smokeTest = unittest.TestSuite([tc1,tc2,tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#  py.test -s -v /Users/aravindanathdm/Documents/Simple_Pom_py_fw/tests/test_suite_demo.py --browser chrome --html=../screenshots/demo.html