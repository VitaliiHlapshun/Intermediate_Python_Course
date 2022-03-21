import sys
import unittest


class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(not sys.platform.startswith("linux"),
                         "This test only runs on Windows")
    def test_linux_feature(self):
        print("This test runs on Linux")

    @unittest.skipIf(sys.platform.startswith("linux"),
                     "This test only runs on Windows")
    def test_other_linux_feature(self):
        print("This test should only run on Linux")

# or you can skip the test by using skipTest method
# class LinuxTests(unittest.TestCase):
#
#     def test_linux_feature(self):
#         if not sys.platform.startswith("linux"):
#             self.skipTest("Test only runs on Linux")


unittest.main()
