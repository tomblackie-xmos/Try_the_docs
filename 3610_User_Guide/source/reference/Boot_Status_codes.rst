Boot status codes (RUN_STATUS)
==========================================

The following table describes the Boot status codes returned by the
startup processes accessible though the GET_RUN_STATUS control utility
command.

+----+-----------------------+-----------------------------------------+
| Co | Label                 | Note                                    |
| de |                       |                                         |
+====+=======================+=========================================+
| 0  | INIT                  | Reserved initial value. Decline         |
|    |                       | attempts to initiate DFU.               |
+----+-----------------------+-----------------------------------------+
| 1  | DAT                   | Not used.                               |
|    | A_PARTITION_NOT_FOUND |                                         |
+----+-----------------------+-----------------------------------------+
| 2  | FACTORY_DATA_SUCCESS  | Normal operation.                       |
+----+-----------------------+-----------------------------------------+
| 3  | UPGRADE_DATA_SUCCESS  | Normal operation.                       |
+----+-----------------------+-----------------------------------------+
| 4  | FAC                   | Image scanning in progress. Decline     |
|    | TORY_DATA_IN_PROGRESS | attempts to initiate DFU.               |
+----+-----------------------+-----------------------------------------+
| 5  | UPG                   | Image scanning in progress. Decline     |
|    | RADE_DATA_IN_PROGRESS | attempts to initiate DFU.               |
+----+-----------------------+-----------------------------------------+
| 6  | DFU_IN_PROGRESS       | Enough DFU commands received to         |
|    |                       | establish a connection to on-board      |
|    |                       | flash memory. Not cleared until reboot. |
+----+-----------------------+-----------------------------------------+
| 7  | HW_BUILD_READ_SUCCESS | Reserved intermediate value. Normally   |
|    |                       | never returned.                         |
+----+-----------------------+-----------------------------------------+
| 8  | HW_BUILD              | Problem reading data partition header.  |
|    | _PARTITION_SIZE_ERROR | Check factory programming.              |
+----+-----------------------+-----------------------------------------+
| 9  | HW_BUILD              | Problem reading data partition header.  |
|    | _PARTITION_BASE_ERROR | Check factory programming.              |
+----+-----------------------+-----------------------------------------+
| 10 | HW_BUILD_READ_ERROR   | Problem reading data partition header.  |
|    |                       | Check factory programming.              |
+----+-----------------------+-----------------------------------------+
| 11 | HW_BUILD_CRC_ERROR    | Problem reading data partition header.  |
|    |                       | Check factory programming. May indicate |
|    |                       | that no data partition is present or a  |
|    |                       | flash wear issue.                       |
+----+-----------------------+-----------------------------------------+
| 12 | HW_BUILD_TAG_ERROR    | Problem reading data partition header.  |
|    |                       | Check factory programming.              |
+----+-----------------------+-----------------------------------------+
| 13 | FACTORY_VERSION_ERROR | No valid upgrade image found. A factory |
|    |                       | image did not match running version.    |
|    |                       | This can indicate fail-safe mode.       |
+----+-----------------------+-----------------------------------------+
| 14 | UPGRADE_VERSION_ERROR | Valid upgrade boot and data images      |
|    |                       | found but data image version does not   |
|    |                       | match running version. Check correct    |
|    |                       | version of deployed field upgrade.      |
+----+-----------------------+-----------------------------------------+
| 15 | FA                    | Problem reading configuration items     |
|    | CTORY_ITEM_READ_ERROR | from data image. Unexpected error.      |
+----+-----------------------+-----------------------------------------+
| 16 | UP                    | Problem reading configuration items     |
|    | GRADE_ITEM_READ_ERROR | from data image. Unexpected error.      |
+----+-----------------------+-----------------------------------------+
| 17 | FACT                  | Last item encountered is not of         |
|    | ORY_ITEM_INVALID_TYPE | terminator type. Should never happen    |
|    |                       | with script generated data images.      |
|    |                       | Check generation procedure.             |
+----+-----------------------+-----------------------------------------+
| 18 | UPGR                  | Last item encountered is not of         |
|    | ADE_ITEM_INVALID_TYPE | terminator type. Should never happen    |
|    |                       | with script generated data images.      |
|    |                       | Check generation procedure.             |
+----+-----------------------+-----------------------------------------+
| 19 | DFU                   | Failed to establish on-board flash      |
|    | _FLASH_CONNECT_FAILED | connection. Check factory programming.  |
|    |                       | Check flash specification (see section  |
|    |                       | below).                                 |
+----+-----------------------+-----------------------------------------+
| 20 | DFU                   | Flash specification unsuitable for DFU. |
|    | _FLASH_SPEC_UNSUITABLE| Check flash specification (see section  |
|    |                       | below).                                 |
+----+-----------------------+-----------------------------------------+
