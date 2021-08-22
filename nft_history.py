import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime

st.title('Generative NFT Collection History')

df = pd.DataFrame({
  'Title': ["Etheria","Curio Cards","CryptoPunks","Mooncats","CryptoKitties","CryptoArte","Autoglyphs","Avastars Gen 1","Art Blocks Curated","Bored Ape Yacht Club","thedudes","Fluf World","Generativemasks","Audioglyphs","HeavenComputer","PixelGlyphs","Deafbeef","Eulerbeats"],
  'Generative?': ["❌","❌","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅","✅"],
  'Generated on chain?': ["❌","❌","❌","✅","❌","❌","✅","✅","✅","❌","✅","❌","✅","✅","✅","✅","✅","✅"],
  'Category': ["Game","Art","PFP","Collectible","Game","Art","Art","PFP","Art","PFP","PFP","PFP","Art","Art","Art","PFP","Art","Art"],
  'File type': ["Game","Image","Image","Image","Image","Image","Image","Image","Image","Image","Interactive","Video","Dynamic image","Music","Video","Image","Music","Music"],
  'Date': ["October 31, 2015","May 9, 2017","June 23, 2017","August 9, 2017","November 28, 2017","June 11, 2018","April 26, 2019","February 7, 2020","November 27, 2020","April 30, 2021","July 28, 2021","August 7, 2021","August 16, 2021","August 17, 2021","August 18, 2021","July 22, 2021","March 26, 2021","February 15, 2021"]
})
onoff_options = ["","Off-chain","On-chain"]
gen_options = ["","Manual","Generative"]
cat_options = list(set(df['Category']))
cat_options.append("")
cat_options.sort()
type_options = list(set(df['File type']))
type_options.append("")
type_options.sort()

df2 = df
df2['timestamp'] = pd.to_datetime(df2['Date'], format='%B %d, %Y')

#Generative or manual production
gen = st.sidebar.selectbox(
    'Generative or manually produced?',
     gen_options)

if gen == "Manual":
  df2 = df2[df2["Generative?"] == "❌"]
  onoff_options = ["","Off-chain"]
elif gen == "Generative":
  df2 = df2[df2["Generative?"] == "✅"]

#Generated on or off chain
onoff = st.sidebar.selectbox(
    'Generated on-chain or off-chain?',
     onoff_options)

if onoff == "On-chain":
  df2 = df2[df2["Generated on chain?"] == "✅"]
elif onoff == "Off-chain":
  df2 = df2[df2["Generated on chain?"] == "❌"]

#Category
cat = st.sidebar.selectbox(
    'Category',
     cat_options)
if cat != "":
  df2 = df2[df2["Category"] == cat]

#Type
filetype = st.sidebar.selectbox(
    'Type',
     type_options)
if filetype != "":
  df2 = df2[df2["File type"] == filetype]

df2 = df2.sort_values(by=['timestamp'])

if onoff=="On-chain": onoff_gen = "on-chain generated"
elif onoff=="Off-chain": onoff_gen = "off-chain generated"
elif gen=="Manual": onoff_gen = "manually created"
else: onoff_gen = onoff.lower() + " " + gen.lower()

if filetype=="Interactive": cat_type = "interactive " + cat.lower()
elif filetype=="": cat_type = cat.lower()
else: cat_type = filetype.lower() + " based " + cat.lower()


'First ', onoff_gen, cat_type, ' NFT collection on Ethereum network is ', df2['Title'].iloc[0]

left_column, right_column = st.columns(2)

if st.checkbox('Show the full list'):
    df

