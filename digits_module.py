import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Digit:
    def __init__(self, digit=0, index=0):
        self.data = pd.read_csv("./sample-data/mnist.csv")
        self.digit_array = self.get_digit_array(digit, index)     

    def get_digit_array(self, digit=None, index=0):
        if(digit == None):
            return self.digit_array
        elif digit < 0 or digit > 9:
            raise ValueError(
                "Expected a value between 0 - 9. You provided " + str(digit)
            )
        else:
            return np.array(
                        self.data.loc[self.data["digit"] == digit].iloc[index, 1:]
                    ).reshape((28, 28))
        
    def show(self, digit=None):
        if(digit == None):
            plt.imshow(self.digit_array)
        else:
            plt.imshow(self.get_digit_array(digit))