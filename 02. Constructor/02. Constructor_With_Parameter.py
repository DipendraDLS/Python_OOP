

class Mobile:
    # Constructor is automatically called whenever the object is created. 
    def __init__(self, m):  # Here 'm' is the formal argument or formal parameter.
        self.model = m
        
        print("Self Calling Constructor.")
        print("Model: ", self.model)


obj_1 = Mobile("Redmi Note 5 Pro")  # yaha pass gareko kura chai actual argument or actual paramete huncha .


