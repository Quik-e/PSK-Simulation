"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Sync Encoder',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        self.row255=0
        self.row0=0
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def work(self, input_items, output_items):
 #       for i in range(0,len(input_items[0])):
 #           output_items[0][i] = input_items[0][i]
 #           if input_items[0][i] == 255 and output_items[0][i-1] == 255 and output_items[0][i-2] == 255:
 #               output_items[0][i] = 1
 #           if input_items[0][i] == 0 and output_items[0][i-1] == 0 and output_items[0][i-2] == 0:
 #               output_items[0][i] = 254
        for i in range(0,len(input_items[0])):
            output_items[0][i]=input_items[0][i]-output_items[0][i-1]/255*170
        return len(output_items[0])
