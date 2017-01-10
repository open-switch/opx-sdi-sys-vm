/**
 * \file   sdi_sys_vm.h
 * \brief  Dell Networking SDI (System Device Interface) VM
 *         (Virtual Machine) private helper function prototypes and includes
 * \date   09-2014
 * (c) Copyright 2014 Dell Inc. All Rights Reserved.
 */

#ifndef _SDI_SYS_VM_H_
#define _SDI_SYS_VM_H_
#include <stdlib.h>
#include "std_error_codes.h"
#include <std_error_ids.h>
#include "std_utils.h"
#include "sdi_vm_sys_init.h"
#include "sdi_db.h"
#include "std_assert.h"

#define VM_SQl_DEFAULT_BUFFER_LENGTH 256

/** @TODO Replace instances of these errors with new SDI error defines... */
/** Hardware Error **/
#define STD_ERR_HARDWARE (-1)

/**
 * \brief   Get database handle stored in global storage
 * \return  handle to database used by sdi-sys-vm to store object state
 */
db_sql_handle_t  sdi_get_db_handle(void);

#endif
