USB HID - Example using the development kit
=======================================================

Worked example
--------------

An XVF3610 development kit, a Raspberry Pi and a jump wire are required
for this example.

The development kit should be configured as XVF3610-UA. Instructions on
updating the firmware are available in the *Updating the firmware*
section.

.. todo::

  Fix hyperlink to firware update

The development kit should then be connected to a Raspberry Pi and set
up according to the development kit setup guide. Extract the Raspberry
Pi host utilities from the release package, and use them to enable
interrupts like so:

.. code-block:: text

  vfctrl_usb.exe SET_GPI_INT_CONFIG 0 0 3

The HID events can be observed on ``/dev/input/event0`` on the Raspberry Pi
either directly (eg ``xxd``) or using the ``evtest`` utility (normally available
through APT on Raspbian).

``event0`` will be the correct HID device is most cases. If the test system
has additional sources of events, the correct one can be identified
under ``/dev/input`` by looking at the ``Handlers`` line in the output of
``/proc/bus/input/devices``.

Now toggle INT_N signal on the XK-VF3610 board by connecting it to 3V3
and GND using a jump wire. Example output from ``evtest`` is:

.. code-block:: text

  Input driver version is 1.0.1
  Input device ID: bus 0x3 vendor 0x20b1 product 0x14 version 0x110
  Input device name: "XMOS XVF3610 (UAC1.0) Adaptive"
  Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
  Event code 128 (KEY_STOP)
  Event code 193 (KEY_F23)
  Event code 194 (KEY_F24)
  Event code 217 (KEY_SEARCH)
  Event type 4 (EV_MSC)
  Event code 4 (MSC_SCAN)
  Key repeat handling:
  Repeat type 20 (EV_REP)
  Repeat code 0 (REP_DELAY)
  Value 250
  Repeat code 1 (REP_PERIOD)
  Value 33
  Properties:
  Testing ... (interrupt to exit)
  Event: time 1586524983.094859, type 4 (EV_MSC), code 4 (MSC_SCAN), value 70072
  Event: time 1586524983.094859, type 1 (EV_KEY), code 193 (KEY_F23), value 1
  Event: time 1586524983.094859, -------------- SYN_REPORT ------------
  Event: time 1586524983.353655, type 1 (EV_KEY), code 193 (KEY_F23), value 2
  Event: time 1586524983.353655, -------------- SYN_REPORT ------------
  Event: time 1586524983.403671, type 1 (EV_KEY), code 193 (KEY_F23), value 2
  Event: time 1586524983.403671, -------------- SYN_REPORT ------------
  Event: time 1586524983.453659, type 1 (EV_KEY), code 193 (KEY_F23), value 2
  Event: time 1586524983.453659, -------------- SYN_REPORT ------------
