import neuron as nr

import database as db

""" Bias neuron located the end of the neurons sequence """
class NeuralNetwork(object):

    def __init__(self, neurons=1, stat_weight=0, learning_rate=1.0, max_error=.0):

        # initialize a list of neurons with weight 0 in count of neurons var
        # last neuron in the list is bias (always presents)
        self.neurons = [nr.Neuron(start_weight=stat_weight) for i in range(neurons+1)]

        self.learning_rate = learning_rate # maximal learning rate 
        self.max_error = max_error # maximal error at epoch

        self.adder_res = 0 # result of adding weight-multiply-data process
        self.activation_res = 0 # result of activation function
        self.curr_error = 0 # error at current learning epoch


    def get_neurons(self):
        return self.neurons
    
    def adder(self, input_list=[0]):
        """ Adding all rezults of neurons work plus bias"""
        summ = 0

        for neu, data in zip(self.neurons, input_list):
            summ = summ + neu.think_process(data)

        # bias neuron
        summ = summ + self.neurons[len(self.neurons)-1].think_process(1)

        return summ

    def adder_process(self, input_list=[0]):
        
        self.adder_res = self.adder(input_list=input_list)

    def heviside_activation(self):
        """ Heviside function implementation """

        if self.adder_res >= 0:
            self.activation_res = 1
        else:
            self.activation_res = 0
    

    def fit(self, input_data, output_signal):

        self.fit_weights(input_data=input_data, output_signal=output_signal)
        self.fit_bias(out_sig=output_signal)

    def fit_bias(self, out_sig):
        """ Adjusting bias neuron weight"""

        return self.neurons[-1].get_weight() + self.learning_rate * (out_sig - self.activation_res)

    def fit_weights(self, input_data, output_signal):
        """ 
        input_data - data for single neuron 
        output_signal - corresponding signal for input data vector  aka d (last in the local file data 'example1.csv')
        """
        # last one is bias and it's calculated in separate way
        for i in range(len(self.neurons)-1):

            new_w = self.neurons[i].get_weight() + self.learning_rate * (output_signal - self.activation_res) * input_data[i]
            self.neurons[i].set_new_weight(new_w)
        
        # calculate bias weight
        bias = self.fit_bias(output_signal)
        self.neurons[-1].set_new_weight(bias)

    def train_network(self, train_data, epochs=100):
        curr_ep = 1

        while curr_ep < epochs:
            self.curr_error = 0

            for i in range(len(train_data)):
                data_list = list(train_data[i][:-1])
                output_signal = int(train_data[i][-1])

                data_list = [float(i) for i in data_list]
                
                self.adder_process(data_list)
                self.heviside_activation()
                
                self.fit(data_list, output_signal)

                self.error_calc(output_signal)

            print(f"Current error is {self.curr_error}")
            
            if self.curr_error <= self.max_error:
                print(f"Optemal weights were found after {curr_ep} epochs.")
                break

            curr_ep = curr_ep + 1

    def error_calc(self, out_sig):
        self.curr_error = self.curr_error + abs(out_sig - self.activation_res)


if __name__ == "__main__":
    neural = NeuralNetwork(neurons=2)

    database = db.Database()
    database.read_csv("D:/PROJECTS/LABKI/Perceptron/example/sample2.csv")

    neural.train_network(database.get_data(), epochs=100)
    
    for i in neural.get_neurons():
        print(f"neuron num has weight {i.get_weight()}")
