/*
 * sdi_vm_sys_init.h
 * Dell Networking SDI (System Device Interface) VM
 * (Virtual Machine) initialization/deinitialization functions
 *
 * (c) Copyright 2014 Dell Inc. All Rights Reserved.
 */

#ifndef _SDI_VM_SYS_INIT_H
#define _SDI_VM_SYS_INIT_H


/*
 * Initialization function for SDI.
 * return  STD_ERR_OK if okay, or error value if initialization fails
 */
t_std_error sdi_sys_init (void);

/*
 * Deinitialization function for SDI.
 * return  STD_ERR_OK if okay, or error value if Deinitialization fails
 */
t_std_error sdi_sys_close (void);

#endif
