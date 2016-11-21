import settings
from unittest import TestCase
from cpdk_db import import_user_models


class TestCPDKModelMultiDir(TestCase):
    def test_import_multiple_files(self):

        settings.MODELS_DIR = 'models'
        print "importing from %s" % settings.MODELS_DIR
        models = import_user_models()
        print "%d models imported: %s" % (len(models), str(models))
        self.assertEqual(len(models), 3)