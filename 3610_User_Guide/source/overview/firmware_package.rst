Firmware release package
==============================

There are two release packages available for the XVF3610, one for the
XVF3610-UA and one for the XVF3610-INT.

.. todo::

   Add in download links

Release packages and firmware builds are identified via a version
number, which follows the standard semantic version specification. The
version number format is X.Y.Z, eg 5.2.0, and these numbers have the
following meaning.

.. list-table:: Firmware version number structure
  :widths: auto
  :header-rows: 1

  * - Digit
    - Name
    - Meaning
  * - X
    - Major version number
    - Significant release of the firmware. The control interface may not be backwards compatible with earlier versions
  * - Y
    - Minor version number
    - New features added, but the control interface is backwards compatible with earlier host applications
  * - Z
    - Patch version number
    - Bug fixes for incorrect functionality only. No change to host interface

The release version is contained in the file name of firmware file
distribution and can also be read via the control interface using the
``GET_VERSION`` command.

Each package consists of several directories and files containing
released firmware binaries, data-partition tools, host binaries and host
source code. A simplified directory structure is shown below.

::

  ├── bin
  ├── data-partition
  │ ├── images
  │ └── input
  └── host
  ├── Linux
  │   └── bin
  ├── MAC
  │   └── bin
  ├── Pi
  │   ├── bin
  │   └── scripts
  ├── Win32
  │   └── bin
  └── src
  ├── dfu
  ├── dpgen
  └── vfctrl


Further information about each component of the release is as follows:

“bin” Directory
~~~~~~~~~~~~~~~

This directory contains the released firmware for the XVF3610. There are
two copies of the firmware; one intended for loading from an external
flash device and one for loading from an external host over SPI (XVF3610
is the slave). Please refer to the SPI Slave boot section of the
datasheet for connections to the external boot source.

“data-partition” Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~

The data partition contains configuration data for the XVF3610 firmware,
implemented as a set of commands that are run at boot time. The data
partition is created using input command source files and a set of tools
which are described in the Data Partition section of this document. The
contents of the data-partition directory are as follows:

The root directory contains default data partition image source files
(int.json or ua.json) as well as the generic flash device specification
16mbit_12.5mhz_sector_4kb.spispec, data partition generation scripts and
short instructions about how to generate data partition binary files.

-  The images subdirectory contains pre-generated data partition binary
   files generated from the default data partition image source file.
   These files are suitable for direct programming into the external
   flash along with the firmware, should the default settings be
   suitable.

-  The input subdirectory contains short command sequences which are
   referenced by the data partition image source file when the data
   partition binary file is generated.

In addition, an output directory is created during the running of the
data partition generation script which contains the newly generated data
partition binary file.

“host” Directory
~~~~~~~~~~~~~~~~

This directory contains files and utilities relating to the host. The
various host utilities that perform parameter control, DFU and data
partition generation are provided pre-compiled for Linux (ARM and x86),
Windows and MacOS platforms. These binaries can be found in the Linux,
Pi, Mac and Win32 directories along with an additional script in for the
Pi release called send_image_from_rpi.py which provides an example of
sending an SPI boot image from the host.

The root of the host directory also contains scripts for unpacking
packed signals which can be captured using the controls described in the
signal routing section of this document.

Instructions for building the host utilities from the source are also
provided in the same directory. The source files for the host utilities
are contained in the src sub-directory allowing building, modification
or integration into other projects.

Within this directory there are three further sub-directories dfu, dpgen
and vfctrl which contain the source files (and dependent libraries) for
the DFU, data partition generator and parameter control utilities.

Required Tools
==============

In order to update the firmware, modify and regenerate Data Partitions
and rebuild the host utilities the following tools are required.

XTC Tools
~~~~~~~~~~~~~

The XMOS XTC Tools contains a comprehensive suite of tools for
compilation, debug and programming of XMOS devices. It is available to
download https://www.xmos.ai/software-tools

NOTE: At the time of writing v14.4.1 of the XTC Tools tools is
recommend for XVF3610 operation.

More recent versions may be available, but unless specified on the
xmos.ai website they will not have been tested and verified for
operation with XVF3610.

Further information about the full tool suite, including installation
instructions for different platforms is available here in the
XTC Tools user guide, available from https://www.xmos.ai/file/tools-user-guide

The XVF3610 Voice Processor is provided in two pre-compiled builds (-UA
and -INT) and as such only requires the usage of the XTC Tools
programming tools, specifically xFLASH. This operates as a command-line
application, to create the boot image, and if using flash, program the
boot image to the attached device.

An XTAG debugger must be connected to the XVF3610 for flash programming
operations. Refer to the Development Kit User Guide for information on
using XTAG connections to XVF3610 development kits.

The basic form of the xFLASH command for flash image creation and
programming with a data partition is as follows (note multiple lines
have been used for clarity, but command should be executed on single line).

.. code-block:: bash

  xflash --boot-partition-size 1048576 --factory [Application executable (.xe)] --data [Data partition description (.bin)]

.. note::

 For boot over SPI from a host processor uses a specific image which
 is supplied in the release package.  No data partition is included as
 configuration command are assumed to be supplied by the host controller used.


* Application executable (.xe)
  The .xe file is a boot image provided with a VocalFusion release package in
  one of the supported configurations (-UA or -INT product variants).

* Data partition description (.bin)
  The .bin file is a data partition description either supplied in the release
  package (-UA or -INT) or customised as described later in this guide.

.. warning::

  Running XTC Tools on macOS Catalina or above triggers a security alert.
  The process to resolve this is detailed here :
  https://www.xmos.ai/file/running-XTimecomposer-on-macos-catalina/

Python 3
~~~~~~~~

Some operations, such as running the SPI boot example on the Raspberry
Pi, require the use of Python 3 (v3.7 onward is recommended). Python can
be downloaded from http://python.org/downloads.

Host build tools
~~~~~~~~~~~~~~~~

In order to build the host utilities, the use of a platform-specific
compiler is required.

.. tab:: Windows

  The host utilities are built with the *x86 Native Tools Command Prompt
  for VS* which is installed as part of the *Build Tools for Visual
  Studio.* This can be downloaded from Microsoft website (at the time of
  writing latest versions available here:
  https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019).
  It is important to ensure that the optional *C++ CMake tools for
  Windows* are included when setting up the installation.

.. tab:: Linux

  Depending on the distribution and version of Linux used, the following
  packages may need to be installed:

  .. code-block:: bash

    sudo apt-get install -y build-essential
    sudo apt-get install -y pkg-config
    sudo apt-get install -y libusb-1.0-0-dev

.. tab:: Mac OS


    The XCode Command Line tools are required to build in on macOS. The
    following command can be used to install the tools.

    .. code-block:: bash

      xcode-select --install

Command-line interface (vfctrl)
================================

To allow command-line access to the control interface on the XVF3610
processor, the **vfctrl** (**V**\ ocal\ **F**\ usion
**C**\ on\ **tr**\ o\ **l**) utility is provided as part of the release
package. This utility

Two versions of this utility are provided for control of the device (a
third is used internally by the Data Partition generation process):

.. list-table:: vfctrl versions and platforms
  :widths: auto
  :header-rows: 1

  * - Version
    - Function
    - Host platforms supported
  * - vfctrl_usb
    - Control of XVF3610-UA over a USB interface
    - Windows, MacOS, Linux, Raspberry Pi OS
  * - vfctrl_i2c
    - Control of XVF3610-INT over i2c interface
    - Raspberry Pi OS


Source code for the utility is also provided for compilation for other
host devices if required.

The general syntax of the command line tool, when used for device
control, is as follows:

.. code-block:: bash

  vfctrl_usb <COMMAND_VERB> [ arg 1] [arg 2]....[arg N] [\# Comment]

The ``<COMMAND_VERB>`` is required and is used to control the parameters of
the device. Commands can be read and write commands and are
distinguished by the prefix ``GET\_`` and ``SET\_`` for parameter read and
write respectively.

The available commands are described in detail in specific sections
later in this document, and a summary table of all the parameters is
provided in Appendix A.

Following the <COMMAND_VERB> there are a number of optional arguments
[arg 1]..[arg N] which depend on the specific parameter. These are
detailed in the command tables later in the document.

If the ``<COMMAND_VERB>` is a ``GET\_`` command, the output of the operation
is printed to the terminal as in the example below:

.. code-block:: bash

  vfctrl_usb GET_GPI
  GET_GPI: 13

The number and type of arguments depend on the command and these are
detailed in the command tables. Arguments are integer numbers separated
by a space. For setting some parameters that require floating-point
data, the numbers have to be first converted to a Q format and then
transferred as integers.

The specification of the Q format for representing floating-point
numbers is given in Appendix H.

A secondary form of vfctrl is also available which provides information
for developers

.. code-block:: bash

  vfctrl [options]

Where [options] can be:

.. code-block:: bash

  -h, --help : List all command options

  -d, --dump-params : Print list of parameter values

  -n, --no-check-version : Do not check version of firmware image

Configuration via Control interface
===================================

The XVF3610 Voice Processor contains parameters which can be read and
written by the host processor at run time. For information writing
parameters at boot time for initial configuration, please see the
section on the Data Partition later in this document.

The XVF3610 firmware is provided as two pre-compiled builds, -UA and
-INT, which provide a parameter control mechanism over USB endpoint 0
and I2C respectively.

Device functions have controllable parameters for the audio pipeline,
GPIO, sample rate settings, audio muxing, timing and general device
setup and adjustment. Commands support either read using the GET\_
prefix or write using the SET\_ prefix. Controllable parameters may
either be readable and writeable, read-only or write-only. Various data
types are supported including signed/unsigned integer of either 8b or
32b, fixed point signed/unsigned and floating-point.

In addition, the -UA build includes volume controls for input (processed
mic from XVF3610) and output (far-end reference signal). These are USB
Audio Class 1.0 compliant controls and are accessed via the host OS
audio control panel instead of the XVF3610 control interface. The
volumes are initialised to 100% (0dB attenuation) on device power up,
which is the recommended setting.

Ensure that the XVF3610-UA USB Audio input and output volume controls on
the host are set to 100% (no attenuation) to ensure proper operation of
the device. Some host OS (eg. Windows) may store volume setting in
between device connections.

For a comprehensive list of parameters, their data types and an
understanding of their function within the device please consult the
User Guide section relevant to the function of interest, or Appendix A
which summarises all the commands. The control utility can also be used
by supplying the -h argument to the command line. This dumps a list of
commands to the console along with a brief description of the function
of each command. The remainder of this section will cover the generic
operation of the control interface.

Control operation
~~~~~~~~~~~~~~~~~

The control interface works by sending a message from the host to the
control process within the XVF3610 device. The time required to execute
commands can vary, but most will respond within 30ms. Since the commands
are fully acknowledged, by design, the control utility blocks until
completion. This interface is designed to allow real-time tuning and
adjustment but may stall due to bus access or data retrieval.

The control interface consists of two parts a host side application and
the device application. These are briefly summarised below.

Host Application
~~~~~~~~~~~~~~~~

The example host applications, found in the /host directory in the
Release Package, are command-line utilities that accept text commands
and, in the case of a read, provides a text response containing the read
parameter(s). Full acknowledgement is included in the protocol and an
error is returned in the case of the command not being executed properly
or handled correctly by the device.

Example host source code and makefiles for are provided in the release
package for x86 Linux, ARM Linux (Raspberry Pi), Windows and Mac
platforms along with pre-compiled executables to allow fast evaluation
and integration. For more information refer to the *Building the host
utilities from source code* section.

Device Application
~~~~~~~~~~~~~~~~~~

The device is always ready to receive commands. The device includes
command buffering and an asynchronous mechanism which means that
Endpoint 0, NACKing for USB or clock stretching for I2C is not required.
This simplifies the host requirements particularly in the cases where
clock stretching is not supported by the host I2C peripheral.

Configuration via Data Partition
--------------------------------

VocalFusion device flash firmware configuration is comprised of a Boot
image and a Data Partition.

-  The **Boot image** in the form of an .xe archive is the executable
   code. It is provided as part of the XVF3610-UA or XVF3610-INT
   Release Package. This configures the underlying operation of the
   device.

-  The **Data Partition** configures a running Boot image instance at
   startup with a set of commands which are customisable for the
   specific application. This contains any command that can be issued
   at run-time via USB or I\ :sup:`2`\ C, plus some more that are
   boot-time only. Pre-configured Data Partitions are supplied in the
   release packages for default operation.

This combination of Boot image and Data Partition allow the
functionality of the processor to be configured and defined without
requiring any modification or recompilation of base firmware. The
commands discussed in subsequent sections can be stored in the Data
Partition, for execution at startup redefining the default operation of
the device.
