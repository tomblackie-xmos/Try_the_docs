USB Interface
==============

The following section details aspects that relate to the USB interface
configuration and usage. This section only pertains to the XVF3610-UA
variant of the processor.

The USB interface provides the host three end points:

* Adaptive USB Audio Class 1.0 endpoint for the transfer of Far-field voice to the host and AEC reference audio from the host.

* Vendor Specific Control allowing the host to control and parameterise the processor.

* Human Interface Device (HID) interrupt endpoint to signal the detection of events which have occurred on the GPIOs.

The USB Audio interface supports class compliant volume controls on both
the input (processed microphone from XVF3610) and output (AEC reference)
interfaces. These controls are accessed via the host OS audio control
panels. They are initialised to 100% (0dB attenuation) on boot and this
is the recommended setting for normal device operation.

By default the device will enumerate with the VID and PID shown below,
but these can be configured using the Data Partition.

.. table:: Default USB Identification

  +-----------------------------------------------------+----------------+
  | USB Identification                                  | Value          |
  +=====================================================+================+
  | Vendor Identification (VID)                         | 0x20B1         |
  +-----------------------------------------------------+----------------+
  | Product Identification (PID)                        | 0x0014         |
  +-----------------------------------------------------+----------------+

The following section describes the parameters available to configure
the USB interface behaviour.

USB Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Due to the nature of the USB enumeration process, USB setup must be done
using a Data Partition so that the configuration is complete prior to
enumeration. The following table summarises the USB interface parameters
which can be configured.

.. table:: USB configuration parameters

  +-------------------+----+----------+----------------------------------+
  | Command           | Ty | A        | Definition                       |
  |                   | pe | rguments |                                  |
  +===================+====+==========+==================================+
  | SET_USB_VENDOR_ID | ui | 1        | Set USB Vendor ID. See notes A,  |
  |                   | nt |          | B.                               |
  | GET_USB_VENDOR_ID | 32 |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | S                 | ui | 1        | Set USB Product ID. See notes A, |
  | ET_USB_PRODUCT_ID | nt |          | B.                               |
  |                   | 32 |          |                                  |
  | G                 |    |          |                                  |
  | ET_USB_PRODUCT_ID |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | S                 | ui | 1        | Set USB Device Release Number    |
  | ET_USB_BCD_DEVICE | nt |          | (bcdDevice). See notes A, B.     |
  |                   | 32 |          |                                  |
  | G                 |    |          |                                  |
  | ET_USB_BCD_DEVICE |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET_USB           | u  | 25       | Set USB Vendor string. See notes |
  | _VENDOR_STRING    | in |          | A, B.                            |
  |                   | t8 |          |                                  |
  | GET_USB           |    |          |                                  |
  | _VENDOR_STRING    |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET_U             | u  | 25       | Set USB Product string. See      |
  | SB_PRODUCT_STRING | in |          | notes A, B.                      |
  |                   | t8 |          |                                  |
  | GET_U             |    |          |                                  |
  | SB_PRODUCT_STRING |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET_USB           | ui | 1        | Write only register, setting the |
  | _SERIAL_NUMBER    | nt |          | behaviour of iSerialNumber field |
  |                   | 32 |          | in USB descriptor (See notes A,  |
  | GET_USB           |    |          | B.):                             |
  | _SERIAL_NUMBER    |    |          |                                  |
  |                   |    |          | 1 - Load from Flash Serial       |
  |                   |    |          | Number                           |
  |                   |    |          |                                  |
  |                   |    |          | 0 - Default to 0 .               |
  +-------------------+----+----------+----------------------------------+
  | SET_U             | ui | 1        | Set sampling frequency of USB    |
  | SB_TO_DEVICE_RATE | nt |          | reference from USB host. Default |
  |                   | 32 |          | is 48000 samples/sec. See notes  |
  | GET_U             |    |          | A, B.                            |
  | SB_TO_DEVICE_RATE |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET_D             | ui | 1        | Set sampling frequency of audio  |
  | EVICE_TO_USB_RATE | nt |          | output to USB host. Default      |
  |                   | 32 |          | device_to_usb_rate is 48000      |
  | GET_D             |    |          | samples/sec. See notes A, B.     |
  | EVICE_TO_USB_RATE |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET_USB_TO        | ui | 1        | Set bit depth of USB reference   |
  | _DEVICE_BIT_RES   | nt |          | from USB host. Default           |
  |                   | 32 |          | usb_to_device_bit_res is 16      |
  | GET_USB_TO        |    |          | bits. See notes A, B.            |
  | _DEVICE_BIT_RES   |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET_DEVI          | ui | 1        | Set bit depth of audio output to |
  | CE_TO_USB_BIT_RES | nt |          | USB host. Default                |
  |                   | 32 |          | device_to_usb_bit_res is 16      |
  | GET_DEVI          |    |          | bits. See notes A, B.            |
  | CE_TO_USB_BIT_RES |    |          |                                  |
  +-------------------+----+----------+----------------------------------+
  | SET               | u  | 1        | Start USB. Set as 1 as the last  |
  | _USB_START_STATUS | in |          | USB item in Data Partition. See  |
  |                   | t8 |          | notes A.                         |
  | GET               |    |          |                                  |
  | _USB_START_STATUS |    |          |                                  |
  +-------------------+----+----------+----------------------------------+

**A:** Command supported for Data Partition use only

**B:** Command must occur before SET_USB_START_STATUS 1

USB HID interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Human Interface Device (HID) is an electronic device with an interface
which a human can use for control. Examples include a Personal Computer
with a keyboard and mouse or a consumer appliance with control knobs,
push buttons or a voice interface.

The XVF3610-UA uses the HID interface to inform the host system of
events which have occurred on the General Purpose Inputs (GPI). The
following section describes the setup of the GPI HID triggers.

HID Report Generation
'''''''''''''''''''''

The XVF3610 is able to send HID reports when an interrupt (logic edge
transition event) on a GPI pin has been received. When interrupts are
enabled using SET_GPI_INT_CONFIG, the interrupt bit is automatically
serviced by the HID report generator. If an interrupt has occurred, then
the sticky bit is immediately cleared and an HID report is generated.
The HID features are described below:

-  HID report for the assertion of GPI pin (positive edge) and report
     for the de-assertion (negative edge)

-  The HID report type is generated with one of the following standard
     USB HID keycodes:

-  GUI Application Control Search (0x221)

-  GUI Application Control Stop (0x226)

-  Keyboard F23 (0x72)

-  Keyboard F24 (0x73)

-  When no event has occurred, depending on “set idle” configuration by
     the host, it will either reply with a de-assert report (default)
     or NAK (set to idle by the host)

NOTE: HID idle behaviour is platform-specific and rarely the high-level
application code will have any control over the settings. Linux, for
example, typically silences the devices by issuing an indefinite idle
(NAK report if no change). Other platforms such as MacOS, on the other
hand, leave the device verbose by not issuing an idle (report always
sent).

The HID function requires that a GPI pin is configured to generate
interrupts on both edges.

The HID Report Descriptor used in XVF3610-UA translates the GPI pin
interrupt into a HID Report asserting one of the predefined usages.

The HID Report has the format:

+-----+------+------+-------------+----------------+---+---+---+---+
| Bit | 7    | 6    | 5           | 4              | 3 | 2 | 1 | 0 |
+=====+======+======+=============+================+===+===+===+===+
|     | F24  | F23  | AC Stop     | AC Search      | R |   |   |   |
|     |      |      |             |                | e |   |   |   |
|     |      |      |             |                | s |   |   |   |
|     |      |      |             |                | e |   |   |   |
|     |      |      |             |                | r |   |   |   |
|     |      |      |             |                | v |   |   |   |
|     |      |      |             |                | e |   |   |   |
|     |      |      |             |                | d |   |   |   |
+-----+------+------+-------------+----------------+---+---+---+---+

The corresponding bit equals 1 when a positive edge interrupt has been
detected and zero where a negative edge interrupt has occurred. In order
to configure the GPI pin that triggers the HID report, the
SET_GPI_INT_CONFIG command is used.

For example, the following command configures GPI pin 0 to generate
interrupts on both edges, which enables the HID report logic:

vfctrl_usb SET_GPI_INT_CONFIG 0 0 3

The first argument is a reserved value and should be set to 0. The
second argument makes the command target pin IP_0. The third argument
selects both edges for the interrupt. To make the device respond to the
falling edge only with the value 1 and rising edge only with the value
2.
