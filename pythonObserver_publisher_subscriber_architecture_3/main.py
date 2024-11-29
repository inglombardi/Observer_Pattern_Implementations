class Publisher:

    """ ==> NEW REQUIREMENT :

    Observing EVENTS - How to implement Subscriber and Publisher:
    Subscriber has a method that receives a message from the publisher and prints it.
    Publisher has
    • a dictionary attribute subscribes with:
    • key: an event
    • value: a dictionary that contains subscribers and their methods.
    • register() and unregister() methods that add and remove subscribers from the publisher's dictionary,
    for the ********* specific event only *********** .
    • Publisher has a dispatch() method that send a message to all the subscribers in the sub-dictionary of
    that specific event, using the appropriate method.

    """

    counter = 0

    def __init__(self, events):
        """ There is a key for each event in the publisher dictionary.
        Each key (event) is a dictionary containing subscribers to this event represented by the callbacks."""
        # The constructor accepts in input a list of events
        # __init__ uses this list to initialize a dictionary
        self.subscribers = {event: dict() for event in events} # "dict_comprehension"
        #subscribers_SET = {
        # 'event1' : callback1
        # ....
        # 'eventk' : callback12
        # ...
        # 'eventN' : callback5
        # }



    def get_subscribers(self, single_event):
        return self.subscribers[single_event] # it returns the specific dict for a specific event !

    def register(self, event, subscriberName, callback=None):
        """
        :param callback: reference to the wanted method
        :param event: reference to a specific event
        """
        default_method = 'update'
        if callback is None:
            # call the default method
            callback = getattr(subscriberName,default_method)
            """Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
            When a default argument is given, it is returned when the attribute doesn't
            exist; without it, an exception is raised in that case."""
        #self.subscribers_SET.add(subscriberName)
        self.get_subscribers(event)[subscriberName] = callback # Adding elements one at a time => access through key

    def unregister(self, event_k, subscriberName):
        if subscriberName not in self.get_subscribers(event_k):
            raise ValueError("This name is not subscribed to this service.\n")
        else:
            del self.get_subscribers(event_k)[subscriberName]


    def dispatch(self, event, topic):
        print("STEP #"+str(self.counter))
        for sub, callback in self.get_subscribers(event).items(): #items() – Returns a list containing a tuple for each key value pair
            callback(topic) # where self == sub for update() or receive() method in Subscriber class according to the subscribe type
        self.counter += 1


############### these classes are exactly the same respect to pythonObserver_publisher_subscriber_architecture_3 #########

class Subscriber1stType: #subscriber_one
    def __init__(self, name):
        self.name = name

    def update(self, topic): # send_message()
        print("[SUBSCRIBER,",self.name,"] : (update method) I'm received the message ==> ",topic,"\n")


class Subscriber2ndType: #subscriber_two
    def __init__(self, name):
        self.name = name

    def receive(self, topic): # send_message()
        print("[SUBSCRIBER,",self.name,"] : (receive method) I'm received the message ==> ",topic,"\n")



if __name__ == "__main__":
    # possible events are ('lunch', 'happyhour')
    publisher = Publisher(['lunch', 'happyhour'])


    bob = Subscriber1stType('Bob')  # an observer => ** update method **
    alice = Subscriber1stType('Alice')  # an observer => ** update method **
    john = Subscriber2ndType('John')  # an observer  => ** receive method **


    # register( name_event , subscriber_name, callback = None )

    publisher.register('lunch', bob)  # explicitly uses the 'update()' method : bob.update is not a string but a REFERENCE to the method
    publisher.register('happyhour', alice)  # implicitly uses the 'update()' method
    publisher.register('lunch', john, john.receive)  # explicitly uses the 'receive()' method

    # send a message
    print('\nLUNCHTIME!')
    publisher.dispatch('lunch', 'Lunchtime!')  # event, message
    print('\nHAPPYHOUR!')
    publisher.dispatch('happyhour', 'HAPPY HOUR!')  # event, message

    print("\nNow  john is no longer interested in event 'happyhour'")
    print("but he remains interested in event 'lunch'\n")

    #publisher.unregister('happyhour', john) # OK !!

    # send a message
    print('\nLUNCHTIME!')
    publisher.dispatch('lunch', 'Lunchtime!')  # event, message
    print('\nHAPPYHOUR!')
    publisher.dispatch('happyhour', 'HAPPY HOUR!')  # event, message