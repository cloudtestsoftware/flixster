import unittest, sys, os
import xmlrunner
from flixster.qa.testcases.Locker        import Locker

def main():
    if len(sys.argv) >= 3:
        Locker.base_url=sys.argv[1]
        Locker.url_path=sys.argv[2]
        Locker.browserType=sys.argv[3]
    else:
        Locker.base_url="http://www.flixster.com"
        Locker.url_path=""
        Locker.browserType="firefox"
    
    suite = unittest.TestSuite()
    suite.addTest(Locker('test_Verify_Theater_showtimes'))

    xmlrunner.XMLTestRunner(output='test-reports').run(suite)
    sys.exit(0)
        
if __name__ == "__main__":
    main()