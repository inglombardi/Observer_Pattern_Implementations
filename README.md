# Observer_Pattern_Implementations

The observer pattern is useful for state monitoring and event handling situations. This pattern allows a given 
object to be monitored by an unknown and dynamic group of "observer" objects. Whenever a value on the 
core object changes, it lets all the observer objects know that a change has occurred, by calling an update() 
method (typically). 
The idea is that you have an object, the observable or publisher, and a group of other objects (observers or 
subscribers) that want to be notified when the (inner state of the) observable changes. The observed object 
must maintain a list of observers and must warn them of the changes. Each observer may be responsible for 
different tasks whenever the observable object changes; the core object doesn't know or care what those 
tasks are, and the observers don't typically know or care what other observers are doing. 
Publisher is the observed object [publisher] while Bob, Alice and John are the observers [subscribers].  
• bob, alice and john are interested on the state of the publisher.  
• When the publisher changes its state, it send a message to all the interested observer using the method 
dispatch(). (Here we simulate the action calling the publisher.dispatch('message') method.)  
• bob, alice and john receive the message. 
• john is no more interested on the object publisher  
• The next time that the publisher calls the dispatch('message') method, the messge is received only by bob 
and alice.

