import sys, os

PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../"
print(PROJECT_ROOT_DIR)
sys.path.append(PROJECT_ROOT_DIR)
import pandas as pd
import csv
import os


def tradebook_generator(filename):
    leverage = 5
    df = pd.read_csv(f"{os.path.dirname(os.path.realpath(__file__))}/../output/orderbooks/{filename}.csv", header = None)
    profit_and_loss = []
    entry_time = []
    entry_price = []
    entry_type = []
    exit_time = []
    exit_price = []
    exit_type = []
    quantity = []
    profit_and_loss_percent = []
    for i in range(0, len(df.index), 2):
        entry_trade = df.iloc[i].values
        exit_trade = df.iloc[i + 1].values
        quantity.append(entry_trade[3])
        entry_time.append(f'{entry_trade[1]}')
        entry_price.append(entry_trade[4])
        entry_type.append(entry_trade[2])
        exit_time.append(f'{exit_trade[1]}')
        exit_price.append(exit_trade[4])
        exit_type.append(exit_trade[2])
        if entry_type == 'B':
            profit_and_loss.append((exit_price[-1] - entry_price[-1]) * quantity[-1])
        else:
            profit_and_loss.append((entry_price[-1] - exit_price[-1]) * quantity[-1])

        profit_and_loss_percent.append((profit_and_loss[-1] / ((entry_price[-1] * quantity[-1]) / leverage)) * 100)

        tradebook_dict = {'entry_time': entry_time,
                          'entry_price': entry_price,
                          'entry_type': entry_type,
                          'exit_time': exit_time,
                          'exit_price': exit_price,
                          'exit_type': exit_type,
                          'quantity': quantity,
                          'profit_and_loss': profit_and_loss,
                          'profit_and_loss_percent': profit_and_loss_percent
                          }

        tradebook_df = pd.DataFrame(tradebook_dict)
        tradebook_df.to_csv(f'{os.path.dirname(os.path.realpath(__file__))}/../output/tradebooks/{filename}tradebook.csv')


# tradebook_generator()
