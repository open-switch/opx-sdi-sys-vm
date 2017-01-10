/*
 * sdi_vm_sys.c
 * SDI initialization routines and helper functions for virtualized implmentation
 *
 * (c) Copyright 2014-2015 Dell Inc. All Rights Reserved.
 */

#include "sdi_sys_vm.h"
#include <stdarg.h>
#include <stdio.h>
#include <event_log.h>
#include "std_assert.h"

static db_sql_handle_t db_handle;

static inline void sdi_set_db_handle(db_sql_handle_t temp_db_handle)
{
  db_handle = temp_db_handle;
}

db_sql_handle_t sdi_get_db_handle(void)
{
  return db_handle;
}

t_std_error sdi_sys_init(void)
{
    t_std_error rc = STD_ERR_OK;
    db_sql_handle_t db = NULL;

    /* Get global variable for DB path */
    rc = sdi_db_open(&db, 1);

    if (rc != STD_ERR_OK) {
        EV_LOGGING(SYSTEM, ERR, __func__, "Can't open database");
    } else {
        EV_LOGGING(SYSTEM, INFO, __func__, "Database opened database successfully");
        sdi_set_db_handle(db);
    }

    return rc;
}


t_std_error sdi_sys_close(void)
{
    sdi_db_close(sdi_get_db_handle());
    return STD_ERR_OK;
}

