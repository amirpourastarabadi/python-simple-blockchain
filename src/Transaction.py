

class Transaction:

    class Input:
        def __init__(self, prev_hash, index):
            pass

        def add_signature(self, sig):
            pass

    class Output:

        def __init__(self,  value,  public_key_address):
            pass

    def transaction(self, tx=None):
        pass

    def add_input(self, prev_transaction_hash, output_index):
        pass

    def add_output(self, value, pubic_key_address):
        pass

    def remove_input_by_index(self, index):
        pass

    def remove_input_by_UTXO(self, utxo):
        pass

    def get_raw_data_to_sign(self, index):
        pass

    def add_signature(self, signature, index):
        pass

    def get_raw_transaction(self):
        pass

    def finalize(self):
        pass

    def set_hash(self, hash):
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

    def inputs_length(self):
        pass

    def outputs_length(self):
        pass
