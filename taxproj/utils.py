'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
class ParamHelper(object):
    
    @staticmethod
    def isBlank(param, message):
        assert(param != None and param != ""), message
    
    @staticmethod
    def isNull(param, message):
        assert(param != None), message