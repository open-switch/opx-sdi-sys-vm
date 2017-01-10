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
""" This module provides an API for modifying data in the SDI SQL database """

import os
import sys
import sqlite3
import ctypes

import sdi_vm_common_consts as consts

def sql_open():
    """Open the sdi sql database."""

    path = os.path.join(consts.SDI_DB_BASE_DEFAULT,
                        consts.SDI_DB_NAME_DEFAULT)

    # Open the db. If it doesn's exist, this call will create.
    global g_sdi_db_handle
    g_sdi_db_handle = sqlite3.connect(path)


def sql_close():
    """Close the sdi sql database."""

    # Close the db
    g_sdi_db_handle.close()


def get_global_sem():
    """Get the sdi_ops semaphore to sequence the access of
        the sql database."""

    return g_sdi_db_ops_sem_own


def sem_get():
    """Get the sdi_ops semaphore to sequence the access of
        the sql database."""


    # Local ownership
    global g_sdi_db_ops_sem_own
    g_sdi_db_ops_sem_own = 0

    # Open the sdi_ops library
    global g_sdi_db_ops_lib
    g_sdi_db_ops_lib = ctypes.CDLL(consts.SDI_DB_SDI_LIB_DEFAULT \
                               + consts.SDI_DB_SDI_LIB_NAME)

    # Get the sdi_ops semaphore
    if g_sdi_db_ops_lib.sdi_db_sem_get() < 0:
        print '\nError could not get sdi_ops semaphore'

        # Close sdi sql database and exit script
        sql_close()
        sys.exit()


def sem_take():
    """Take the sdi_ops semaphore."""

    global g_sdi_db_ops_sem_own

    # Get semaphore for sql vm db access
    g_sdi_db_ops_lib.sdi_db_sem_take()
    g_sdi_db_ops_sem_own = 1


def sem_give():
    """Give the sdi_ops semaphore."""

    global g_sdi_db_ops_sem_own

    # Release semaphore for sql vm db access
    g_sdi_db_ops_lib.sdi_db_sem_give()
    g_sdi_db_ops_sem_own = 0


def sql_get_attr(table_name, attribute_name, condition):
    """Query the sdi sql database for the attributes satisfying
        the condition."""

    ret = 0

    # Build parameter list for sql query
    sql = 'SELECT %s from %s' % (attribute_name, table_name)
    if condition:
        sql += ' where %s' % (condition)

    sem_take()

    try:
        # Execute sql command
        ret = g_sdi_db_handle.execute(sql)

    except sqlite3.Error as err:
        # Print sql query and returned err message
        print '    Error: sql ', sql
        print '        ', err.message
        ret = 0

    sem_give()
    return ret


def sql_set_attr(table_name, attribute_name, condition):
    """Set the sdi sql database attribute satisfying the
        condition."""

    ret = 0

    # Build parameter list for sql query
    sql = 'UPDATE %s set %s' % (table_name, attribute_name)
    if condition:
        sql += ' where %s' % (condition)

    sem_take()

    try:
        # Execute sql command
        g_sdi_db_handle.execute(sql)

        # Commit change
        g_sdi_db_handle.commit()
        ret = 1

    except sqlite3.Error as err:
        # Rollback on error
        g_sdi_db_handle.rollback()

        # Print sql query and returned err message
        print '    Error: sql ', sql
        print '        ', err.message
        ret = 0

    sem_give()
    return ret

def sql_get_cursor():
    sem_take()
    curs = g_sdi_db_handle.cursor()
    sem_give()
    return curs

def sql_get_data_by_command(sqlCommand):
    curs = sql_get_cursor()
    sem_take()
    try:
        curs.execute(sqlCommand)
    except sqlite3.Error as err:
        print '    Error: sql ', sqlCommand
        print '        ', err.message
    data = curs.fetchall()
    sem_give()
    return data

def sql_get_column_info(table_name, info = 'name'):
    data = sql_get_data_by_command('PRAGMA TABLE_INFO({})'.format(table_name))
    return      [tup[1] for tup in data] if info=='name'   \
           else [tup[2] for tup in data] if info=='type'   \
           else data

def sql_get_column_names(table_name):
    return sql_get_column_info(table_name, 'name')

def sql_get_column_types(table_name):
    return sql_get_column_info(table_name, 'type')

def sql_get_all_rows(table_name):
    return sql_get_data_by_command('SELECT * FROM ' + table_name)


