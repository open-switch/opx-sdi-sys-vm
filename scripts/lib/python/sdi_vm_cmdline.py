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

""" This module provides scripting capabilities to the platform-event script """

import argparse
import sdi_vm_common as common
import sdi_vm_common_consts as consts
import sdi_vm_interactive as interactive

#commandline actions
INSERT_OPTIC_ACTION             = 'insert-optic'
REMOVE_OPTIC_ACTION             = 'remove-optic'
INSERT_FANTRAY_ACTION           = 'insert-fantray'
REMOVE_FANTRAY_ACTION           = 'remove-fantray'
INSERT_FANTRAY_FAULT_ACTION     = 'insert-fantray-fault'
CLEAR_FANTRAY_FAULT_ACTION      = 'clear-fantray-fault'
INSERT_FANTRAY_FAN_FAULT_ACTION = 'insert-fantray-fan-fault'
CLEAR_FANTRAY_FAN_FAULT_ACTION  = 'clear-fantray-fan-fault'
INSERT_PSU_ACTION               = 'insert-psu'
REMOVE_PSU_ACTION               = 'remove-psu'
INSERT_PSU_FAULT_ACTION         = 'insert-psu-fault'
CLEAR_PSU_FAULT_ACTION          = 'clear-psu-fault'
INSERT_PSU_FAN_FAULT_ACTION     = 'insert-psu-fan-fault'
CLEAR_PSU_FAN_FAULT_ACTION      = 'clear-psu-fan-fault'
INSERT_TEMP_SENSOR_FAULT_ACTION = 'insert-temp-sensor-fault'
CLEAR_TEMP_SENSOR_FAULT_ACTION  = 'clear-temp-sensor-fault'
SET_TEMP_SENSOR_VALUE_ACTION    = 'set-temp-sensor-value'
INTERACTIVE_ACTION              = 'interactive'
SHOW_TABLE_ACTION               = 'show-table'

#commandline arguments
ACTION         = '--action'
PORT_ID        = '--port-id'
OPTIC_TYPE     = '--optic-type'
FAN_ID         = '--fan-id'
SLOT           = '--slot'
TEMP_SENSOR_ID = '--temp-sensor-id'
TEMP_VALUE     = '--temp-value'
TABLE_NAME     = '--table-name'

#error str
ERROR_HELP_STRING = 'error:  argument --%s: Unexpected value \'%s\',(Choose from [%s..%s])'

#state dictionary
g_state_dict = {
    INSERT_OPTIC_ACTION             : consts.PLAT_MEDIA_PRESENT,
    INSERT_PSU_ACTION               : consts.PLAT_MEDIA_PRESENT,
    INSERT_FANTRAY_ACTION           : consts.PLAT_MEDIA_PRESENT,
    REMOVE_OPTIC_ACTION             : consts.PLAT_MEDIA_NOT_PRESENT,
    REMOVE_PSU_ACTION               : consts.PLAT_MEDIA_NOT_PRESENT,
    REMOVE_FANTRAY_ACTION           : consts.PLAT_MEDIA_NOT_PRESENT,
    INSERT_PSU_FAULT_ACTION         : consts.PLAT_MEDIA_FAULT,
    INSERT_FANTRAY_FAULT_ACTION     : consts.PLAT_MEDIA_FAULT,
    INSERT_TEMP_SENSOR_FAULT_ACTION : consts.PLAT_MEDIA_FAULT,
    INSERT_FANTRAY_FAN_FAULT_ACTION : consts.PLAT_MEDIA_FAULT,
    INSERT_PSU_FAN_FAULT_ACTION     : consts.PLAT_MEDIA_FAULT,
    CLEAR_PSU_FAULT_ACTION          : consts.PLAT_MEDIA_NO_FAULT,
    CLEAR_FANTRAY_FAULT_ACTION      : consts.PLAT_MEDIA_NO_FAULT,
    CLEAR_TEMP_SENSOR_FAULT_ACTION  : consts.PLAT_MEDIA_NO_FAULT,
    CLEAR_FANTRAY_FAN_FAULT_ACTION  : consts.PLAT_MEDIA_NO_FAULT,
    CLEAR_PSU_FAN_FAULT_ACTION      : consts.PLAT_MEDIA_NO_FAULT
}


def __get_state(action):
   return g_state_dict[action]


def __insert_optic_action(req):
    """ Function to process optic insert action """

    port_id    = req[PORT_ID]
    optic_type = req[OPTIC_TYPE]

    if common.g_port_tbl.has_key(port_id):

        if consts.OPTICS_TABLE.has_key(optic_type):

         common.insert_port_optics(port_id, optic_type, common.g_qsfp_mode)

        else:
            print ERROR_HELP_STRING % (OPTIC_TYPE, optic_type,
                                       min(consts.OPTICS_TABLE),
                                       max(consts.OPTICS_TABLE))
    else:
        print ERROR_HELP_STRING % (PORT_ID, port_id,
                                   min(common.g_port_tbl),
                                   max(common.g_port_tbl))


def __remove_optic_action(req):
    """ Function to process optic remove action """

    port_id  = req[PORT_ID]

    if common.g_port_tbl.has_key(port_id):

        res_hdl = common.g_port_tbl[port_id]['res_hdl']
        common.chk_port_optics_state(port_id, res_hdl, 0)

    else:
        print ERROR_HELP_STRING % (PORT_ID, port_id,
                                   min(common.g_port_tbl),
                                   max(common.g_port_tbl))


def __ins_rem_fantray_action(req):
    """ Function to process fantray insert/remove action """

    slot     = req[SLOT]

    if common.g_fantray_tbl.has_key(slot):

        res_hdl   = common.g_fantray_tbl[slot]['res_hdl']
        cur_state = common.get_entity_info_state(res_hdl)
        state     = __get_state(req[ACTION])

        if cur_state != consts.PLAT_MEDIA_ERROR:

            if cur_state != state:
                common.set_entity_info_state(res_hdl, state)

            else:
                print 'error: Fantray %s is already in state present=%s' \
                         % (slot, cur_state)
    else:
        print ERROR_HELP_STRING % (SLOT, slot,
                                   min(common.g_fantray_tbl),
                                   max(common.g_fantray_tbl))


def __ins_rem_psu_action(req):
    """ Function to process psu insert/remove action """

    slot     = req[SLOT]

    if common.g_psu_tbl.has_key(slot):

        res_hdl   = common.g_psu_tbl[slot]['res_hdl']
        cur_state = common.get_entity_info_state(res_hdl)
        state     = __get_state(req[ACTION])

        if cur_state != consts.PLAT_MEDIA_ERROR:

            if cur_state != state:
                common.set_entity_info_state(res_hdl, state)

            else:
                print 'error: Psu %s is already in state present=%s' \
                        % (slot, cur_state)

        else:
            print ERROR_HELP_STRING % (SLOT, slot,
                                       min(common.g_psu_tbl),
                                       max(common.g_psu_tbl))


def __ins_rem_fantray_fault_action(req):
    """ Function to process fantray fault action """

    slot     = req[SLOT]

    if common.g_fantray_tbl.has_key(slot):

        res_hdl   = common.g_fantray_tbl[slot]['res_hdl']
        cur_state = common.get_entity_info_state(res_hdl)
        state     = __get_state(req[ACTION])

        if cur_state == consts.PLAT_MEDIA_PRESENT:
            common.set_entity_info_status(res_hdl, state)

        elif cur_state == consts.PLAT_MEDIA_NOT_PRESENT:
            print 'error: Fantray %s is already in state present=0' % (slot)

    else:
        print ERROR_HELP_STRING % (SLOT, slot,
                                   min(common.g_fantray_tbl),
                                   max(common.g_fantray_tbl))


def __ins_rem_psu_fault_action(req):
    """ Function to process psu fault action """

    slot     = req[SLOT]

    if common.g_psu_tbl.has_key(slot):

        res_hdl   = common.g_psu_tbl[slot]['res_hdl']
        cur_state = common.get_entity_info_state(res_hdl)
        state     = __get_state(req[ACTION])

        if cur_state == consts.PLAT_MEDIA_PRESENT:
            common.set_entity_info_status(res_hdl, state)

        elif cur_state == consts.PLAT_MEDIA_NOT_PRESENT:
            print 'error: Psu %s is already in state present=0' % (slot)

    else:
        print ERROR_HELP_STRING % (SLOT, slot,
                                   min(common.g_psu_tbl),
                                   max(common.g_psu_tbl))


def __ins_rem_fantray_fan_fault_action(req):
    """ Function to process fantray fan fault action """

    slot     = req[SLOT]
    fan_id   = req[FAN_ID]

    if common.g_fantray_tbl.has_key(slot):

        entity    = common.g_fantray_tbl[slot]
        res_hdl   = common.g_fantray_tbl[slot]['res_hdl']
        cur_state = common.get_entity_info_state(res_hdl)

        if cur_state == consts.PLAT_MEDIA_PRESENT:

            if fan_id in xrange(1, entity['fNum'] + 1):
                state = __get_state(req[ACTION])
                common.set_entity_fan_status(entity['f%sres_hdl' % fan_id], state)

            else:
                print ERROR_HELP_STRING % (FAN_ID, fan_id, 1, entity['fNum'])

        elif cur_state == consts.PLAT_MEDIA_NOT_PRESENT:
            print 'error: Fantray %s is already in state present=0'     \
                    % (slot)

        else:
            print 'error: Unknown issue in reading data for Fantray %s' \
                    % (slot)
    else:
        print ERROR_HELP_STRING % (SLOT, slot,
                                   min(common.g_fantray_tbl),
                                   max(common.g_fantray_tbl))


def __ins_rem_psu_fan_fault_action(req):
    """ Function to process psu fan fault action """

    slot     = req[SLOT]
    fan_id   = req[FAN_ID]

    if common.g_psu_tbl.has_key(slot):
        entity    = common.g_psu_tbl[slot]
        res_hdl   = common.g_psu_tbl[slot]['res_hdl']
        cur_state = common.get_entity_info_state(res_hdl)

        if cur_state == consts.PLAT_MEDIA_PRESENT:

            if fan_id in xrange(1, entity['fNum'] + 1):
                state = __get_state(req[ACTION])
                common.set_entity_fan_status(entity['f%sres_hdl' % fan_id], state)

            else:
                print ERROR_HELP_STRING % (FAN_ID, fan_id, 1, entity['fNum'])

        elif cur_state == consts.PLAT_MEDIA_NOT_PRESENT:
            print 'error: Psu %s is already in state present=0' % (slot)

        else:
            print 'error: Unknown issue in reading data for Psu %s' % (slot)

    else:
        print ERROR_HELP_STRING % (SLOT, slot,
                                   min(common.g_psu_tbl),
                                   max(common.g_psu_tbl))


def __ins_rem_temp_fault_action(req):
    """ Function to process temperature sensor fault action """

    temp_sensor_id  = req[TEMP_SENSOR_ID]

    if common.g_thermal_tbl.has_key(temp_sensor_id):

        res_hdl = common.g_thermal_tbl[temp_sensor_id]['res_hdl']
        state   = __get_state(req[ACTION])
        common.set_thermal_status(res_hdl, state)

    else:
        common.list_thermal_sensors()
        print ERROR_HELP_STRING % (TEMP_SENSOR_ID, temp_sensor_id,
                                   min(common.g_thermal_tbl),
                                   max(common.g_thermal_tbl))


def __set_temp_value_action(req):
    """ Function to process set temperature value action """

    temp_sensor_id = req[TEMP_SENSOR_ID]
    temp_value     = req[TEMP_VALUE]

    if common.g_thermal_tbl.has_key(temp_sensor_id):

        if temp_value in xrange(consts.PLAT_THERMAL_MAX_TEMP):

             res_hdl = common.g_thermal_tbl[temp_sensor_id]['res_hdl']
             common.set_thermal_temp(res_hdl, temp_value)

        else:
            print ERROR_HELP_STRING % (TEMP_VALUE, temp_value,
                                       consts.PLAT_THERMAL_MIN_TEMP,
                                       consts.PLAT_THERMAL_MAX_TEMP)
    else:
        common.list_thermal_sensors()
        print ERROR_HELP_STRING % (TEMP_SENSOR_ID, temp_sensor_id,
                                   min(common.g_thermal_tbl),
                                   max(common.g_thermal_tbl))

def __show_table_action(req):
    """ Function to process showing table """


    common.show_table(req[TABLE_NAME])

# Dictionary for command line arguments
actions = {

     INTERACTIVE_ACTION: {
         'hlpr': None,
         'func': None,
         'args': None
     },

     INSERT_OPTIC_ACTION: {
         'hlpr': __insert_optic_action,
         'args': [ACTION, PORT_ID, OPTIC_TYPE]
     },

     REMOVE_OPTIC_ACTION: {
         'hlpr': __remove_optic_action,
         'args': [ACTION, PORT_ID]
     },

     INSERT_FANTRAY_ACTION: {
         'hlpr': __ins_rem_fantray_action,
         'args': [ACTION, SLOT]
     },

     REMOVE_FANTRAY_ACTION: {
         'hlpr': __ins_rem_fantray_action,
         'args': [ACTION, SLOT]
     },

     INSERT_FANTRAY_FAULT_ACTION: {
         'hlpr': __ins_rem_fantray_fault_action,
         'args': [ACTION, SLOT]
     },

     CLEAR_FANTRAY_FAULT_ACTION: {
         'hlpr': __ins_rem_fantray_fault_action,
         'args': [ACTION, SLOT]
     },

     INSERT_FANTRAY_FAN_FAULT_ACTION: {
         'hlpr': __ins_rem_fantray_fan_fault_action,
         'args': [ACTION, SLOT, FAN_ID]
     },

     CLEAR_FANTRAY_FAN_FAULT_ACTION: {
         'hlpr': __ins_rem_fantray_fan_fault_action,
         'args': [ACTION, SLOT, FAN_ID]
     },

     INSERT_PSU_ACTION: {
         'hlpr': __ins_rem_psu_action,
         'args': [ACTION, SLOT]
     },

     REMOVE_PSU_ACTION: {
         'hlpr': __ins_rem_psu_action,
         'args': [ACTION, SLOT]
     },

     INSERT_PSU_FAULT_ACTION: {
         'hlpr': __ins_rem_psu_fault_action,
         'args': [ACTION, SLOT]
     },

     CLEAR_PSU_FAULT_ACTION: {
         'hlpr': __ins_rem_psu_fault_action,
         'args': [ACTION, SLOT]
     },

     INSERT_PSU_FAN_FAULT_ACTION: {
         'hlpr': __ins_rem_psu_fan_fault_action,
         'args': [ACTION, SLOT, FAN_ID]
     },

     CLEAR_PSU_FAN_FAULT_ACTION: {
         'hlpr': __ins_rem_psu_fan_fault_action,
         'args': [ACTION, SLOT, FAN_ID]
     },

     INSERT_TEMP_SENSOR_FAULT_ACTION: {
         'hlpr': __ins_rem_temp_fault_action,
         'args': [ACTION, TEMP_SENSOR_ID]
     },

     CLEAR_TEMP_SENSOR_FAULT_ACTION: {
         'hlpr': __ins_rem_temp_fault_action,
         'args': [ACTION, TEMP_SENSOR_ID]
     },

     SET_TEMP_SENSOR_VALUE_ACTION: {
         'hlpr': __set_temp_value_action,
         'args': [ACTION, TEMP_SENSOR_ID, TEMP_VALUE]
     },

     SHOW_TABLE_ACTION: {
         'hlpr': __show_table_action,
         'args': [ACTION, TABLE_NAME]
    }
}


def parse_arguments(cmd_args):
    """Parses all the actions and required arguments
       and reacts accordingly"""

    giv = cmd_args
    req = actions[cmd_args[ACTION]]['args']

    if set(giv) != set(req):

        print 'error: arguments given for \'--action=%s\' don\'t match required arguments. (Provide %s)' % (cmd_args[ACTION], req)
        return

    actions[cmd_args[ACTION]]['hlpr'](cmd_args)



def enable_cmdline():
    """Enables accepting commandline arguments
       for the os10-vm-plat-events script"""

    parser = argparse.ArgumentParser()

    parser.add_argument(ACTION,
                        action='store',
                        dest=ACTION,
                        help='Desired action',
                        choices=actions.keys(),
                        default=INTERACTIVE_ACTION)

    parser.add_argument(SLOT,
                        action='store',
                        dest=SLOT,
                        type=int,
                        help='Slot of the fantray or Psu')

    parser.add_argument(PORT_ID,
                        action='store',
                        dest=PORT_ID,
                        type=int,
                        help='Port number')

    parser.add_argument(OPTIC_TYPE,
                        action='store',
                        dest=OPTIC_TYPE,
                        type=int,
                        help='Optic type')

    parser.add_argument(FAN_ID,
                        action='store',
                        dest=FAN_ID,
                        type=int,
                        help='Fan index')

    parser.add_argument(TEMP_VALUE,
                        action='store',
                        dest=TEMP_VALUE,
                        type=int,
                        help='Temperature value to be set')

    parser.add_argument(TEMP_SENSOR_ID,
                        action='store',
                        dest=TEMP_SENSOR_ID,
                        type=int,
                        help='Temperature sensor index')

    parser.add_argument(TABLE_NAME,
                        action='store',
                        dest=TABLE_NAME,
                        choices=[consts.TABLE_THERMAL_SENSOR, consts.TABLE_FAN,
                                 consts.TABLE_INFO, consts.TABLE_MEDIA,
                                 consts.TABLE_RESOURCES, consts.TABLE_MEDIA_PARAMS,
                                 consts.TABLE_MEDIA_VENDOR_INFO, consts.TABLE_PHYSICAL_LED,
                                 consts.TABLE_LED, consts.TABLE_DIGIT_DISPLAY_LED,
                                 consts.TABLE_PLD, consts.TABLE_MEDIA_CHANNEL,
                                 consts.TABLE_MEDIA_MONITOR_THRESHOLDS, consts.TABLE_NVRAM],
                        help='Table name')

    res = vars(parser.parse_args())
    res = {k:v for k,v in res.items() if v is not None}

    if res[ACTION] != INTERACTIVE_ACTION:
        parse_arguments(res)
        return

    interactive.execute_interactive()
