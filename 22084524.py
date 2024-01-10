import pandas as pds
import seaborn as seb
import matplotlib.pyplot as plo

infograph = pds.read_csv('/home/priyanka/Infographics_Project/diabetes_prediction_dataset.csv')
infograph=infograph.dropna()
infograph['diabetes'] = infograph['diabetes'].replace([0], 'absence of diabetes')
infograph['diabetes'] = infograph['diabetes'].replace([1], 'presence of diabetes')
infograph
seb.set_theme(style="whitegrid")
plo.figure(figsize=(6, 5))

sx= seb.countplot(x ='diabetes', data = infograph, saturation= 0.5, palette=['red', 'skyblue'])
for label in sx.containers:
    sx.bar_label(label)
    
plo.title("diabetes class", fontsize=16)
plo.ylabel("count", fontsize=13)
plo.xlabel("class", fontsize=13)
plo.savefig('figure1.png')
plo.figure(figsize=(6, 5))
sx= plo.hist(infograph['bmi'], color='salmon')

plo.title("Body Mass Index", fontsize=16)
plo.ylabel("count", fontsize=13)
plo.xlabel("bmi range", fontsize=13)
plo.savefig('figure2.png')

plo.figure(figsize=(6, 5))
sx= plo.hist(infograph['bmi'], color='salmon')

plo.title("Body Mass Index", fontsize=16)
plo.ylabel("count", fontsize=13)
plo.xlabel("bmi range", fontsize=13)
plo.savefig('figure_2.png')

sx= seb.countplot(x ='gender', hue='diabetes', data = infograph, saturation= 0.5, palette=['orange', 'maroon'])
for label in sx.containers:
    sx.bar_label(label)

plo.legend(loc='upper left', bbox_to_anchor=(0.59, .89))
plo.title("Diabetes with respect to gender", fontsize=16)

plo.savefig('figure3.png')

sx= seb.boxplot(x ="age", y ="diabetes", data = infograph, palette=['orangered', 'green'], saturation= 0.6)
plo.title("Diabetes with respect to gender", fontsize=16)

plo.savefig('figure4.png')



