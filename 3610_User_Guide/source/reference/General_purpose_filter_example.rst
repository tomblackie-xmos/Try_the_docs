General purpose filter example
==========================================

Worked Example
--------------

Steps in this example:

*  Set the stereo USB output to listen to the stereo USB input (loopback, skipping audio processing pipeline completely)

*  Apply a stereo 500Hz high-pass and 4kHz low-pass cascaded biquad filter

* The 500Hz high-pass filter coefficients are:

     | a1 = -1.90748889
     | a2 = 0.91158173
     | b0 = 0.95476766
     | b1 = -1.90953531
     | b2 = 0.95476766

* The 4kHz low-pass filter coefficients are:

     | a1 = -1.27958194
     | a2 = 0.47753396
     | b0 = 0.04948800
     | b1 = 0.09897601
     | b2 = 0.04948800

* Hear the effect filtered signals when the filters are enabled

This example assumes that the input and output sample rate is 48kHz.

First, connect the USB output to the USB input:

.. code-block:: bash

  vfctrl_usb SET_IO_MAP 0 7 # (USB output left outputs USB input left)
  vfctrl_usb SET_IO_MAP 1 8 # (As above for right channel)

Now configure the filter:

.. code-block:: bash

  vfctrl_usb SET_FILTER_INDEX 2 (USB output left filter)
  vfctrl_usb SET_FILTER_COEFF -1.90748889 0.91158173 0.95476766 -1.90953531 0.95476766 -1.27958194 0.47753396 0.04948800 0.09897601 0.04948800
  vfctrl_usb SET_FILTER_INDEX 3 (USB output right filter)
  vfctrl_usb SET_FILTER_COEFF -1.90748889 0.91158173 0.95476766 -1.90953531 0.95476766 -1.27958194 0.47753396 0.04948800 0.09897601 0.04948800

Now enable the filter:

.. code-block:: bash

  vfctrl_usb SET_FILTER_INDEX 0
  vfctrl_usb SET_FILTER_BYPASS 0
  vfctrl_usb SET_FILTER_INDEX 1
  vfctrl_usb SET_FILTER_BYPASS 0

Play a white noise source from the USB device and record the input. Use
a spectrogram to show the band limited signal due to the effect of the
filters. The effect should also be audible.
