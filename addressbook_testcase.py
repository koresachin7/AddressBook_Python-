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
    id = 11
    addressbook.remove(id)
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
    id = 11
    option = 1
    update_data = "Kapil"

    addressbook.update(id, option, update_data, contact)
    assert contact.name == "Kapil"


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
    id = 11
    option = 2
    update_data = 8888888888

    addressbook.update(id, option, update_data, contact)
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
    id = 11
    option = 3
    update_data = "At Nanded"

    addressbook.update(id, option, update_data, contact)
    assert contact.address == "At Nanded"


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
    id = 11
    option = 4
    update_data = 456789

    addressbook.update(id, option, update_data, contact)
    assert contact.zip == 456789


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
    id = 11
    option = 5
    update_data = "Mumbai"

    addressbook.update(id, option, update_data, contact)
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
    id = 11
    option = 6
    update_data = "Kerala"

    addressbook.update(id, option, update_data, contact)
    assert contact.state == "Kerala"
