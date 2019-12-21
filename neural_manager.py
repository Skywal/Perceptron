from network_core import neuron

import database as db

class NetManager(object):
    def __init__(self, database, synapses=0, stat_weight=0, learning_rate=1, max_error=.0):

        self.database = []
        self.trans_to_fl(database)

        self.neuron = neuron.Neuron(synapses=synapses, stat_weight=stat_weight, 
                                    learning_rate=learning_rate, max_error=max_error)
        self.train_history = []

        self.epochs_passed = 0

        self.optimal_error = 0
        self.optimal_epochs = 0
        self.optimal_weights = []
    
    def cut_data(self, row = 0):
        """Return list of all column in a row except last one and return value in the last column as separate var"""
        d_list = list(self.database[row][:-1]) # cut all columns before last from database            
        out_sig = int(self.database[row][-1]) # get value from the last column
        
        return d_list, out_sig

    def neuron_act(self, input_data):
        self.neuron.adder_process(input_data)
        self.neuron.heviside_activation()

    def form_history_line(self, neuron_weights, current_error, epoch):
        """ Form one line of train history log in format
            [n_w1, n_w2, ... , n_w3, cur_err, epoch]
        """
        line = list(neuron_weights)
        line.append(current_error)
        line.append(epoch)

        return line

    def write_history(self, neuron_w, curr_err, epoch):
        self.train_history.append(self.form_history_line(neuron_w, curr_err, epoch))
    
    def trans_to_fl(self, database):
        """ Transform all data from database input into float nums """
        for i in database:
            self.database.append([float(j) for j in i])

    def get_epochs_passed(self):
        return self.epochs_passed

    def get_error(self):
        return self.optimal_error

    def get_optimal_weights(self):
        return self.optimal_weights
    
    def get_opt_epochs(self):
        return self.optimal_epochs

    def reverse_weights(self):
        w = list()
        n_weights = self.optimal_weights

        for i in range(len(n_weights)-1, -1, -1 ):
            w.append(n_weights[i])
        
        return w

    def predict_2d(self, arr_x1):
        """Make prediction about arr_x2 on base of arr_x1. Works only for two dimensions"""
        arr_x2 = [] # result
        
        w = self.reverse_weights()

        for i in arr_x1:
            equation = (-1) * ((w[1] * i)/w[-1]) - (w[0] / w[-1])
            arr_x2.append(equation)
        
        return arr_x2

    def train_network(self, epochs=0):
        curr_ep = 0
        
        while curr_ep < epochs:
            
            self.neuron.curr_error = 0

            for i in range(len(self.database)):
                data_list, output_signal = self.cut_data(i)

                self.neuron_act(data_list)
                
                self.neuron.fit_weights(input_data=data_list, output_signal=output_signal)

                self.neuron.error_calc(output_signal)
            
            self.write_history(self.neuron.get_weights(), self.neuron.curr_error, curr_ep)
            
            if self.neuron.curr_error <= self.neuron.max_error:
                self.optimal_error = self.neuron.curr_error
                self.epochs_passed = curr_ep

                print(f"Optimal weights were found after {curr_ep} epochs.")
                break
            
            curr_ep = curr_ep + 1
        
        self.epochs_passed = curr_ep

        self.set_up_opimal_val()
        #print(f"Epochs {curr_ep}")
    
    def set_up_opimal_val(self):
        
        l = self.find_optimal_values()

        self.optimal_error = l[-2]
        self.optimal_epochs = l[-1]
        self.optimal_weights = l[:-2]

    def find_optimal_values(self):
        """ Find optimal values of neuron weights
        Return result in format [w_n, ..., w_1, w_0, error, epoch]
        """
        temp_l = []
        for i in self.train_history:
            temp_l.append(i[-2:-1])
        
        min_val = min(temp_l)
        index_min = temp_l.index(min_val)

        return list(self.train_history[index_min])

if __name__ == "__main__":

    database = db.Database()
    database.read_csv("D:/PROJECTS/LABKI/Perceptron/example/sample3.csv")
    
    net_manager = NetManager(database=database.get_data(), synapses=3, max_error=0)
    
    net_manager.train_network(epochs=1000)
    '''
    print(net_manager.find_optimal_values())
    print("All epochs", net_manager.get_epochs_passed())
    print("Error ", net_manager.get_error())
    print("Opt epochs ", net_manager.get_opt_epochs())
    print("Opt weights ", net_manager.get_optimal_weights())
    print(" ")
    '''
    ep = 967
    print(f"{ep}  w0={net_manager.train_history[ep][2]} w1={net_manager.train_history[ep][1]} w3={net_manager.train_history[ep][0]}")
    print(f"{ep} {net_manager.train_history[ep]}")
    for i in net_manager.neuron.get_synapses():
        print(f"neuron num has weight {i.get_weight()}")