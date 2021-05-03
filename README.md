# Application of Clustering Methods for Genetic Analaysis of SARS-CoV-2
## Poster  
![Covid_Genetic_Analysis_Research_Poster (1)-1](https://user-images.githubusercontent.com/71059181/116836694-5f69dd80-ab7c-11eb-8dd7-292cafb77365.png)

## Abstract

The SARS-CoV-2 pandemic has affected many individuals and completely changed the way the world functions. To date, there have been over 150 million cases around the world, and counting. Similar to many resipiratory viruses, the COVID-19 virus has rapidly mutated into dozens of prolific strains. The current vaccine has been designed using the original strains sequence from Wuhan, China, however, there is reason for speculation that the vaccine may not be as affective with the other dominant strains. Our project aims to provide scientists with a tool to help them compare these strains and predict characteristics that can aid in determining key factors such as vaccine efficacy. This can also be used to assist public health officials target specific strains of any virus and develop further preventative measures.
## Primary Goals
- **Speed**: Determine if clustering is quicker than MEGA
- **Reliability**: Determine if clustering results accurately group sequences
## Methods

### _Data Retrieval_
- Utilized [Severe Acute Respiratory Syndrome Coronavirus 2 Data Hub](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049&ProtNames_ss=surface%20glycoprotein) to retrieve nucleotide sequnces of various strains
- Manually donwloaded 228 sequences in .fasta format, ensuring 3-4 sequences from each of the 6 continents for each month from January 2020 - January 2021
### _Pre-Processing_
- Parsed .fasta file, retrieving nucleotide sequences and sequence ID
- Depending on Clustering method used, trimmed sequences to a uniform length
- Fed ID and sequence into 2x2 matrix
- Converted from string to Array
### _Clustering_
- K-Means 
  - Defined levenshtein function and applied to sequences to produce similarity ratios
  - Produced square matrix containing values
  - Applied K-Means clustering algorithm on matrix using Levenshtein Distance Metric
- Agglomerative
  - Formatted matrix so that each sequence is compared against reference (X) and UK Variant (Y)
  - Defined levenshtein function and applied to sequences to produce similarity ratios
  - Applied Agglomerative clustering on these values using L1 or Euclidean Affinity
### _Results_
- Produced scatter plots for all clustering results
- Due to lack of uniformity in order of clustering results, produced a hash-map to align cluster labels with MEGA sample data
- Computed Accuracy and Purity scores for each result
### _Libraries Used_
Sklearn, plotly, Pandas, numPy, Matplot, Biopython

## Data
### Agglomerative Dendogram
![agglomerativeDendrogram](https://user-images.githubusercontent.com/71059181/116838284-aa86ef00-ab82-11eb-8bdf-eaaa2cf609ef.png)

### Agglomerative Scatterplots
**Euclidean**  
![euclidianAgglomerative2](https://user-images.githubusercontent.com/71059181/116838285-ab1f8580-ab82-11eb-902a-aea030035b0f.png)
![euclidianAgglomerative3](https://user-images.githubusercontent.com/71059181/116838287-ac50b280-ab82-11eb-9fd8-f1ecfa0e738a.png)
![euclidianAgglomerative4](https://user-images.githubusercontent.com/71059181/116838288-ace94900-ab82-11eb-87c3-5959af835508.png)  
**L1**    
![L1agglomerative2](https://user-images.githubusercontent.com/71059181/116838293-ae1a7600-ab82-11eb-877f-cc64c23bfce7.png)
![L1agglomerative3](https://user-images.githubusercontent.com/71059181/116838294-ae1a7600-ab82-11eb-830b-c9e89af39858.png)
![L1agglomerative4](https://user-images.githubusercontent.com/71059181/116838296-aeb30c80-ab82-11eb-9ea8-d26ec57515f2.png)

### K-Means Dendogram
![kmeansDendrogram](https://user-images.githubusercontent.com/71059181/116838292-ae1a7600-ab82-11eb-84a2-c504c03f96a5.png)

### K-Means Scatterplots
![kmeans2clusters](https://user-images.githubusercontent.com/71059181/116838289-ace94900-ab82-11eb-8038-777bc7494563.png)
![kmeans3clusters](https://user-images.githubusercontent.com/71059181/116838290-ad81df80-ab82-11eb-8ff6-572af8834559.png)
![kmeans4clusters](https://user-images.githubusercontent.com/71059181/116838291-ad81df80-ab82-11eb-8a85-c6ea5b31bfc2.png)

## Conclusion + Future steps
Our preliminary results show that there is promise to this methodology. Our models show that they perform better than random chance and with the proper adjustments, can be made to be highly accurate and efficient. It is also important to note that 9 different models were run simultaneously and produced results in under a minute, 4.5 times faster than MEGA. Ideally, these models can lead to efficient and correct predictions of vaccine efficacy, resistance and more on not only COVID but other fast-mutating viruses as well.

In the future, we plan on implementing:
- Streamlined data retrieval from database
- Implement gene-specific Distance Metric
- Experiment with a wider variety of clustering methods

## Contributors
- [Divya Gollapalli](https://github.com/divya-g-248)
- [Rushi Surampudi](https://github.com/rushisurampudi)
- [Areeba Qazi](https://github.com/areebakq)
- [Shriya Jejurkar](https://github.com/sjejurkar23)
- Team Lead - [Bryant Hou](https://github.com/BryantH24)
- Faculty Advisor - [Dr. Anjum Chida](https://cs.utdallas.edu/people/faculty/chida-anjum/)


