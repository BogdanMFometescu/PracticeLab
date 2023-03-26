import pandas as pd


class Utils:
    def __init__(self):
        pass
        self.items_dict = {"Item": ["Computer",
                                    "Monitor",
                                    "Keyboard",
                                    "Mouse"],
                           "Price": [10, 20, 30, 40]}

        self.items_list_from_csv = pd.DataFrame(self.items_dict)
        self.items_to_csv = self.items_list_from_csv.to_csv("sample_data.csv", index=False)

ut = Utils()