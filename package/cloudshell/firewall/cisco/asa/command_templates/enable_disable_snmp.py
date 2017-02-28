#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template import CommandTemplate

SHOW_SNMP_COMMUNITY = CommandTemplate("do more system:running-config | inc snmp-server community")
ENABLE_SNMP = CommandTemplate("snmp-server community {snmp_community} ro")
DISABLE_SNMP = CommandTemplate("no snmp-server community {snmp_community}")
