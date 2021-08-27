
Principles of configuration, control and usage
==============================================

The XVF3610 is intended to be used to provide Far-Field voice to a host
system or processor in speech recognition and communication
applications, either closely integrated to the main processor or as a
USB accessory. As such the XVF3610 provides boot mechanisms from either
an external QSPI flash or by the host processor over SPI interface.

To facilitate control in both boot configurations and to allow the
specification of the default behaviour, the XVF3610 implements two
mechanisms for control and parameterisation. The first is the Control
Interface which is a direct connection between the host and the XVF3610
and is operational at runtime. The second is the Data Partition which is
held in flash and contains configuration data to parameterise the
XVF3610 on boot up. Both mechanisms have access to the full set of
parameters and can both be used in the application to control and
specify the behaviour of the device.

A host tool (vfctrl) is also provided provides command-line access to
the control interface, allowing user access to all the configuration
parameters of the XVF3610.

The following sections describe the following aspects of usage,
configuration and control:

-  Firmware release package

-  XTC Tools

-  vfctrl host command line tool

-  Configuration via a control interface

-  Configuration via the Data Partition

-  XVF3610 Development kit usage
