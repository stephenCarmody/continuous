import luigi
import pandas as pd
import pandas_datareader.data as web
import datetime
import seaborn as sns


class GetCompanies(luigi.Task):

    def run(self):
        print('test')
        sp_500_table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
        
        with self.output().open('w') as f:
            sp_500_table.to_csv(f, index=False)
            
            
    def output(self):
        print('test')
        return luigi.LocalTarget('companies.csv')
    

class GetStocks(luigi.Task):
    
    # Note that requires() can not return a Target object.
    def requires(self):
        return GetCompanies()
 
    def output(self):
        return luigi.LocalTarget('stock.csv')
 
    def run(self):
        
        def get_comp_stocks(company, col):

            df_500 = web.DataReader(company, 'yahoo', start, end)
            closing_prices = df_500[col]
            closing_prices.name=company

            return closing_prices
        
        stocks_df = []
        start = datetime.datetime(2009, 1, 1)
        end = datetime.datetime.today()
        
        comps = pd.read_csv(self.input().open())
        comps.head().apply(lambda x: stocks_df.append(get_comp_stocks(x['Symbol'], 'Close')), axis=1)
        stocks_all = pd.DataFrame(stocks_df).T
        
        with self.output().open('w') as f:
            stocks_all.to_csv(f)
            
    
    