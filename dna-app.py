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
sequence

# DNA nucleotide count
st.header("OUTPUT (DNA Nuclotide Count)")

# 1. Print dictionary of nucleotide counts
st.subheader("1. Nucleotide Composition")
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_labels = list(X)
X_values = list(X.values())

X

# 2. Print text
st.subheader("2. Text")
st.write(f"""
There are {X['A']} adenine (A) <br>
There are {X['T']} thymine (T) <br>
There are {X['G']} guanine (G) <br>
There are {X['C']} cytosine (C)) <br>
""", unsafe_allow_html=True) 

# 3. Display data frame
st.subheader("3. DataFrame")
X_df = pd.DataFrame.from_dict(X, orient='index')
X_df = X_df.rename({0: 'count'}, axis='columns')
X_df.reset_index(inplace=True)
X_df = X_df.rename(columns={'index': 'nucleotide'})
st.write(X_df)   

# 4. Display bar chart
st.subheader("4. Bar Chart")
bar_chart = alt.Chart(X_df).mark_bar().encode(
    x=alt.X('nucleotide', title='Nucleotide'),
    y=alt.Y('count', title='Count'),
    color=alt.Color('nucleotide', legend=None)  
)

bar_chart = bar_chart.properties(
    width=alt.Step(80)  # Set the width of each bar
)

st.write(bar_chart)


