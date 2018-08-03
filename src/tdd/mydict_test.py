import unittest

from tdd.mydict import Dict

#TODO 报错

#测试类，从unittest.TestCase继承
class TestDict(unittest.TestCase):
    
    #以test开头的方法就是测试方法
    def test_init(self):
        d=Dict(a=1,b='test')
        #print(d)
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d, Dict))
        
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        #期待抛出指定类型的Error
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
            
if __name__ == '__main__':
    unittest.main()