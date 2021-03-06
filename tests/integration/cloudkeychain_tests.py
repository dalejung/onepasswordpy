import os.path

from unittest2 import TestCase

import onepassword.keychain


class CloudKeychainIntegrationTestCase(TestCase):
    test_file_root = os.path.realpath(os.path.join(__file__, '..', '..', '..', 'data', 'sample.cloudkeychain'))

    def test_open(self):
        c = onepassword.keychain.CKeychain(self.test_file_root)
        c.unlock("fred")

    def test_item_parsing(self):
        c = onepassword.keychain.CKeychain(self.test_file_root)
        c.unlock("fred")
        skype_item = c.get_by_uuid('2A632FDD32F5445E91EB5636C7580447')
        self.assertEqual(skype_item.title, 'Skype')
        self.assertEqual(skype_item.decrypt()['fields'][1]['value'], 'dej3ur9unsh5ian1and5')
