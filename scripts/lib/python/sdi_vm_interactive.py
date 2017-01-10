#!/usr/bin/python
# Copyright (c) 2016 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED ON AN  *AS IS* BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
# LIMITATION (ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
# FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.

""" This module provides interaction capabilities to the platform-event script """

import sdi_vm_common as common
import sdi_vm_common_consts as consts

# Help string for platform
HELP_STRING_PLATFORM_EVENT = '\n\
  Enter PlatCmd: [-h|-q|#]\n\
    -h    Help\n\
    -q    Quit\n\
     #    Event to generate\n\
          1 = Optics\n\
          2 = Fantray\n\
          3 = PSU\n\
          4 = Thermal Sensors\n'

# Help string for optics
HELP_STRING_OPTICS_EVENT = '\n\
  Enter OpticsCmd: [-h|-q|-e|#]\n\
    -h    Help\n\
    -q    Quit\n\
    -e    Exit\n\
     #    Optics event to generate\n\
          1 = Insert port optics\n\
          2 = Remove port optics\n\
          3 = Insert same port optics (optics presence)\n'

# Help string for optics presence
HELP_STRING_OPTICS_PRESENCE_EVENT = '\n\
  Enter OpticsPort%s: [-q|-e|#]\n\
    -q    Quit\n\
    -e    Exit\n\
     #    Port [1..%d]\n'

# Help string for optics insert
HELP_STRING_OPTICS_INSERT_EVENT = '\n\
  Enter opticsPortIns: [-h|-q|-e|-m|#]\n\
    -h    Help\n\
    -q    Quit\n\
    -e    Exit\n\
    -m    Mode QSFP/QSFP-PLUS (%s)\n\
     #    Port [1..%d]\n\
          Optics Type [1..%d]    Default: 36  QSFP_40GBASE_CR4_1M\n'

# Help string for fantray
HELP_STRING_MEDIA_EVENT = '\n\
  Enter %sCmd: [-h|-q|-e|#]\n\
    -h    Help\n\
    -q    Quit\n\
    -e    Exit\n\
     #    Event to generate\n\
          1 = Insert %s\n\
          2 = Remove %s\n\
          3 = Insert %s fault\n\
          4 = Clear  %s fault\n\
          5 = Insert %s fan fault\n\
          6 = Clear  %s fan fault\n'

# Help string for entity media state
HELP_STRING_MEDIA_STATE_EVENT = '\n\
  Enter %s%s: [-q|-e|#]\n\
    -q    Quit\n\
    -e    Exit\n\
     #    %s [1..%d]\n'

# Help string for entity media fault
HELP_STRING_MEDIA_FAULT_EVENT = '\n\
  Enter %sFlt%s: [-q|-e|#]\n\
    -q    Quit\n\
    -e    Exit\n\
     #    %s [1..%d]\n'

# Help string for entity fan fault
HELP_STRING_MEDIA_FAN_FAULT_EVENT = '\n\
  Enter %sFanFlt%s: [-q|-e|#]\n\
    -q    Quit\n\
    -e    Exit\n\
     #    %s [1..%d]\n\
          Fan [1..%d]\n'

# Help string for thermal
HELP_STRING_THERMAL_EVENT = '\n\
  Enter ThermalCmd: [-h|-q|-e|#]\n\
    -h    Help\n\
    -q    Quit\n\
    -e    Exit\n\
     #    Thermal event to generate\n\
          1 = Insert fault\n\
          2 = Clear fault\n\
          3 = Set temp\n\
          4 = List sensors & temps\n'

# Help string for thermal fault
HELP_STRING_THERMAL_FAULT_EVENT = '\n\
  Enter ThermalFlt%s: [-q|-e|#]\n\
    -q    Quit\n\
    -e    Exit\n\
     #    Sensor [1..%d]'

# Help string for thermal temp
HELP_STRING_THERMAL_TEMP_EVENT = '\n\
  Enter ThermalSensor: [-q|-e|#]\n\
    -q    Quit\n\
    -e    Exit\n\
     #    Sensor [1..%d]\n\
          Temp [%d..%d]           Default: 20'


def process_optics_state(state):
    """Process the platform optics state event."""

    if state == consts.PLAT_MEDIA_NOT_PRESENT:
        cli_str = 'Rmv'

    else:
        cli_str = 'Pres'

    while True:

        print HELP_STRING_OPTICS_PRESENCE_EVENT % \
                (cli_str,
                 max(common.g_port_tbl.keys()))

        cmd = raw_input('Enter OpticsPort%s ' % (cli_str))

        if cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd.isdigit() and common.g_port_tbl.has_key(int(cmd)):

            # All chars of string are digits and within range
            common.chk_port_optics_state(int(cmd),
                                         common.g_port_tbl[int(cmd)]['res_hdl'],
                                         state)
        else:
            print '  Invalid OpticsPort%s %s\n' % (cli_str, cmd)


def process_optics_insert():
    """Process the platform optics insert event."""

    q_mode = consts.SDI_IDENT[common.g_qsfp_mode]

    while True:
        print HELP_STRING_OPTICS_INSERT_EVENT % \
              (q_mode['name'],
              max(common.g_port_tbl.keys()),
              max(consts.OPTICS_TABLE.keys()))

        common.print_optics_type()

        cmd = raw_input('Enter OpticsPortIns: ')

        if cmd in ['-h', 'h']:
            print HELP_STRING_OPTICS_INSERT_EVENT % \
                  (q_mode['name'],
                  max(common.g_port_tbl.keys()),
                  max(consts.OPTICS_TABLE.keys()))

            common.print_optics_type()

        elif cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd in ['-m', 'm']:

            if common.g_qsfp_mode == consts.PLAT_SDI_QSFP_MODE:
                common.g_qsfp_mode = consts.PLAT_SDI_QSFP_PLUS_MODE

            else:
                common.g_qsfp_mode = consts.PLAT_SDI_QSFP_MODE

            q_mode = consts.SDI_IDENT[common.g_qsfp_mode]
            print '    Change to %s mode' % (q_mode['name'])

        elif cmd.isdigit() and common.g_port_tbl.has_key(int(cmd)):
            # All chars of string are digits and within range

            o_type = raw_input('Enter OpticsTypeIns: ')

            if o_type.isdigit() and consts.OPTICS_TABLE.has_key(int(o_type)):

                common.insert_port_optics(int(cmd),
                                          int(o_type),
                                          common.g_qsfp_mode)

            else:
                print '  Unexpected OpticsTypeIns %s' % (o_type)

        else:
            print '  Unexpected OpticsPortIns %s' % (cmd)


def process_optics_event():
    """Process the platform optics events."""

    while True:
        print HELP_STRING_OPTICS_EVENT

        cmd = raw_input('Enter OpticsCmd: ')
        if cmd in ['-h', 'h']:
            print HELP_STRING_OPTICS_EVENT

        elif cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd == '1':
            process_optics_insert()

        elif cmd == '2':
            process_optics_state(consts.PLAT_MEDIA_NOT_PRESENT)

        elif cmd == '3':
            process_optics_state(consts.PLAT_MEDIA_PRESENT)

        else:
            print '  Unexpected OpticsCmd %s' % (cmd)


def process_entity_fan_status(media_tbl, media_str, status):
    """Process the platform entity media fan fault status event."""

    # Get the max fan for script CLI prompt
    max_fan = media_tbl[1]['fNum']

    if status == consts.PLAT_MEDIA_NO_FAULT:
        cli_str = 'Clr'
    else:
        cli_str = 'Ins'

    while True:
        print HELP_STRING_MEDIA_FAN_FAULT_EVENT % (media_str,
                                                   cli_str,
                                                   media_str,
                                                   max(media_tbl.keys()),
                                                   max_fan)

        cmd = raw_input('Enter %sFanFlt%s: ' % (media_str, cli_str))

        if cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd.isdigit() and media_tbl.has_key(int(cmd)):
            # All chars of string are digits and within range

            media_entry = media_tbl[int(cmd)]

            # Get current media state
            state = common.get_entity_info_state(media_entry['res_hdl'])

            if state == consts.PLAT_MEDIA_PRESENT:
                fan = raw_input('Enter %sFanFlt%sFan: ' % (media_str, cli_str))

                if fan.isdigit() and \
                   (int(fan) in xrange(1, media_entry['fNum'] + 1)):

                    common.set_entity_fan_status(media_entry['f%sres_hdl' \
                                                        % int(fan)], status)

                else:
                    print '  Unexpected %sFanFlt%sFan %s' % (media_str,
                                                             cli_str,
                                                             fan)

            elif state == consts.PLAT_MEDIA_NOT_PRESENT:
                print '    Error %s %s not present' % (media_str, cmd)

            else:
                print '    Error in reading %s %s state %s' % (media_str,
                                                               cmd,
                                                               state)
        else:
            print '  Unexpected %s %s\n' % (media_str, cmd)


def process_entity_fault(media_tbl, media_str, status):
    """Process the platform entity media fault event."""

    if status == consts.PLAT_MEDIA_NO_FAULT:
        cli_str = 'Clr'
    else:
        cli_str = 'Ins'

    while True:
        print HELP_STRING_MEDIA_FAULT_EVENT % (media_str,
                                               cli_str,
                                               media_str,
                                               max(media_tbl.keys()))

        cmd = raw_input('Enter %sFlt%s: ' % (media_str, cli_str))

        if cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd.isdigit() and media_tbl.has_key(int(cmd)):

            # All chars of string are digits and within range
            res_hdl = media_tbl[int(cmd)]['res_hdl']
            state = common.get_entity_info_state(res_hdl)

            if state == consts.PLAT_MEDIA_PRESENT:
                common.set_entity_info_status(res_hdl, status)

            elif state == consts.PLAT_MEDIA_NOT_PRESENT:
                print '    Error %s %s not present' % (media_str, cmd)

            else:
                print '    Error in reading %s %s state %d' % (media_str,
                                                               cmd,
                                                               state)

        else:
            print '  Unexpected %sFlt%s %s\n' % (media_str, cli_str, cmd)


def process_entity_state(media_tbl, media_str, state):
    """Process the platform entity info media state."""

    if state == consts.PLAT_MEDIA_NOT_PRESENT:
        cli_str = 'Rmv'

    else:
        cli_str = 'Ins'

    while True:
        print HELP_STRING_MEDIA_STATE_EVENT % (media_str,
                                               cli_str,
                                               media_str,
                                               max(media_tbl.keys()))
        cmd = raw_input('Enter %s%s: ' % (media_str, cli_str))

        if cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd.isdigit() and media_tbl.has_key(int(cmd)):
            # All chars of string are digits and within range
            res_hdl = media_tbl[int(cmd)]['res_hdl']

            # Get current state of entity media
            cur_state = common.get_entity_info_state(res_hdl)
            if cur_state == consts.PLAT_MEDIA_PRESENT \
               or cur_state == consts.PLAT_MEDIA_NOT_PRESENT:

                if cur_state != state:
                    common.set_entity_info_state(res_hdl, state)

                else:
                    print '   %s %s already %s' % (media_str, cmd, cli_str)
            else:
                print '    Error in reading %s %s state %d' % (media_str,
                                                               cmd,
                                                               state)
        else:
            print '  Unexpected %s%s %s\n' % (media_str, cli_str, cmd)


def process_entity_event(media_tbl, media_str):
    """Process the platform entity info media events."""

    while True:
        print HELP_STRING_MEDIA_EVENT % (media_str,
                                         media_str,
                                         media_str,
                                         media_str,
                                         media_str,
                                         media_str,
                                         media_str)

        cmd = raw_input('Enter %sCmd: ' % (media_str))

        if cmd in ['-h', 'h']:
            print HELP_STRING_MEDIA_EVENT % (media_str,
                                             media_str,
                                             media_str,
                                             media_str,
                                             media_str,
                                             media_str,
                                             media_str)
        elif cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd == '1':
            process_entity_state(media_tbl,
                                 media_str,
                                 consts.PLAT_MEDIA_PRESENT)

        elif cmd == '2':
            process_entity_state(media_tbl,
                                 media_str,
                                 consts.PLAT_MEDIA_NOT_PRESENT)


        elif cmd == '3':
            process_entity_fault(media_tbl,
                                 media_str,
                                 consts.PLAT_MEDIA_FAULT)


        elif cmd == '4':
            process_entity_fault(media_tbl,
                                 media_str,
                                 consts.PLAT_MEDIA_NO_FAULT)


        elif cmd == '5':
            process_entity_fan_status(media_tbl,
                                      media_str,
                                      consts.PLAT_MEDIA_FAULT)


        elif cmd == '6':
            process_entity_fan_status(media_tbl,
                                      media_str,
                                      consts.PLAT_MEDIA_NO_FAULT)

        else:
            print '  Unexpected %sCmd %s' % (media_str, cmd)


def process_thermal_fault(status):
    """Process the platform thermal sensor fault event."""
    if status == consts.PLAT_MEDIA_NO_FAULT:
        cli_str = 'Clr'

    else:
        cli_str = 'Ins'

    while True:
        print HELP_STRING_THERMAL_FAULT_EVENT % \
                (cli_str,
                 max(common.g_thermal_tbl.keys()))

        for idx in common.g_thermal_tbl:
            print '          %d = %s' % (idx,
                                         common.g_thermal_tbl[idx]['name'])
            print '\n'

        cmd = raw_input('Enter ThermalFlt%s: ' % (cli_str))

        if cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd.isdigit() and common.g_thermal_tbl.has_key(int(cmd)):
            # All chars of string are digits and within range
            res_hdl = common.g_thermal_tbl[int(cmd)]['res_hdl']
            common.set_thermal_status(res_hdl, status)
            #print common.get_thermal_status(res_hdl)

        else:
            print '  Unexpected ThermalFlt%s %s\n' % (cli_str, cmd)


def process_thermal_temp():
    """Process the platform thermal temperature event."""

    while True:
        print HELP_STRING_THERMAL_TEMP_EVENT % \
                (max(common.g_thermal_tbl.keys()),
                 consts.PLAT_THERMAL_MIN_TEMP,
                 consts.PLAT_THERMAL_MAX_TEMP)

        # List sensors & current temps
        common.list_thermal_sensors()

        cmd = raw_input('Enter ThermalSensor: ')
        if cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd.isdigit() and common.g_thermal_tbl.has_key(int(cmd)):
            # All chars of string are digits and within range
            temp = raw_input('Enter ThermalTemp: ')
            if temp.isdigit() and \
               (int(temp) in xrange(consts.PLAT_THERMAL_MIN_TEMP,
                                    consts.PLAT_THERMAL_MAX_TEMP + 1)):

                common.set_thermal_temp(common.g_thermal_tbl \
                                        [int(cmd)]['res_hdl'], temp)

            else:
                print '  Unexpected ThermalTemp %s\n' % (temp)

        else:
            print '  Unexpected ThermalSensor %s\n' % (cmd)


def process_thermal_event():
    """Process the platform thermal sensor events."""

    while True:
        print HELP_STRING_THERMAL_EVENT

        cmd = raw_input('Enter ThermalCmd: ')

        if cmd in ['-h', 'h']:
            print HELP_STRING_MEDIA_EVENT

        elif cmd in ['-q', 'q']:
            common.exit_script()

        elif cmd in ['-e', 'e']:
            break

        elif cmd == '1':
            process_thermal_fault(consts.PLAT_MEDIA_FAULT)

        elif cmd == '2':
            process_thermal_fault(consts.PLAT_MEDIA_NO_FAULT)

        elif cmd == '3':
            process_thermal_temp()

        elif cmd == '4':
            common.list_thermal_sensors()

        else:
            print '  Unexpected ThermalCmd %s' % (cmd)


def execute_interactive():
    """Process the platform thermal sensor events."""

    while True:
        print HELP_STRING_PLATFORM_EVENT

        cmd = raw_input('Enter PlatCmd: ')

        if cmd in ['-h', 'h']:
            print HELP_STRING_PLATFORM_EVENT

        elif cmd in ['-q', 'q']:
            break

        elif cmd == '1':
            process_optics_event()

        elif cmd == '2':
            process_entity_event(common.g_fantray_tbl,
                                 consts.PLAT_MEDIA_FANTRAY_STR)

        elif cmd == '3':
            process_entity_event(common.g_psu_tbl,
                                 consts.PLAT_MEDIA_PSU_STR)

        elif cmd == '4':
            process_thermal_event()

        else:
            print '  Unexpected PlatCmd %s' % (cmd)
