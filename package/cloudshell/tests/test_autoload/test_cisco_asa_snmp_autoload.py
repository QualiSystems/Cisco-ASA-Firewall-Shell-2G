#!/usr/bin/python
# -*- coding: utf-8 -*-

import mock
import unittest

from cloudshell.firewall.cisco.asa.autoload.cisco_asa_snmp_autoload import CiscoASASNMPAutoload


class TestCiscoASASaveFlow(unittest.TestCase):
    def setUp(self):
        self.snmp_handler = mock.MagicMock()
        logger = mock.MagicMock()
        self.shell_name = "Cisco ASA Firewall"
        self.shell_type = "CS_Firewall"
        self.resource_name = "Test_ASA"
        self.supported_os = [r"A(daptive)? ?S(ecurity)? ?A(ppliance)?"]
        super(TestCiscoASASaveFlow, self).setUp()
        self.tested_instance = CiscoASASNMPAutoload(snmp_handler=self.snmp_handler,
                                                    shell_name=self.shell_name,
                                                    shell_type=self.shell_type,
                                                    resource_name=self.resource_name,
                                                    logger=logger)

    def tearDown(self):
        super(TestCiscoASASaveFlow, self).tearDown()
        del self.tested_instance

    def test_is_valid_device_os_true(self):
        """ Correct device Operation System """

        self.snmp_handler.get_property.return_value = "Adaptive Security Appliance"
        self.assertTrue(self.tested_instance._is_valid_device_os(self.supported_os))

    def test_is_valid_device_os_false(self):
        """ Wrong device Operation System """

        self.snmp_handler.get_property.return_value = "Some Device System Description"
        self.assertFalse(self.tested_instance._is_valid_device_os(self.supported_os))

    def test__load_snmp_tables_success(self):
        """ Error during load Entity Table information """

        self.tested_instance._get_entity_table = mock.MagicMock(return_value={"Some data": "from Entity Table"})

        self.tested_instance._load_snmp_tables()
        self.assertEqual(self.snmp_handler.get_table.call_count, 8)

    # def test__load_snmp_tables_fail_entity_table(self):
    #     """ Error during load Entity Table information """
    #
    #     self.tested_instance._get_entity_table = mock.MagicMock(return_value=None)
    #
    #     with self.assertRaisesRegexp(Exception, r"Cannot load entPhysicalTable"):
    #         self.tested_instance._load_snmp_tables()
    #
    #         # self.assertEqual(self.snmp_handler.get_table, 3)
    #     self.snmp_handler.get_table.assert_called_once_with("IF-MIB", self.tested_instance.IF_ENTITY)

            # 'IF-MIB', self.IF_ENTITY

        # folder_path = mock.MagicMock()
        # sys_actions = mock.MagicMock()
        # system_actions_class.return_value = sys_actions
        # action_map = sys_actions.prepare_action_map()
        #
        # self.tested_instance.execute_flow(folder_path, "running")
        # sys_actions.copy.assert_called_once_with("running-config", folder_path, action_map=action_map)
