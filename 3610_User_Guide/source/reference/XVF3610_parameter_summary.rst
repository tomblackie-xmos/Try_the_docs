Parameter summary
=============================

The following section summarises the XVF3610 parameters which are
programmable via the control interfaces or flash data partition. These
parameters allow the setup of the XVF3610 processor’s interfaces and
tuning of the internal signal processing.

To aid quick reference of the key parameters the summary is split into
two sections. The first details the most frequently used parameters
which are required for interface configuration and basic control, and
the second detail advanced parameters which will not generally need to
be modified. Further details on the specific usage of parameters are
discussed in the previous sections of the document and referenced below
for convenience.

NOTE: The parameters shown below can be formatted into Read and Write
commands, where appropriate by adding the prefix ‘GET\_’ and ‘SET\_’ for
Read and Write respectively.

Table 6‑1 Basic parameter summary ('-' used to indicate not applicable)

+-------------+----+------------------------+-----------+-----------+
| Parameter   | Re | Description            | 3610-UA   | 3610-INT  |
|             | ad |                        | default   | default   |
|             | /  |                        |           |           |
|             | W  |                        |           |           |
|             | ri |                        |           |           |
|             | te |                        |           |           |
+=============+====+========================+===========+===========+
| VERSION     | R  | Firmware version – See | vX.Y.Z    | vX.Y.Z    |
|             |    | release notes and      |           |           |
|             |    | section 3.1 above      |           |           |
+-------------+----+------------------------+-----------+-----------+
| DE          | R  | Configurable delay in  | 0         | 0         |
| LAY_SAMPLES | /W | samples                |           |           |
+-------------+----+------------------------+-----------+-----------+
| STATUS      | R  | Status                 | 0         | 0         |
+-------------+----+------------------------+-----------+-----------+
| DEVICE_TO   | R  | Device to USB bit      | 16        | -         |
| _USB_BIT_RES| /W | resolution             |           |           |
+-------------+----+------------------------+-----------+-----------+
| DEVICE      | R  | Device to USB rate     | 48000     | -         |
| _TO_USB_RATE| /W |                        |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI         | W  | Sets the interrupt     | -         | -         |
| _INT_CONFIG |    | config for a specific  |           |           |
|             |    | pin                    |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI_INT     | R  | Read whether interrupt | -         | -         |
| _PENDING_PIN|    | was triggered for      |           |           |
|             |    | selected pin           |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI_INT_P   | R  | Read whether interrupt | -         | -         |
| ENDING_PORT |    | was triggered for all  |           |           |
|             |    | pins on selected port  |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI_PIN     | R  | Read current state of  | -         | -         |
|             |    | the selected GPIO pin  |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI_PIN_A   | W  | Set the active level   | 0         | 0         |
| CTIVE_LEVEL |    | for a specific GPI     |           |           |
|             |    | pin. 0: active low 1:  |           |           |
|             |    | active high            |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI_PORT    | R  | Read current state of  | -         | -         |
|             |    | the selected GPIO port |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPI         | R  | Sets the selected port |  0  0     |  0  0     |
| _READ_HEADER| /W | and pin for the next   |           |           |
|             |    | GPIO read              |           |           |
+-------------+----+------------------------+-----------+-----------+
| G           | W  | Set the serial flash   | 0         | 0         |
| PO_FLASHING |    | mask for a specific    |           |           |
|             |    | pin. Each bit in the   |           |           |
|             |    | mask describes the GPO |           |           |
|             |    | state for 100ms        |           |           |
|             |    | intervals              |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPO_PIN     | W  | Write to a specific    | -         | -         |
|             |    | GPIO pin               |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPO_PIN_A   | W  | Set the active level   | 0         | 0         |
| CTIVE_LEVEL |    | for a specific GPO     |           |           |
|             |    | pin. 0: active low 1:  |           |           |
|             |    | active high            |           |           |
+-------------+----+------------------------+-----------+-----------+
| GPO_PORT    | W  | GPIO: Write to all     | -         | -         |
|             |    | pins of a GPIO port    |           |           |
+-------------+----+------------------------+-----------+-----------+
| G           | W  | GPIO: Set the pwm duty | 0         | 0         |
| PO_PWM_DUTY |    | for a specific pin.    |           |           |
|             |    | Value given as an      |           |           |
|             |    | integer percentage     |           |           |
+-------------+----+------------------------+-----------+-----------+
| I2S_RATE    | R  | I2S rate. This command | 48000     | 48000     |
|             | /W | can be used in SPI     |           |           |
|             |    | Boot Delay mode prior  |           |           |
|             |    | to                     |           |           |
|             |    | SET_MIC_START_STATUS 1 |           |           |
+-------------+----+------------------------+-----------+-----------+
| I2S_S       | R  | Start I2S. This        | -         | -         |
| TART_STATUS | /W | command can be         |           |           |
|             |    | specified from the     |           |           |
|             |    | control interface in   |           |           |
|             |    | case of SPI booting    |           |           |
|             |    | INT device in delayed  |           |           |
|             |    | start mode.            |           |           |
+-------------+----+------------------------+-----------+-----------+
| IO_MAP      | W  | Set IO map for the     | -         | -         |
|             |    | device.                |           |           |
|             |    |                        |           |           |
|             |    | arg1: dest             |           |           |
|             |    |                        |           |           |
|             |    | arg2: source           |           |           |
+-------------+----+------------------------+-----------+-----------+
| IO_MA       | R  | Get IO map and output  | -         | -         |
| P_AND_SHIFT |    | shift values for the   |           |           |
|             |    | device.                |           |           |
+-------------+----+------------------------+-----------+-----------+
| O           | W  | For a selected output  | -         | -         |
| UTPUT_SHIFT |    | set the no. of bits    |           |           |
|             |    | the output samples     |           |           |
|             |    | will be shifted by.    |           |           |
|             |    | Positive shift value   |           |           |
|             |    | indicates left shift,  |           |           |
|             |    | negative indicates     |           |           |
|             |    | right shift.           |           |           |
+-------------+----+------------------------+-----------+-----------+
| SE          | R  | Read / Write the       |  0        |  0        |
| RIAL_NUMBER | /W | serial number from USB |           |           |
|             |    | descriptor (normally   |           |           |
|             |    | initialised from       |           |           |
|             |    | flash.                 |           |           |
+-------------+----+------------------------+-----------+-----------+
| SYS_C       | R  | Get XCore divider from | 11        | 11        |
| LK_TO_MCLK  | /W | system clock to output |           |           |
| _OUT_DIVIDER|    | master clock. This     |           |           |
|             |    | command can be used in |           |           |
|             |    | SPI Boot Delay mode    |           |           |
|             |    | prior to               |           |           |
|             |    | SET_MIC_START_STATUS 1 |           |           |
+-------------+----+------------------------+-----------+-----------+
| USB         | R  | USB Device Release     | 1         | -         |
| _BCD_DEVICE | /W | Number (bcdDevice)     |           |           |
+-------------+----+------------------------+-----------+-----------+
| USB         | R  | USB Product ID         | 20        | -         |
| _PRODUCT_ID | /W |                        | (0x0014)  |           |
+-------------+----+------------------------+-----------+-----------+
| USB_PRO     | R  |  Get USB Product       |  XVF3610  |  -        |
| DUCT_STRING | /W | string                 | (UAC1.0)  |           |
|             |    |                        | Adaptive  |           |
+-------------+----+------------------------+-----------+-----------+
| USB_SE      | W  | Load serial number     | -         | -         |
| RIAL_NUMBER |    | from flash and         |           |           |
|             |    | initialise USB device  |           |           |
|             |    | descriptor with it.    |           |           |
|             |    | Will not work after    |           |           |
|             |    | boot since descriptor  |           |           |
|             |    | is populated only      |           |           |
|             |    | once  with USB start.  |           |           |
+-------------+----+------------------------+-----------+-----------+
| USB_S       | R  | Start USB. This        | -         | 0         |
| TART_STATUS | /W | command is only run    |           |           |
|             |    | from the flash. Run it |           |           |
|             |    | only with -l option to |           |           |
|             |    | generate the json item |           |           |
|             |    | to use in the flash    |           |           |
|             |    | data-partition         |           |           |
+-------------+----+------------------------+-----------+-----------+
| USB_TO_DEV  | R  | USB to device bit      | 16        | -         |
| ICE_BIT_RES | /W | resolution             |           |           |
+-------------+----+------------------------+-----------+-----------+
| USB_TO      | R  | USB to device rate     | 48000     | -         |
| _DEVICE_RATE| /W |                        |           |           |
+-------------+----+------------------------+-----------+-----------+
| US          | R  | USB Vendor ID          | 8369      | -         |
| B_VENDOR_ID | /W |                        | (0x20B1)  |           |
+-------------+----+------------------------+-----------+-----------+
| USB_VE      | R  | USB Vendor string      |  XMOS     |  -        |
| NDOR_STRING | /W |                        |           |           |
+-------------+----+------------------------+-----------+-----------+
| MCLK        | R  | xCORE divider from     | 2         | 2         |
| _IN_TO_PDM  | /W | input master clock to  |           |           |
| _CLK_DIVIDER|    | 6.144MHz DDR PDM       |           |           |
|             |    | microphone clock       |           |           |
+-------------+----+------------------------+-----------+-----------+
| A           | R  | Automatic delay        | 0         | 0         |
| DEC_ENABLED | /W | estimator controller   |           |           |
|             |    | enabled: 0: off  1: on |           |           |
+-------------+----+------------------------+-----------+-----------+
| ADEC_MODE   | R  | Automatic delay        | 0         | 0         |
|             |    | estimator controller   |           |           |
|             |    | mode: 0: normal AEC    |           |           |
|             |    | mode  1: delay         |           |           |
|             |    | estimation mode        |           |           |
+-------------+----+------------------------+-----------+-----------+
| DELA        | R  | Configurable delay     | 0         | 0         |
| Y_DIRECTION | /W | direction: 0: delay    |           |           |
|             |    | references  1: delay   |           |           |
|             |    | mics                   |           |           |
+-------------+----+------------------------+-----------+-----------+
| DEL         | R  | Delay estimate         | -         | -         |
| AY_ESTIMATE |    |                        |           |           |
+-------------+----+------------------------+-----------+-----------+
| D           | R  | Enable/disable delay   | 0         | 0         |
| ELAY_ESTIMA | /W | estimation             |           |           |
| TOR_ENABLED |    |                        |           |           |
+-------------+----+------------------------+-----------+-----------+
| MAN         | W  | Trigger a delay        | -         | -         |
| UAL_ADEC_CY |    | estimate               |           |           |
| CLE_TRIGGER |    |                        |           |           |
+-------------+----+------------------------+-----------+-----------+
| MIC_SHI     | R  | The shift value and    |  0  0     |  0  0     |
| FT_SATURATE | /W | saturation (1=enable)  |           |           |
|             |    | to be applied to the   |           |           |
|             |    | input mic samples      |           |           |
+-------------+----+------------------------+-----------+-----------+

Table 6‑2 Advanced parameter summary

+--------------+-----+---------------------+------------+------------+
| Parameter    | R   | Description         | 3610-UA    | 3610-INT   |
|              | ead |                     | default    | default    |
|              | /   |                     |            |            |
|              | Wr  |                     |            |            |
|              | ite |                     |            |            |
+==============+=====+=====================+============+============+
| BLD_HOST     | R   | Build host          |  Jenkins   |  Jenkins   |
+--------------+-----+---------------------+------------+------------+
| BLD_MODIFIED | R   | Build modified from |  false     |  false     |
|              |     | given view/hash     |            |            |
+--------------+-----+---------------------+------------+------------+
| BLD_MSG      | R   | Build message       |  Default   |  Default   |
+--------------+-----+---------------------+------------+------------+
| B            | R   | Repo hash – unique  |  See       |  See       |
| LD_REPO_HASH |     | source version      | release    | release    |
|              |     |                     | notes      | notes      |
+--------------+-----+---------------------+------------+------------+
| B            | R   | xgit hash – unique  |  See       |  See       |
| LD_XGIT_HASH |     | build version       | release    | release    |
|              |     |                     | notes      | notes      |
+--------------+-----+---------------------+------------+------------+
| B            | R   | xgit view           |  sw_xvf3   |  sw_xvf3   |
| LD_XGIT_VIEW |     |                     | 510_master | 510_master |
+--------------+-----+---------------------+------------+------------+
| F            | R/W | Filter bypass       | 1          | 1          |
| ILTER_BYPASS |     | state.              |            |            |
|              |     |                     |            |            |
|              |     | arg1: 0 - filter    |            |            |
|              |     | enabled  1 -        |            |            |
|              |     | bypassed            |            |            |
+--------------+-----+---------------------+------------+------------+
| FILTER_COEFF | R/W | Set biquad coeffs   | 0.000000   | 0.000000   |
|              |     | for a selected      | 0.000000   | 0.000000   |
|              |     | filter using        | 0.000000   | 0.000000   |
|              |     | floating point.     | 0.000000   | 0.000000   |
|              |     |                     | 0.000000   | 0.000000   |
|              |     | arg1..10: 5x2 float | 0.000000   | 0.000000   |
|              |     | coeffs in forward   | 0.000000   | 0.000000   |
|              |     | order (a1, a2, b0,  | 0.000000   | 0.000000   |
|              |     | b1, b2) where a0    | 0.000000   | 0.000000   |
|              |     | always is 1.0.      | 0.000000   | 0.000000   |
+--------------+-----+---------------------+------------+------------+
| FILT         | R/W | Set raw biquad      |  0  0  0   |  0  0  0   |
| ER_COEFF_RAW |     | coeffs for a        | 0  0  0    | 0  0  0    |
|              |     | selected filters.   | 0  0  0    | 0  0  0    |
|              |     |                     | 0          | 0          |
|              |     | arg1..10: 2 sets of |            |            |
|              |     | coeffs in forward   |            |            |
|              |     | order (b0, b1, b2,  |            |            |
|              |     | =-E1, -a2) signed   |            |            |
|              |     | Q28 format          |            |            |
+--------------+-----+---------------------+------------+------------+
| FILTER_INDEX | R/W | Set filter index.   | 0          | 0          |
|              |     | Selects which       |            |            |
|              |     | filter block will   |            |            |
|              |     | be read             |            |            |
|              |     | from/written to     |            |            |
|              |     |                     |            |            |
|              |     | arg1: dest          |            |            |
+--------------+-----+---------------------+------------+------------+
| HA           | R   | Get the build       | -1         | -1         |
| RDWARE_BUILD |     | number from the     |            |            |
|              |     | hardware build      |            |            |
|              |     | section of the      |            |            |
|              |     | flash data          |            |            |
|              |     | partition.          |            |            |
+--------------+-----+---------------------+------------+------------+
| I2C          | R/W | Read from an I2C    | -          | -          |
|              |     | device connected to |            |            |
|              |     | the xvf device      |            |            |
+--------------+-----+---------------------+------------+------------+
| I2C          | R/W | Get the address     |  0  0  0   | -          |
| _READ_HEADER |     | register address    |            |            |
|              |     | and count of next   |            |            |
|              |     | I2C read            |            |            |
+--------------+-----+---------------------+------------+------------+
| I2C_WITH_REG | R/W | Read from the       |  -         | -          |
|              |     | register of an I2C  |            |            |
|              |     | device connected to |            |            |
|              |     | the xvf device      |            |            |
+--------------+-----+---------------------+------------+------------+
| MONITOR      | W   | Enable monitoring   | -          | -          |
| _STATE_USING |     | of AEC and Delay    |            |            |
| _GPO_ENABLED |     | Estimation state on |            |            |
|              |     | GPO. This command   |            |            |
|              |     | is only run from    |            |            |
|              |     | the flash. Run it   |            |            |
|              |     | only with -l option |            |            |
|              |     | to generate the     |            |            |
|              |     | json item to use in |            |            |
|              |     | the flash           |            |            |
|              |     | data-partition      |            |            |
+--------------+-----+---------------------+------------+------------+
| KWD          | R   | Gets boot status    | 0          | 0          |
| _BOOT_STATUS |     | for keyword         |            |            |
|              |     | detectors           |            |            |
+--------------+-----+---------------------+------------+------------+
| KWD_I        | R/W | GPI pin index to    | 4          | 4          |
| NTERRUPT_PIN |     | receive keyword     |            |            |
|              |     | interrupt on        |            |            |
+--------------+-----+---------------------+------------+------------+
| MA           | R   | Get maximum no. of  | -          | -          |
| X_UBM_CYCLES |     | cycles taken by the |            |            |
|              |     | user buffer         |            |            |
|              |     | management function |            |            |
+--------------+-----+---------------------+------------+------------+
| MIC_START    | R/W | Get microphone      | 2          | 2          |
| _STATUS      |     | client start        |            |            |
|              |     | status.             |            |            |
+--------------+-----+---------------------+------------+------------+
| REMA         | W   | Reset the max user  | -          | -          |
| X_UBM_CYCLES |     | buffer management   |            |            |
|              |     | cycles count        |            |            |
+--------------+-----+---------------------+------------+------------+
| RUN_STATUS   | R   | Gets run status for | -          | -          |
|              |     | the device (See     |            |            |
|              |     | Appendix B )        |            |            |
+--------------+-----+---------------------+------------+------------+
| SPI          | R   | Gets the contents   | -          | -          |
|              |     | of the SPI read     |            |            |
|              |     | buffer              |            |            |
+--------------+-----+---------------------+------------+------------+
| SPI_PUSH     | W   | Push SPI command    | -          | -          |
|              |     | data onto the       |            |            |
|              |     | execution queue     |            |            |
+--------------+-----+---------------------+------------+------------+
| SPI_P        | W   | Push SPI command    | -          | -          |
| USH_AND_EXEC |     | data and execute    |            |            |
|              |     | the command from    |            |            |
|              |     | the stack           |            |            |
+--------------+-----+---------------------+------------+------------+
| SPI          | R/W | Address and count   |  0  0      |  0  0      |
| _READ_HEADER |     | of next SPI read    |            |            |
+--------------+-----+---------------------+------------+------------+
| ADAPTATIO    | R/W | Adaptation config   | 0          | 0          |
| N_CONFIG_AEC |     |                     |            |            |
|              |     | 0 = filter adapt    |            |            |
|              |     | with variable       |            |            |
|              |     | stepsize            |            |            |
|              |     |                     |            |            |
|              |     | 1 = filter adapt    |            |            |
|              |     | with fixed stepsize |            |            |
|              |     |                     |            |            |
|              |     | 2 = filter fixed    |            |            |
+--------------+-----+---------------------+------------+------------+
| BYPASS_AEC   | R/W | AEC bypass          | 1          | 1          |
+--------------+-----+---------------------+------------+------------+
| COE          | R/W | AEC coefficient     | 0          | 0          |
| FF_INDEX_AEC |     | index               |            |            |
+--------------+-----+---------------------+------------+------------+
| ERLE_CH0_AEC | R   | AEC channel 0 ERLE  | -          | -          |
+--------------+-----+---------------------+------------+------------+
| ERLE_CH1_AEC | R   | AEC channel 1 ERLE  | -          | -          |
+--------------+-----+---------------------+------------+------------+
| F_B          | R   | AEC f bin count     | 257        | 257        |
| IN_COUNT_AEC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| FILTER_COEF  | R   | AEC filter          | -          | -          |
| FICIENTS_AEC |     | coefficients        |            |            |
+--------------+-----+---------------------+------------+------------+
| FORCED_MU    | R/W | AEC forced mu value | 1          | 1          |
| _VALUE_AEC   |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| FRAME        | R   | AEC frame advance   | 240        | 240        |
| _ADVANCE_AEC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| M            | R/W | AEC mu_high and     | 1.0000     | 1.0000     |
| U_LIMITS_AEC |     | mu_low              | 0.0001     | 0.0001     |
+--------------+-----+---------------------+------------+------------+
| M            | R/W | AEC get mu_scalar   | 0.4        | 0.4        |
| U_SCALAR_AEC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| RESE         | W   | AEC reset filter.   | -          | -          |
| T_FILTER_AEC |     | Note: do NOT prefix |            |            |
|              |     | with SET\_          |            |            |
+--------------+-----+---------------------+------------+------------+
| SIGM         | R/W | AEC sigma alphas    | 5  5  11   | 5  5  11   |
| A_ALPHAS_AEC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| X_CHANNE     | R   | AEC x channel       | 15  15  4  | 15  15  4  |
| L_PHASES_AEC |     | phases              | 0  0  0    | 0  0  0    |
|              |     |                     | 0  0  0    | 0  0  0    |
|              |     |                     | 0          | 0          |
+--------------+-----+---------------------+------------+------------+
| X_CHANNELS   | R   | AEC x channels      | 2          | 2          |
| _AEC         |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| X_ENER       | R/W | AEC X energy delta  |  -         |  -         |
| GY_DELTA_AEC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| X_ENERGY_GA  | R/W | AEC X energy gamma  | -          | -          |
| MMA_LOG2_AEC |     | log2                |            |            |
+--------------+-----+---------------------+------------+------------+
| Y_CHANNELS   | R   | AEC y channels      | 1          | 1          |
| _AEC         |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| ADAPTATI     | R/W |  IC: get adaptation | 0          | 0          |
| ON_CONFIG_IC |     | config              |            |            |
+--------------+-----+---------------------+------------+------------+
| BYPASS_IC    | R/W |  IC: get bypass     | 0          | 0          |
|              |     | state               |            |            |
+--------------+-----+---------------------+------------+------------+
| CH1_BEA      | R/W | Channel 1           | 1          | 1          |
| MFORM_ENABLE |     | Beamforming enabled |            |            |
+--------------+-----+---------------------+------------+------------+
| COEFFICI     | R/W | IC Coefficient      | 0          | 0          |
| ENT_INDEX_IC |     | index               |            |            |
+--------------+-----+---------------------+------------+------------+
| FILTER_COE   | R   | IC Filter           | -          | -          |
| FFICIENTS_IC |     | coefficients        |            |            |
+--------------+-----+---------------------+------------+------------+
| FORCED       | R/W | IC forced mu value  | -          | -          |
| _MU_VALUE_IC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| PHASES_IC    | R   | IC phases           | 10         | 10         |
+--------------+-----+---------------------+------------+------------+
| PROC_F       | R   | IC proc frame bins  | 256        | 256        |
| RAME_BINS_IC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| RES          | W   | IC reset filter,    | -          | -          |
| ET_FILTER_IC |     | note: do not prefix |            |            |
|              |     | with SET\_          |            |            |
+--------------+-----+---------------------+------------+------------+
| SI           | R/W | IC adaptation       | 11         | 11         |
| GMA_ALPHA_IC |     | config              |            |            |
+--------------+-----+---------------------+------------+------------+
| X_ENE        | R/W | IC X energy delta   |  -         | -          |
| RGY_DELTA_IC |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| X_ENERGY_G   | R/W | IC X energy gamma   | -          | -          |
| AMMA_LOG2_IC |     | log2                |            |            |
+--------------+-----+---------------------+------------+------------+
| BYPASS_SUP   | R/W | SUP bypass          | 0          | 0          |
+--------------+-----+---------------------+------------+------------+
| ENABLED_AES  | R/W | SUP echo            | 0          | 0          |
|              |     | suppression enabled |            |            |
|              |     | (DO NOT ENABLE)     |            |            |
+--------------+-----+---------------------+------------+------------+
| ENABLED_NS   | R/W | SUP noise           | 1          | 1          |
|              |     | suppression enabled |            |            |
+--------------+-----+---------------------+------------+------------+
| NO           | R/W | SUP noise           | 0.1259     | 0.1259     |
| ISE_FLOOR_NS |     | suppression noise   |            |            |
|              |     | floor               |            |            |
+--------------+-----+---------------------+------------+------------+
| ADEC_F       | R/W | ADEC Far-end signal |  0.000002  |  0.000002  |
| AR_THRESHOLD |     | energy threshold    |            |            |
|              |     | above which AGM is  |            |            |
|              |     | updated             |            |            |
+--------------+-----+---------------------+------------+------------+
| ADEC_PEAK    | R/W | ADEC the peak to    |  4.000000  |  4.000000  |
| _TO_AVER     |     | average ratio that  |            |            |
| AGE_GOOD_AEC |     | is considered good  |            |            |
|              |     | when in normal AEC  |            |            |
|              |     | mode                |            |            |
+--------------+-----+---------------------+------------+------------+
| ADEC_TIME    | R   | Time in             | -          | -          |
| _SINCE_RESET |     | milliseconds since  |            |            |
|              |     | last automatic      |            |            |
|              |     | delay change by     |            |            |
|              |     | ADEC                |            |            |
+--------------+-----+---------------------+------------+------------+
| A            | R   | AEC coefficients    | -          | -          |
| EC_PEAK_TO_A |     | peak to average     |            |            |
| VERAGE_RATIO |     | ratio               |            |            |
+--------------+-----+---------------------+------------+------------+
| AGM          | R   | AEC Goodness Metric | -          | -          |
|              |     | estimate (0.0 -     |            |            |
|              |     | 1.0)                |            |            |
+--------------+-----+---------------------+------------+------------+
| ALT_ARCH     | R/W | State of XVF3610    | 1          | 1          |
| _ENABLED     |     | alternate           |            |            |
|              |     | architecture        |            |            |
|              |     | setting             |            |            |
+--------------+-----+---------------------+------------+------------+
| E            | R/W | ERLE bad threshold  | -          | -          |
| RLE_BAD_BITS |     | in bits (log2)      |            |            |
+--------------+-----+---------------------+------------+------------+
| E            | R/W | Set how steeply AGM | 0.0664     | 0.0664     |
| RLE_BAD_GAIN |     | drops off when ERLE |            |            |
|              |     | below threshold     |            |            |
+--------------+-----+---------------------+------------+------------+
| ER           | R/W | ERLE good threshold | 2          | 2          |
| LE_GOOD_BITS |     | in bits (log2)      |            |            |
+--------------+-----+---------------------+------------+------------+
| LOCKER_DELAY | R/W | Delay set point     | 0          | 0          |
| _SETPOINT    |     | direction           |            |            |
| _DIRECTION   |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| LOCKER       | R/W | Delay set point     | 0          | 0          |
| _DELAY_SETP  |     | enabled             |            |            |
| OINT_ENABLED |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| LOCKE        | R/W | Delay setpoint      | 0          | 0          |
| R_DELAY_SETP |     | samples             |            |            |
| OINT_SAMPLES |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| LOCKER       | R/W | Locker delay        | 0          | 0          |
| _ENABLED     |     | detection and       |            |            |
|              |     | control             |            |            |
+--------------+-----+---------------------+------------+------------+
| LOCKER_NUM   | R/W | No. of bad peak to  | 666        | 666        |
| _BAD_FRAM    |     | avg ERLE frames     |            |            |
| ES_THRESHOLD |     | that locker sees    |            |            |
|              |     | before it triggers  |            |            |
|              |     | ADEC.               |            |            |
+--------------+-----+---------------------+------------+------------+
| LOCKER_STATE | R   | Locker state        | BOTH_WAIT  | BOTH_WAIT  |
+--------------+-----+---------------------+------------+------------+
| MAX_CONTROL  | R   | Max control time    |  -         | -          |
| _TIME_STAGE_A|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_DSP      | R   | Max dsp time per    | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_IDLE     | R   | Max idle time per   | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_RX       | R   | Max rx time per     | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_TX       | R   | Max tx time per     | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_CONTROL  | R   | Min control time    | -          | -          |
| _TIME_STAGE_A|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_DSP      | R   | Min dsp time per    | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_IDLE     | R   | Min idle time per   | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_RX       | R   | Min rx time per     | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_TX       | R   | Min tx time per     | -          | -          |
| _TIME_STAGE_A|     | frame               |            |            |
+--------------+-----+---------------------+------------+------------+
| PEAK         | R/W | Value which sets    | 3          | 3          |
| _PHASE_ENERG |     | AGM sensitivity to  |            |            |
| Y_TREND_GAIN |     | peak phase energy   |            |            |
|              |     | slope               |            |            |
+--------------+-----+---------------------+------------+------------+
| PHASE        | R/W | ERLE gain           | 0          | 0          |
| _POWER_INDEX |     |                     |            |            |
+--------------+-----+---------------------+------------+------------+
| PHASE_POWERS | R   | 5 phase powers (240 | 0.000000   | 0.000000   |
|              |     | samples per phase)  | dB         | dB         |
|              |     | used in delay       | 0.000000   | 0.000000   |
|              |     | estimation from the | dB         | dB         |
|              |     | index set.          | 0.000000   | 0.000000   |
|              |     |                     | dB         | dB         |
|              |     |                     | 0.000000   | 0.000000   |
|              |     |                     | dB         | dB         |
|              |     |                     | 0.000000   | 0.000000   |
|              |     |                     | dB         | dB         |
+--------------+-----+---------------------+------------+------------+
| RESET        | W   | Reset stage A frame | -          | -          |
| _TIME_STAGE_A|     | time                |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_CONTROL  | R   | Max control time    | -          | -          |
| _TIME_STAGE_B|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_DSP      | R   | Stage B max dsp     | -          | -          |
| _TIME_STAGE_B|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_IDLE     | R   | Stage B max idle    | -          | -          |
| _TIME_STAGE_B|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_RX       | R   | Stage B max rx time | -          | -          |
| _TIME_STAGE_B|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_TX       | R   | Stage B max tx time | -          | -          |
| _TIME_STAGE_B|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_CONTROL  | R   | Stage B min control | -          | -          |
| _TIME_STAGE_B|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_DSP      | R   | Stage B min dsp     | -          | -          |
| _TIME_STAGE_B|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_IDLE     | R   | Stage B min idle    | -          | -          |
| _TIME_STAGE_B|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_RX       | R   | Stage B min rx time | -          | -          |
| _TIME_STAGE_B|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_TX       | R   | Stage B min tx time | -          | -          |
| _TIME_STAGE_B|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| RESET        | W   | Reset stage B frame | -          | -          |
| _TIME_STAGE_B|     | time                |            |            |
+--------------+-----+---------------------+------------+------------+
| A            | R/W | AGC adaptation for  | 1          | 1          |
| DAPT_CH0_AGC |     | channel 0           |            |            |
+--------------+-----+---------------------+------------+------------+
| A            | R/W | AGC adaptation for  | 1          | 1          |
| DAPT_CH1_AGC |     | channel 1           |            |            |
+--------------+-----+---------------------+------------+------------+
| DECREME      | R/W | Stepsize with which | 0.87       | 0.87       |
| NT_GAIN_STEP |     | gain is decremented |            |            |
| SIZE_CH0_AGC |     | for AGC ch0         |            |            |
+--------------+-----+---------------------+------------+------------+
| DECREME      | R/W | Stepsize with which | 0.988      | 0.988      |
| NT_GAIN_STEP |     | gain is decremented |            |            |
| SIZE_CH1_AGC |     | for AGC ch1         |            |            |
+--------------+-----+---------------------+------------+------------+
| GAIN_CH0_AGC | R/W | Gain for channel 0  | -          | -          |
+--------------+-----+---------------------+------------+------------+
| GAIN_CH1_AGC | R/W | Gain for channel 1  | -          | -          |
+--------------+-----+---------------------+------------+------------+
| INCREME      | R/W | Stepsize with which | 1.197      | 1.197      |
| NT_GAIN_STEP |     | gain is incremented |            |            |
| SIZE_CH0_AGC |     | for AGC ch0         |            |            |
+--------------+-----+---------------------+------------+------------+
| INCREME      | R/W | Stepsize with which | 1.0034     | 1.0034     |
| NT_GAIN_STEP |     | gain is incremented |            |            |
| SIZE_CH1_AGC |     | for AGC ch1         |            |            |
+--------------+-----+---------------------+------------+------------+
| LC_ENA       | R/W | Loss control enable | 0          | 0          |
| BLED_CH0_AGC |     | for channel 0       |            |            |
+--------------+-----+---------------------+------------+------------+
| LC_ENA       | R/W | Loss control enable | 1          | 1          |
| BLED_CH1_AGC |     | for channel 1       |            |            |
+--------------+-----+---------------------+------------+------------+
| LOWER_THRES  | R/W | Lower threshold of  | 0.1905     | 0.1905     |
| HOLD_CH0_AGC |     | AGC desired level   |            |            |
|              |     | for channel 0       |            |            |
+--------------+-----+---------------------+------------+------------+
| LOWER_THRES  | R/W | Lower threshold of  | 0.4        | 0.4        |
| HOLD_CH1_AGC |     | AGC desired level   |            |            |
|              |     | for channel 1       |            |            |
+--------------+-----+---------------------+------------+------------+
| UPPER_THRES  | R/W | Upper threshold of  | 0.7079     | 0.7079     |
| HOLD_CH0_AGC |     | AGC desired level   |            |            |
|              |     | for channel 0       |            |            |
+--------------+-----+---------------------+------------+------------+
| UPPER_THRES  | R/W | Upper threshold of  | 0.4        | 0.4        |
| HOLD_CH1_AGC |     | AGC desired level   |            |            |
|              |     | for channel 1       |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_CONTROL  | R   | Stage C max control | -          | -          |
| _TIME_STAGE_C|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_DSP      | R   | Stage C max dsp     | -          | -          |
| _TIME_STAGE_C|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_GAIN     | R/W | Max gain for        | 999.9847   | 999.9847   |
| _CH0_AGC     |     | channel 0           |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_GAIN     | R/W | Max gain for        | 999.9847   | 999.9847   |
| _CH1_AGC     |     | channel 1           |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_IDLE     | R   | Stage C max idle    | -          | -          |
| _TIME_STAGE_C|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_RX       | R   | Stage C max rx time | -          | -          |
| _TIME_STAGE_C      | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MAX_TX       | R   | Stage C max tx time | -          | -          |
| _TIME_STAGE_C|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_CONTROL  | R   | Stage C min control | -          | -          |
| _TIME_STAGE_C|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_DSP      | R   | Stage C min dsp     | -          | -          |
| _TIME_STAGE_C|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_IDLE     | R   | Stage C min idle    | -          | -          |
| _TIME_STAGE_C|     | time per frame      |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_RX       | R   | Stage C min rx time | -          | -          |
| _TIME_STAGE_C|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| MIN_TX       | R   | Stage C min tx time | -          | -          |
| _TIME_STAGE_C|     | per frame           |            |            |
+--------------+-----+---------------------+------------+------------+
| REF_OUT_CH1  | R/W | Stage C: check if   | 0          | 0          |
|              |     | reference audio is  |            |            |
|              |     | output in channel 1 |            |            |
+--------------+-----+---------------------+------------+------------+
| RESET_TIME   | W   | Reset stage C frame | -          | -          |
| _STAGE_C     |     | time                |            |            |
+--------------+-----+---------------------+------------+------------+
