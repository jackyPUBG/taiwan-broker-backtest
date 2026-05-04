import pandas as pd

def generate_data():
    data = {
        'date':["2026-02-20", "2026-02-21","2026-02-22"],
        'stock_id':["2330", "2330", "2330"],
        'broker_id':["元大","元大","元大"],
        'broker_net_buy':[200, 300,400],
        'broker_rank':[1,2,1],
        'avg_cost':[2270, 2230, 2240],
        'price':[2260, 2220, 2230],
        'holder_count':[12300,12200,11000]
    }
    return pd.DataFrame(data)


