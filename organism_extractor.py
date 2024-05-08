"""Mack, I have 200 URLs like this one
https://www.ncbi.nlm.nih.gov/protein/MDZ7745522.1?report=genbank&log$=prottop&blast_rank=12&RID=XFEP5U7R016

the list of URLs is below

there are just  a few fields I want from each of them.
Can you obtain these fields automatically from the list and put them in a table?

At this point I just want to know if it is an easy problem.
thanks

This data might help to answer a key question: did the ice-binding proteins first evolve in to bind to mineral substrates other than ice and then evolve to bind to ice later?
Dad

MAG: ice-binding family protein [Halobacteriales archaeon]
GenBank: MDZ7745522.1

Identical Proteins FASTA Graphics 

Go to:
LOCUS       MDZ7745522               217 aa            linear   ENV 21-DEC-2023
DEFINITION  MAG: ice-binding family protein [Halobacteriales archaeon].
ACCESSION   MDZ7745522
VERSION     MDZ7745522.1
DBLINK      BioProject: PRJNA1023877
            BioSample: SAMN38083154
DBSOURCE    accession JAXHLZ010000003.1
KEYWORDS    ENV; Metagenome Assembled Genome; MAG.
SOURCE      Halobacteriales archaeon (salt pan metagenome)
  ORGANISM  Halobacteriales archaeon
            Archaea; Euryarchaeota; Stenosarchaea group; Halobacteria;
            Halobacteriales.
REFERENCE   1  (residues 1 to 217)
  AUTHORS   Veloso,M., Waldisperg,A., Arros,P., Berrios-Pasten,C., Acosta,J.,
            Colque,H., Varas,M.A., Allende,M.L., Orellana,L.H. and
            Marcoleta,A.E.
  TITLE     Diversity, taxonomic novelty, and encoded functions of Salar de
            Ascotan microbiota as revealed by metagenome-assembled genomes
  JOURNAL   Unpublished
REFERENCE   2  (residues 1 to 217)
  AUTHORS   Marcoleta,A.E.
  TITLE     Direct Submission
  JOURNAL   Submitted (08-NOV-2023) Biology, Grupo de Microbiologia
            Integrativa, Facultad de Ciencias, Universidad de Chile, Las
            Palmeras 3425 Nunoa, Santiago, RM 780000, Chile
COMMENT     The annotation was added by the NCBI Prokaryotic Genome Annotation
            Pipeline (PGAP). Information about PGAP can be found here:
            https://www.ncbi.nlm.nih.gov/genome/annotation_prok/
            
            ##Genome-Assembly-Data-START##
            Assembly Date          :: 24-NOV-2022
            Assembly Method        :: metaFlye v. v1
            Genome Representation  :: Full
            Expected Final Version :: Yes
            Genome Coverage        :: 60,7x
            Sequencing Technology  :: Illumina NovaSeq; Oxford Nanopore MinION
            ##Genome-Assembly-Data-END##
            
            ##Genome-Annotation-Data-START##
            Annotation Provider               :: NCBI
            Annotation Date                   :: 12/15/2023 09:59:16
            Annotation Pipeline               :: NCBI Prokaryotic Genome
                                                 Annotation Pipeline (PGAP)
            Annotation Method                 :: Best-placed reference protein
                                                 set; GeneMarkS-2+
            Annotation Software revision      :: 6.6
            Features Annotated                :: Gene; CDS; rRNA; tRNA; ncRNA
            Genes (total)                     :: 2,666
            CDSs (total)                      :: 2,613
            Genes (coding)                    :: 2,437
            CDSs (with protein)               :: 2,437
            Genes (RNA)                       :: 53
            rRNAs                             :: 1, 1, 1 (5S, 16S, 23S)
            complete rRNAs                    :: 1, 1, 1 (5S, 16S, 23S)
            tRNAs                             :: 48
            ncRNAs                            :: 2
            Pseudo Genes (total)              :: 176
            CDSs (without protein)            :: 176
            Pseudo Genes (ambiguous residues) :: 0 of 176
            Pseudo Genes (frameshifted)       :: 121 of 176
            Pseudo Genes (incomplete)         :: 72 of 176
            Pseudo Genes (internal stop)      :: 16 of 176
            Pseudo Genes (multiple problems)  :: 28 of 176
            ##Genome-Annotation-Data-END##
FEATURES             Location/Qualifiers
     source          1..217
                     /organism="Halobacteriales archaeon"
                     /isolate="Salar_de_Ascotan_soil_MAG_ASO38"
                     /isolation_source="Salar de Ascotan soil"
                     /db_xref="taxon:1904752"
                     /environmental_sample
                     /country="Chile: Atacama desert"
                     /lat_lon="21.49825 S 68.257472 W"
                     /collection_date="2021-10-09"
                     /metagenome_source="salt pan metagenome"
                     /note="metagenomic"
     Protein         1..217
                     /product="ice-binding family protein"
                     /note="GO_function: GO:0050825 - ice binding [Evidence
                     IEA]"
     CDS             1..217
                     /locus_tag="U5K28_02995"
                     /coded_by="JAXHLZ010000003.1:146632..147285"
                     /inference="COORDINATES: protein motif:HMM:NF023425.3"
                     /note="Derived by automated computational analysis using
                     gene prediction method: Protein Homology.
                     GO_function: GO:0050825 - ice binding [Evidence IEA]"
                     /transl_table=11
ORIGIN      
        1 mdlgaagnyh ilsksgissv pasnvtgnig vspvdstait gfsltmdssg eyatsdqvgg
       61 rvyasdyaap tpsklttavs dmegaytdaa grsnpdvtel gggdisgmtl dpglykwgtg
      121 vvinedvtln ggaddtwifq iageltvasd tqvvlsggak aenvvwqaae rvslgtgaqf
      181 agtvltktgv dvrtgasakg rlyaqtdvtl eqatitr
 
 
 
"""
urls = [
"https://www.ncbi.nlm.nih.gov/protein/MDP3103863.1?report=genbank&log$=prottop&blast_rank=1&RID=XFEP5U7R016 ",
"https://www.ncbi.nlm.nih.gov/protein/MDO8873156.1?report=genbank&log$=prottop&blast_rank=2&RID=XFEP5U7R016 ",
"https://www.ncbi.nlm.nih.gov/protein/MBU4138769.1?report=genbank&log$=prottop&blast_rank=3&RID=XFEP5U7R016 ",
"https://www.ncbi.nlm.nih.gov/protein/MCX6685512.1?report=genbank&log$=prottop&blast_rank=4&RID=XFEP5U7R016 ",
"https://www.ncbi.nlm.nih.gov/protein/WP_304919595.1?report=genbank&log$=prottop&blast_rank=5&RID=XFEP5U7R01",
"https://www.ncbi.nlm.nih.gov/protein/WP_304918890.1?report=genbank&log$=prottop&blast_rank=6&RID=XFEP5U7R01",
"https://www.ncbi.nlm.nih.gov/protein/WP_304920199.1?report=genbank&log$=prottop&blast_rank=7&RID=XFEP5U7R01",
"https://www.ncbi.nlm.nih.gov/protein/MDO9325335.1?report=genbank&log$=prottop&blast_rank=8&RID=XFEP5U7R016 ",
"https://www.ncbi.nlm.nih.gov/protein/MDP3742195.1?report=genbank&log$=prottop&blast_rank=9&RID=XFEP5U7R016 ",
"https://www.ncbi.nlm.nih.gov/protein/MCZ7396303.1?report=genbank&log$=prottop&blast_rank=10&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8563700.1?report=genbank&log$=prottop&blast_rank=11&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDZ7745522.1?report=genbank&log$=prottop&blast_rank=12&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/OIO25135.1?report=genbank&log$=prottop&blast_rank=13&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MCX9025393.1?report=genbank&log$=prottop&blast_rank=14&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDZ7700833.1?report=genbank&log$=prottop&blast_rank=15&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MBI2445173.1?report=genbank&log$=prottop&blast_rank=16&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HWR97857.1?report=genbank&log$=prottop&blast_rank=17&RID=XFEP5U7R016", 
"https://www.ncbi.nlm.nih.gov/protein/MBE3136604.1?report=genbank&log$=prottop&blast_rank=18&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MCZ7357609.1?report=genbank&log$=prottop&blast_rank=19&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/NOL60813.1?report=genbank&log$=prottop&blast_rank=20&RID=XFEP5U7R016", 
"https://www.ncbi.nlm.nih.gov/protein/MBS3076254.1?report=genbank&log$=prottop&blast_rank=21&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/WP_009887486.1?report=genbank&log$=prottop&blast_rank=22&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/HEX9906870.1?report=genbank&log$=prottop&blast_rank=23&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/WP_236942555.1?report=genbank&log$=prottop&blast_rank=24&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/MDO8556421.1?report=genbank&log$=prottop&blast_rank=25&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HME56504.1?report=genbank&log$=prottop&blast_rank=26&RID=XFEP5U7R016", 
"https://www.ncbi.nlm.nih.gov/protein/MBU4075636.1?report=genbank&log$=prottop&blast_rank=27&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8661418.1?report=genbank&log$=prottop&blast_rank=28&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDZ7701400.1?report=genbank&log$=prottop&blast_rank=29&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8517311.1?report=genbank&log$=prottop&blast_rank=30&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/OGS56693.1?report=genbank&log$=prottop&blast_rank=31&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/MBU1915386.1?report=genbank&log$=prottop&blast_rank=32&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8554794.1?report=genbank&log$=prottop&blast_rank=33&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8873153.1?report=genbank&log$=prottop&blast_rank=34&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MBX8636586.1?report=genbank&log$=prottop&blast_rank=35&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MCL6015072.1?report=genbank&log$=prottop&blast_rank=36&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MBI2445175.1?report=genbank&log$=prottop&blast_rank=37&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MCU4801588.1?report=genbank&log$=prottop&blast_rank=38&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDH2905673.1?report=genbank&log$=prottop&blast_rank=39&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MBU0685189.1?report=genbank&log$=prottop&blast_rank=40&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8873550.1?report=genbank&log$=prottop&blast_rank=41&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HME19337.1?report=genbank&log$=prottop&blast_rank=42&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/PJE81337.1?report=genbank&log$=prottop&blast_rank=43&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/HSA35139.1?report=genbank&log$=prottop&blast_rank=44&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/MDO8554799.1?report=genbank&log$=prottop&blast_rank=45&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HPR97773.1?report=genbank&log$=prottop&blast_rank=46&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/HNX46997.1?report=genbank&log$=prottop&blast_rank=47&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/MDO8725985.1?report=genbank&log$=prottop&blast_rank=48&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/KHO48997.1?report=genbank&log$=prottop&blast_rank=49&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/MCX6652634.1?report=genbank&log$=prottop&blast_rank=50&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/OGS55662.1?report=genbank&log$=prottop&blast_rank=51&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/MBW4258520.1?report=genbank&log$=prottop&blast_rank=52&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HME56501.1?report=genbank&log$=prottop&blast_rank=53&RID=XFEP5U7R016",  
"https://www.ncbi.nlm.nih.gov/protein/HIH23586.1?report=genbank&log$=prottop&blast_rank=54&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/MDO8537943.1?report=genbank&log$=prottop&blast_rank=55&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/WP_077076086.1?report=genbank&log$=prottop&blast_rank=56&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/HEX7391906.1?report=genbank&log$=prottop&blast_rank=57&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HIH03457.1?report=genbank&log$=prottop&blast_rank=58&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/SJK84579.1?report=genbank&log$=prottop&blast_rank=59&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/WP_298275473.1?report=genbank&log$=prottop&blast_rank=60&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/MDO8528707.1?report=genbank&log$=prottop&blast_rank=61&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HIJ17456.1?report=genbank&log$=prottop&blast_rank=62&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/MDP2901087.1?report=genbank&log$=prottop&blast_rank=63&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HLC61509.1?report=genbank&log$=prottop&blast_rank=64&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/MBU0685601.1?report=genbank&log$=prottop&blast_rank=65&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDP3992097.1?report=genbank&log$=prottop&blast_rank=66&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDO8537288.1?report=genbank&log$=prottop&blast_rank=67&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/WP_238709336.1?report=genbank&log$=prottop&blast_rank=68&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/MDZ7687581.1?report=genbank&log$=prottop&blast_rank=69&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDP2628948.1?report=genbank&log$=prottop&blast_rank=70&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDD1689652.1?report=genbank&log$=prottop&blast_rank=71&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDA4113734.1?report=genbank&log$=prottop&blast_rank=72&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MCJ7463854.1?report=genbank&log$=prottop&blast_rank=73&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/WP_276255516.1?report=genbank&log$=prottop&blast_rank=74&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/WP_198324425.1?report=genbank&log$=prottop&blast_rank=75&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/ABS56009.1?report=genbank&log$=prottop&blast_rank=76&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/MBU0685600.1?report=genbank&log$=prottop&blast_rank=77&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HIH50485.1?report=genbank&log$=prottop&blast_rank=78&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/WP_089671545.1?report=genbank&log$=prottop&blast_rank=79&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/ACL15585.1?report=genbank&log$=prottop&blast_rank=80&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/MDD3174919.1?report=genbank&log$=prottop&blast_rank=81&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HEX9906871.1?report=genbank&log$=prottop&blast_rank=82&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/HMF30516.1?report=genbank&log$=prottop&blast_rank=83&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/WP_255169182.1?report=genbank&log$=prottop&blast_rank=84&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/MCU4972809.1?report=genbank&log$=prottop&blast_rank=85&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MCU4740543.1?report=genbank&log$=prottop&blast_rank=86&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/ELZ12651.1?report=genbank&log$=prottop&blast_rank=87&RID=XFEP5U7R016 ", 
"https://www.ncbi.nlm.nih.gov/protein/WP_241430159.1?report=genbank&log$=prottop&blast_rank=88&RID=XFEP5U7R0",
"https://www.ncbi.nlm.nih.gov/protein/MDO8511584.1?report=genbank&log$=prottop&blast_rank=89&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MDD1743077.1?report=genbank&log$=prottop&blast_rank=90&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MBW4258519.1?report=genbank&log$=prottop&blast_rank=91&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/MBU1914646.1?report=genbank&log$=prottop&blast_rank=92&RID=XFEP5U7R016",
"https://www.ncbi.nlm.nih.gov/protein/WP_076143156.1?report=genbank&log$=prottop&blast_rank=93&RID=XFEP5U7R0",
]

import pandas as pd
import requests
from bs4 import BeautifulSoup


# Function to extract data from html content
def extract_data_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    result = {'VERSION': None, 'DBLINK': None, 'SOURCE': None, 'ORGANISM': None,
              '/organism=': None, '/isolate=': None, '/isolation_source=': None,
              '/country=': None, '/metagenome_source=': None}
    
    genbank = soup.find('pre', class_="genbank")
    if genbank:  # Check if genbank element is found
        text = genbank.get_text()
        lines = text.split('\n')
        for line in lines:
            for key in result.keys():
                if line.startswith(key):
                    # Extract the information after the key and strip it to remove extra spaces
                    result[key] = line.replace(key, '').strip()
                    break  # Move to the next line once the key is found and processed
    return result


html_contents = []
for url in urls[:1]:
    response = requests.get(url)
    html_contents.append(response.content)


# Simulate the process of fetching each page and extracting data
for html_content in html_contents:
    extract_data_from_html(html_content)

# Create DataFrame from the extracted data
df = pd.DataFrame(extracted_data)
df

response.content.decode('utf-8').split('\n')

#%%
import requests
from bs4 import BeautifulSoup

url = "https://www.ncbi.nlm.nih.gov/protein/MDP3103863.1?report=genbank&log$=prottop&blast_rank=1&RID=XFEP5U7R016#gotoMDP3103863.1_0"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# %%
