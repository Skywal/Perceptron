
class Synapse(object):

    def __init__(self, start_weight=0):

        self.weight = start_weight
    
    def set_new_weight(self, weight):
        self.weight = weight
    
    def get_weight(self):
        return self.weight

    def think_process(self, input_data):
        return (self.weight * input_data)