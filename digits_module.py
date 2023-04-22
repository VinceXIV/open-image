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
            existing_digits = self.data.loc[self.data["digit"] == digit]
            if(index > len(existing_digits)):
                raise ValueError(
                    '''
                        We only have {count} digits with value {digit} as at now, please pick an index value between 0 and {upper_limit}
                    '''.format(count = len(existing_digits), digit=digit, upper_limit = len(existing_digits) - 1)
                )
            
            return np.array(
                        existing_digits.iloc[index, 1:]
                    ).reshape((28, 28))
        
    def show(self, digit=None):
        if(digit == None):
            plt.imshow(self.digit_array)
        else:
            plt.imshow(self.get_digit_array(digit))