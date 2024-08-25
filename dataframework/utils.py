import pandas as pd
import plotly.graph_objects as go


def load_data_from_source(loader, params: dict):
    data = loader.load_data(params)
    return data
    # Do something with the data


def DataFrame_sameloader(loader, List: list):
    df = None

    for i in List:
        data = loader.load_data(i)
        # Check if data is a DataFrame
        if isinstance(data, pd.DataFrame):
            # Modify column names to include the country name
            data.columns = [f'{i}_{col}' for col in data.columns]
        else:
            data = data.to_frame(f'{i}_value')
        # Infer the frequency of the data
        freq = data.index.to_series().diff().min()
        data = data.resample(freq).first()
        if df is None:
            df = data
        else:
            df = df.merge(data, left_index=True, right_index=True, how='outer')

    return df
    # Create a DataFrame from the data


def DataFrame_vl(loader, List: list):
    df = None

    for i in range(len(List)):
        data = loader[i].load_data(List[i])
        # Check if data is a DataFrame
        if isinstance(data, pd.DataFrame):
            # Modify column names to include the country name
            data.columns = [f'{List[i]}_{col}' for col in data.columns]
        else:
            data = data.to_frame(f'{List[i]}_value')
        # Infer the frequency of the data
        freq = data.index.to_series().diff().min()
        data = data.resample(freq).first()
        if df is None:
            df = data
        else:
            df = df.merge(data, left_index=True, right_index=True, how='outer')

    return df
