from abc import ABC, abstractmethod
from . import Entsodictionaries

class DataLoader(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end

        # Dynamically assign dictionaries
        self.AuctionType = Entsodictionaries.AuctionType
        self.AuctionCategory = Entsodictionaries.AuctionCategory
        self.PsrType = Entsodictionaries.PsrType
        self.BusinessType = Entsodictionaries.BusinessType
        self.ProcessType = Entsodictionaries.ProcessType
        self.DocStatus = Entsodictionaries.DocStatus
        self.DocumentType = Entsodictionaries.DocumentType
        self.flowDirectionDirection = Entsodictionaries.flowDirectionDirection
        self.Standard_MarketProduct = Entsodictionaries.Standard_MarketProduct
        self.Imbalance_Pricecategory = Entsodictionaries.Imbalance_Pricecategory
        self.PriceDescriptortype = Entsodictionaries.PriceDescriptortype
        self.financial_Pricedirection = Entsodictionaries.financial_Pricedirection
        self.Areas = Entsodictionaries.Areas

    @abstractmethod
    def load_data(self):
        pass



