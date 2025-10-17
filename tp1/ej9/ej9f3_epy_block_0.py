"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Potencia media',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        prom_cuadratico = np.mean(input_items[0] ** 2)
        prom_vec = np.repeat(prom_cuadratico, len(output_items[0]))
        output_items[0][:] = prom_vec
        return len(output_items[0])
