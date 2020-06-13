import hashlib

class Block:
    def __init__ (self, no, nonce, data, hash, prev):
        self.no = no
        self.nonce = nonce
        self.data = data
        self.hash = hash
        self.prev = prev

    def getStringVal():
        return self.no, self.nonce, self.data, self.hash, self.prev


class MedBlock:
    def __init__(self):
        self.chain = []
        self.prefix = '0000'

    def appendNewBlock(self, data):
        no = (self.chain)
        nonce = 0

        if len(self.chain) == 0:
            prev = '0'
        else:
            prev = self.chain[-1].hashcode

        myHash = hashlib.sha256(str(data).encode('UF-8')).hexdigest()
        block = Block(no, nonce, data, myHash, prev)

        self.chain.append(block)

    def printBlockchain(self):
        chainDict = {}
        for n in range(len(self.chain)):
            chainDict[no] = self.chain[no].getStrignVal()

        print (chainDict)


    def mineChain(self):
        brokenLink = self.checkIfBroken()
        if brokenLink==None:
            pass
        else:
            for block in self.chain[brokerLink.no]:
                print ("Mining Block:" block.getStringVal())
                self.mineBlock(block)

    def mineBlock(self,):
        nonce = 0;
        myHash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()

        while myHash[0:4] == self.prefix:
                myHash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
                nonce = nonce + 1
        else:
            self.chain[block.no] = myHash
            self.chain[block.no].nonce = nonce
            if (block.no<len(self.chain)-1):
            self.chain[block.no]

    def checkIfBroken(self):
        for n in range(len(self.chain)):
            if (self.chain[no].hash[0:4]==self.prefix):
                pass
            else:
                self.chain[no]

    def changeData(self, no, data):
        self.chain[no].data = data
        self.chain[no].hash = hashlib.sha256(str(str(nonce)+str(block.data)).encode('utf-8')).hexdigest()
