import pandas 
from pandas import DataFrame

class CustomFrame(DataFrame):

    """
    A DataFrame with a column called "abbrev" that has state abbreviations
    """

    def add_state_names_column(self):
        """
        Add a column of corresponding state names to a dataframe
        """
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self["name"] = self["abbrev"].map(names_map) 

if __name__ == "__main__":
    #df = DataFrame({"abbrev": ['CA','CO','CT','DC','TX']})
    #print(df.head())

    custom_frame = CustomFrame({"abbrev": ['CA','CO','CT','DC','TX']})
    print(custom_frame.head())

    custom_frame.add_state_names_column()
    print(custom_frame.head())