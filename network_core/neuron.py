
class Neuron(object):

    def __init__(self, start_weight=0):

        self.weight = start_weight
        self.calculation_res = 0
    
    def set_new_weight(self, weight):
        self.weight = weight
    
    def get_weight(self):
        return self.weight

    def calculate(self, input_data):
        self.calculation_res = think_process(input_data)

    def think_process(self, input_data):
        return (self.weight * input_data)