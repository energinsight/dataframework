Contract_MarketAgreementType = {
    "Daily": "A01",
    "Weekly": "A02",
    "Monthly": "A03",
    "Yearly": "A04",
    "Total": "A05",
    "Long term": "A06",
    "Intraday": "A07",
    "Hourly (Type_MarketAgreement.Type only)": "A13"
}

AuctionType = {
    "Implicit": "A01",
    "Explicit": "A02"
}

AuctionCategory = {
    "Base": "A01",
    "Peak": "A02",
    "Off Peak": "A03",
    "Hourly": "A04"
}

PsrType = {
    "Mixed": "A03",
    "Generation": "A04",
    "Load": "A05",
    "Biomass": "B01",
    "Fossil Brown coal/Lignite": "B02",
    "Fossil Coal-derived gas": "B03",
    "Fossil Gas": "B04",
    "Fossil Hard coal": "B05",
    "Fossil Oil": "B06",
    "Fossil Oil shale": "B07",
    "Fossil Peat": "B08",
    "Geothermal": "B09",
    "Hydro Pumped Storage": "B10",
    "Hydro Run-of-river and poundage": "B11",
    "Hydro Water Reservoir": "B12",
    "Marine": "B13",
    "Nuclear": "B14",
    "Other renewable": "B15",
    "Solar": "B16",
    "Waste": "B17",
    "Wind Offshore": "B18",
    "Wind Onshore": "B19",
    "Other": "B20",
    "AC Link": "B21",
    "DC Link": "B22",
    "Substation": "B23",
    "Transformer": "B24"
}

BusinessType = {
    "Production": "A01",
    "Consumption": "A04",
    "Aggregated energy data": "A14",
    "Balance energy deviation": "A19",
    "General Capacity Information": "A25",
    "Already allocated capacity (AAC)": "A29",
    "Installed generation": "A37",
    "Requested capacity (without price)": "A43",
    "System Operator redispatching": "A46",
    "Planned maintenance": "A53",
    "Unplanned outage": "A54",
    "Minimum possible": "A60",
    "Maximum possible": "A61",
    "Internal redispatch": "A85",
    "Positive forecast margin (if installed capacity > load forecast)": "A91",
    "Negative forecast margin (if load forecast > installed capacity)": "A92",
    "Wind generation": "A93",
    "Solar generation": "A94",
    "Frequency containment reserve": "A95",
    "Automatic frequency restoration reserve": "A96",
    "Manual frequency restoration reserve": "A97",
    "Replacement reserve": "A98",
    "Interconnector network evolution": "B01",
    "Interconnector network dismantling": "B02",
    "Counter trade": "B03",
    "Congestion costs": "B04",
    "Capacity allocated (including price)": "B05",
    "Auction revenue": "B07",
    "Total nominated capacity": "B08",
    "Net position": "B09",
    "Congestion income": "B10",
    "Production unit": "B11",
    "Area Control Error": "B33",
    "Offer": "B74",
    "Need": "B75",
    "Procured capacity": "B95",
    "Shared Balancing Reserve Capacity": "C22",
    "Share of reserve capacity": "C23",
    "Actual reserve capacity": "C24"
}

ProcessType = {
    "Day ahead": "A01",
    "Intra day incremental": "A02",
    "Realised": "A16",
    "Intraday total": "A18",
    "Week ahead": "A31",
    "Month ahead": "A32",
    "Year ahead": "A33",
    "Synchronisation process": "A39",
    "Intraday process": "A40",
    "Replacement reserve": "A46",
    "Manual frequency restoration reserve": "A47",
    "Automatic frequency restoration reserve": "A51",
    "Frequency containment reserve": "A52",
    "Frequency restoration reserve": "A56",
    "Scheduled activation mFRR": "A60",
    "Direct activation mFRR": "A61",
    "Central Selection aFRR": "A67",
    "Local Selection aFRR": "A68"
}

DocStatus = {
    "Intermediate": "A01",
    "Final": "A02",
    "Active": "A05",
    "Cancelled": "A09",
    "Withdrawn": "A13",
    "Estimated": "X01"
}

DocumentType = {
    "Finalised schedule": "A09",
    "Aggregated energy data report": "A11",
    "Acquiring system operator reserve schedule": "A15",
    "Bid document": "A24",
    "Allocation result document": "A25",
    "Capacity document": "A26",
    "Agreed capacity": "A31",
    "Reserve bid document": "A37",
    "Reserve allocation result document": "A38",
    "Price Document": "A44",
    "Estimated Net Transfer Capacity": "A61",
    "Redispatch notice": "A63",
    "System total load": "A65",
    "Installed generation per type": "A68",
    "Wind and solar forecast": "A69",
    "Load forecast margin": "A70",
    "Generation forecast": "A71",
    "Reservoir filling information": "A72",
    "Actual generation": "A73",
    "Wind and solar generation": "A74",
    "Actual generation per type": "A75",
    "Load unavailability": "A76",
    "Production unavailability": "A77",
    "Transmission unavailability": "A78",
    "Offshore grid infrastructure unavailability": "A79",
    "Generation unavailability": "A80",
    "Contracted reserves": "A81",
    "Accepted offers": "A82",
    "Activated balancing quantities": "A83",
    "Activated balancing prices": "A84",
    "Imbalance prices": "A85",
    "Imbalance volume": "A86",
    "Financial situation": "A87",
    "Cross border balancing": "A88",
    "Contracted reserve prices": "A89",
    "Interconnection network expansion": "A90",
    "Counter trade notice": "A91",
    "Congestion costs": "A92",
    "DC link capacity": "A93",
    "Non EU allocations": "A94",
    "Configuration document": "A95",
    "Flow-based allocations": "B11",
    "Aggregated netted external TSO schedule document": "B17",
    "Bid Availability Document": "B45"
}

flowDirectionDirection = {
    "Up": "A01",
    "Down": "A02",
    "Symmetric": "A03"
}

Standard_MarketProduct = {
    "Standard": "A01",
    "Specific": "A02",
    "Integrated process": "A03",
    "Local": "A04",
    "Standard mFRR DA": "A05",
    "Standard mFRR SA+DA": "A07"
}

Imbalance_Pricecategory = {
    "Excess balance": "A04",
    "Insufficient balance": "A05",
    "Average bid price": "A06",
    "Single marginal bid price": "A07",
    "Cross border marginal price": "A08"
}

PriceDescriptortype = {
    "Scarcity": "A01",
    "Incentive": "A02",
    "Financial neutrality": "A03"
}


financial_Pricedirection = {
    "Expenditure": "A01",
    "Income": "A02"
}



Areas = {
    "CTA|NIE": "10Y1001A1001A016",
    "MBA|SEM(SONI)": "10Y1001A1001A016",
    "SCA|NIE": "10Y1001A1001A016",
    "SCA|EE": "10Y1001A1001A39I",
    "MBA|EE": "10Y1001A1001A39I",
    "CTA|EE": "10Y1001A1001A39I",
    "BZN|EE": "10Y1001A1001A39I",
    "Estonia (EE)": "10Y1001A1001A39I",
    "IPA|SE1": "10Y1001A1001A44P",
    "BZN|SE1": "10Y1001A1001A44P",
    "MBA|SE1": "10Y1001A1001A44P",
    "SCA|SE1": "10Y1001A1001A44P",
    "SCA|SE2": "10Y1001A1001A45N",
    "MBA|SE2": "10Y1001A1001A45N",
    "BZN|SE2": "10Y1001A1001A45N",
    "IPA|SE2": "10Y1001A1001A45N",
    "IPA|SE3": "10Y1001A1001A46L",
    "BZN|SE3": "10Y1001A1001A46L",
    "MBA|SE3": "10Y1001A1001A46L",
    "SCA|SE3": "10Y1001A1001A46L",
    "SCA|SE4": "10Y1001A1001A47J",
    "MBA|SE4": "10Y1001A1001A47J",
    "BZN|SE4": "10Y1001A1001A47J",
    "IPA|SE4": "10Y1001A1001A47J",
    "IPA|NO5": "10Y1001A1001A48H",
    "IBA|NO5": "10Y1001A1001A48H",
    "BZN|NO5": "10Y1001A1001A48H",
    "MBA|NO5": "10Y1001A1001A48H",
    "SCA|NO5": "10Y1001A1001A48H",
    "SCA|RU": "10Y1001A1001A49F",
    "MBA|RU": "10Y1001A1001A49F",
    "BZN|RU": "10Y1001A1001A49F",
    "CTA|RU": "10Y1001A1001A49F",
    "CTA|RU-KGD": "10Y1001A1001A50U",
    "BZN|RU-KGD": "10Y1001A1001A50U",
    "MBA|RU-KGD": "10Y1001A1001A50U",
    "SCA|RU-KGD": "10Y1001A1001A50U",
    "SCA|BY": "10Y1001A1001A51S",
    "MBA|BY": "10Y1001A1001A51S",
    "BZN|BY": "10Y1001A1001A51S",
    "CTA|BY": "10Y1001A1001A51S",
    "BZN|IE(SEM)": "10Y1001A1001A59C",
    "MBA|IE(SEM)": "10Y1001A1001A59C",
    "SCA|IE(SEM)": "10Y1001A1001A59C",
    "LFB|IE-NIE": "10Y1001A1001A59C",
    "SNA|Ireland": "10Y1001A1001A59C",
    "BZN|DE-AT-LU": "10Y1001A1001A63L",
    "BZN|NO1A": "10Y1001A1001A64J",
    "Denmark (DK)": "10Y1001A1001A65H",
    "BZN|IT-GR": "10Y1001A1001A66F",
    "BZN|IT-North-SI": "10Y1001A1001A67D",
    "BZN|IT-North-CH": "10Y1001A1001A68B",
    "BZN|IT-Brindisi": "10Y1001A1001A699",
    "SCA|IT-Brindisi": "10Y1001A1001A699",
    "MBA|IT-Z-Brindisi": "10Y1001A1001A699",
    "MBA|IT-Z-Centre-North": "10Y1001A1001A70O",
    "SCA|IT-Centre-North": "10Y1001A1001A70O",
    "BZN|IT-Centre-North": "10Y1001A1001A70O",
    "BZN|IT-Centre-South": "10Y1001A1001A71M",
    "SCA|IT-Centre-South": "10Y1001A1001A71M",
    "MBA|IT-Z-Centre-South": "10Y1001A1001A71M",
    "MBA|IT-Z-Foggia": "10Y1001A1001A72K",
    "SCA|IT-Foggia": "10Y1001A1001A72K",
    "BZN|IT-Foggia": "10Y1001A1001A72K",
    "BZN|IT-North": "10Y1001A1001A73I",
    "SCA|IT-North": "10Y1001A1001A73I",
    "MBA|IT-Z-North": "10Y1001A1001A73I",
    "MBA|IT-Z-Sardinia": "10Y1001A1001A74G",
    "SCA|IT-Sardinia": "10Y1001A1001A74G",
    "BZN|IT-Sardinia": "10Y1001A1001A74G",
    "BZN|IT-Sicily": "10Y1001A1001A75E",
    "SCA|IT-Sicily": "10Y1001A1001A75E",
    "MBA|IT-Z-Sicily": "10Y1001A1001A75E",
    "MBA|IT-Z-Priolo": "10Y1001A1001A76C",
    "SCA|IT-Priolo": "10Y1001A1001A76C",
    "BZN|IT-Priolo": "10Y1001A1001A76C",
    "BZN|IT-Rossano": "10Y1001A1001A77A",
    "SCA|IT-Rossano": "10Y1001A1001A77A",
    "MBA|IT-Z-Rossano": "10Y1001A1001A77A",
    "MBA|IT-Z-South": "10Y1001A1001A788",
    "SCA|IT-South": "10Y1001A1001A788",
    "BZN|IT-South": "10Y1001A1001A788",
    "CTA|DK": "10Y1001A1001A796",
    "BZN|IT-North-AT": "10Y1001A1001A80L",
    "BZN|IT-North-FR": "10Y1001A1001A81J",
    "BZN|DE-LU": "10Y1001A1001A82H",
    "IPA|DE-LU": "10Y1001A1001A82H",
    "SCA|DE-LU": "10Y1001A1001A82H",
    "MBA|DE-LU": "10Y1001A1001A82H",
    "Germany (DE)": "10Y1001A1001A83F",
    "MBA|IT-MACRZONENORTH": "10Y1001A1001A84D",
    "SCA|IT-MACRZONENORTH": "10Y1001A1001A84D",
    "SCA|IT-MACRZONESOUTH": "10Y1001A1001A85B",
    "MBA|IT-MACRZONESOUTH": "10Y1001A1001A85B",
    "SCA|UA-DobTPP": "10Y1001A1001A869",
    "BZN|UA-DobTPP": "10Y1001A1001A869",
    "CTA|UA-DobTPP": "10Y1001A1001A869",
    "BZN|IT-Malta": "10Y1001A1001A877",
    "BZN|IT-SACOAC": "10Y1001A1001A885",
    "BZN|IT-SACODC": "10Y1001A1001A893",
    "SCA|IT-SACODC": "10Y1001A1001A893",
    "SNA|Nordic": "10Y1001A1001A91G",
    "REG|Nordic": "10Y1001A1001A91G",
    "LFB|Nordic": "10Y1001A1001A91G",
    "United Kingdom (UK)": "10Y1001A1001A92E",
    "Malta (MT)": "10Y1001A1001A93C",
    "BZN|MT": "10Y1001A1001A93C",
    "CTA|MT": "10Y1001A1001A93C",
    "SCA|MT": "10Y1001A1001A93C",
    "MBA|MT": "10Y1001A1001A93C",
    "MBA|MD": "10Y1001A1001A990",
    "SCA|MD": "10Y1001A1001A990",
    "CTA|MD": "10Y1001A1001A990",
    "BZN|MD": "10Y1001A1001A990",
    "Moldova (MD)": "10Y1001A1001A990",
    "Armenia (AM)": "10Y1001A1001B004",
    "BZN|AM": "10Y1001A1001B004",
    "CTA|AM": "10Y1001A1001B004",
    "CTA|GE": "10Y1001A1001B012",
    "BZN|GE": "10Y1001A1001B012",
    "Georgia (GE)": "10Y1001A1001B012",
    "SCA|GE": "10Y1001A1001B012",
    "MBA|GE": "10Y1001A1001B012",
    "Azerbaijan (AZ)": "10Y1001A1001B05V",
    "BZN|AZ": "10Y1001A1001B05V",
    "CTA|AZ": "10Y1001A1001B05V",
    "BZN|UA": "10Y1001C--00003F",
    "Ukraine (UA)": "10Y1001C--00003F",
    "MBA|UA": "10Y1001C--00003F",
    "SCA|UA": "10Y1001C--00003F",
    "SCA|UA-IPS": "10Y1001C--000182",
    "MBA|UA-IPS": "10Y1001C--000182",
    "BZN|UA-IPS": "10Y1001C--000182",
    "CTA|UA-IPS": "10Y1001C--000182",
    "BZA|CZ-DE-SK-LT-SE4": "10Y1001C--00038X",
    "REG|CORE": "10Y1001C--00059P",
    "REG|AFRR": "10Y1001C--00090V",
    "SCA|AFRR": "10Y1001C--00090V",
    "REG|SWE": "10Y1001C--00095L",
    "SCA|IT-Calabria": "10Y1001C--00096J",
    "MBA|IT-Z-Calabria": "10Y1001C--00096J",
    "BZN|IT-Calabria": "10Y1001C--00096J",
    "BZN|GB(IFA)": "10Y1001C--00098F",
    "BZN|XK": "10Y1001C--00100H",
    "CTA|XK": "10Y1001C--00100H",
    "Kosovo (XK)": "10Y1001C--00100H",
    "MBA|XK": "10Y1001C--00100H",
    "LFB|XK": "10Y1001C--00100H",
    "LFA|XK": "10Y1001C--00100H",
    "SCA|IN": "10Y1001C--00119X",
    "BZN|NO2A": "10Y1001C--001219",
    "REG|ITALYNORTH": "10Y1001C--00137V",
    "REG|GRIT": "10Y1001C--00138T",
    "LFB|AL": "10YAL-KESH-----5",
    "LFA|AL": "10YAL-KESH-----5",
    "BZN|AL": "10YAL-KESH-----5",
    "CTA|AL": "10YAL-KESH-----5",
    "Albania (AL)": "10YAL-KESH-----5",
    "SCA|AL": "10YAL-KESH-----5",
    "MBA|AL": "10YAL-KESH-----5",
    "MBA|AT": "10YAT-APG------L",
    "SCA|AT": "10YAT-APG------L",
    "Austria (AT)": "10YAT-APG------L",
    "IPA|AT": "10YAT-APG------L",
    "CTA|AT": "10YAT-APG------L",
    "BZN|AT": "10YAT-APG------L",
    "LFA|AT": "10YAT-APG------L",
    "LFB|AT": "10YAT-APG------L",
    "LFA|BA": "10YBA-JPCC-----D",
    "BZN|BA": "10YBA-JPCC-----D",
    "CTA|BA": "10YBA-JPCC-----D",
    "Bosnia and Herz. (BA)": "10YBA-JPCC-----D",
    "SCA|BA": "10YBA-JPCC-----D",
    "MBA|BA": "10YBA-JPCC-----D",
    "MBA|BE": "10YBE----------2",
    "SCA|BE": "10YBE----------2",
    "Belgium (BE)": "10YBE----------2",
    "CTA|BE": "10YBE----------2",
    "BZN|BE": "10YBE----------2",
    "LFA|BE": "10YBE----------2",
    "LFB|BE": "10YBE----------2",
    "LFB|BG": "10YCA-BULGARIA-R",
    "LFA|BG": "10YCA-BULGARIA-R",
    "BZN|BG": "10YCA-BULGARIA-R",
    "CTA|BG": "10YCA-BULGARIA-R",
    "Bulgaria (BG)": "10YCA-BULGARIA-R",
    "SCA|BG": "10YCA-BULGARIA-R",
    "MBA|BG": "10YCA-BULGARIA-R",
    "SCA|DE_DK1_LU": "10YCB-GERMANY--8",
    "LFB|DE_DK1_LU": "10YCB-GERMANY--8",
    "LFB|RS_MK_ME": "10YCB-JIEL-----9",
    "LFB|PL": "10YCB-POLAND---Z",
    "LFB|SI_HR_BA": "10YCB-SI-HR-BA-3",
    "LFB|CH": "10YCH-SWISSGRIDZ",
    "LFA|CH": "10YCH-SWISSGRIDZ",
    "SCA|CH": "10YCH-SWISSGRIDZ",
    "MBA|CH": "10YCH-SWISSGRIDZ",
    "Switzerland (CH)": "10YCH-SWISSGRIDZ",
    "CTA|CH": "10YCH-SWISSGRIDZ",
    "BZN|CH": "10YCH-SWISSGRIDZ",
    "BZN|ME": "10YCS-CG-TSO---S",
    "CTA|ME": "10YCS-CG-TSO---S",
    "Montenegro (ME)": "10YCS-CG-TSO---S",
    "MBA|ME": "10YCS-CG-TSO---S",
    "SCA|ME": "10YCS-CG-TSO---S",
    "LFA|ME": "10YCS-CG-TSO---S",
    "LFA|RS": "10YCS-SERBIATSOV",
    "SCA|RS": "10YCS-SERBIATSOV",
    "MBA|RS": "10YCS-SERBIATSOV",
    "Serbia (RS)": "10YCS-SERBIATSOV",
    "CTA|RS": "10YCS-SERBIATSOV",
    "BZN|RS": "10YCS-SERBIATSOV",
    "BZN|CY": "10YCY-1001A0003J",
    "CTA|CY": "10YCY-1001A0003J",
    "Cyprus (CY)": "10YCY-1001A0003J",
    "MBA|CY": "10YCY-1001A0003J",
    "SCA|CY": "10YCY-1001A0003J",
    "SCA|CZ": "10YCZ-CEPS-----N",
    "MBA|CZ": "10YCZ-CEPS-----N",
    "Czech Republic (CZ)": "10YCZ-CEPS-----N",
    "CTA|CZ": "10YCZ-CEPS-----N",
    "BZN|CZ": "10YCZ-CEPS-----N",
    "LFA|CZ": "10YCZ-CEPS-----N",
    "LFB|CZ": "10YCZ-CEPS-----N",
    "LFA|DE(TransnetBW)": "10YDE-ENBW-----N",
    "CTA|DE(TransnetBW)": "10YDE-ENBW-----N",
    "SCA|DE(TransnetBW)": "10YDE-ENBW-----N",
    "SCA|DE(TenneT GER)": "10YDE-EON------1",
    "CTA|DE(TenneT GER)": "10YDE-EON------1",
    "LFA|DE(TenneT GER)": "10YDE-EON------1",
    "LFA|DE(Amprion)": "10YDE-RWENET---I",
    "CTA|DE(Amprion)": "10YDE-RWENET---I",
    "SCA|DE(Amprion)": "10YDE-RWENET---I",
    "SCA|DE(50Hertz)": "10YDE-VE-------2",
    "CTA|DE(50Hertz)": "10YDE-VE-------2",
    "LFA|DE(50Hertz)": "10YDE-VE-------2",
    "BZA|DE(50HzT)": "10YDE-VE-------2",
    "BZN|DK1A": "10YDK-1-------AA",
    "IPA|DK1": "10YDK-1--------W",
    "IBA|DK1": "10YDK-1--------W",
    "BZN|DK1": "10YDK-1--------W",
    "SCA|DK1": "10YDK-1--------W",
    "MBA|DK1": "10YDK-1--------W",
    "LFA|DK1": "10YDK-1--------W",
    "LFA|DK2": "10YDK-2--------M",
    "MBA|DK2": "10YDK-2--------M",
    "SCA|DK2": "10YDK-2--------M",
    "IBA|DK2": "10YDK-2--------M",
    "IPA|DK2": "10YDK-2--------M",
    "BZN|DK2": "10YDK-2--------M",
    "CTA|PL-CZ": "10YDOM-1001A082L",
    "BZA|PL-CZ": "10YDOM-1001A082L",
    "BZA|CZ-DE-SK": "10YDOM-CZ-DE-SKK",
    "BZN|CZ+DE+SK": "10YDOM-CZ-DE-SKK",
    "BZA|LT-SE4": "10YDOM-PL-SE-LT2",
    "REG|CWE": "10YDOM-REGION-1V",
    "LFB|ES": "10YES-REE------0",
    "LFA|ES": "10YES-REE------0",
    "BZN|ES": "10YES-REE------0",
    "Spain (ES)": "10YES-REE------0",
    "CTA|ES": "10YES-REE------0",
    "SCA|ES": "10YES-REE------0",
    "MBA|ES": "10YES-REE------0",
    "SNA|Continental Europe": "10YEU-CONT-SYNC0",
    "MBA|FI": "10YFI-1--------U",
    "SCA|FI": "10YFI-1--------U",
    "CTA|FI": "10YFI-1--------U",
    "Finland (FI)": "10YFI-1--------U",
    "BZN|FI": "10YFI-1--------U",
    "IPA|FI": "10YFI-1--------U",
    "IBA|FI": "10YFI-1--------U",
    "BZN|FR": "10YFR-RTE------C",
    "France (FR)": "10YFR-RTE------C",
    "CTA|FR": "10YFR-RTE------C",
    "SCA|FR": "10YFR-RTE------C",
    "MBA|FR": "10YFR-RTE------C",
    "LFB|FR": "10YFR-RTE------C",
    "LFA|FR": "10YFR-RTE------C",
    "LFA|GB": "10YGB----------A",
    "LFB|GB": "10YGB----------A",
    "SNA|GB": "10YGB----------A",
    "MBA|GB": "10YGB----------A",
    "SCA|GB": "10YGB----------A",
    "CTA|National Grid": "10YGB----------A",
    "BZN|GB": "10YGB----------A",
    "BZN|GR": "10YGR-HTSO-----Y",
    "Greece (GR)": "10YGR-HTSO-----Y",
    "CTA|GR": "10YGR-HTSO-----Y",
    "SCA|GR": "10YGR-HTSO-----Y",
    "MBA|GR": "10YGR-HTSO-----Y",
    "LFB|GR": "10YGR-HTSO-----Y",
    "LFA|GR": "10YGR-HTSO-----Y",
    "LFA|HR": "10YHR-HEP------M",
    "MBA|HR": "10YHR-HEP------M",
    "SCA|HR": "10YHR-HEP------M",
    "CTA|HR": "10YHR-HEP------M",
    "Croatia (HR)": "10YHR-HEP------M",
    "BZN|HR": "10YHR-HEP------M",
    "BZN|HU": "10YHU-MAVIR----U",
    "Hungary (HU)": "10YHU-MAVIR----U",
    "CTA|HU": "10YHU-MAVIR----U",
    "SCA|HU": "10YHU-MAVIR----U",
    "MBA|HU": "10YHU-MAVIR----U",
    "LFA|HU": "10YHU-MAVIR----U",
    "LFB|HU": "10YHU-MAVIR----U",
    "MBA|SEM(EirGrid)": "10YIE-1001A00010",
    "SCA|IE": "10YIE-1001A00010",
    "CTA|IE": "10YIE-1001A00010",
    "Ireland (IE)": "10YIE-1001A00010",
    "Italy (IT)": "10YIT-GRTN-----B",
    "CTA|IT": "10YIT-GRTN-----B",
    "SCA|IT": "10YIT-GRTN-----B",
    "MBA|IT": "10YIT-GRTN-----B",
    "LFB|IT": "10YIT-GRTN-----B",
    "LFA|IT": "10YIT-GRTN-----B",
    "MBA|LT": "10YLT-1001A0008Q",
    "SCA|LT": "10YLT-1001A0008Q",
    "CTA|LT": "10YLT-1001A0008Q",
    "Lithuania (LT)": "10YLT-1001A0008Q",
    "BZN|LT": "10YLT-1001A0008Q",
    "Luxembourg (LU)": "10YLU-CEGEDEL-NQ",
    "CTA|LU": "10YLU-CEGEDEL-NQ",
    "CTA|LV": "10YLV-1001A00074",
    "Latvia (LV)": "10YLV-1001A00074",
    "BZN|LV": "10YLV-1001A00074",
    "SCA|LV": "10YLV-1001A00074",
    "MBA|LV": "10YLV-1001A00074",
    "MBA|MK": "10YMK-MEPSO----8",
    "SCA|MK": "10YMK-MEPSO----8",
    "BZN|MK": "10YMK-MEPSO----8",
    "North Macedonia (MK)": "10YMK-MEPSO----8",
    "CTA|MK": "10YMK-MEPSO----8",
    "LFA|MK": "10YMK-MEPSO----8",
    "LFA|NL": "10YNL----------L",
    "LFB|NL": "10YNL----------L",
    "CTA|NL": "10YNL----------L",
    "Netherlands (NL)": "10YNL----------L",
    "BZN|NL": "10YNL----------L",
    "SCA|NL": "10YNL----------L",
    "MBA|NL": "10YNL----------L",
    "MBA|NO": "10YNO-0--------C",
    "SCA|NO": "10YNO-0--------C",
    "Norway (NO)": "10YNO-0--------C",
    "CTA|NO": "10YNO-0--------C",
    "BZN|NO1": "10YNO-1--------2",
    "IBA|NO1": "10YNO-1--------2",
    "IPA|NO1": "10YNO-1--------2",
    "SCA|NO1": "10YNO-1--------2",
    "MBA|NO1": "10YNO-1--------2",
    "MBA|NO2": "10YNO-2--------T",
    "SCA|NO2": "10YNO-2--------T",
    "IPA|NO2": "10YNO-2--------T",
    "IBA|NO2": "10YNO-2--------T",
    "BZN|NO2": "10YNO-2--------T",
    "BZN|NO3": "10YNO-3--------J",
    "IBA|NO3": "10YNO-3--------J",
    "IPA|NO3": "10YNO-3--------J",
    "SCA|NO3": "10YNO-3--------J",
    "MBA|NO3": "10YNO-3--------J",
    "MBA|NO4": "10YNO-4--------9",
    "SCA|NO4": "10YNO-4--------9",
    "IPA|NO4": "10YNO-4--------9",
    "IBA|NO4": "10YNO-4--------9",
    "BZN|NO4": "10YNO-4--------9",
    "BZN|PL": "10YPL-AREA-----S",
    "Poland (PL)": "10YPL-AREA-----S",
    "CTA|PL": "10YPL-AREA-----S",
    "SCA|PL": "10YPL-AREA-----S",
    "MBA|PL": "10YPL-AREA-----S",
    "BZA|PL": "10YPL-AREA-----S",
    "LFA|PL": "10YPL-AREA-----S",
    "LFA|PT": "10YPT-REN------W",
    "LFB|PT": "10YPT-REN------W",
    "MBA|PT": "10YPT-REN------W",
    "SCA|PT": "10YPT-REN------W",
    "CTA|PT": "10YPT-REN------W",
    "Portugal (PT)": "10YPT-REN------W",
    "BZN|PT": "10YPT-REN------W",
    "BZN|RO": "10YRO-TEL------P",
    "Romania (RO)": "10YRO-TEL------P",
    "CTA|RO": "10YRO-TEL------P",
    "SCA|RO": "10YRO-TEL------P",
    "MBA|RO": "10YRO-TEL------P",
    "LFB|RO": "10YRO-TEL------P",
    "LFA|RO": "10YRO-TEL------P",
    "MBA|SE": "10YSE-1--------K",
    "SCA|SE": "10YSE-1--------K",
    "CTA|SE": "10YSE-1--------K",
    "Sweden (SE)": "10YSE-1--------K",
    "Slovenia (SI)": "10YSI-ELES-----O",
    "BZN|SI": "10YSI-ELES-----O",
    "CTA|SI": "10YSI-ELES-----O",
    "SCA|SI": "10YSI-ELES-----O",
    "MBA|SI": "10YSI-ELES-----O",
    "LFA|SI": "10YSI-ELES-----O",
    "LFA|SK": "10YSK-SEPS-----K",
    "LFB|SK": "10YSK-SEPS-----K",
    "MBA|SK": "10YSK-SEPS-----K",
    "SCA|SK": "10YSK-SEPS-----K",
    "CTA|SK": "10YSK-SEPS-----K",
    "BZN|SK": "10YSK-SEPS-----K",
    "Slovakia (SK)": "10YSK-SEPS-----K",
    "Turkey (TR)": "10YTR-TEIAS----W",
    "BZN|TR": "10YTR-TEIAS----W",
    "CTA|TR": "10YTR-TEIAS----W",
    "SCA|TR": "10YTR-TEIAS----W",
    "MBA|TR": "10YTR-TEIAS----W",
    "LFB|TR": "10YTR-TEIAS----W",
    "LFA|TR": "10YTR-TEIAS----W",
    "LFA|UA-BEI": "10YUA-WEPS-----0",
    "LFB|UA-BEI": "10YUA-WEPS-----0",
    "MBA|UA-BEI": "10YUA-WEPS-----0",
    "SCA|UA-BEI": "10YUA-WEPS-----0",
    "CTA|UA-BEI": "10YUA-WEPS-----0",
    "BZN|UA-BEI": "10YUA-WEPS-----0",
    "BZN|GB(ElecLink)": "11Y0-0000-0265-K",
    "BZN|GB(IFA2)": "17Y0000009369493",
    "BZN|DK1-NO1": "46Y000000000007M",
    "BZN|NO2NSL": "50Y0JVU59B4JWQCU",
    "Belarus (BY)": "BY",
    "Russia (RU)": "RU",
    "Iceland (IS)": "IS"
}






