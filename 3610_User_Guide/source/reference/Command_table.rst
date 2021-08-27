Command list
*************

.. list-table:: Command List
    :widths: auto
    :header-rows: 1

    * - Cmd_Group
      - Parameter
      -  Description
    * - AP
      - GET_VERSION
      - CONTROL: get version
    * - AP
      - GET_STATUS
      - CONTROL: get status
    * - AP
      - GET_DELAY_SAMPLES
      - CONTROL: get configurable delay in samples
    * - AP
      - GET_BLD_MSG
      - CONTROL: get build message
    * - AP
      - GET_BLD_HOST
      - CONTROL: get build host
    * - AP
      - GET_BLD_REPO_HASH
      - CONTROL: get repo hash
    * - AP
      - GET_BLD_XGIT_VIEW
      - CONTROL: get xgit view
    * - AP
      - GET_BLD_XGIT_HASH
      - CONTROL: get xgit hash
    * - AP
      - GET_BLD_MODIFIED
      - CONTROL: get build modified from given view/hash
    * - GPIO
      - GET_I2C
      - GPIO: Read from an I2C device connected to the xvf device
    * - GPIO
      - GET_I2C_WITH_REG
      - GPIO: Read from the register of an I2C device connected to the xvf device
    * - GPIO
      - GET_I2C_READ_HEADER
      - GPIO: Get the address, register address, and count of next I2C read
    * - GPIO
      - SET_I2C
      - GPIO: Write to an I2C device connected to the xvf device
    * - GPIO
      - SET_I2C_WITH_REG
      - GPIO: Write to the register of an I2C device connected to the xvf device
    * - GPIO
      - SET_I2C_READ_HEADER
      - GPIO: Set address, register address, and count of next I2C read
    * - GPIO
      - GET_SPI
      - GPIO: Gets the contents of the SPI read buffer
    * - GPIO
      - GET_SPI_READ_HEADER
      - GPIO: Get the address and count of next SPI read
    * - GPIO
      - SET_SPI_PUSH
      - GPIO: Push SPI command data onto the execution queue
    * - GPIO
      - SET_SPI_PUSH_AND_EXEC
      - GPIO: Push SPI command data and execute the command from the stack
    * - GPIO
      - SET_SPI_READ_HEADER
      - GPIO: Set address and count of next SPI read
    * - GPIO
      - GET_GPI_PORT
      - GPIO: Read current state of the selected GPIO port
    * - GPIO
      - GET_GPI_PIN
      - GPIO: Read current state of the selected GPIO pin
    * - GPIO
      - GET_GPI_INT_PENDING_PIN
      - GPIO: Read whether interrupt was triggered for selected pin
    * - GPIO
      - GET_GPI_INT_PENDING_PORT
      - GPIO: Read whether interrupt was triggered for all pins on selected port
    * - GPIO
      - GET_KWD_HID_EVENT_CNT
      - GPIO: read number of KWD HID events detected
    * - GPIO
      - SET_KWD_HID_EVENT_CNT
      - GPIO: write number of KWD HID events detected
    * - GPIO
      - SET_GPO_PORT
      - GPIO: Write to all pins of a GPIO port
    * - GPIO
      - SET_GPO_PIN
      - GPIO: Write to a specific GPIO pin
    * - GPIO
      - SET_GPO_PIN_ACTIVE_LEVEL
      - GPIO: Set the active level for a specific GPO pin. 0: active low, 1: active high
    * - GPIO
      - SET_GPI_PIN_ACTIVE_LEVEL
      - GPIO: Set the active level for a specific GPI pin. 0: active low, 1: active high
    * - GPIO
      - SET_GPI_INT_CONFIG
      - GPIO: Sets the interrupt config for a specific pin
    * - GPIO
      - SET_GPI_READ_HEADER
      - GPIO: Sets the selected port and pin for the next GPIO read
    * - GPIO
      - GET_GPI_READ_HEADER
      - GPIO: Gets the currently selected port and pin
    * - GPIO
      - SET_GPO_PWM_DUTY
      - GPIO: Set the pwm duty for a specific pin. Value given as an integer percentage
    * - GPIO
      - SET_GPO_FLASHING
      - GPIO: Set the serial flash mask for a specific pin. Each bit in the mask describes the GPO state for 100ms intervals
    * - GPIO
      - GET_KWD_BOOT_STATUS
      - GPIO: Gets boot status for keyword detectors
    * - GPIO
      - GET_RUN_STATUS
      - GPIO: Gets run status for the device
    * - GPIO
      - GET_IO_MAP_AND_SHIFT
      - Get IO map and output shift values for the device
    * - GPIO
      - SET_IO_MAP
      - Set IO map for the device. arg1: dest(output_io_map_t), arg2: source(input_io_map_t)
    * - GPIO
      - SET_FILTER_INDEX
      - Set filter index. Selects which filter block will be read from/written to arg1: dest(filter_block_map_t)
    * - GPIO
      - SET_FILTER_BYPASS
      - Set filter bypass state. arg1: 0 - filter enabled, 1 - bypassed
    * - GPIO
      - SET_FILTER_COEFF
      - Set biquad coeffs for a selected filter using floating point. arg1..10: 5x2 float coeffs in forward order (a1,a2,b0,b1,b2) where a0 always is 1.0
    * - GPIO
      - SET_FILTER_COEFF_RAW
      - Set raw biquad coeffs for a selected filters. arg1..10: 2 sets of coeffs in forward order (b0,b1,b2,-a1,-a2) signed Q28 format
    * - GPIO
      - GET_FILTER_INDEX
      - Get filter index. Selects which filter block will be read from/written to
    * - GPIO
      - GET_FILTER_BYPASS
      - Get filter bypass state. 0 - filter enabled, 1 - bypassed
    * - GPIO
      - GET_FILTER_COEFF
      - Get biquad coeffs for a selected filter using floating point. arg1..10: 5x2 float coeffs in forward order (a1,a2,b0,b1,b2) where a0 always is 1.0
    * - GPIO
      - GET_FILTER_COEFF_RAW
      - Get raw biquad coeffs for a selected filters. arg1..10: 2 sets of coeffs in forward order (b0,b1,b2,-a1,-a2) signed Q28 format
    * - GPIO
      - SET_OUTPUT_SHIFT
      - For a selected output(output_io_map_t), set the no. of bits the output samples will be shifted by. Postive shift value indicates left shift, negative indicates right shift
    * - GPIO
      - GET_MAX_UBM_CYCLES
      - Get maximum no. of cycles taken by the user buffer management function
    * - GPIO
      - RESET_MAX_UBM_CYCLES
      - reset the max user buffer management cycles count
    * - GPIO
      - GET_I2S_RATE
      - Get I2S rate
    * - GPIO
      - SET_I2S_RATE
      - Set I2S rate. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_I2S_START_STATUS
      - Start I2S. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - GET_I2S_START_STATUS
      - Get I2S start status
    * - GPIO
      - GET_USB_VENDOR_ID
      - Get USB Vendor ID
    * - GPIO
      - GET_USB_PRODUCT_ID
      - Get USB Product ID
    * - GPIO
      - GET_USB_BCD_DEVICE
      - Get USB Device Release Number (bcdDevice)
    * - GPIO
      - GET_USB_VENDOR_STRING
      - Get USB Vendor string
    * - GPIO
      - GET_USB_PRODUCT_STRING
      - Get USB Product string
    * - GPIO
      - GET_HID_MAP
      - Get HID map. Returns byte and bit in HID report for event type and index given by SET_HID_MAP_READ_HEADER.
    * - GPIO
      - GET_HID_MAP_READ_HEADER
      - Get HID map read header. Returns event type, e.g., GPI or keyword, and index.
    * - GPIO
      - GET_HID_USAGE
      - Get HID usage. Returns usage page number and short item bytes 0..2 for the HID report byte and bit set by SET_HID_USAGE_READ_HEADER.
    * - GPIO
      - GET_HID_USAGE_READ_HEADER
      - Get HID usage read header. Returns the HID report byte and bit and the usage page given by SET_HID_USAGE_READ_HEADER.
    * - GPIO
      - GET_SERIAL_NUMBER
      - Read serial number from USB descriptor (normally initialised from flash).
    * - GPIO
      - GET_HARDWARE_BUILD
      - Get the build number from the hardware build section of the flash data partition.
    * - GPIO
      - SET_USB_VENDOR_ID
      - Set USB Vendor ID. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_USB_PRODUCT_ID
      - Set USB Product ID. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_USB_VENDOR_STRING
      - Set USB Vendor string. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_USB_PRODUCT_STRING
      - Set USB Product string. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_USB_BCD_DEVICE
      - Set USB Device Release Number (bcdDevice)
    * - GPIO
      - SET_HID_MAP
      - Set HID map for event type and index from SET_HID_MAP_READ_HEADER. arg1: HID report byte. arg2: HID report bit. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_HID_MAP_READ_HEADER
      - Set HID map read header. arg1: type of event, e.g., GPI or keyword. arg2: index of event.
    * - GPIO
      - SET_HID_USAGE
      - Set HID usage for report byte and bit and with usage page from SET_HID_USAGE_READ_HEADER. arg1..3: short item bytes 0..2. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_HID_USAGE_READ_HEADER
      - Set HID usage read header. arg1: HID report byte. arg2: HID report bit. arg3: usage page number (see USB HID Usage Tables).
    * - GPIO
      - SET_SERIAL_NUMBER
      - Program serial number to flash
    * - GPIO
      - SET_USB_SERIAL_NUMBER
      - Load serial number from flash and initialise USB device descriptor with it. Will not work after boot since descriptor is populated only once, with USB start.
    * - GPIO
      - SET_USB_START_STATUS
      - Start USB. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - GET_USB_START_STATUS
      - Get USB start status
    * - GPIO
      - GET_USB_TO_DEVICE_RATE
      - Get USB to device rate
    * - GPIO
      - GET_DEVICE_TO_USB_RATE
      - Get device to USB rate
    * - GPIO
      - GET_USB_TO_DEVICE_BIT_RES
      - Get USB to device bit resolution
    * - GPIO
      - GET_DEVICE_TO_USB_BIT_RES
      - Get device to USB bit resolution
    * - GPIO
      - SET_USB_TO_DEVICE_RATE
      - Set USB to device rate
    * - GPIO
      - SET_DEVICE_TO_USB_RATE
      - Set device to USB rate
    * - GPIO
      - SET_USB_TO_DEVICE_BIT_RES
      - Set USB to device bit resolution
    * - GPIO
      - SET_DEVICE_TO_USB_BIT_RES
      - Set device to USB bit resolution
    * - GPIO
      - GET_MCLK_IN_TO_PDM_CLK_DIVIDER
      - Get XCore divider from input master clock to 6.144MHz DDR PDM microphone clock
    * - GPIO
      - GET_SYS_CLK_TO_MCLK_OUT_DIVIDER
      - Get XCore divider from system clock to output master clock
    * - GPIO
      - SET_MCLK_IN_TO_PDM_CLK_DIVIDER
      - Set XCore divider from input master clock to 6.144MHz DDR PDM microphone clock (when master clock is slaved). Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_SYS_CLK_TO_MCLK_OUT_DIVIDER
      - Set XCore divider from system clock to output master clock (where master clock output is used). Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - GET_MIC_START_STATUS
      - Get microphone client start status.
    * - GPIO
      - SET_MIC_START_STATUS
      - Start microphone client (audio frontend).  This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_MONITOR_STATE_USING_GPO_ENABLED
      - enable monitoring of state on GPO. This command is only run from the flash. Run only with -l option, generates a json item for the flash data-partition.
    * - GPIO
      - SET_KWD_INTERRUPT_PIN
      - set gpi pin index to receive kwd interrupt on
    * - GPIO
      - GET_KWD_INTERRUPT_PIN
      - get gpi pin index to receive kwd interrupt on
    * - AEC
      - GET_BYPASS_AEC
      - AEC: get bypass
    * - AEC
      - GET_X_ENERGY_DELTA_AEC
      - AEC: get X energy delta
    * - AEC
      - GET_X_ENERGY_GAMMA_LOG2_AEC
      - AEC: get X energy gamma log2
    * - AEC
      - GET_FORCED_MU_VALUE_AEC
      - AEC: get forced mu value
    * - AEC
      - GET_ADAPTATION_CONFIG_AEC
      - AEC: get adaptation config
    * - AEC
      - GET_MU_SCALAR_AEC
      - AEC: get mu_scalar
    * - AEC
      - GET_MU_LIMITS_AEC
      - AEC: get mu_high and mu_low
    * - AEC
      - GET_SIGMA_ALPHAS_AEC
      - AEC: get sigma alphas
    * - AEC
      - GET_ERLE_CH0_AEC
      - AEC: get channel 0 ERLE
    * - AEC
      - GET_ERLE_CH1_AEC
      - AEC: get channel 1 ERLE
    * - AEC
      - GET_FRAME_ADVANCE_AEC
      - AEC: get frame advance
    * - AEC
      - GET_Y_CHANNELS_AEC
      - AEC: get y channels
    * - AEC
      - GET_X_CHANNELS_AEC
      - AEC: get x channels
    * - AEC
      - GET_X_CHANNEL_PHASES_AEC
      - AEC: get x channel phases
    * - AEC
      - GET_F_BIN_COUNT_AEC
      - AEC: get f bin count
    * - AEC
      - GET_FILTER_COEFFICIENTS_AEC
      - AEC: get filter coefficients
    * - AEC
      - GET_COEFF_INDEX_AEC
      - AEC: get coefficient index
    * - IC
      - GET_CH1_BEAMFORM_ENABLE
      - get if beamforming is enabled on channel1. default:enable
    * - AP
      - GET_DELAY_ESTIMATOR_ENABLED
      - CONTROL: enable/disable delay estimation
    * - AP
      - GET_DELAY_ESTIMATE
      - CONTROL: get delay estimate
    * - AP
      - GET_DELAY_DIRECTION
      - CONTROL: get configurable delay direction: 0: delay references, 1: delay mics
    * - AP
      - GET_MIC_SHIFT_SATURATE
      - CONTROL: get the shift value and saturation (1=enable) to be applied to the input mic samples
    * - AP
      - GET_AEC_RESET_TIMEOUT
      - stage A: Get timeout between consecutive AEC resets, values are expressed in 15ms frames. If timeout is -1, the AEC reset is disabled
    * - AP
      - GET_ALT_ARCH_ENABLED
      - stage A: Get state of xvf3610 alternate architecture setting: 0: normal, 1: alt-arch
    * - AP
      - GET_ADEC_ENABLED
      - stage A: get automatic delay estimator controller enabled: 0: off, 1: on
    * - AP
      - GET_ADEC_MODE
      - stage A: get automatic delay estimator controller mode: 0: normal AEC mode, 1: delay estimation mode
    * - AP
      - GET_ADEC_TIME_SINCE_RESET
      - stage A: get time in milliseconds since last automatic delay change by ADEC
    * - AP
      - GET_AGM
      - stage A: get AEC Goodness Metric estimate (0.0 - 1.0
    * - AP
      - GET_ERLE_BAD_BITS
      - stage A: get ERLE bad threshold in bits (log2)
    * - AP
      - GET_ERLE_GOOD_BITS
      - stage A: get ERLE good threshold in bits (log2)
    * - AP
      - GET_PEAK_PHASE_ENERGY_TREND_GAIN
      - stage A: get value which sets AGM sensitivity to peak phase energy slope
    * - AP
      - GET_ERLE_BAD_GAIN
      - stage A: set how steeply AGM drops off when ERLE below threshold
    * - AP
      - GET_ADEC_FAR_THRESHOLD
      - stage A: get far signal energy threshold above which we update AGM
    * - AP
      - GET_AEC_PEAK_TO_AVERAGE_RATIO
      - stage A: get AEC coefficients peak to average ratio
    * - AP
      - GET_PHASE_POWERS
      - stage A: get 5 phase powers (240 samples per phase) used in delay estimation from the index set.
    * - AP
      - GET_PHASE_POWER_INDEX
      - stage A: get GERLE gain (how strongly it responds either side of mid point)
    * - AP
      - GET_MIN_RX_TIME_STAGE_A
      - stage A min rx time per frame
    * - AP
      - GET_MAX_RX_TIME_STAGE_A
      - stage A max rx time per frame
    * - AP
      - GET_MIN_CONTROL_TIME_STAGE_A
      - stage A min control time per frame
    * - AP
      - GET_MAX_CONTROL_TIME_STAGE_A
      - stage A max control time per frame
    * - AP
      - GET_MIN_DSP_TIME_STAGE_A
      - stage A min dsp time per frame
    * - AP
      - GET_MAX_DSP_TIME_STAGE_A
      - stage A max dsp time per frame
    * - AP
      - GET_MIN_TX_TIME_STAGE_A
      - stage A min tx time per frame
    * - AP
      - GET_MAX_TX_TIME_STAGE_A
      - stage A max tx time per frame
    * - AP
      - GET_MIN_IDLE_TIME_STAGE_A
      - stage A min idle time per frame
    * - AP
      - GET_MAX_IDLE_TIME_STAGE_A
      - stage A max idle time per frame
    * - AP
      - GET_ADEC_PEAK_TO_AVERAGE_GOOD_AEC
      - stage A: get the peak to average ratio that is considered good when in normal AEC mode
    * - AP
      - SET_ADEC_PEAK_TO_AVERAGE_GOOD_AEC
      - stage A: set the peak to average ratio that is considered good when in normal AEC mode
    * - AP
      - GET_MIN_RX_TIME_STAGE_B
      - stage B min rx time per frame
    * - AP
      - GET_MAX_RX_TIME_STAGE_B
      - stage B max rx time per frame
    * - AP
      - GET_MIN_CONTROL_TIME_STAGE_B
      - stage B min control time per frame
    * - AP
      - GET_MAX_CONTROL_TIME_STAGE_B
      - stage B max control time per frame
    * - AP
      - GET_MIN_DSP_TIME_STAGE_B
      - stage B min dsp time per frame
    * - AP
      - GET_MAX_DSP_TIME_STAGE_B
      - stage B max dsp time per frame
    * - AP
      - GET_MIN_TX_TIME_STAGE_B
      - stage B min tx time per frame
    * - AP
      - GET_MAX_TX_TIME_STAGE_B
      - stage B max tx time per frame
    * - AP
      - GET_MIN_IDLE_TIME_STAGE_B
      - stage B min idle time per frame
    * - AP
      - GET_MAX_IDLE_TIME_STAGE_B
      - stage B max idle time per frame
    * - AP
      - GET_MIN_RX_TIME_STAGE_C
      - stage C min rx time per frame
    * - AP
      - GET_MAX_RX_TIME_STAGE_C
      - stage C max rx time per frame
    * - AP
      - GET_MIN_CONTROL_TIME_STAGE_C
      - stage C min control time per frame
    * - AP
      - GET_MAX_CONTROL_TIME_STAGE_C
      - stage C max control time per frame
    * - AP
      - GET_MIN_DSP_TIME_STAGE_C
      - stage C min dsp time per frame
    * - AP
      - GET_MAX_DSP_TIME_STAGE_C
      - stage C max dsp time per frame
    * - AP
      - GET_MIN_TX_TIME_STAGE_C
      - stage C min tx time per frame
    * - AP
      - GET_MAX_TX_TIME_STAGE_C
      - stage C max tx time per frame
    * - AP
      - GET_MIN_IDLE_TIME_STAGE_C
      - stage C min idle time per frame
    * - AP
      - GET_MAX_IDLE_TIME_STAGE_C
      - stage C max idle time per frame
    * - AGC
      - GET_GAIN_CH0_AGC
      - get gain for channel 0
    * - AGC
      - GET_GAIN_CH1_AGC
      - get gain for channel 1
    * - AGC
      - GET_MAX_GAIN_CH0_AGC
      - get max gain for channel 0
    * - AGC
      - GET_MAX_GAIN_CH1_AGC
      - get max gain for channel 1
    * - AGC
      - GET_MIN_GAIN_CH0_AGC
      - get min gain for channel 0
    * - AGC
      - GET_MIN_GAIN_CH1_AGC
      - get min gain for channel 1
    * - AGC
      - GET_UPPER_THRESHOLD_CH0_AGC
      - get upper threshold of desired level for channel 0
    * - AGC
      - GET_UPPER_THRESHOLD_CH1_AGC
      - get upper threshold of desired level for channel 1
    * - AGC
      - GET_LOWER_THRESHOLD_CH0_AGC
      - get lower threshold of desired level for channel 0
    * - AGC
      - GET_LOWER_THRESHOLD_CH1_AGC
      - get lower threshold of desired level for channel 1
    * - AGC
      - GET_ADAPT_CH0_AGC
      - get AGC adaptation for channel 0
    * - AGC
      - GET_ADAPT_CH1_AGC
      - get AGC adaptation for channel 1
    * - AGC
      - GET_ADAPT_ON_VAD_CH0_AGC
      - get AGC adaptation using VAD data for channel 0
    * - AGC
      - GET_ADAPT_ON_VAD_CH1_AGC
      - get AGC adaptation using VAD data for channel 1
    * - AGC
      - GET_SOFT_CLIPPING_CH0_AGC
      - get AGC soft clipping for channel 0
    * - AGC
      - GET_SOFT_CLIPPING_CH1_AGC
      - get AGC soft clipping  for channel 1
    * - AGC
      - GET_LC_ENABLED_CH0_AGC
      - get loss control enable for channel 0
    * - AGC
      - GET_LC_ENABLED_CH1_AGC
      - get loss control enable for channel 1
    * - AGC
      - GET_LC_N_FRAMES_CH1_AGC
      - get number of near-end and far-end frames in loss control for channel 1
    * - AGC
      - GET_LC_CORR_THRESHOLD_CH0_AGC
      - get loss control correlation threshold for channel 0
    * - AGC
      - GET_LC_CORR_THRESHOLD_CH1_AGC
      - get loss control correlation threshold for channel 1
    * - AGC
      - GET_LC_DELTAS_CH0_AGC
      - get loss control delta coefficient for channel 0: far-end only, near-end only, both far-end and near-end
    * - AGC
      - GET_LC_DELTAS_CH1_AGC
      - get loss control delta coefficient for channel 1: far-end only, near-end only, both far-end and near-end
    * - AGC
      - GET_LC_GAMMAS_CH0_AGC
      - get loss control gamma coefficients for channel 0: background power, increment and decrement
    * - AGC
      - GET_LC_GAMMAS_CH1_AGC
      - get loss control gamma coefficients for channel 1: background power, increment and decrement
    * - AGC
      - GET_LC_GAINS_CH0_AGC
      - get loss control gains for channel 0: max, double-talk, silence and min
    * - AGC
      - GET_LC_GAINS_CH1_AGC
      - get loss control gains for channel 1: max, double-talk, silence and min
    * - AGC
      - GET_INCREMENT_GAIN_STEPSIZE_CH0_AGC
      - get stepsize with which gain is incremented for AGC ch0
    * - AGC
      - GET_INCREMENT_GAIN_STEPSIZE_CH1_AGC
      - get stepsize with which gain is incremented for AGC ch1
    * - AGC
      - GET_DECREMENT_GAIN_STEPSIZE_CH0_AGC
      - get stepsize with which gain is decremented for AGC ch0
    * - AGC
      - GET_DECREMENT_GAIN_STEPSIZE_CH1_AGC
      - get stepsize with which gain is decremented for AGC ch1
    * - IC
      - GET_BYPASS_IC
      - IC: get bypass state
    * - IC
      - GET_X_ENERGY_DELTA_IC
      - IC: get X energy delta
    * - IC
      - GET_X_ENERGY_GAMMA_LOG2_IC
      - IC: get X energy gamma log2
    * - IC
      - GET_FORCED_MU_VALUE_IC
      - IC: get forced mu value
    * - IC
      - GET_ADAPTATION_CONFIG_IC
      - IC: get adaptation config
    * - IC
      - GET_SIGMA_ALPHA_IC
      - IC: get adaptation config
    * - IC
      - GET_PHASES_IC
      - IC: get phases
    * - IC
      - GET_PROC_FRAME_BINS_IC
      - IC: get proc frame bins
    * - IC
      - GET_FILTER_COEFFICIENTS_IC
      - IC: get filter coefficients
    * - IC
      - GET_COEFFICIENT_INDEX_IC
      - IC: get coefficient index
    * - SUP
      - GET_BYPASS_SUP
      - SUP: get bypass
    * - AEC
      - SET_BYPASS_AEC
      - AEC: set bypass
    * - AEC
      - SET_X_ENERGY_DELTA_AEC
      - AEC: set X energy delta
    * - AEC
      - SET_X_ENERGY_GAMMA_LOG2_AEC
      - AEC: set X energy gamma log2
    * - AEC
      - SET_FORCED_MU_VALUE_AEC
      - AEC: set forced mu value
    * - AEC
      - SET_ADAPTATION_CONFIG_AEC
      - AEC: set adaptation config
    * - AEC
      - SET_MU_SCALAR_AEC
      - AEC: set mu_scalar
    * - AEC
      - SET_MU_LIMITS_AEC
      - AEC: set mu_high and mu_low
    * - AEC
      - SET_SIGMA_ALPHAS_AEC
      - AEC: set sigma alphas
    * - AEC
      - RESET_FILTER_AEC
      - AEC: reset filter
    * - AEC
      - SET_COEFF_INDEX_AEC
      - AEC: set coefficient index
    * - AP
      - SET_DELAY_DIRECTION
      - set configurable delay direction: 0: delay references, 1: delay mics
    * - AP
      - SET_DELAY_SAMPLES
      - CONTROL: set configurable delay in samples
    * - AP
      - SET_DELAY_ESTIMATOR_ENABLED
      - set delay estimator enabled
    * - AP
      - SET_MIC_SHIFT_SATURATE
      - CONTROL: set the shift value and saturation (1=enable) to be applied to the input mic samples
    * - AP
      - SET_ALT_ARCH_ENABLED
      - stage A: Set state of xvf3610 alternate architecture setting: 0: normal, 1: alt-arch
    * - AP
      - SET_AEC_RESET_TIMEOUT
      - stage A: Set timeout between consecutive AEC resets, values are expressed in 15ms frames. If timeout is -1, the AEC reset is disabled
    * - AP
      - SET_ADEC_ENABLED
      - set delay estimator controller enabled: 0: off, 1: on
    * - AP
      - SET_MANUAL_ADEC_CYCLE_TRIGGER
      - trigger a delay estimate + delay configure cycle when 1 is written
    * - AP
      - SET_ERLE_BAD_BITS
      - set ERLE threshold at which AGM is decreased
    * - AP
      - SET_ERLE_GOOD_BITS
      - set ERLE threshold at which AGM is increased
    * - AP
      - SET_ERLE_BAD_GAIN
      - set how strongly AGM is updated when ERLE below threshold
    * - AP
      - SET_PEAK_PHASE_ENERGY_TREND_GAIN
      - set how strongly AGM is updated by the peak phase slope
    * - AP
      - SET_ADEC_FAR_THRESHOLD
      - set energy threshold of far signal above which AGM is updated
    * - AP
      - SET_PHASE_POWER_INDEX
      - set index for reading phase powers
    * - AP
      - RESET_TIME_STAGE_A
      - reset stage A frame time
    * - AP
      - RESET_TIME_STAGE_B
      - reset stage B frame time
    * - AP
      - RESET_TIME_STAGE_C
      - reset stage C frame time
    * - AGC
      - SET_GAIN_CH0_AGC
      - set gain for channel 0
    * - AGC
      - SET_GAIN_CH1_AGC
      - set gain for channel 1
    * - AGC
      - SET_MAX_GAIN_CH0_AGC
      - set max gain for channel 0
    * - AGC
      - SET_MAX_GAIN_CH1_AGC
      - set gain for channel 1
    * - AGC
      - SET_MAX_GAIN_CH1_AGC
      - set max gain for channel 1
    * - AGC
      - SET_MIN_GAIN_CH0_AGC
      - set min gain for channel 0
    * - AGC
      - SET_MIN_GAIN_CH1_AGC
      - set min gain for channel 1
    * - AGC
      - SET_UPPER_THRESHOLD_CH0_AGC
      - set upper threshold of desired level for channel 0
    * - AGC
      - SET_UPPER_THRESHOLD_CH1_AGC
      - set upper threshold of desired level for channel 1
    * - AGC
      - SET_LOWER_THRESHOLD_CH0_AGC
      - set lower threshold of desired level for channel 0
    * - AGC
      - SET_LOWER_THRESHOLD_CH1_AGC
      - set lower threshold of desired level for channel 1
    * - AGC
      - SET_ADAPT_CH0_AGC
      - set AGC adaptation for channel 0
    * - AGC
      - SET_ADAPT_CH1_AGC
      - set AGC adaptation for channel 1
    * - AGC
      - SET_ADAPT_ON_VAD_CH0_AGC
      - set AGC adaptation using VAD data for channel 0
    * - AGC
      - SET_ADAPT_ON_VAD_CH1_AGC
      - set AGC adaptation using VAD data for channel 1
    * - AGC
      - SET_SOFT_CLIPPING_CH0_AGC
      - set AGC soft clipping for channel 0
    * - AGC
      - SET_SOFT_CLIPPING_CH1_AGC
      - set AGC soft clipping for channel 1
    * - AGC
      - SET_LC_ENABLED_CH0_AGC
      - enable loss control for channel 0
    * - AGC
      - SET_LC_ENABLED_CH1_AGC
      - enable loss control for channel 1
    * - AGC
      - SET_LC_N_FRAMES_CH0_AGC
      - set number of frames in loss control for near-end and far-end activity on channel 0
    * - AGC
      - SET_LC_N_FRAMES_CH1_AGC
      - set number of frames in loss control for near-end and far-end activity on channel 1
    * - AGC
      - SET_LC_CORR_THRESHOLD_CH0_AGC
      - set loss control correlation threshold for channel 0
    * - AGC
      - SET_LC_CORR_THRESHOLD_CH1_AGC
      - set loss control correlation threshold for channel 1
    * - AGC
      - SET_LC_DELTAS_CH0_AGC
      - set loss control delta coefficients for channel 0: far-end only, near-end only, both far-end and near-end
    * - AGC
      - SET_LC_DELTAS_CH1_AGC
      - set loss control delta coefficients for channel 1: far-end only, near-end only, both far-end and near-end
    * - AGC
      - SET_LC_GAMMAS_CH0_AGC
      - set loss control gamma coefficients for channel 0: background power, increment and decrement
    * - AGC
      - SET_LC_GAMMAS_CH1_AGC
      - set loss control gamma coefficients for channel 1: background power, increment and decrement
    * - AGC
      - SET_LC_GAINS_CH0_AGC
      - set loss control gains for channel 0: max, double-talk, silence and min
    * - AGC
      - SET_LC_GAINS_CH1_AGC
      - set loss control gains for channel 1: max, double-talk, silence and min
    * - AGC
      - SET_INCREMENT_GAIN_STEPSIZE_CH0_AGC
      - set stepsize with which gain is incremented for AGC ch0
    * - AGC
      - SET_INCREMENT_GAIN_STEPSIZE_CH1_AGC
      - set stepsize with which gain is incremented for AGC ch1
    * - AGC
      - SET_DECREMENT_GAIN_STEPSIZE_CH0_AGC
      - set stepsize with which gain is decremented for AGC ch0
    * - AGC
      - SET_DECREMENT_GAIN_STEPSIZE_CH1_AGC
      - set stepsize with which gain is decremented for AGC ch1
    * - IC
      - SET_BYPASS_IC
      - IC: set bypass
    * - IC
      - SET_X_ENERGY_DELTA_IC
      - IC: set X energy delta
    * - IC
      - SET_X_ENERGY_GAMMA_LOG2_IC
      - IC: set X energy gamma log2
    * - IC
      - SET_FORCED_MU_VALUE_IC
      - IC: set forced mu value
    * - IC
      - SET_ADAPTATION_CONFIG_IC
      - IC: set adaptation config
    * - IC
      - SET_SIGMA_ALPHA_IC
      - IC: set adaptation config
    * - IC
      - SET_COEFFICIENT_INDEX_IC
      - IC: set coefficient index
    * - IC
      - RESET_FILTER_IC
      - IC: reset filter
    * - IC
      - SET_CH1_BEAMFORM_ENABLE
      - set if beamforming is enabled on channel1
    * - SUP
      - SET_BYPASS_SUP
      - SUP: set bypass






.. csv-table::
  :file: 46-commands.csv
  :widths: 5, 10 ,10, 5, 60
  :header-rows: 1
