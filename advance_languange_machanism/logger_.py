from dataclasses import make_dataclass


try:
    import datetime
    import os
    import sys
    import sys
    import logging
except Exception as e:
    print("Some Modules are Missing {}".format(e))

    
    
    
class Meta(type):
    """Meta Class"""
    def __call__(cls, *args, **kwargs):
        instance = super(Meta, cls).__call__(*args, **kwargs)
        return instance
    
    def __init__(cls, name, base, attr):
        super(Meta, cls).__init__(name, base, attr)
        
    
    
class log(object):
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        
        """wrapper function"""
        start = datetime.datetime.now()   #start time
        Tem = self.func(self,*args, **kwargs)  #call function
        FunName = self.func.__name__      #get function
        end = datetime.datetime.now()     #end time
        
        
        message = """
        Function : {}
        Execution Time : {}
        Address : {}
        Memory : {} Bytes
        Date : {}
        """.format(FunName,
                  end-start,
                  self.func.__name__,
                  sys.getsizeof(self.func),
                  start)
        cwd = os.getcwd()
        folder = 'Logs'
        newPath = os.path.join(cwd, folder)
        
        try:
            """ try to create a folder"""
            os.mkdir(newPath)
        except:
            """Directory already exist"""
            logging.basicConfig(filename = '{}/log.log'.format(newPath), level = logging.DEBUG)
            logging.debug(message)
        return Tem
    
    
class Test(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        pass
    
    @log
    def methodA(self):
        print("Hello")
        return "1111"
if __name__ == "__main__":
    obj = Test()
    print(obj.methodA())
        
        
