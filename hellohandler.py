import simx
import message

class HelloHandler(simx.PyService):
    
    def __init__(self,name,person, service_input):
        # do some initialization here
        self.person = person
        
    def recv_HelloMessage(self,msg):    
        self.send_info(Message.ReplyMessage(), 
                       simx.get_min_delay(), 
		       msg.source_id,  
                       HelloHandlerAddress)

    def recv_ReplyMessage(self,msg):
        print "HelloHandler at",
        self.get_entity_id
        "received Reply at"
        self.get_now()
