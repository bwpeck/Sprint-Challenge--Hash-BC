#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:

        hash_table_insert(hashtable, ticket.source, ticket.destination)

    key = 'NONE'
    index = 0
    while hash_table_retrieve(hashtable, key) != 'NONE':
        print(hash_table_retrieve(hashtable, key))
        route[index] = hash_table_retrieve(hashtable, key)
        print('route', route)
        index += 1
        key = hash_table_retrieve(hashtable, key)
    else:
        route[index] = hash_table_retrieve(hashtable, key)
    return route