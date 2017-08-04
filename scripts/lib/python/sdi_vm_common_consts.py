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

# Constants
SDI_DB_BASE_DEFAULT     = '/etc/opx/sdi/'
SDI_DB_NAME_DEFAULT     = 'vm.db'
SDI_DB_QUERY_ALL        = ''                 # No condition filtering
SDI_DB_SDI_LIB_DEFAULT  = '/usr/lib/x86_64-linux-gnu/'
SDI_DB_SDI_LIB_NAME     = 'libsdi_db.so'     # sdi_db_ops semaphore library

# SDI DB table identifiers
TABLE_THERMAL_SENSOR    = 'Thermal'          # Thermal sensor table
TABLE_FAN               = 'Fan'              # Fan table
TABLE_INFO              = 'Entity_Info'      # Entity information
TABLE_MEDIA             = 'Media'            # Media devices
TABLE_RESOURCES         = 'Entity_Resource'  # Global resource list
TABLE_MEDIA_PARAMS      = 'Media_Parameters' # Media parameters table
TABLE_MEDIA_VENDOR_INFO = 'Media_Vendor_Info'# Media vendor info table

TABLE_PHYSICAL_LED             = 'Physical_LED'              # Physical LED info table
TABLE_LED                      = 'LED'                       # LED info table
TABLE_DIGIT_DISPLAY_LED        = 'Digit_Display_LED'         # Digital display LED info table
TABLE_PLD                      = 'PLD'                       # PLD info table
TABLE_MEDIA_CHANNEL            = 'Media_Channel'             # Media channel info table
TABLE_MEDIA_MONITOR_THRESHOLDS = 'Media_Monitor_Thresholds'  # Media monitor thresholds
TABLE_NVRAM                    = 'NVRAM'                     # NRAM info table    

# SDI TABLE_INFO DB fields
INFO_ENTITY_NAME        = 'Entity_Name'      # Entity Name
INFO_PRESENCE           = 'Presence'         # Entity Info Presence flag
INFO_NUM_FANS           = 'Num_Fans'         # Entity Info num fans
INFO_FAULT              = 'Fault_Status'     # Entity Info Fault flag

# SDI TABLE_INFO DB, field TBL_ENTITY_TYPE
TBL_INFO_TYPE_FAN_MEDIA = 1                  # Resource Type of Fan Media
TBL_INFO_TYPE_PSU_MEDIA = 2                  # Resource Type of PSU Media

# SDI TABLE_RESOURCES DB fields
TBL_ENTITY_HDL          = 'Entity_Handle'    # Entity Handle
TBL_RESOURCE_HDL        = 'Resource_Handle'  # Resource Handle
TBL_ENTITY_TYPE         = 'Entity_Type'      # Entity Type
TBL_ENTITY_INSTANCE     = 'Instance'         # Entity Instance
TBL_RESOURCE_TYPE       = 'Resource_Type'    # Resource Type
TBL_RESOURCE_INSTANCE   = 'Instance'         # Resource Instance
TBL_RESOURCE_ALIAS      = 'Alias'            # Resource Alias

# SDI TABLE_RESOURCES DB, field TBL_RESOURCE_TYPE
TBL_RESOURCE_TYPE_THERM_MEDIA = 0            # Resource Type of Thermal Sensor
TBL_RESOURCE_TYPE_OPTICS_MEDIA = 6           # Resource Type of Optics Media

# SDI TABLE_MEDIA DB fields
MEDIA_DELL_QUALIFIED    = 'DELL_Qualified'   # Dell qualified
MEDIA_PRESENCE          = 'Present'          # Media presence
MEDIA_VENDOR_OUI        = 'Vendor_OUI'       # Media OUI
MEDIA_OPTIC_SPEED       = 'Optic_Speed'      # Optics speed
MEDIA_DELL_PROD_INFO    = 'DELL_Product_Info'# Dell product info
MEDIA_SUPPORTED_FEATURES = 'Media_Supported_Features' # Media supported
MEDIA_TRANSCEIVER_CODE  = 'XCVR_Code'        # Media transceiver code
MEDIA_LP_MODE           = 'Low_Power_Mode'   # Media low power mode
MEDIA_RESET             = 'Reset'            # Media reset

# SDI TABLE MEDIA DB, field MEDIA_DELL_PROD_INFO
PLAT_SDI_SFP_PLUS_MODE_1   = 3               # SDI Media Identifier, SFP+
PLAT_SDI_SFP_PLUS_MODE_2   = 11              # SDI Media Identifier, SFP+
PLAT_SDI_QSFP_MODE         = 12              # SDI Media Identifier, QSFP
PLAT_SDI_QSFP_PLUS_MODE    = 13              # SDI Media Identifier, QSFP+

# SDI TABLE_MEDIA_PARAMS DB fields (Parameter, Value) pairs
MEDIA_PARAM_TYPE        = 'Parameter'        # Media parameter type
MEDIA_PARAM_VALUE       = 'Value'            # Media parameter value

# SDI TABLE_MEDIA_PARAMS DB, field MEDIA_PARAM_TYPE pair
SDI_MEDIA_WAVELENGTH    = 0          # SDI MEDIA Nominal laser wavelength
SDI_MEDIA_IDENTIFIER    = 8          # SDI MEDIA Identifier Type of serial Mod
SDI_MEDIA_LENGTH_CABLE_ASSEMBLY = 14 # SDI MEDIA length support for copper or
                                     #  direct attach cable
SDI_MEDIA_DEVICE_TECH   = 19         # SDI MEDIA Transmitter/Device Technology

# SDI TABLE_MEDIA_VENDOR_INFO DB, fields (Vendor_Info, Value) pairs
MEDIA_VENDOR_INFO_TYPE  = 'Vendor_Info'      # Media vendor info type
MEDIA_VENDOR_INFO_VALUE = 'Value'            # Media vendor info value

# SDI TABLE_MEDIA_VENDOR DB, field MEDIA_VENDOR_INFO_TYPE pair
SDI_MEDIA_VENDOR_PN     = 4                  # Media vendor part number

# SDI TABLE_FAN DB, fields
FAN_FAULT               = 'Alert_On'         # Fan Fault

# SDI TABLE_THERMAL_SENSOR DB, fields
THERMAL_TEMPERATURE        = 'Temp_C'        # Thermal temperature value
THERMAL_FAULT              = 'Alert_On'      # Thermal Sensor Fault
THERMAL_THRESHOLD_LOW      = 'Threshold_Low' # Low Threshold
THERMAL_THRESHOLD_HIGH     = 'Threshold_High'# High Threshold
THERMAL_THRESHOLD_CRITICAL = 'Threshold_Critical' # Critical Threshold

PLAT_MEDIA_FANTRAY_STR  = 'Fantray'          # Fantray string
PLAT_MEDIA_PSU_STR      = 'PSU'              # PSU string

PLAT_MEDIA_NOT_PRESENT = 0                   # Media not present value
PLAT_MEDIA_PRESENT     = 1                   # Media present value
PLAT_MEDIA_ERROR       = 0xFFFFFFFF          # Media error value

PLAT_MEDIA_NO_FAULT    = 0                   # Media no fault value
PLAT_MEDIA_FAULT       = 1                   # Media fault value

PLAT_THERMAL_MIN_TEMP  = 0                   # Thermal min temp input
PLAT_THERMAL_MAX_TEMP  = 255                 # Thermal max temp input

# Optics SDI Identifier to names
SDI_IDENT = {
  PLAT_SDI_SFP_PLUS_MODE_1: {'name': 'SFP-PLUS'},
  PLAT_SDI_SFP_PLUS_MODE_2: {'name': 'SFP-PLUS'},
  PLAT_SDI_QSFP_MODE:       {'name': 'QSFP'},
  PLAT_SDI_QSFP_PLUS_MODE:  {'name': 'QSFP-PLUS'}
}

# Optics table
#   Default values are from sql init file
OPTICS_TABLE = {
   # SFP_PLUS - type based on sdi and pInfo
   1: { 'name': 'SFPPLUS_10GBASE_USR', 'sdi': 3,\
        'pInfo': "x'0F1000931F4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   2: { 'name': 'SFPPLUS_10GBASE_SR (wvL 1)', 'sdi': 3,\
        'pInfo': "x'0F100013FF4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   3: { 'name': 'SFPPLUS_10GBASE_SR (wvL 11)', 'sdi': 3,\
        'pInfo': "x'0F1000B3FF4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   4: { 'name': 'SFPPLUS_10GBASE_LR', 'sdi': 3,\
        'pInfo': "x'0F100023FF4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   5: { 'name': 'SFPPLUS_10GBASE_ER', 'sdi': 3,\
        'pInfo': "x'0F1000334F4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   6: { 'name': 'SFPPLUS_10GBASE_ZR', 'sdi': 3,\
        'pInfo': "x'0F1000335F4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   7: { 'name': 'SFPPLUS_10GBASE_CX4', 'sdi': 3,\
        'pInfo': "x'0F100043FF4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   8: { 'name': 'SFPPLUS_10GBASE_LRM', 'sdi': 3,\
        'pInfo': "x'0F100063FF4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   9: { 'name': 'SFPPLUS_10GBASE_T', 'sdi': 3,\
        'pInfo': "x'0F100053FF4000'", 'tCode': "x'2000000700000000'",\
        'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   10: { 'name': 'SFPPLUS_10GBASE_CU1M', 'sdi': 11,\
         'pInfo': "x'0F1000A36F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   11: { 'name': 'SFPPLUS_10GBASE_CU2M', 'sdi': 11,\
         'pInfo': "x'0F1000A3CF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   12: { 'name': 'SFPPLUS_10GBASE_CU3M', 'sdi': 11,\
         'pInfo': "x'0F1000A37F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   13: { 'name': 'SFPPLUS_10GBASE_CU5M', 'sdi': 11,\
         'pInfo': "x'0F1000A38F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   14: { 'name': 'SFPPLUS_10GBASE_CU7M', 'sdi': 11,\
         'pInfo': "x'0F1000A3DF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   15: { 'name': 'SFPPLUS_10GBASE_CU10M', 'sdi': 11,\
         'pInfo': "x'0F1000A39F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   16: { 'name': 'SFPPLUS_10GBASE_CUHALFM', 'sdi': 11,\
         'pInfo': "x'0F1000A3BF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   17: { 'name': 'SFPPLUS_10GBASE_ACU10M', 'sdi': 11,\
         'pInfo': "x'0F1000C39F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   18: { 'name': 'SFPPLUS_10GBASE_ACU15M', 'sdi': 11,\
         'pInfo': "x'0F1000C3AF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   19: { 'name': 'SFPPLUS_10GBASE_DWDM', 'sdi': 11,\
         'pInfo': "x'0F100073FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},

   # QSFP/QSFP_PLUS - type based on sdi and pInfo
   20: { 'name': 'QSFP_40GBASE_SR4', 'sdi': 12,\
         'pInfo': "x'0F100013FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   21: { 'name': 'QSFP_40GBASE_SR4 (wvL 10,dst 5)', 'sdi': 12,\
         'pInfo': "x'0F1000A35F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   22: { 'name': 'QSFP_40GBASE_SR4 (wvL 10,dst 8)', 'sdi': 12,\
         'pInfo': "x'0F1000A38F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   23: { 'name': 'QSFP_40GBASE_SR4_EXT', 'sdi': 12,\
         'pInfo': "x'0F1000C3FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   24: { 'name': 'QSFP_40GBASE_LR4 (wvL 2,dst 1)', 'sdi': 12,\
         'pInfo': "x'0F1000231F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   25: { 'name': 'QSFP_40GBASE_LR4 (wvL 2,dst 2)', 'sdi': 12,\
         'pInfo': "x'0F1000232F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   26: { 'name': 'QSFP_40GBASE_LR4 (wvL 3,dst 3)', 'sdi': 12,\
         'pInfo': "x'0F1000333F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   27: { 'name': 'QSFP_40GBASE_LM4', 'sdi': 12,\
         'pInfo': "x'0F100043FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   28: { 'name': 'QSFP_40GBASE_PSM4_LR', 'sdi': 12,\
         'pInfo': "x'0F100053FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   29: { 'name': 'QSFP_40GBASE_PSM4_1490NM', 'sdi': 12,\
         'pInfo': "x'0F1000D3FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   30: { 'name': 'QSFP_40GBASE_PSM4_1490NM_1M', 'sdi': 12,\
         'pInfo': "x'0F1000D32F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   31: { 'name': 'QSFP_40GBASE_PSM4_1490NM_3M', 'sdi': 12,\
         'pInfo': "x'0F1000D33F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   32: { 'name': 'QSFP_40GBASE_PSM4_1490NM_5M', 'sdi': 12,\
         'pInfo': "x'0F1000D34F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   33: { 'name': 'QSFP_40GBASE_SM4', 'sdi': 12,\
         'pInfo': "x'0F100063FF4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   34: { 'name': 'QSFP_40GBASE_CR4', 'sdi': 12,\
         'pInfo': "x'0F1000A34F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   35: { 'name': '4x10_10GBASE_CR4_HAL_M', 'sdi': 12,\
         'pInfo': "x'0F1000936F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   36: { 'name': 'QSFP_40GBASE_CR4_1M', 'sdi': 12,\
         'pInfo': "x'0F1000932F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   37: { 'name': 'QSFP_40GBASE_CR4_2M', 'sdi': 12,\
         'pInfo': "x'0F1000939F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   38: { 'name': 'QSFP_40GBASE_CR4_3M', 'sdi': 12,\
         'pInfo': "x'0F1000933F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   39: { 'name': 'QSFP_40GBASE_CR4_5M',  'sdi': 12,\
         'pInfo': "x'0F1000934F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   40: { 'name': 'QSFP_40GBASE_CR4_7M',  'sdi': 12,\
         'pInfo': "x'0F1000937F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   41: { 'name': 'QSFP_40GBASE_CR4_10M', 'sdi': 12,\
         'pInfo': "x'0F1000935F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   42: { 'name': 'QSFP_40GBASE_CR4_50M', 'sdi': 12,\
         'pInfo': "x'0F1000938F4000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   43: { 'name': '4x10_10GBASE_CR1_HAL_M', 'sdi': 12,\
         'pInfo': "x'0F100093624000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   44: { 'name': '4x10_10GBASE_CR1_1M', 'sdi': 12,\
         'pInfo': "x'0F100093224000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   45: { 'name': '4x10_10GBASE_CR1_3M', 'sdi': 12,\
         'pInfo': "x'0F100093324000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   46: { 'name': '4x10_10GBASE_CR1_5M', 'sdi': 12,\
         'pInfo': "x'0F100093424000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   47: { 'name': '4x10_10GBASE_CR1_7M', 'sdi': 12,\
         'pInfo': "x'0F100093724000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   48: { 'name': '4X_10GBASE_SR_AOCXXM', 'sdi': 12,\
         'pInfo': "x'0F1000A3F14000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   49: { 'name': '4x1_1000BASE_T', 'sdi': 12,\
         'pInfo': "x'0F1000E3F24000'", 'tCode': "x'2000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},

   # Dell Non-Qual - Type based on sdi, pInfo, tCode, and dTech
   50: { 'name': 'QSFP_40GBASE_LR4 (nQual)', 'sdi': 12,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0200000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   51: { 'name': 'QSFP_40GBASE_SR4 (nQual)', 'sdi': 12,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0400000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   52: { 'name': 'QSFP_40GBASE_CR4 (nQual)', 'sdi': 12,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0800000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   53: { 'name': 'QSFP_40GBASE_CR4 (nQual,psv)', 'sdi': 12,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0000000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 11<<4},
   54: { 'name': 'SFPPLUS_10GBASE_SR4 (nQual)', 'sdi': 3,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0100000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   55: { 'name': 'SFPPLUS_10GBASE_LR4 (nQual)', 'sdi': 3,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0200000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   56: { 'name': 'SFPPLUS_10GBASE_LRM (nQual)', 'sdi': 3,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0400000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   57: { 'name': 'SFPPLUS_10GBASE_ER (nQual)', 'sdi': 3,\
         'pInfo': "x'000000FFFF4000'", 'tCode': "x'0800000700000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},

   58: { 'name': 'SFPPLUS_10GBASE_CU1M (nQual,psv,cLn 1)', 'sdi': 3,\
         'pInfo': "x'00000000004000'", 'tCode': "x'0000000000100000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 1, 'dTech': 0},
   59: { 'name': 'SFPPLUS_10GBASE_CU2M (nQual,psv,cLn 2)', 'sdi': 3,\
         'pInfo': "x'00000000004000'", 'tCode': "x'0000000000100000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 2, 'dTech': 0},
   60: { 'name': 'SFPPLUS_10GBASE_CU3M (nQual,psv,cLn 3)', 'sdi': 3,\
         'pInfo': "x'00000000004000'", 'tCode': "x'0000000000100000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 3, 'dTech': 0},
   61: { 'name': 'SFPPLUS_10GBASE_CU5M (nQual,psv,cLn 5)', 'sdi': 3,\
         'pInfo': "x'00000000004000'", 'tCode': "x'0000000000100000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 5, 'dTech': 0},
   62: { 'name': 'SFPPLUS_10GBASE_CU7M (nQual,act,cLn 7)', 'sdi': 3,\
         'pInfo': "x'00000000004000'", 'tCode': "x'0000000000200000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 7, 'dTech': 0},
   63: { 'name': 'SFPPLUS_10GBASE_CU10M (nQual,act,cLn 10)', 'sdi': 3,\
         'pInfo': "x'00000000004000'", 'tCode': "x'0000000000200000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 10, 'dTech': 0},

   # UNKNOWN - Type based on sdi, pInfo, tCode
   64: { 'name': 'UNKNOWN (sdi 1)', 'sdi': 1,\
         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   65: { 'name': 'UNKNOWN SFPPLUS', 'sdi': 3,\
         'pInfo': "x'0F100000004000'", 'tCode': "x'0000000000000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
   66: { 'name': 'UNKNOWN QSFP', 'sdi': 12,\
         'pInfo': "x'0F100000004000'", 'tCode': "x'0000000000000000'",\
         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},

   # The below optic types are currently not supported

   # Type based on sdi, pInfo, tCode, and wlen
#   50: { 'name': 'SFP_SX', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'",  'tCode': "x'0000000100000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   51: { 'name': 'SFP_LX (sdi 2)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000200000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   52: { 'name': 'SFP_LX (sdi 16)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000001000000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   53: { 'name': 'SFP_ZX (LX, wvL 1550)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000200000000'",\
#         'vInfo': "'599690001'", 'wlen': 1550, 'cLen': 0, 'dTech': 0},
#   54: { 'name': 'SFP_CX', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000400000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   55: { 'name': 'SFP_T', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000800000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   56: { 'name': 'SFP_FX', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000002000000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   57: { 'name': 'SFP_BX10', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000004000000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   58: { 'name': 'SFP_PX', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000008000000000'",\
#         'vInfo': "'599690001'", 'wlen': 64, 'cLen': 0, 'dTech': 0},

   # Type based on sdi, pInfo, tCode, and vInfo
#   59: { 'name': 'SFP_ZX (FTRJ-1519-7D-CSC)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FTRJ-1519-7D-CSC'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   60: { 'name': 'SFP_ZX (FTLF1519P1BCL)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FTLF1519P1BCL'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   61: { 'name': 'SFP_ZX (FTLF1519P1WCL)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FTLF1519P1WCL'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   62: { 'name': 'SFP_CWDM (FWDM-1619-7D-47)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-47'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   63: { 'name': 'SFP_CWDM (FWDM-1619-7D-49)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-49'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   64: { 'name': 'SFP_CWDM (FWDM-1619-7D-51)', 'sdi': 3,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-51'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   65: { 'name': 'SFP_CWDM (FWDM-1619-7D-53)', 'sdi': 11,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-53'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   66: { 'name': 'SFP_CWDM (FWDM-1619-7D-55)', 'sdi': 11,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-55'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   67: { 'name': 'SFP_CWDM (FWDM-1619-7D-57)', 'sdi': 11,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-57'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   68: { 'name': 'SFP_CWDM (FWDM-1619-7D-59)', 'sdi': 11,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-59'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
#   69: { 'name': 'SFP_CWDM (FWDM-1619-7D-61)', 'sdi': 11,\
#         'pInfo': "x'0F1000FFFF4000'", 'tCode': "x'0000000000000000'",\
#         'vInfo': "'FWDM-1619-7D-61'", 'wlen': 64, 'cLen': 0, 'dTech': 0},
}
