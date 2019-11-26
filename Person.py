class Person:
    # Instance Variables
    _name = ''
    _address = ''

    # Constructor =============================================================
    def __init__(self, name, address):
        self._name = name
        self.address = address

    # Setters ==================================================================
    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    # Getters ==================================================================
    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    # Destructor =============================================================
    # def __del__(self):
    # print('I have been deleted.')
