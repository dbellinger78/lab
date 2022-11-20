import pytest
from account import *

class Test:
    def setup_method(self):
        self.one = Account('John')
        self.two = Account('Jane')

    def teardown_method(self):
        del self.one
        del self.two

    def test_init(self):
        self.three = Account('Doug')
        assert self.three.get_name() == 'Doug'
        assert self.three.get_balance() == 0

    def test_deposit(self):    
        assert self.one.deposit(-1.01) is False
        assert self.one.get_balance() == 0
        assert self.one.deposit(-1) is False
        assert self.one.get_balance() == 0
        assert self.two.deposit(0) is False
        assert self.two.get_balance() == 0
        self.two.deposit(2) is True
        assert self.two.get_balance() == pytest.approx(2.0, abs=0.001)
        self.two.deposit(25.05) is True
        assert self.two.get_balance() == pytest.approx(27.05, abs=0.001)

    def test_withdraw(self):    
        assert self.one.withdraw(-1.01) is False
        assert self.one.get_balance() == 0
        assert self.one.withdraw(-1) is False
        assert self.one.get_balance() == 0
        assert self.two.withdraw(0) is False
        assert self.two.get_balance() == 0
        self.two.deposit(25.05) is True
        self.two.withdraw(25.05) is True
        assert self.two.get_balance() == 0
        self.two.deposit(25.05) is True
        self.two.withdraw(2.50) is True
        assert self.two.get_balance() == pytest.approx(22.55, abs=0.001)    
        self.two.withdraw(1) is True
        assert self.two.get_balance() == pytest.approx(21.55, abs=0.001)    

    def test_get_name(self):
        assert self.one.get_name() == 'John'

    def test_get_balance(self):
        assert self.one.get_balance() == 0    


if __name__ == '__main__':
    pytest.main()