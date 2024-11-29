
class Publisher:
    def __init__(self):
        self.subscribers_SET = set() #list of unique publisher names  .. set=[]

    def register(self, subscriberName):
        self.subscribers_SET.add(subscriberName)

    def unregister(self, subscriberName):
        if subscriberName not in self.subscribers_SET:
            raise ValueError("This name is not subscribed to this service.\n")
        else:
            self.subscribers_SET.remove(subscriberName)

    def dispatch(self, topic):
        for sub in self.subscribers_SET:
            sub.update(topic) # where self == sub for update() method in Subscriber class

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