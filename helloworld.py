import simx
from Person import *
from HelloHandler import *

# initialize
simx.init("helloworld")
simx.set_end_time(1024)
simx.set_min_delay(1)
simx.init_env()

# create Persons
person_list = []
num_persons = 1024
for i in xrange(num_persons):
    simx.create_entity(('p',i), Person)
    person_list.append(('p',i))

#schedule events
for evt_time in range(1,end_time):
    hello_rcvr = random.choice(person_list)
    reply_rcvr = random.choice(person_list)
    simx.schedule_event(evt_time, hello_rcvr, eAddr_HelloHandlerPerson,
                        HelloMessage(source_id=reply_rcvr))

#Run the simulation
simx.run()
