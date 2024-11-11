import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
#Data
data = pd.read_stata("all_plottable_region_final_v2.dta", index_col=None)
df = data[['Number', 'Calendaryearofpublication', 'Outcome', 'Region', 'Age', 'Gender', 'DeliveryAgent', 'School', 'Title', 'firstauthor', 'Journalsource', 'AdditionalFactors', 'Finding', 'Duration', 'Setting', 'FollowUp']]


df['Number'] = df['Number'].astype(int)
df=df.astype(str)



# Streamlit dropdowns for year and outcome
st.title("SRH scoping review - Filter eligible papers")

age = st.multiselect('Age', ['All'] + df['Age'].unique().tolist(), default='All')
gender = st.multiselect('Gender', ['All'] +  df['Gender'].unique().tolist(), default='All')
region = st.multiselect('Region', ['All'] + df['Region'].unique().tolist(), default='All')
deliveryagent = st.multiselect('Delivery agent', ['All'] + df['DeliveryAgent'].unique().tolist(), default='All')
school = st.multiselect('School-attending', ['All'] + df['School'].unique().tolist(), default='All')
duration = st.multiselect('Duration', ['All'] + df['Duration'].unique().tolist(), default='All')
setting = st.multiselect('Setting', ['All'] + df['Setting'].unique().tolist(), default='All')
outcome = st.multiselect('Outcome', ['All'] + df['Outcome'].unique().tolist(), default='All')
followup = st.multiselect('Timing of Follow-up', df['FollowUp'].unique(), default='Immediately post-intervention')
finding = st.multiselect('Finding', df['Finding'].unique(), default='(Significant) improvements')




#Filter data based on selection
df_filtered =  df[(df['Finding'].isin(finding))]

if 'All' not in region:
    df_filtered = df_filtered[(df['Region'].isin(region))]

if 'All' not in age:
    df_filtered = df_filtered[(df['Age'].isin(age))]

if 'All' not in deliveryagent:
    df_filtered = df_filtered[(df['DeliveryAgent'].isin(deliveryagent))]

if 'All' not in outcome:
    df_filtered = df_filtered[(df['Outcome'].isin(outcome))]

if 'All' not in gender:
    df_filtered = df_filtered[(df['Gender'].isin(gender))]

if 'All' not in school:
    df_filtered = df_filtered[(df['School'].isin(school))]

if 'All' not in duration:
    df_filtered = df_filtered[(df['Duration'].isin(duration))]

if 'All' not in setting:
    df_filtered = df_filtered[(df['Setting'].isin(setting))]

if 'All' not in followup:
    df_filtered = df_filtered[(df['FollowUp'].isin(followup))]


df_filtered = df_filtered[['Number', 'firstauthor', 'Calendaryearofpublication', 'Title']]
df_filtered = df_filtered.drop_duplicates()
df_filtered = df_filtered.reset_index(drop=True)
# Display filtered data
st.write("Filtered Results:")


# Rename columns to your custom text
df_filtered = df_filtered.rename(columns={
    'Number': 'Number in extraction table',
    'firstauthor': 'First Author',
    'Calendaryearofpublication': 'Publication year',
})


st.dataframe(df_filtered[['Number in extraction table', 'First Author', 'Publication year', 'Title']], use_container_width=True)








