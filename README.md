# making-music-from-images

This is a little Python project I made where I convert images into music.

The conversion process takes an image and converts it into HSV color space. Then the Hue channel is mapped to a note on a scale which can be associated with a frequency and thus a sound. The results are pretty cool!

The pixels used to construct can be either selected in order (top left and moving across the width, row by row) or chosen at random.

A wide variety of scales are coded in that define the frequencies to match every pixel color to.

Harmonies can also be readily created by specifying the desired intervals (i.e., perfect fifth, minor third, etc.).

The files can be placed into 1D or 2D numpy arrays which can then be exported as .wav files which can be listened to.

The pedalboard module from Spotify can be used to add a variety of sound processing effects like reverb, delay and distortion to the songs made from the images.

A few example song outputs and the associated images are included here.

