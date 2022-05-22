

class Transaction:

    class Input:
        def __init__(self, prev_hash, index):
            pass

        def add_signature(self, sig):
            pass

    class Output:

        def __init__(self,  v,  addr):
            pass

    def transaction(self, tx=None):
        pass

    def add_input(self, prev_tx_hash, output_index):
        pass

    def add_output(self, value, address):
        pass

    def remove_input(self, index):
        pass

    def remove_input(self, ut):
        pass

    def get_raw_data_to_sign(self, index):
        pass

    def add_signature(self, signature, index):
        pass

    def get_raw_tx(self):
        pass

    def finalize(self):
        pass

    def set_hash(self, h):
        pass

    def get_hash(self):
        pass

    def get_inputs(self):
        pass

    def get_outputs(self):
        pass

    def get_input(self, index):
        pass

    def get_output(self, index):
        pass

    def num_inputs(self):
        pass

    def num_outputs(self):
        pass
