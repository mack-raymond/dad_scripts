# List of URLs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd

urls = [
"https://www.ncbi.nlm.nih.gov/protein/HKZ49248.1?report=genbank&log$=prottop&blast_rank=1&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HKZ98357.1?report=genbank&log$=prottop&blast_rank=2&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HKZ49255.1?report=genbank&log$=prottop&blast_rank=3&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HKZ49254.1?report=genbank&log$=prottop&blast_rank=4&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HKZ98356.1?report=genbank&log$=prottop&blast_rank=5&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEV8361550.1?report=genbank&log$=prottop&blast_rank=6&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4331080.1?report=genbank&log$=prottop&blast_rank=7&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HXQ93928.1?report=genbank&log$=prottop&blast_rank=8&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/NNN17896.1?report=genbank&log$=prottop&blast_rank=9&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HUZ79434.1?report=genbank&log$=prottop&blast_rank=10&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEV8050666.1?report=genbank&log$=prottop&blast_rank=11&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4345165.1?report=genbank&log$=prottop&blast_rank=12&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4342426.1?report=genbank&log$=prottop&blast_rank=13&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4317128.1?report=genbank&log$=prottop&blast_rank=14&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4361513.1?report=genbank&log$=prottop&blast_rank=15&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4330898.1?report=genbank&log$=prottop&blast_rank=16&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4370592.1?report=genbank&log$=prottop&blast_rank=17&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEY1199249.1?report=genbank&log$=prottop&blast_rank=18&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HXQ95146.1?report=genbank&log$=prottop&blast_rank=19&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4337231.1?report=genbank&log$=prottop&blast_rank=20&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4342140.1?report=genbank&log$=prottop&blast_rank=21&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4317130.1?report=genbank&log$=prottop&blast_rank=22&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4356932.1?report=genbank&log$=prottop&blast_rank=23&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4356933.1?report=genbank&log$=prottop&blast_rank=24&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4337232.1?report=genbank&log$=prottop&blast_rank=25&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/NNN17392.1?report=genbank&log$=prottop&blast_rank=26&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4350354.1?report=genbank&log$=prottop&blast_rank=27&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4333728.1?report=genbank&log$=prottop&blast_rank=28&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4333727.1?report=genbank&log$=prottop&blast_rank=29&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4329304.1?report=genbank&log$=prottop&blast_rank=30&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4323798.1?report=genbank&log$=prottop&blast_rank=31&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HLG24334.1?report=genbank&log$=prottop&blast_rank=32&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4327921.1?report=genbank&log$=prottop&blast_rank=33&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HLN50769.1?report=genbank&log$=prottop&blast_rank=34&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HZS74796.1?report=genbank&log$=prottop&blast_rank=35&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4350355.1?report=genbank&log$=prottop&blast_rank=36&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDO8724684.1?report=genbank&log$=prottop&blast_rank=37&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4368840.1?report=genbank&log$=prottop&blast_rank=38&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEY1198041.1?report=genbank&log$=prottop&blast_rank=39&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET6459009.1?report=genbank&log$=prottop&blast_rank=40&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HWY34231.1?report=genbank&log$=prottop&blast_rank=41&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDH2899713.1?report=genbank&log$=prottop&blast_rank=42&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/QLH08823.1?report=genbank&log$=prottop&blast_rank=43&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_179369338.1?report=genbank&log$=prottop&blast_rank=44&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/OGS59824.1?report=genbank&log$=prottop&blast_rank=45&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_052347570.1?report=genbank&log$=prottop&blast_rank=46&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCX9028957.1?report=genbank&log$=prottop&blast_rank=47&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/CAG0957755.1?report=genbank&log$=prottop&blast_rank=48&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEX4919544.1?report=genbank&log$=prottop&blast_rank=49&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HVC76924.1?report=genbank&log$=prottop&blast_rank=50&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET6457337.1?report=genbank&log$=prottop&blast_rank=51&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HVA21912.1?report=genbank&log$=prottop&blast_rank=52&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET6457477.1?report=genbank&log$=prottop&blast_rank=53&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDQ1280443.1?report=genbank&log$=prottop&blast_rank=54&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HZS72968.1?report=genbank&log$=prottop&blast_rank=55&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDP3992099.1?report=genbank&log$=prottop&blast_rank=57&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_052347571.1?report=genbank&log$=prottop&blast_rank=66&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_302719419.1?report=genbank&log$=prottop&blast_rank=67&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDA3836399.1?report=genbank&log$=prottop&blast_rank=69&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HUY56571.1?report=genbank&log$=prottop&blast_rank=71&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET6310288.1?report=genbank&log$=prottop&blast_rank=85&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MEA3137813.1?report=genbank&log$=prottop&blast_rank=88&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4329303.1?report=genbank&log$=prottop&blast_rank=89&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDO8467498.1?report=genbank&log$=prottop&blast_rank=90&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_011991321.1?report=genbank&log$=prottop&blast_rank=92&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4338056.1?report=genbank&log$=prottop&blast_rank=94&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MEA3165182.1?report=genbank&log$=prottop&blast_rank=101&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_304919299.1?report=genbank&log$=prottop&blast_rank=102&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_304838419.1?report=genbank&log$=prottop&blast_rank=103&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEX7391907.1?report=genbank&log$=prottop&blast_rank=108&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4324042.1?report=genbank&log$=prottop&blast_rank=116&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/QLH08825.1?report=genbank&log$=prottop&blast_rank=123&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HME56502.1?report=genbank&log$=prottop&blast_rank=124&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HWQ67532.1?report=genbank&log$=prottop&blast_rank=126&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEX5672720.1?report=genbank&log$=prottop&blast_rank=133&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/OGS42941.1?report=genbank&log$=prottop&blast_rank=134&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCJ7697748.1?report=genbank&log$=prottop&blast_rank=135&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBN1133407.1?report=genbank&log$=prottop&blast_rank=145&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDO8634401.1?report=genbank&log$=prottop&blast_rank=148&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCJ7463855.1?report=genbank&log$=prottop&blast_rank=149&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBU0684247.1?report=genbank&log$=prottop&blast_rank=150&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/OGS56691.1?report=genbank&log$=prottop&blast_rank=151&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI15272.1?report=genbank&log$=prottop&blast_rank=157&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCR4327096.1?report=genbank&log$=prottop&blast_rank=160&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBS3078275.1?report=genbank&log$=prottop&blast_rank=161&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCX6706965.1?report=genbank&log$=prottop&blast_rank=162&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDD1689653.1?report=genbank&log$=prottop&blast_rank=165&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MEA3191188.1?report=genbank&log$=prottop&blast_rank=166&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEX7515054.1?report=genbank&log$=prottop&blast_rank=169&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_304918891.1?report=genbank&log$=prottop&blast_rank=170&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/OGS56513.1?report=genbank&log$=prottop&blast_rank=172&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCL4391165.1?report=genbank&log$=prottop&blast_rank=173&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HWQ65359.1?report=genbank&log$=prottop&blast_rank=174&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDZ7687926.1?report=genbank&log$=prottop&blast_rank=177&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HXL09357.1?report=genbank&log$=prottop&blast_rank=178&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/PIN93227.1?report=genbank&log$=prottop&blast_rank=179&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4333639.1?report=genbank&log$=prottop&blast_rank=180&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBZ6496370.1?report=genbank&log$=prottop&blast_rank=182&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_242634238.1?report=genbank&log$=prottop&blast_rank=183&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4324138.1?report=genbank&log$=prottop&blast_rank=184&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_226040395.1?report=genbank&log$=prottop&blast_rank=185&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/NNN16753.1?report=genbank&log$=prottop&blast_rank=186&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/OAQ54487.1?report=genbank&log$=prottop&blast_rank=188&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_012107037.1?report=genbank&log$=prottop&blast_rank=189&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBU0623560.1?report=genbank&log$=prottop&blast_rank=190&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_180840174.1?report=genbank&log$=prottop&blast_rank=191&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HMB45060.1?report=genbank&log$=prottop&blast_rank=192&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_238717352.1?report=genbank&log$=prottop&blast_rank=193&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_224214720.1?report=genbank&log$=prottop&blast_rank=194&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/PIN81724.1?report=genbank&log$=prottop&blast_rank=197&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_263020474.1?report=genbank&log$=prottop&blast_rank=199&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_285928391.1?report=genbank&log$=prottop&blast_rank=200&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MEA1930473.1?report=genbank&log$=prottop&blast_rank=201&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_016939654.1?report=genbank&log$=prottop&blast_rank=202&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_014963092.1?report=genbank&log$=prottop&blast_rank=203&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/AGB15433.1?report=genbank&log$=prottop&blast_rank=208&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_256396448.1?report=genbank&log$=prottop&blast_rank=210&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_245835463.1?report=genbank&log$=prottop&blast_rank=211&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_278305158.1?report=genbank&log$=prottop&blast_rank=212&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_281098736.1?report=genbank&log$=prottop&blast_rank=213&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_243637899.1?report=genbank&log$=prottop&blast_rank=214&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCE5297277.1?report=genbank&log$=prottop&blast_rank=215&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBU2559481.1?report=genbank&log$=prottop&blast_rank=216&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MBS3087884.1?report=genbank&log$=prottop&blast_rank=217&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/PJE81338.1?report=genbank&log$=prottop&blast_rank=218&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_302719665.1?report=genbank&log$=prottop&blast_rank=219&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_177316546.1?report=genbank&log$=prottop&blast_rank=220&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET7337704.1?report=genbank&log$=prottop&blast_rank=221&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_179368118.1?report=genbank&log$=prottop&blast_rank=222&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/QLH09289.1?report=genbank&log$=prottop&blast_rank=223&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_179369053.1?report=genbank&log$=prottop&blast_rank=224&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/QLH08532.1?report=genbank&log$=prottop&blast_rank=225&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCI4322073.1?report=genbank&log$=prottop&blast_rank=226&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HZS72969.1?report=genbank&log$=prottop&blast_rank=227&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MCZ7357921.1?report=genbank&log$=prottop&blast_rank=228&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_302719258.1?report=genbank&log$=prottop&blast_rank=229&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_081781874.1?report=genbank&log$=prottop&blast_rank=230&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_179368116.1?report=genbank&log$=prottop&blast_rank=231&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/WP_052347728.1?report=genbank&log$=prottop&blast_rank=232&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI44214.1?report=genbank&log$=prottop&blast_rank=233&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TLZ41254.1?report=genbank&log$=prottop&blast_rank=234&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDA4113463.1?report=genbank&log$=prottop&blast_rank=235&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET7336586.1?report=genbank&log$=prottop&blast_rank=209&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET6457472.1?report=genbank&log$=prottop&blast_rank=96&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/MDO9096828.1?report=genbank&log$=prottop&blast_rank=108&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI60803.1?report=genbank&log$=prottop&blast_rank=118&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI48246.1?report=genbank&log$=prottop&blast_rank=119&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI29589.1?report=genbank&log$=prottop&blast_rank=120&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI68186.1?report=genbank&log$=prottop&blast_rank=121&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HEX9240710.1?report=genbank&log$=prottop&blast_rank=122&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI68446.1?report=genbank&log$=prottop&blast_rank=126&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/TMI20112.1?report=genbank&log$=prottop&blast_rank=129&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HYL66774.1?report=genbank&log$=prottop&blast_rank=131&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HWY34695.1?report=genbank&log$=prottop&blast_rank=133&RID=Y2M430Z501N ",
"https://www.ncbi.nlm.nih.gov/protein/HET7336476.1?report=genbank&log$=prottop&blast_rank=141&RID=Y2M430Z501N ",

]
def parse_content(content):
    # Regular expressions for the fields
    version_re = re.compile(r"VERSION\s+(.+)")
    dblink_re = re.compile(r"DBLINK\s+(.+)")
    source_re = re.compile(r"SOURCE\s+(.+)")
    organism_re = re.compile(r"ORGANISM\s+(.+)")
    country_re = re.compile(r'/country="([^"]+)"')
    iosloate_re = re.compile(r'isolate="([^"]+)"')
    isolation_source_re = re.compile(r'/isolation_source="([^"]+)"')
    metagenome_source_re = re.compile(r'/metagenome_source="([^"]+)"')
    #/lat_lon="72.00 S 25.00 E"
    lat_lon_re = re.compile(r'/lat_lon="([^"]+)"')
    data = []

    # Search for matches in the content
    version_match = version_re.search(content)
    dblink_match = dblink_re.search(content)
    source_match = source_re.search(content)
    organism_match = organism_re.search(content)
    isolate_match = iosloate_re.search(content)
    isolation_source_match = isolation_source_re.search(content)
    metagenome_source_match = metagenome_source_re.search(content)
    country_match = country_re.search(content)
    lat_lon_match = lat_lon_re.search(content)

    # Extracting and printing the results
    version = version_match.group(1).strip() if version_match else None
    dblink = dblink_match.group(1).strip() if dblink_match else None
    source = source_match.group(1).strip() if source_match else None
    organism = organism_match.group(1).strip() if organism_match else None
    isolate = isolate_match.group(1) if isolate_match else None
    isolation_source = isolation_source_match.group(1) if isolation_source_match else None
    metagenome_source = metagenome_source_match.group(1) if metagenome_source_match else None
    country = country_match.group(1) if country_match else None
    lat_lon = lat_lon_match.group(1) if lat_lon_match else None

    return {
        "VERSION": version,
        "DBLINK": dblink,
        "SOURCE": source,
        "ORGANISM": organism,
        "ISOLATE": isolate,
        "ISOLATION_SOURCE": isolation_source,
        "METAGENOME_SOURCE": metagenome_source,
        "COUNTRY": country,
        "LAT_LON": lat_lon,
    }



with open("143 DUF3494-like.txt", "r") as file:
    data = file.read()
    pages = data.split("DEFINITION  ")

data = []
for content in pages:
    parsed_data = parse_content(content)
    data.append(parsed_data)
df = pd.DataFrame(data)


# Selenium WebDriver options
chrome_options = Options()

print("Starting the WebDriver service...")
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)


for url in urls:
    try:
        print(f"Accessing URL: {url}")
        driver.get(url)
        
        # Wait for the dynamic content to load
        print("Waiting for the dynamic content to load...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//pre"))  # Adjust the XPath as needed
        )
        
        # Extract the content
        print("Extracting the content...")
        content = driver.find_element(By.XPATH, "//pre").text  # Adjust the XPath as needed
        print(f"Content: {content}")  # Or process the content as needed

        # Parse the content using the defined method
        parsed_data = parse_content(content)

        # Print the extracted data
        for data in parsed_data:
            print(f"VERSION: {data['VERSION']}")
            print(f"DBLINK: {data['DBLINK']}")
            print(f"SOURCE: {data['SOURCE']}")
            print(f"ORGANISM: {data['ORGANISM']}")
            print(f"COUNTRY: {data['COUNTRY']}")

        # Add the parsed data to the main data list
        data.extend(parsed_data)
    except Exception as e:
        print(f"An error occurred while processing the URL: {url}")
        print(e)

driver.quit()

df = pd.DataFrame(data)
