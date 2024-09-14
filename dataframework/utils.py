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



import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_to_dataframe(xml_content, namespaces):
    root = ET.fromstring(xml_content)
    data = []

    # Example: Extracting general information (customize based on your XML structure)
    document_info = {
        'mRID': root.findtext('.//mRID', namespaces=namespaces),
        'revisionNumber': root.findtext('.//revisionNumber', namespaces=namespaces),
        'type': root.findtext('.//type', namespaces=namespaces),
        'processType': root.findtext('.//process.processType', namespaces=namespaces),
        'createdDateTime': root.findtext('.//createdDateTime', namespaces=namespaces),
        'start': root.findtext('.//time_Period.timeInterval/start', namespaces=namespaces),
        'end': root.findtext('.//time_Period.timeInterval/end', namespaces=namespaces)
    }

    # Example: Extracting TimeSeries information (customize based on your XML structure)
    for time_series in root.findall('.//TimeSeries', namespaces=namespaces):
        series_info = {
            'series_mRID': time_series.findtext('mRID', namespaces=namespaces),
            'businessType': time_series.findtext('businessType', namespaces=namespaces),
            'objectAggregation': time_series.findtext('objectAggregation', namespaces=namespaces),
            'outBiddingZone_Domain': time_series.findtext('outBiddingZone_Domain.mRID', namespaces=namespaces),
            'quantity_Measure_Unit': time_series.findtext('quantity_Measure_Unit.name', namespaces=namespaces),
            'curveType': time_series.findtext('curveType', namespaces=namespaces)
        }

        for period in time_series.findall('.//Period', namespaces=namespaces):
            period_start = period.findtext('timeInterval/start', namespaces=namespaces)
            period_end = period.findtext('timeInterval/end', namespaces=namespaces)
            resolution = period.findtext('resolution', namespaces=namespaces)

            for point in period.findall('Point', namespaces=namespaces):
                position = point.findtext('position', namespaces=namespaces)
                quantity = point.findtext('quantity', namespaces=namespaces)
                data.append({
                    **document_info,
                    **series_info,
                    'period_start': period_start,
                    'period_end': period_end,
                    'resolution': resolution,
                    'position': position,
                    'quantity': quantity
                })

    df = pd.DataFrame(data)

    pivot_df = df.pivot(index='position', columns='series_mRID', values='quantity')

    # Optionally, fill missing values if necessary
    pivot_df = pivot_df.to_csv('pivot_df.csv')
    #pivot_df.fillna(0)

    df.to_csv('df.csv')
    return df
'''
# Example usage
if __name__ == "__main__":
    xml_content = b'<?xml version="1.0" encoding="UTF-8"?>\n<GL_MarketDocument xmlns="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">\n    <mRID>2734519c03a949b8aec63501264e635e</mRID>\n    <revisionNumber>1</revisionNumber>\n    <type>A65</type>\n    <process.processType>A16</process.processType>\n    <sender_MarketParticipant.mRID codingScheme="A01">10X1001A1001A450</sender_MarketParticipant.mRID>\n    <sender_MarketParticipant.marketRole.type>A32</sender_MarketParticipant.marketRole.type>\n    <receiver_MarketParticipant.mRID codingScheme="A01">10X1001A1001A450</receiver_MarketParticipant.mRID>\n    <receiver_MarketParticipant.marketRole.type>A33</receiver_MarketParticipant.marketRole.type>\n    <createdDateTime>2024-09-11T20:01:30Z</createdDateTime>\n    <time_Period.timeInterval>\n        <start>2024-08-01T00:00Z</start>\n        <end>2024-08-01T03:00Z</end>\n    </time_Period.timeInterval>\n    <TimeSeries>\n        <mRID>1</mRID>\n        <businessType>A04</businessType>\n        <objectAggregation>A01</objectAggregation>\n        <outBiddingZone_Domain.mRID codingScheme="A01">10YCZ-CEPS-----N</outBiddingZone_Domain.mRID>\n        <quantity_Measure_Unit.name>MAW</quantity_Measure_Unit.name>\n        <curveType>A01</curveType>\n        <Period>\n            <timeInterval>\n                <start>2024-08-01T00:00Z</start>\n                <end>2024-08-01T03:00Z</end>\n            </timeInterval>\n            <resolution>PT15M</resolution>\n            <Point>\n                <position>1</position>\n                <quantity>4985</quantity>\n            </Point>\n            <Point>\n                <position>2</position>\n                <quantity>4958</quantity>\n            </Point>\n            <Point>\n                <position>3</position>\n                <quantity>4945</quantity>\n            </Point>\n            <Point>\n                <position>4</position>\n                <quantity>4932</quantity>\n            </Point>\n            <Point>\n                <position>5</position>\n                <quantity>4898</quantity>\n            </Point>\n            <Point>\n                <position>6</position>\n                <quantity>4882</quantity>\n            </Point>\n            <Point>\n                <position>7</position>\n                <quantity>4836</quantity>\n            </Point>\n            <Point>\n                <position>8</position>\n                <quantity>4815</quantity>\n            </Point>\n            <Point>\n                <position>9</position>\n                <quantity>4850</quantity>\n            </Point>\n            <Point>\n                <position>10</position>\n                <quantity>4885</quantity>\n            </Point>\n            <Point>\n                <position>11</position>\n                <quantity>4984</quantity>\n            </Point>\n            <Point>\n                <position>12</position>\n                <quantity>5070</</Point>\n        </Period>\n    </TimeSeries>\n</GL_MarketDocument>'
    namespaces = {'': 'urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0'}
    df = parse_xml_to_dataframe(xml_content, namespaces)
    print(df)
'''