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

""" This module provides common utility functions to the platform-event script """

import sys
import time
import sdi_vm_db_ops as db
import sdi_vm_common_consts as consts



def init_script():
    """Provide 1-step init in the script."""

    # Open sdi sql database
    db.sql_open()
    db.sem_get()


def exit_script():
    """Provide 1-step exit from the script."""

    # Release if still have ownership
    if db.get_global_sem():
        db.sem_give()

    # Close sdi sql database
    db.sql_close()

    # Exit script
    sys.exit()


def get_media_param_attr(res_hdl, parameter):
    """Query the sdi Media Parameter database table for the value
      satisfying the condition."""

      # Build db query parameters
    condition = '%s = %s and %s = %s' % (
        consts.TBL_RESOURCE_HDL, str(res_hdl),
        consts.MEDIA_PARAM_TYPE, str(parameter))

    query = db.sql_get_attr(consts.TABLE_MEDIA_PARAMS,
                            consts.MEDIA_PARAM_VALUE,
                            condition)

    if not query:
        print '    Error reading res_hdl %d media param %d' % (res_hdl,
                                                               parameter)
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def set_media_param_attr(res_hdl, parameter, value):
    """Set the sdi Media Param database table attribute satisfying the
       condition."""

    # Build db query parameters
    attr = '%s = %s' % (consts.MEDIA_PARAM_VALUE, str(value))
    condition = '%s = %s and %s = %s' % (consts.TBL_RESOURCE_HDL,
                                         str(res_hdl),
                                         consts.MEDIA_PARAM_TYPE,
                                         str(parameter))

    db.sql_set_attr(consts.TABLE_MEDIA_PARAMS, attr, condition)


def get_media_vendor_info_attr(res_hdl, parameter):
    """Query the sdi Media Vendor Info database table for the value
       satisfying the condition."""

    # Build db query parameters
    condition = '%s = %s and %s = %s' % (consts.TBL_RESOURCE_HDL,
                                         str(res_hdl),
                                         consts.MEDIA_VENDOR_INFO_TYPE,
                                         str(parameter))

    query = db.sql_get_attr(consts.TABLE_MEDIA_VENDOR_INFO,
                            consts.MEDIA_VENDOR_INFO_VALUE,
                            condition)

    if not query:
        print '    Error in reading res_hdl %d media vendor info %d' %\
              (res_hdl, parameter)
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def set_media_vendor_info_attr(res_hdl, parameter, value):
    """Set the sdi Media Vendor Info database table attribute satisfying
       the condition."""

    # Build db query parameters
    attr = '%s = %s' % (consts.MEDIA_VENDOR_INFO_VALUE, str(value))
    condition = '%s = %s and %s = %s' % (consts.TBL_RESOURCE_HDL,
                                         str(res_hdl),
                                         consts.MEDIA_VENDOR_INFO_TYPE,
                                         str(parameter))

    db.sql_set_attr(consts.TABLE_MEDIA_VENDOR_INFO, attr, condition)


def get_media_attr(res_hdl, parameter):
    """Get the sdi Media database table attribute satisfying the condition."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    query = db.sql_get_attr(consts.TABLE_MEDIA, parameter, condition)

    if not query:
        print '    Error in reading res_hdl %d media %s' % (res_hdl,
                                                            parameter)
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def dsp_media_attr_blob(res_hdl, parameter):
    """Debug example of how to display the sdi Media database table
       BLOB type attribute satisfying the condition."""

    row = get_media_attr(res_hdl, parameter)

    # Since the sql BLOB type attribute seems to be like a string but
    # with a length of 1, document how can print.

    print str(row).encode('hex')


def set_media_attr(res_hdl, parameter, value):
    """Set the sdi Media database table attribute to the value
       satisfying the condition."""

    # Build db query parameters
    attr = '%s = %s' % (parameter, value)
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_MEDIA, attr, condition)


def get_thermal_thresh(res_hdl):
    """Get the thermal threholds."""

    # Build db query parameters
    attr = '%s, %s, %s' % (consts.THERMAL_THRESHOLD_LOW,
                           consts.THERMAL_THRESHOLD_HIGH,
                           consts.THERMAL_THRESHOLD_CRITICAL)

    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    # Get db attributes
    query = db.sql_get_attr(consts.TABLE_THERMAL_SENSOR, attr, condition)

    if not query:
        print '    Error in reading therm res_hdl %s thresholds' %\
              (str(res_hdl))
        return consts.PLAT_MEDIA_ERROR

    # Get row
    return query.fetchone()


def get_entity_info_status(res_hdl):
    """Get the entity info faulty state."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    # Get db attributes
    query = db.sql_get_attr(consts.TABLE_INFO,
                            consts.INFO_FAULT,
                            condition)

    if not query:
        print '    Error in reading media res_hdl %s presence' %\
              (str(res_hdl))
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def get_entity_info_state(res_hdl):
    """Get the entity info presence state."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    # Get db attributes
    query = db.sql_get_attr(consts.TABLE_INFO,
                            consts.INFO_PRESENCE,
                            condition)

    if not query:
        print '    Error in reading media res_hdl %s presence' %\
              (str(res_hdl))
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def set_port_optics_state(res_hdl, state):
    """Set the port optics state."""

    # Build db query parameters
    attr = '%s = %s' % (consts.MEDIA_PRESENCE, str(state))
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_MEDIA, attr, condition)


def get_port_optics_state(res_hdl):
    """Get the port optics state."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    # Get db attributes
    query = db.sql_get_attr(consts.TABLE_MEDIA,
                            consts.MEDIA_PRESENCE,
                            condition)

    if not query:
        print '    Error in reading res_hdl %d optics state' % (res_hdl)
        return consts.PLAT_MEDIA_ERROR

   # Get row
    row = query.fetchone()
    return row[0]


def print_optics_type():
    """Display the platform optics types in columns."""

    num = max(consts.OPTICS_TABLE)

    # First column row should have +1 objects with odd num
    maxrows = (num >> 1) + (num & 0x1)

    # Loop through first column, +1 since start with 1
    for idx in xrange(1, maxrows +1):
        col = consts.OPTICS_TABLE[idx]
        idx2 = idx + maxrows

        # If odd num, first column will be +1 objects
        if idx2 <= num:
            col2 = consts.OPTICS_TABLE[idx2]
            print '     %-2d  %-33s    %-2d  %-33s' % (idx,
                                                       col['name'],
                                                       idx2,
                                                       col2['name'])
        else:
            print '     %-2d  %-33s' % (idx, col['name'])
    print '\n'


def set_thermal_status(res_hdl, status):
    """Set the thermal sensor fault status."""

    # Build db query parameters
    attr = '%s = %s' % (consts.THERMAL_FAULT, str(status))
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_THERMAL_SENSOR, attr, condition)


def get_thermal_status(res_hdl):
    """Get the thermal sensor fault status."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

   # Get db attributes
    query = db.sql_get_attr(consts.TABLE_THERMAL_SENSOR,
                            consts.THERMAL_FAULT,
                            condition)

    if not query:
        print '    Error in reading therm res_hdl %s status' % \
                (str(res_hdl))
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def get_thermal_temp(res_hdl):
    """Get the thermal temperature."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    # Get db attributes
    query = db.sql_get_attr(consts.TABLE_THERMAL_SENSOR,
                            consts.THERMAL_TEMPERATURE,
                            condition)

    if not query:
        print '    Error in reading therm res_hdl %s temp' % (str(res_hdl))
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def list_thermal_sensors():
    """List the thermal sensors, temperature, and thresholds."""

    print '\n'
    for idx in g_thermal_tbl:
        thermal = g_thermal_tbl[idx]
        temp = get_thermal_temp(thermal['res_hdl'])
        thresh = get_thermal_thresh(thermal['res_hdl'])

        if thresh[0] != consts.PLAT_MEDIA_ERROR      \
           and thresh[1] != consts.PLAT_MEDIA_ERROR  \
           and thresh[2] != consts.PLAT_MEDIA_ERROR  \
           and temp != consts.PLAT_MEDIA_ERROR:

            print '     %d   %-25s  %3s    (low %s, hi %s, crt %s)' % \
                (idx, thermal['name'], temp, thresh[0], thresh[1], thresh[2])
        else:
            print '    Error in reading temp or thresholds %d %s' %   \
                (idx, thermal['name'])

    print '\n'


def set_thermal_temp(res_hdl, status):
    """Set the thermal sensor temperature."""

    # Build db query parameters
    attr = '%s = %s' % (consts.THERMAL_TEMPERATURE, str(status))
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_THERMAL_SENSOR, attr, condition)


def insert_port_optics(port, type, qMode):
    """Insert the platform optics event."""

    # Get port handle
    res_hdl = g_port_tbl[port]['res_hdl']

    # Get optics entry
    optic = consts.OPTICS_TABLE[type]

    state = get_port_optics_state(res_hdl)
    if state == consts.PLAT_MEDIA_PRESENT:
        print '   Remove OpticsPort %d, 5 sec delay' % (port)

        # For ease of script use, remove optics port if present
        set_port_optics_state(res_hdl, consts.PLAT_MEDIA_NOT_PRESENT)

        time.sleep(5)

       # Change state and continue below

    elif state == consts.PLAT_MEDIA_ERROR \
            or state != consts.PLAT_MEDIA_NOT_PRESENT:
        print '   Error unknown OpticsPort %d state %s' % (port, state)
        return

    # Port optics should be not present

   # Check if QSFP should be overwritten as QSFP-PLUS
    sdi = optic['sdi']
    if sdi == consts.PLAT_SDI_QSFP_MODE \
       and qMode == consts.PLAT_SDI_QSFP_PLUS_MODE:
        sdi = qMode

    # Set the SDI Identifier to set category
    set_media_param_attr(res_hdl, consts.SDI_MEDIA_IDENTIFIER, sdi)

    # Set the Product Info
    set_media_attr(res_hdl,
                   consts.MEDIA_DELL_PROD_INFO,
                   optic['pInfo'])

   #dsp_media_attr_blob(res_hdl, consts.MEDIA_DELL_PROD_INFO)

    # Set the transceiver code
    set_media_attr(res_hdl,
                   consts.MEDIA_TRANSCEIVER_CODE,
                   optic['tCode'])

    #dsp_media_attr_blob(res_hdl, consts.MEDIA_TRANSCEIVER_CODE)

    # Set the Vendor part number
    set_media_vendor_info_attr(res_hdl,
                               consts.SDI_MEDIA_VENDOR_PN,
                               optic['vInfo'])

    #row = get_media_vendor_info_attr(res_hdl,
    #                                 consts.SDI_MEDIA_VENDOR_PN)
    #print row

    # Set the wavelength
    set_media_param_attr(res_hdl,
                         consts.SDI_MEDIA_WAVELENGTH,
                         optic['wlen'])

    # Set the cable length
    set_media_param_attr(res_hdl,
                         consts.SDI_MEDIA_LENGTH_CABLE_ASSEMBLY,
                         optic['cLen'])

    #row = get_media_param_attr(res_hdl,
    #                           consts.SDI_MEDIA_LENGTH_CABLE_ASSEMBLY)
    #print row

    # Set the device tech
    set_media_param_attr(res_hdl,
                         consts.SDI_MEDIA_DEVICE_TECH,
                         optic['dTech'])

    # Set Optics presence
    set_port_optics_state(res_hdl, consts.PLAT_MEDIA_PRESENT)


def chk_port_optics_state(port, res_hdl, state):
    """Check the port optics state."""

    if state == consts.PLAT_MEDIA_NOT_PRESENT:
        state_str = 'not present'
    else:
        state_str = 'present'

    # Get current state
    cur_state = get_port_optics_state(res_hdl)

    if cur_state == consts.PLAT_MEDIA_NOT_PRESENT or \
       cur_state == consts.PLAT_MEDIA_PRESENT:

        if cur_state != state:
            set_port_optics_state(res_hdl, state)
        else:
            print '   OpticsPort %d is %s' % (port, state_str)


def get_entity_fan_status(res_hdl):
    """Get the platform media entity fan fault status."""

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    # Get db attributes
    query = db.sql_get_attr(consts.TABLE_FAN,
                            consts.FAN_FAULT,
                            condition)

    if not query:
        print '    Error in reading media res_hdl %s presence' %\
              (str(res_hdl))
        return consts.PLAT_MEDIA_ERROR

    # Get row
    row = query.fetchone()
    return row[0]


def set_entity_fan_status(res_hdl, status):
    """Set the platform media entity fan fault status."""

    # Build db query parameters
    attr = '%s = %s' % (consts.FAN_FAULT, str(status))
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_FAN, attr, condition)


def set_entity_info_status(res_hdl, status):
    """Set the entity info fault status."""

    # Build db query parameters
    attr = '%s = %s' % (consts.INFO_FAULT, str(status))
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_INFO, attr, condition)


def set_entity_info_state(res_hdl, state):
    """Set the entity info presence state."""

    # Build db query parameters
    attr = '%s = %s' % (consts.INFO_PRESENCE, str(state))
    condition = '%s = %s' % (consts.TBL_RESOURCE_HDL, str(res_hdl))

    db.sql_set_attr(consts.TABLE_INFO, attr, condition)


def bld_port_tbl():
    """Query the sdi database to build the port table containing the
       port's resource handles and the number of ports."""

    # Global to keep through session
    global g_qsfp_mode
    g_qsfp_mode = consts.PLAT_SDI_QSFP_PLUS_MODE

    global g_port_tbl
    g_port_tbl = {}

    # Build db query parameters
    condition = '%s = %s' % (consts.TBL_RESOURCE_TYPE,
                str(consts.TBL_RESOURCE_TYPE_OPTICS_MEDIA))

    # Get the database table fields
    query = db.sql_get_attr(consts.TABLE_RESOURCES,
                            consts.TBL_RESOURCE_HDL,
                            condition)

    if not query:
        print '   Error: in building portTable'
        return

    # Count the resources
    num = 0
    for row in query:
        num += 1
        g_port_tbl[num] = {'res_hdl': row[0]}

    print '    %2d ports' % (max(g_port_tbl.keys()))


def bld_fantray_tbl():
    """Query the sdi database to build the fan table containing the
       fanTray, its associated fan resource handles, and the number
       of each resource."""

    global g_fantray_tbl

    g_fantray_tbl = {}

    # Build db query parameters for fantray
    attr = '%s, %s, %s' % (consts.TBL_ENTITY_HDL,
                           consts.TBL_RESOURCE_HDL,
                           consts.INFO_NUM_FANS)

    condition = '%s = %s' % (consts.TBL_ENTITY_TYPE,
                             str(consts.TBL_INFO_TYPE_FAN_MEDIA))

    # Get the database table fields
    query = db.sql_get_attr(consts.TABLE_INFO, attr, condition)

    if not query:
        print '   Error: in building FantrayTable'
        return

    # Count resources and build fantray table
    num = 0
    for row in query:
        num += 1

        # Add fantray entity resource into table
        g_fantray_tbl[num] = {'eHndl': row[0],
                              'res_hdl': row[1],
                              'fNum': row[2]}

        # Build db query parameters for # of fans per fantray entity resource
        condition = '%s = %s and %s = %s' % (
                    consts.TBL_ENTITY_HDL, str(row[0]),
                    consts.TBL_RESOURCE_TYPE,
                    str(consts.TBL_INFO_TYPE_FAN_MEDIA))

        # Get the fan resources per fantray entity resource
        query2 = db.sql_get_attr(consts.TABLE_RESOURCES,
                                 consts.TBL_RESOURCE_HDL,
                                 condition)

        if not query2:
            print '   Error: in building FantrayTable Fans'
            return

        # Table entry for fantray
        fan2 = g_fantray_tbl[num]

        num2 = 0
        for row2 in query2:

            # If the number of fans < total fantray fans, append fan handle
            # to table entry
            if num2 < row[2]:
                num2 += 1
                fan2['f%sres_hdl' % (num2)] = row2[0]

        # Check whether num of fans match. Adjust max if not.
        if num2 != g_fantray_tbl[num]['fNum']:
            print '    Warning: Num of fantray fans is %d not %d as config' % \
                 (num2, g_fantray_tbl[num]['fNum'])

            g_fantray_tbl[num]['fNum'] = num2

    print '    %2d fantrays' % (max(g_fantray_tbl.keys()))
    for idx in g_fantray_tbl:
        print '      %2d - %d fans' % (idx, g_fantray_tbl[idx]['fNum'])


def bld_psu_tbl():
    """Query the sdi database to build the psu table containing the psu,
       its associated fan resouce handle, and the number of resource."""

    global g_psu_tbl

    g_psu_tbl = {}

    # Build db query parameters for psu
    attr = '%s, %s, %s' % (consts.TBL_ENTITY_HDL,
                           consts.TBL_RESOURCE_HDL,
                           consts.INFO_NUM_FANS)

    condition = '%s = %s' % (consts.TBL_ENTITY_TYPE,
                             str(consts.TBL_INFO_TYPE_PSU_MEDIA))

    # Get the database table fields
    query = db.sql_get_attr(consts.TABLE_INFO, attr, condition)

    if not query:
        print '   Error: in building psuTable'
        return

    # Count resources and build psu table
    num = 0
    for row in query:
        num += 1

        # Add psu entity resource int table
        g_psu_tbl[num] = {'eHndl': row[0],
                            'res_hdl': row[1],
                            'fNum': row[2]}

        # Build db query parameters for # of fans per psu entity resource
        condition = '%s = %s and %s = %s' % (
                    consts.TBL_ENTITY_HDL, str(row[0]),
                    consts.TBL_RESOURCE_TYPE,
                    str(consts.TBL_INFO_TYPE_FAN_MEDIA))

        # Get the fans per psu entity resource
        query2 = db.sql_get_attr(consts.TABLE_RESOURCES,
                                 consts.TBL_RESOURCE_HDL,
                                 condition)

        if not query2:
            print '   Error: in building psuTable Fan'
            return

        # Table entry for psu
        fan2 = g_psu_tbl[num]

        num2 = 0
        for row2 in query2:

            # If the number of fans < total psu fans, append fan handle
            if num2 < row[2]:
                num2 += 1
                fan2['f%sres_hdl' % (num2)] = row2[0]

        # Check whether num of fans match. Adjust max if not.
        if num2 != g_psu_tbl[num]['fNum']:
            print '    Warning: Num of psu fans is %d not %d as config' % \
                  (num2, g_psu_tbl[num]['fNum'])

            g_psu_tbl[num]['fNum'] = num2


    print '    %2d psus' % (max(g_psu_tbl.keys()))
    for idx in g_psu_tbl.keys():
        print '      %2d - %d fan' % (idx, g_psu_tbl[idx]['fNum'])


def bld_thermal_tbl():
    """Query the sdi database to build the thermal sensor table containing
       the sensor resource handle, and the number of sensors."""

    global g_thermal_tbl

    g_thermal_tbl = {}

    # Build db query parameters
    attr = '%s, %s' % (consts.TBL_RESOURCE_HDL,
                       consts.TBL_RESOURCE_ALIAS)
    condition = '%s = %s' % (
                consts.TBL_RESOURCE_TYPE,
                str(consts.TBL_RESOURCE_TYPE_THERM_MEDIA))

    # Get the database table fields
    query = db.sql_get_attr(consts.TABLE_RESOURCES, attr, condition)

    if not query:
        print '   Error: in building thermTable'
        return

    # Count the resources
    num = 0
    for row in query:
        num += 1
        g_thermal_tbl[num] = {'res_hdl': row[0], 'name': row[1]}

    print '    %2d thermal sensors' % (max(g_thermal_tbl.keys()))


def sigint_handler(signum, frame):
    """Trap received SIGINT signals to prevent abrupt script
       terminations from performing cleanup."""

    exit_script()

def show_table(table_name, columns_per_view = 6, spacing = 25):
    """Query the sdi sql database for the specified table"""
    # Get rows
    allRows = db.sql_get_all_rows(table_name)
    # Get the column names
    columnNames = db.sql_get_column_names(table_name)
    # Get the column types
    columnTypes = db.sql_get_column_types(table_name)
    staticColumns = 2
    maxDynamicColumns = columns_per_view - staticColumns

    #for grouping the tables into subgroups
    subGroupCount  = (len(columnNames) - staticColumns)/maxDynamicColumns
    
    for innerCounter in range (0, subGroupCount+1):
        alignString = ''    #for alignment of columns
        groupText = ''
        newStartIndex = (maxDynamicColumns * innerCounter)+ staticColumns
        endIndex = len(columnNames)

        if (subGroupCount != 0):
            groupText = ' : Group ' + str(innerCounter)
            endIndex = newStartIndex + maxDynamicColumns

        print '\n \n  Table Info For: ', table_name + groupText
        currentColumnNames = [columnNames[0]] + [columnNames[1]] \
        + columnNames[newStartIndex:endIndex]
        currentColumnTypes = [columnTypes[0]] + [columnTypes[1]] \
        + columnTypes[newStartIndex:endIndex]

        for count in range(0, len(currentColumnNames)):
            alignString = alignString + '{:<' + str(spacing)+ '} '
        print(alignString.format(*currentColumnNames)+'\r\n'     \
        + alignString.format(*currentColumnTypes))

        for row in allRows:
            currentRow = [row[0]]+[row[1]]+list(row[newStartIndex:endIndex])

            # for printing BLOB type
            for index in range(2, len(currentRow)):
                if columnTypes[newStartIndex + index -2].find("BLOB") != -1:
                    h = ""
                    for x in currentRow[index]:
                        h = h + (hex(ord(x)))[2:]
                        currentRow[index] =  "0x" + h

            print(alignString.format(*currentRow))


