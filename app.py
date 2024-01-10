import streamlit as st
import pandas as pd
import altair as alt

data = [
    {'Month': 'Sep 2022', 'I_Consumption': 404353,'Peak_Consumption': 109143,'Night_Consumption': 77659.2,'Commer_charge':2266,'Tempsupply_charge':6853,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Oct 2022', 'I_Consumption': 420201,'Peak_Consumption': 155019,'Night_Consumption': 112194,'Commer_charge':2231,'Tempsupply_charge':8490,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Nov 2022', 'I_Consumption': 473964,'Peak_Consumption': 178882,'Night_Consumption': 121173,'Commer_charge':1769,'Tempsupply_charge':10294,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Dec 2022', 'I_Consumption': 493774,'Peak_Consumption': 175017,'Night_Consumption': 138947,'Commer_charge':0,'Tempsupply_charge':13256,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Jan 2023', 'I_Consumption': 404121,'Peak_Consumption': 148266,'Night_Consumption': 113838,'Commer_charge':1697,'Tempsupply_charge':11483,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Feb 2023', 'I_Consumption': 371985,'Peak_Consumption': 142718,'Night_Consumption': 109845,'Commer_charge':11826,'Tempsupply_charge':11227,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Mar 2023', 'I_Consumption': 493774,'Peak_Consumption': 175017,'Night_Consumption': 138947,'Commer_charge':0,'Tempsupply_charge':13256,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Apr 2023', 'I_Consumption': 423980,'Peak_Consumption': 153744,'Night_Consumption': 117298,'Commer_charge':0,'Tempsupply_charge':27044,'Demand_charge':1286.4,'Max demand':1250,'Levy compensation charge':40040},
    {'Month': 'May 2023', 'I_Consumption': 532261,'Peak_Consumption': 195624,'Night_Consumption': 139970,'Commer_charge':567,'Tempsupply_charge':28962,'Demand_charge':1273.6,'Max demand':1250,'Levy compensation charge':25960},
    {'Month': 'Jun 2023', 'I_Consumption': 463522,'Peak_Consumption': 170880,'Night_Consumption': 122256,'Commer_charge':1795,'Tempsupply_charge':26971,'Demand_charge':1286.4,'Max demand':1250,'Levy compensation charge':40040},
    {'Month': 'Jul 2023', 'I_Consumption': 324239,'Peak_Consumption': 129853,'Night_Consumption': 92550,'Commer_charge':1636,'Tempsupply_charge':24387,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Aug 2023', 'I_Consumption': 393759,'Peak_Consumption': 155255,'Night_Consumption': 112579,'Commer_charge':1864,'Tempsupply_charge':27084,'Demand_charge':1125,'Max demand':1250},
    {'Month': 'Sep 2023', 'I_Consumption': 422264,'Peak_Consumption': 159813,'Night_Consumption': 113795,'Commer_charge':1828,'Tempsupply_charge':22270,'Demand_charge':1216,'Max demand':1250},
]
total_consumption = [
    601399.72, 722119, 787207, 784225, 680530, 648726, 822119, 
    723388.8, 898681.2, 786746.8, 573790, 691666, 721186
]

total_amount = [
    3947939, 4359263, 4850439, 4792852, 4243144, 4076435, 5000904, 
    4725596, 5658043, 5085852, 3822309, 4465226, 4696321
]    
max_length = max(len(data), len(total_consumption), len(total_amount))


data.extend([{} for _ in range(max_length - len(data))])
total_consumption.extend([None] * (max_length - len(total_consumption)))
total_amount.extend([None] * (max_length - len(total_amount)))

for index, entry in enumerate(data):
    entry['Total_Consumption_KVA'] = total_consumption[index]
    entry['Total_Amount_Rs'] = total_amount[index]

df = pd.DataFrame(data)
month_order = ['Sep 2022', 'Oct 2022', 'Nov 2022', 'Dec 2022', 'Jan 2023', 'Feb 2023', 'Mar 2023', 'Apr 2023', 'May 2023', 'Jun 2023', 'Jul 2023', 'Aug 2023', 'Sep 2023']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
df.set_index('Month', inplace=True)

st.title('Amrita Energy Auditing')
st.title('Yearly Energy Consumption')
st.write('This bar chart shows the Yearly energy consumption.')

selected_column = st.selectbox('Select parameter', df.columns)
if selected_column:
    chart = alt.Chart(df.reset_index()).mark_bar().encode(
        x=alt.X('Month:N', sort=month_order),
        y=selected_column,
        tooltip=[selected_column]
    ).properties(width=600, height=400)
    
    st.altair_chart(chart)
