
class Publisher:

    """ ==> NEW REQUIREMENT : The subscriber specify :

    "I want to be notified when this interesting event happens"     """

    counter = 0

    def __init__(self):
        self.subscribers_SET = set() #list of unique publisher names  .. set=[]
        self._value = 0 # shared to change with a rule ( it must be greater or equal to 0)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if v >= 0 and v != self.value:  # admission control
            self._value = v
            self.dispatch("The value of <value> parameter has changed into " + str( self.value ) )
        elif v == self.value:
            self.dispatch('No news for the moment')
        else:
            #raise ValueError("This resource is not acceptable less than 0 to this service.\n")
            print("This resource is not acceptable less than 0 to this service.\n")


    def register(self, subscriberName):
        self.subscribers_SET.add(subscriberName)

    def unregister(self, subscriberName):
        if subscriberName not in self.subscribers_SET:
            raise ValueError("This name is not subscribed to this service.\n")
        else:
            self.subscribers_SET.remove(subscriberName)

    def dispatch(self, topic):
        print("STEP #"+str(self.counter))
        for sub in self.subscribers_SET:
            sub.update(topic) # where self == sub for update() method in Subscriber class
        self.counter += 1




class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, topic): # send_message()
        print("[SUBSCRIBER,",self.name,"] : I'm received the message ==> ",topic,"\n")


if __name__ == "__main__":
    publisher = Publisher()  # the observed object
    bob = Subscriber('Bob')  # an observer
    alice = Subscriber('Alice')  # an observer
    john = Subscriber('John')  # an observer
    # add the subscribers (bob, alice, john)
    # to the the subscribers' set of the Publisher
    publisher.register(bob)
    publisher.register(alice)
    publisher.register(john)
    # send a message
    publisher.dispatch('new marvel comics movie!')
    # Bob received the message **Lunchtime!**
    # John received the message **Lunchtime!**
    # Alice received the message **Lunchtime!**
    print("Now Publisher discards John's registration and the new list of receivers: \n")
    publisher.unregister(john)
    publisher.dispatch('Happy hour!')
    # Bob received the message **Happy hour!**
    # Alice received the message **Happy hour!**

    # setter method of the publisher  ===> REMEMBER THIS SINTAX
    publisher.value = 5
    publisher.value = 10
    publisher.value = 10
    # getter method of the subscriber
    print(publisher.value)

    publisher.value = -0.10

    for el in publisher.subscribers_SET:
        publisher.unregister(el)

    print("-------------")
    publisher.dispatch("bye") # no output because there is nobody
