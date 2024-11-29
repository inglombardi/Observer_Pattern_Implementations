
class Publisher:

    """ ==> NEW REQUIREMENT : The subscriber can specify not only
    "I want to be notified when this interesting event happens"
    but also
    "I want you to notify me in this specific way, that is, using this specific method"
    For example, we can have
    • bob and alice (SubscriberOne) with method update()
    • john (SubscriberTwo) with method receive()

    publisher=Publisher()

    bob=SubscriberOne('Bob')  #update
    alice=SubscriberOne('Alice') #update

    john=SubscriberTwo('John') #receive

    # explicitly uses the 'update()' method
    publisher.register(bob, bob.update)
    # implicitly uses the 'update()' method
    publisher.register(alice)
    # explicitly uses the 'receive()' method
    publisher.register(john, john.receive)

    # send a message
    publisher.dispatch('Lunchtime!')
    publisher.unregister(john)
    publisher.dispatch('Happy hour!')

    # send a message
    publisher.dispatch('Lunchtime!')
    # Bob received the message **Lunchtime!**
    # John received the message **Lunchtime!**
    # Alice received the message **Lunchtime!**
    publisher.unregister(john)
    publisher.dispatch('Happy hour!')
    # Bob received the message **Happy hour!**
    # Alice received the message **Happy hour!**


    """

    counter = 0

    def __init__(self):
        """ Why now does publisher have a dict instead of set ?? Because the same "name" of two different
        person could be subscribed in both tipologies of subscriber e.g. Nicola Lombardi and Nicola Salaris"""
        self.subscribers_SET = dict() #list of unique publisher names  .. set=[]
        # key : an_observer_name ==========================> name
        # value : subscriber_method (update or receive ) ==> callback
        #subscribers_SET = {
        # 'Nicola' : callback1
        # ....
        # 'Nicola' : callback12
        # ...
        # 'Ilaria' : callback5
        # }

    def register(self, subscriberName, callback=None):
        """
        :param callback: reference to the wanted method
        """
        default_method = 'update'
        if callback is None:
            # call the default method
            callback = getattr(subscriberName,default_method)
        #self.subscribers_SET.add(subscriberName)
        self.subscribers_SET[subscriberName] = callback # Adding elements one at a time => access through key

    def unregister(self, subscriberName):
        if subscriberName not in self.subscribers_SET:
            raise ValueError("This name is not subscribed to this service.\n")
        else:
            del self.subscribers_SET[subscriberName]

    def dispatch(self, topic):
        print("STEP #"+str(self.counter))
        for sub, callback in self.subscribers_SET.items(): #items() – Returns a list containing a tuple for each key value pair
            callback(topic) # where self == sub for update() or receive() method in Subscriber class according to the subscribe type
        self.counter += 1




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
    publisher = Publisher()  # the observed object
    bob = Subscriber1stType('Bob')  # an observer => ** update method **
    alice = Subscriber1stType('Alice')  # an observer => ** update method **
    john = Subscriber2ndType('John')  # an observer  => ** receive method **

    publisher.register(bob, bob.update)  # explicitly uses the 'update()' method : bob.update is not a string but a REFERENCE to the method
    publisher.register(alice)  # implicitly uses the 'update()' method
    publisher.register(john, john.receive)  # explicitly uses the 'receive()' method

    # send a message
    publisher.dispatch('new marvel comics movie!')
    # Bob received the message **Lunchtime!**
    # John received the message **Lunchtime!**
    # Alice received the message **Lunchtime!**
    print("Now Publisher discards John's registration and the new list of receivers: \n")
    publisher.unregister(john)
    publisher.dispatch('Happy hour!')
