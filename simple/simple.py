def id_ages() -> list:
    """
    Returns a list of dictionaries with id and ages

    >>> type(id_ages())
    <class 'list'>

    >>> len(id_ages())
    10

    """
    import random


    list_ages = []

    for id in range(10):
        dicc = {}
        dicc['id'] = id
        dicc['age'] = random.randint(1,100)
        list_ages.append(dicc)

    return list_ages


def sort_by_ages(list_ages: list) -> list:
    """
    param: list of dictionaries with id and ages
    Prints the youngest and oldest ID.
    Returns a list ordered from oldest to youngest

    >>> sort_by_ages([{'id': 7, 'age': 89},{'id': 6, 'age': 26}])
    Youngest person ID: 6
    Oldest person ID: 7
    [{'id': 7, 'age': 89}, {'id': 6, 'age': 26}]

    >>> sort_by_ages([{'id': 1, 'age': 1},{'id': 2, 'age': 2}])
    Youngest person ID: 1
    Oldest person ID: 2
    [{'id': 2, 'age': 2}, {'id': 1, 'age': 1}]

    >>> sort_by_ages("string")
    Traceback (most recent call last):
        ...
    ValueError: list_ages must be a list

    """
    if type(list_ages) != list:
        raise ValueError('list_ages must be a list')

    sorted_list = sorted(list_ages, key = lambda x: x['age'], reverse = True)

    print("Youngest person ID:", sorted_list[-1]['id'])
    print("Oldest person ID:", sorted_list[0]['id'])

    return sorted_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
