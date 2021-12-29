from addressbook import AddressBook, Contact


def test_add_detail():
    """
    Description:
               Test add_detail method using object and list
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    assert len(addressbook.person_list) > 0


def test_remove():
    """
    Description:
               Test remove method using list in for loop
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    for delete in addressbook.person_list:
        if delete.id == 11:
            del addressbook.person_list[0]
    assert len(addressbook.person_list) == 0


def test_name_update():
    """
    Description:
                Test update method name
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    contact.name = "kapil"
    assert contact.name == "kapil"


def test_mobile_update():
    """
    Description:
                Test update method mobile number
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    contact.mobile = 8888888888
    assert contact.mobile == 8888888888


def test_address_update():
    """
    Description:
                Test update method address
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    contact.address = "At nanded"
    assert contact.address == "At nanded"


def test_zip_update():
    """
    Description:
                Test update method zip code
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    contact.zip = 654321
    assert contact.zip == 654321


def test_city_update():
    """
    Description:
                Test update method city name
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    contact.city = "Mumbai"
    assert contact.city == "Mumbai"


def test_state_update():
    """
    Description:
                Test update method state name
    """
    addressbook = AddressBook()
    add_new = {"id": 11, "name": "Sachin", "mobile": 9999999999, "address": "At hinjewadi", "zip": 123456,
               "city": "pune",
               "state": "MH"}
    contact = Contact(add_new)
    addressbook.add_detail(contact)
    contact.state = "kerala"
    assert contact.state == "kerala"
