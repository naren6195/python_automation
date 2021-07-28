import os
import pytest
import math
import logging
'''
print(os.getcwd())
logging.basicConfig(filename="mylog1.log"
                    ,format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("***********************************Test1**************************")
'''
@pytest.fixture()
def number(self,int=25):
    self.int=int
    return self.int

def square_root(num):
    assert math.sqrt(num)==5


