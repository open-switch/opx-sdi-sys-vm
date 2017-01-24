/**
 * sdi_db_config.h
 * Configuration for location of DB files
 *
 * Copyright (c) 2015, Dell Products LP. All Rights Reserved.
 */

#ifndef __SDI_DB_CONFIG_H
#define __SDI_DB_CONFIG_H

/** Default parameters for the SDI database **/

/** Name of the environment variable which sets the default base path */
#define SDI_DB_BASE_ENV     "DN_SDI_DB_BASE_DIR"

/** Default base path for SDI DB related files **/
#define SDI_DB_BASE_DEFAULT "/etc/opx/sdi"

/** Name of the database **/
#define SDI_DB_NAME_DEFAULT "vm.db"

/** Name of the script to create the tables **/
#define SDI_DB_CREATE_SQL   "sdi-db-create.sql"

/** Name of the script to initialize the data **/
#define SDI_DB_INIT_SQL     "sdi-db-data.sql"

/** Name of the environment variable with the database name **/
#define SDI_DB_NAME_ENV     "DN_SDI_DB_NAME"

/** Name of the environment variable with the initialization script name **/
#define SDI_DB_INIT_ENV     "DN_SDI_DB_INIT"

/** Name of the environment variable with the semaphore key **/
#define SDI_DB_SEM_ENV      "DN_SDI_DB_SEM_KEY"

/** Default semaphore key if the above environment variable is unspecified **/
#define SDI_DB_SEM_DEFAULT  0x53444900

/** Name of the environment variable which if set will prevent writing to the
 * regular database field
 */
#define SDI_DB_NO_SYNC_ENV  "DN_SDI_DB_NO_SYNC"

#endif /* __SDI_DB_CONFIG_H */
