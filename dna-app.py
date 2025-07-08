import pandas  as pd
import streamlit as st
import altair as alt


st.write("""
# DNA Nucleotide Analysis App

This app counts the nucleotide composition of a DNA sequence and visualizes it.

***
""")

# Load the data
st.header("Enter DNA Sequence")
sequence_input = ">DNA QUERY\nAGCTTCGTAG\nAGCTTCGTAG\nAGCTTCGTAG "

sequence = st.text_area("Sequence Input", sequence_input, height=250) 
sequence = sequence.splitlines() # Split the input into lines
sequence = sequence[1:]  # Skip the first line (header)
sequence = ''.join(sequence)  # Join the remaining lines into a single string

st.write('***')


st.header("INPUT (DNA Sequence)")

