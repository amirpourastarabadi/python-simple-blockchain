

class Transaction:

    class Input:
        def __init__(self, prevHash, index):
            pass

        def addSignature(self, sig):
            pass


    class Output:

        def __init__(self,  v,  addr):
            pass

    def Transaction(self, tx=None):
        pass


    def  addInput(self, prevTxHash, outputIndex):
        pass

    def  addOutput(self, value, address):
        pass

    def  removeInput(self, index):
        pass

    def removeInput(self,  ut):
        pass

    def getRawDataToSign(self, index):
        pass

    def addSignature(self, signature, index):
        pass


    def getRawTx(self):
        pass

    def finalize(self):
        pass

    def setHash(self, h):
        pass

    def getHash(self):
        pass

    def getInputs(self):
        pass

    def getOutputs(self):
        pass

    def getInput(self, index):
        pass

    def getOutput(self, index):
        pass

    def numInputs(self ):
        pass

    def numOutputs(self):
        pass