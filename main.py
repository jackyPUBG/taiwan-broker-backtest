from data import generate_data
from strategy import calculate_signal

df = generate_data()
df = calculate_signal(df)

print(df)