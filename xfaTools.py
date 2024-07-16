import pypdf
class XfaObj(dict):
    def __init__(self, sourcePdf):
        self.source = sourcePdf
        self.xfaDict = self.source.xfa
        
        #this next line is way more important/useful than it appears!
        # it makes someone able to treat an XfaObj as a dict pretty much.
        super(XfaObj,self).__init__(self.xfaDict)
        
    def __getitem__(self,key):
        if(isinstance(self.xfaDict[key],bytes)):
            return self.xfaDict[key].decode('utf-8')
        else:
            print('xfa item detected was not a stream')
            return self.xfaDict[key]

    def __setitem__(self,key,value):
        if(isinstance(value,str)):
            value = bytes(value,'utf-8')
        self.xfaDict[key] = value