XVF3610 Far-field voice processor
==================================

The XMOS XVF3610 range of voice processors uses microphone array
processing to capture clear, high-quality voice from anywhere in the
room. XVF3610 processors use highly optimised digital signal processing
algorithms implementing ‘barge-in', point noise and ambient noise
reduction to increase the Signal-to-Noise Ratio (SNR) achieving a
reliable voice interface whatever the environment.

The XVF3610 processor is designed for seamless integration into consumer
electronic products requiring voice interfaces for Automatic Speech
Recognition (ASR), communications or conferencing. In addition to its
class-leading voice processing, the XVF3610 voice processor provides a
comprehensive set of interfaces and configuration options to simplify
the integration of a voice interface into a wide range of system
architectures. This includes specific features required in TV and
set-top box applications, including audio switching and digital inputs
and outputs that support switches and LED indicators.

The XVF3610 voice processor executes a firmware image that is either
read from a flash memory device or loaded by a host processor. The
Device Firmware Upgrade (DFU) function of the processor allows in field
upgrade ensuring all products can benefit from the latest releases.
While the voice processor is running, this configuration can be modified
by the host system over the XVF3610 control interface. The control
interface also allows the host system to control peripheral devices and
obtain status information from the device and its digital inputs.

Two variants of the XVF3610 are available which have been optimised for
different application use cases. These two variants require different
firmware to be loaded onto the device.

.. table:: XVF3610 variants
   :widths: auto

   +-------------+---------------------------+---------------------------+
   | Product     | Key features              | Target Application        |
   +=============+===========================+===========================+
   | XVF3610-INT | Far-field voice interface | Voice interface           |
   |             |                           | integrated into the       |
   |             | Audio interface: I2S      | product                   |
   |             | (Slave)                   |                           |
   |             |                           |                           |
   |             | Control interface: I2C    |                           |
   |             | (Slave)                   |                           |
   |             |                           |                           |
   |             | Device Firmware Upgrade:  |                           |
   |             | I2C (Slave)               |                           |
   +-------------+---------------------------+---------------------------+
   | XVF3610-UA  | Far-field voice interface | USB plug-in voice         |
   |             |                           | accessory, and integrated |
   |             | Audio interfaces: USB     | products using USB        |
   |             | UAC1.0 (and optionally    |                           |
   |             | I2S Master)               |                           |
   |             |                           |                           |
   |             | Control interface: USB2.0 |                           |
   |             | Full Speed                |                           |
   |             |                           |                           |
   |             | Device Firmware Upgrade:  |                           |
   |             | USB                       |                           |
   +-------------+---------------------------+---------------------------+

These application use cases are described in more detail in the
following sections.
