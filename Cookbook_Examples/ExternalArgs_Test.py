import subprocess
import unittest
import Tests.apptestutils as apptestutils

"""
    Python NOTE:  Default of Popen is to send output from print statements
        to the bit bucket.

    subprocess.Popen NOTES:
       stderr=subprocess.STDOUT  - re-directs stderr to stdout
"""

csvFR1 = 'this.csv'
comparmFR1 = 'common.py'

class Test1(unittest.TestCase):
    outs = None
    errs = None

    def common(cls):
        apptestutils.displayNextTest(cls)

    def commonSP(cls, exeStr):
        """ Run the shell command in  exeStr as a subprocess,
        trap the print statements + other stdout + stderr.
        :param cls:
        :param exeStr: Shell command including arguments.
        :return: List of stdout & stderr lines
        """
        sp = subprocess.Popen(exeStr,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              shell=True)  # must have "shell=True" for windows OS
        outs, errs = sp.communicate()  # traps output from Python print statements

        if not errs == "":       # make sure we pay attention to stderr if any
            print('Stderr: %s' % errs)
        return outs.splitlines(), outs, errs

    def test_1(self):
        apptestutils.displayNextTest(self)
        outList, outs, errs = self.commonSP("ExternalArgs_Read.py -requiredSt %s" % csvFR1)
        for i, line in enumerate(outList):
            print('  arg %d: %s' % (i, line))
        # self.assertEqual(csvFR1,outList[0])
        # self.assertEqual('None', outList[1])
        # self.assertEqual(errs,'')


    def test_2RequiredArg(self):
        apptestutils.displayNextTest(self)
        outList, outs, errs = self.commonSP(
            "ExternalArgs_Read.py -commonparms %s" % csvFR1)
        for i, line in enumerate(outList):
            print('arg %d: %s' % (i, line))
        self.assertEqual(0,len(outList),msg="stdlist should be blank")
        self.assertIn('argument -requiredStr is required', errs)

    def test_3(self):
        apptestutils.displayNextTest(self)
        outList, outs, errs = \
            self.commonSP(
                "ExternalArgs_Read.py -someStr %s -commonparms %s" %
                        (csvFR1, comparmFR1))
        for i, line in enumerate(outList):
            print('arg %d: %s' % (i, line))
        #print(outs)
        self.assertEqual(comparmFR1, outList[1])

    def test_help1(self):
        apptestutils.displayNextTest(self)
        outList, outs, errs = \
            self.commonSP(
                "ExternalArgs_Read.py --help")
        #for i, line in enumerate(outList):
        #    print('arg %d: %s' % (i, line))
        print(outs)
if __name__ == '__main__':
    unittest.main()


