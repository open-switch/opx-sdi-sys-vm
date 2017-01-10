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

import time
import os
import subprocess
import sdi_vm_common as common
import sdi_vm_common_consts as consts
import sdi_vm_cmdline as cmdline

#Main Menu options
MAIN_MENU_OPTICS_OPTION  = '1'
MAIN_MENU_FANTRAY_OPTION = '2'
MAIN_MENU_PSU_OPTION     = '3'
MAIN_MENU_THERMAL_OPTION = '4'
MAIN_MENU_QUIT_OPTION    = '-q'

#Optics Menu options
OPTIC_INSERT      = '1'
OPTIC_REMOVE      = '2'
OPTIC_SAME_INSERT = '3'

#Fantray Menu options
FANTRAY_INSERT           = '1'
FANTRAY_REMOVE           = '2'
FANTRAY_FAULT_INSERT     = '3'
FANTRAY_FAULT_CLEAR      = '4'
FANTRAY_FAN_FAULT_INSERT = '5'
FANTRAY_FAN_FAULT_CLEAR  = '6'

#Psu Menu options
PSU_INSERT           = '1'
PSU_REMOVE           = '2'
PSU_FAULT_INSERT     = '3'
PSU_FAULT_CLEAR      = '4'
PSU_FAN_FAULT_INSERT = '5'
PSU_FAN_FAULT_CLEAR  = '6'

#Psu Menu options
THERMAL_INSERT_FAULT = '1'
THERMAL_CLEAR_FAULT  = '2'
THERMAL_SET_TEMP     = '3'
THERMAL_LIST_TEMP    = '4'

#os10-vm-plat-event script name
OS10_VM_PLAT_EVENT = 'os10-vm-plat-event'




#insert optic in port=1 type=36
def chk_port_optics_is_present(args):
    """ Check for port optics presence """

    res_hdl = common.g_port_tbl[int(args[cmdline.PORT_ID])]['res_hdl']
    curr_state = common.get_port_optics_state(res_hdl)
    return curr_state == consts.PLAT_MEDIA_PRESENT

port                 = '1'
optic_type           = '36'
insert_optic         = {
    'name'        : cmdline.INSERT_OPTIC_ACTION,
    'args'        : {cmdline.PORT_ID : port, cmdline.OPTIC_TYPE : optic_type},

    'interactive' : [MAIN_MENU_OPTICS_OPTION, OPTIC_INSERT, port, optic_type,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_OPTIC_ACTION,
                     cmdline.PORT_ID, port,
                     cmdline.OPTIC_TYPE, optic_type],

    'check'       : chk_port_optics_is_present,
    'i_state'     : False,
    'c_state'     : False
}




#remove optic in port=1
def chk_port_optics_is_absent(args):
    """ Check for port optics absence """

    res_hdl = common.g_port_tbl[int(args[cmdline.PORT_ID])]['res_hdl']
    curr_state = common.get_port_optics_state(res_hdl)
    return curr_state == consts.PLAT_MEDIA_NOT_PRESENT

port                 = '1'
remove_optic         = {
    'name'        : cmdline.REMOVE_OPTIC_ACTION,
    'args'        : {cmdline.PORT_ID : port},

    'interactive' : [MAIN_MENU_OPTICS_OPTION, OPTIC_REMOVE, port,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.REMOVE_OPTIC_ACTION,
                     cmdline.PORT_ID, port],

    'check'       : chk_port_optics_is_absent,
    'i_state'     : False,
    'c_state'     : False
}




#insert fantray in slot=1
def chk_fantray_is_present(args):
    """ Check for fantray presence """

    res_hdl = common.g_fantray_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_state(res_hdl)
    return curr_state == consts.PLAT_MEDIA_PRESENT

slot                 = '1'
insert_fantray       = {
    'name'        : cmdline.INSERT_FANTRAY_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_FANTRAY_OPTION, FANTRAY_INSERT, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_FANTRAY_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_fantray_is_present,
    'i_state'     : False,
    'c_state'     : False
}




#remove fantray in slot=1
def chk_fantray_is_absent(args):
    """ Check for fantray absence """

    res_hdl = common.g_fantray_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_state(res_hdl)
    return curr_state == consts.PLAT_MEDIA_NOT_PRESENT

slot                 = '1'
remove_fantray       = {
    'name'        : cmdline.REMOVE_FANTRAY_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_FANTRAY_OPTION, FANTRAY_REMOVE, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                    cmdline.ACTION, cmdline.REMOVE_FANTRAY_ACTION,
                    cmdline.SLOT, slot],

    'check'       : chk_fantray_is_absent,
    'i_state'     : False,
    'c_state'     : False
}




#insert fantray fault in slot=1
def chk_fantray_is_faulty(args):
    """ Check for fantray fault """

    res_hdl = common.g_fantray_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_status(res_hdl)
    return curr_state == consts.PLAT_MEDIA_FAULT

slot                 = '1'
insert_fantray_fault = {
    'name'        : cmdline.INSERT_FANTRAY_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_FANTRAY_OPTION, FANTRAY_FAULT_INSERT, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_FANTRAY_FAULT_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_fantray_is_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#clear fantray fault in slot=1
def chk_fantray_is_not_faulty(args):
    """ Check for fantray fault """

    res_hdl = common.g_fantray_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_status(res_hdl)
    return curr_state == consts.PLAT_MEDIA_NO_FAULT

slot                 = '1'
clear_fantray_fault  = {
    'name'        : cmdline.CLEAR_FANTRAY_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_FANTRAY_OPTION, FANTRAY_FAULT_CLEAR, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.CLEAR_FANTRAY_FAULT_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_fantray_is_not_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#insert fantray fan fault in slot=1, fan-id=1
def chk_fantray_fan_is_faulty(args):
    """ Check for fantray fan fault """

    media_entry = common.g_fantray_tbl[int(args[cmdline.SLOT])]

    # Get current media state
    state = common.get_entity_info_state(media_entry['res_hdl'])

    if state == consts.PLAT_MEDIA_PRESENT:

        if (int(args[cmdline.FAN_ID]) in xrange(1, media_entry['fNum'] + 1)):
            curr_state = common.get_entity_fan_status(
                media_entry['f%sres_hdl' % int(args[cmdline.FAN_ID])])

            return curr_state == consts.PLAT_MEDIA_FAULT

slot                     = '1'
fan_id                   = '1'
insert_fantray_fan_fault = {
    'name'        : cmdline.INSERT_FANTRAY_FAN_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot, cmdline.FAN_ID : fan_id},

    'interactive' : [MAIN_MENU_FANTRAY_OPTION, FANTRAY_FAN_FAULT_INSERT, slot,
                     fan_id, MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_FANTRAY_FAN_FAULT_ACTION,
                     cmdline.SLOT, slot,
                     cmdline.FAN_ID, fan_id],

    'check'       : chk_fantray_fan_is_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#clear fantray fan fault in slot=1, fan-id=1
def chk_fantray_fan_is_not_faulty(args):
    """ Check for fantray fan fault """

    media_entry = common.g_fantray_tbl[int(args[cmdline.SLOT])]

    # Get current media state
    state = common.get_entity_info_state(media_entry['res_hdl'])

    if state == consts.PLAT_MEDIA_PRESENT:

        if (int(args[cmdline.FAN_ID]) in xrange(1, media_entry['fNum'] + 1)):
            curr_state = common.get_entity_fan_status(
                media_entry['f%sres_hdl' % int(args[cmdline.FAN_ID])])

            return curr_state == consts.PLAT_MEDIA_NO_FAULT


slot                    = '1'
fan_id                  = '1'
clear_fantray_fan_fault = {
    'name'        : cmdline.CLEAR_FANTRAY_FAN_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot, cmdline.FAN_ID : fan_id},

    'interactive' : [MAIN_MENU_FANTRAY_OPTION, FANTRAY_FAN_FAULT_CLEAR, slot,
                     fan_id, MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.CLEAR_FANTRAY_FAN_FAULT_ACTION,
                     cmdline.SLOT, slot,
                     cmdline.FAN_ID, fan_id],

    'check'       : chk_fantray_fan_is_not_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#insert psu in slot=1
def chk_psu_is_present(args):
    """ Check for psu presence """

    res_hdl = common.g_psu_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_state(res_hdl)
    return curr_state == consts.PLAT_MEDIA_PRESENT

slot             = '1'
insert_psu       = {
    'name'        : cmdline.INSERT_PSU_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_PSU_OPTION, PSU_INSERT, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_PSU_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_psu_is_present,
    'i_state'     : False,
    'c_state'     : False
}




#remove psu in slot=1
def chk_psu_is_absent(args):
    """ Check for psu absence """

    res_hdl = common.g_psu_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_state(res_hdl)
    return curr_state == consts.PLAT_MEDIA_NOT_PRESENT

slot             = '1'
remove_psu       = {
    'name'        : cmdline.REMOVE_PSU_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_PSU_OPTION, PSU_REMOVE, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.REMOVE_PSU_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_psu_is_absent,
    'i_state'     : False,
    'c_state'     : False
}




#insert psu fault in slot=1
def chk_psu_is_faulty(args):
    """ Check for psu fault """

    res_hdl = common.g_psu_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_status(res_hdl)
    return curr_state == consts.PLAT_MEDIA_FAULT

slot             = '1'
insert_psu_fault = {
    'name'        : cmdline.INSERT_PSU_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_PSU_OPTION, PSU_FAULT_INSERT, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_PSU_FAULT_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_psu_is_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#clear psu fault in slot=1
def chk_psu_is_not_faulty(args):
    """ Check for psu fault """

    res_hdl = common.g_psu_tbl[int(args[cmdline.SLOT])]['res_hdl']
    curr_state = common.get_entity_info_status(res_hdl)
    return curr_state == consts.PLAT_MEDIA_NO_FAULT

slot             = '1'
clear_psu_fault  = {
    'name'        : cmdline.CLEAR_PSU_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot},

    'interactive' : [MAIN_MENU_PSU_OPTION, PSU_FAULT_CLEAR, slot,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.CLEAR_PSU_FAULT_ACTION,
                     cmdline.SLOT, slot],

    'check'       : chk_psu_is_not_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#insert psu fault in slot=1, fan-id=1
def chk_psu_fan_is_faulty(args):
    """ Check for psu fan fault """

    media_entry = common.g_psu_tbl[int(args[cmdline.SLOT])]

    # Get current media state
    state = common.get_entity_info_state(media_entry['res_hdl'])

    if state == consts.PLAT_MEDIA_PRESENT:

        if (int(args[cmdline.FAN_ID]) in xrange(1, media_entry['fNum'] + 1)):
            curr_state = common.get_entity_fan_status(
                media_entry['f%sres_hdl' % int(args[cmdline.FAN_ID])])

            return curr_state == consts.PLAT_MEDIA_FAULT

slot                 = '1'
fan_id               = '1'
insert_psu_fan_fault = {
    'name'        : cmdline.INSERT_PSU_FAN_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot, cmdline.FAN_ID : fan_id},

    'interactive' : [MAIN_MENU_PSU_OPTION, PSU_FAN_FAULT_INSERT, slot,
                     fan_id, MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_PSU_FAN_FAULT_ACTION,
                     cmdline.SLOT, slot,
                     cmdline.FAN_ID, fan_id],

    'check'       : chk_psu_fan_is_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#clear psu fault in slot=1, fan-id=1
def chk_psu_fan_is_not_faulty(args):
    """ Check for psu fan fault """

    media_entry = common.g_psu_tbl[int(args[cmdline.SLOT])]

    # Get current media state
    state = common.get_entity_info_state(media_entry['res_hdl'])

    if state == consts.PLAT_MEDIA_PRESENT:

        if (int(args[cmdline.FAN_ID]) in xrange(1, media_entry['fNum'] + 1)):
            curr_state = common.get_entity_fan_status(
                media_entry['f%sres_hdl' % int(args[cmdline.FAN_ID])])

            return curr_state == consts.PLAT_MEDIA_NO_FAULT

slot                = '1'
fan_id              = '1'
clear_psu_fan_fault = {
    'name'        : cmdline.CLEAR_PSU_FAN_FAULT_ACTION,
    'args'        : {cmdline.SLOT : slot, cmdline.FAN_ID : fan_id},

    'interactive' : [MAIN_MENU_PSU_OPTION, PSU_FAN_FAULT_CLEAR, slot,
                     fan_id, MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.CLEAR_PSU_FAN_FAULT_ACTION,
                     cmdline.SLOT, slot,
                     cmdline.FAN_ID, fan_id],

    'check'       : chk_psu_fan_is_not_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#insert thermal sensor fault in type=1
def chk_temp_sensor_is_faulty(args):
    """ Check for thermal sensor fault """

    res_hdl = common.g_thermal_tbl[int(args[cmdline.TEMP_SENSOR_ID])]['res_hdl']
    curr_state = common.get_thermal_status(res_hdl)
    return curr_state == consts.PLAT_MEDIA_FAULT


sensor_id            = '1'
insert_thermal_fault = {
    'name'        : cmdline.INSERT_TEMP_SENSOR_FAULT_ACTION,
    'args'        : {cmdline.TEMP_SENSOR_ID : sensor_id},

    'interactive' : [MAIN_MENU_THERMAL_OPTION, THERMAL_INSERT_FAULT,
                     sensor_id, MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.INSERT_TEMP_SENSOR_FAULT_ACTION,
                     '--temp-sensor-id', sensor_id],

    'check'       : chk_temp_sensor_is_faulty,
    'i_state'     : False,
    'c_state'     : False
}




#clear thermal sensor fault in type=1
def chk_temp_sensor_is_not_faulty(args):
    """ Check for thermal sensor fault """

    res_hdl = common.g_thermal_tbl[int(args[cmdline.TEMP_SENSOR_ID])]['res_hdl']
    curr_state = common.get_thermal_status(res_hdl)
    return curr_state == consts.PLAT_MEDIA_NO_FAULT


sensor_id           = '1'
clear_thermal_fault = {
    'name'        : cmdline.CLEAR_TEMP_SENSOR_FAULT_ACTION,
    'args'        : {cmdline.TEMP_SENSOR_ID : sensor_id},

    'interactive' : [MAIN_MENU_THERMAL_OPTION, THERMAL_CLEAR_FAULT, sensor_id,
                     MAIN_MENU_QUIT_OPTION],

    'cmdline'     : [OS10_VM_PLAT_EVENT,
                     cmdline.ACTION, cmdline.CLEAR_TEMP_SENSOR_FAULT_ACTION,
                     '--temp-sensor-id', sensor_id],

    'check'       : chk_temp_sensor_is_not_faulty,
    'i_state'     : False,
    'c_state'     : False
}


test_cases = [remove_optic,
              insert_optic,

              remove_fantray,
              insert_fantray,

              clear_fantray_fault,
              insert_fantray_fault,
              clear_fantray_fault,

              clear_fantray_fan_fault,
              insert_fantray_fan_fault,
              clear_fantray_fan_fault,

              remove_psu,
              insert_psu,

              clear_psu_fault,
              insert_psu_fault,
              clear_psu_fault,

              clear_psu_fan_fault,
              insert_psu_fan_fault,
              clear_psu_fan_fault,

              clear_thermal_fault,
              insert_thermal_fault,
              clear_thermal_fault]


def print_test_results():
    """Print test results"""

    total_fail = 0
    for test in test_cases:
        print "Test: " + test['name']

        if test['i_state']:
            print '\tInteractive : Success'
        else:
            print '\tInteractive : Failed'
            total_fail += 1

        if test['c_state']:
            print '\tCmdline     : Success'
        else:
            print '\tCmdline     : Failed'
            total_fail += 1

        print '\n'
    print 'Total test cases   : ', len(test_cases)
    print 'Failed test cases  : ', total_fail
    print 'Success test cases : ', len(test_cases) - total_fail


def execute_interactive_test(input_test):
    """Runs the tests in interactive format"""

    print "\n Running interactive test case : " + input_test['name']
    tarpipe = subprocess.Popen([OS10_VM_PLAT_EVENT], stdin=subprocess.PIPE)

    for line in input_test['interactive']:
        tarpipe.stdin.write(line + '\n')

    tarpipe.stdin.close()
    tarpipe.wait()

    func = input_test['check']
    input_test['i_state'] = func(input_test['args']);


def execute_cmdline_test(input_test):
    """Runs the tests in cmdline format"""

    print "\n Running cmdline test case : " + input_test['name']
    subprocess.call(input_test['cmdline'])
    func = input_test['check']
    input_test['c_state'] = func(input_test['args']);


if __name__ == "__main__":
    """test main"""

    #initialization
    common.init_script()

    print '\n  Media:'
    # Build tables of resource handles
    common.bld_port_tbl()
    common.bld_fantray_tbl()
    common.bld_psu_tbl()
    common.bld_thermal_tbl()
    print '\n'

    for test in test_cases:
        execute_interactive_test(test)

    for test in test_cases:
        execute_cmdline_test(test)

    print_test_results()

    #exit process
    common.exit_script()
