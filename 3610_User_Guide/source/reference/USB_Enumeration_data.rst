USB enumeration
===========================

The XVF3610 includes a Human Interface Device (HID) endpoint to enable
the XVF3610 to signal interrupts caused by GPIO events. The table below
shows how the XVF3610 HID appears on Windows using `USB
view <https://www.nirsoft.net/utils/usb_devices_view.html>`__.


.. csv-table:: USB HID Endpoint
    :file: USB-HID Endpoint.csv
    :widths: auto
    :header-rows: 1





During USB enumeration, the XVF3610 HID produces three descriptors. The
listing below shows them as recorded on Windows using `USB
View <https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/usbview>`__.
For details of the structure and meaning of these descriptors, see the
`USB Specification
v2.0 <https://www.usb.org/document-library/usb-20-specification>`__
sections 9.6.5 and 9.6.6 and the `Device Class Definition for Human
Interface Devices (HID)
v1.11 <https://www.usb.org/document-library/device-class-definition-hid-111>`__
section 6.2.1.



.. code-block:: text

  ===>Interface Descriptor<===
  bLength: 0x09
  bDescriptorType: 0x04
  bInterfaceNumber: 0x04
  bAlternateSetting: 0x00
  bNumEndpoints: 0x01
  bInterfaceClass: 0x03 -> HID Interface Class
  bInterfaceSubClass: 0x00
  bInterfaceProtocol: 0x00
  iInterface: 0x00
  ===>HID Descriptor<===
  bLength: 0x09
  bDescriptorType: 0x21
  bcdHID: 0x0110
  bCountryCode: 0x00
  bNumDescriptors: 0x01
  bDescriptorType: 0x22 (Report Descriptor)
  wDescriptorLength: 0x002B
  ===>Endpoint Descriptor<===
  bLength: 0x07
  bDescriptorType: 0x05
  bEndpointAddress: 0x82 -> Direction: IN - EndpointID: 2
  bmAttributes: 0x03 -> Interrupt Transfer Type
  wMaxPacketSize: 0x0040 = 0x40 bytes
  bInterval: 0x08
