import pandas as pd

r_filenameTSV = 'C:/Users/90531/Desktop/Genom2/CosmicMutantExportCensus.tsv'                          # names of files to read from

tsv_read = pd.read_csv(r_filenameTSV, sep='\t')                                                       # read the data

#print(tsv_read)                                                                                      # print the first 10 records      

######liver-carcinoma##########################################################################################

w_livercarcinoma = 'C:/Users/90531/Desktop/Genom2/Liver-carcinoma.tsv'                     

filter1 = tsv_read[(tsv_read['Primary site']== 'liver') & (tsv_read['Primary histology']== 'carcinoma')]

filter2 = filter1.loc[:, ['Accession Number' , 'Mutation CDS']]

"""
with open(w_livercarcinoma,'w') as write_tsv:
    write_tsv.write(filter2.to_csv(sep='\t', index=False))
"""
######skin-carcinoma##########################################################################################

w_skincarcinoma = 'C:/Users/90531/Desktop/Genom2/Skin-carcinoma.tsv'  

filter3 = tsv_read[(tsv_read['Primary site']== 'skin') & (tsv_read['Primary histology']== 'carcinoma')]

filter4 = filter3.loc[:, ['Accession Number' , 'Mutation CDS']]
print(filter4)
"""
with open(w_skincarcinoma,'w') as write_tsv:
    write_tsv.write(filter4.to_csv(sep='\t', index=False))
"""
######Liver-carcinoma hastalarında en çok karşılaşılan 30 gen######################################################################################

w_liverGen = 'C:/Users/90531/Desktop/Genom2/liverGen.tsv'

count = filter1['Gene name']
sortedGen = count.value_counts()                      #gen sayıları büyükten küçüğe sıralandı
sortedGen = sortedGen.head(30)
"""
with open(w_liverGen,'w') as write_tsv:
    write_tsv.write(sortedGen.to_csv(sep='\t', index=False))
"""
########skin-carcinoma hastalarıda en çok karşılaşılan 30 gen#####################################################################################

w_skinGen = 'C:/Users/90531/Desktop/Genom2/skinGen.tsv'

count2 = filter3['Gene name']
sortedGen2 = count2.value_counts()                      #gen sayıları büyükten küçüğe sıralandı
sortedGen2 = sortedGen2.head(30)
"""
with open(w_skinGen,'w') as write_tsv:
    write_tsv.write(sortedGen2.to_csv(sep='\t', index=False))
"""
######skin ve Liver karsinomalarında ortak yer alan genler###################################################### 

w_skin_livercarcinoma = 'C:/Users/90531/Desktop/Genom2/skin_livercarcinoma.tsv'

filter5 = filter1.loc[: , ['Gene name']]           #liver karsinoma hastalığı gen sütunu
filter6 = filter3.loc[: , ['Gene name']]           #skin karsinoma hastalığı gen sütunu

filter5 = filter5.drop_duplicates()                #tekrarlanan gen isimleri silindi
filter6 = filter6.drop_duplicates()

intersected = pd.merge(filter5, filter6, how='inner')       #ortak genler belirlendi
"""
with open(w_skin_livercarcinoma,'w') as write_tsv:
    write_tsv.write(filter5.to_csv(sep='\t', index=False))
"""
### Malignant_melanoma , skin ve Liver karsinomalarında ortak mutasyonlu genler##################################

w_skin_liver_malignant_melanoma = 'C:/Users/90531/Desktop/Genom2/skin_liver_malignantmelanoma.tsv'

filter7 = tsv_read[(tsv_read['Primary histology']== 'malignant_melanoma')]

filter8 = filter7.loc[:, ['Mutation CDS']]                        #malignant_melanoma mutasyonlu gen sütunu
filter1 = filter1.loc[:, ['Mutation CDS']]                        #liver mutasyonlu gen sütunu
filter3 = filter3.loc[:, ['Mutation CDS']]                        #skin mutasyonlu gen sütunu

filter8 = filter8.drop_duplicates()                               #tekrarlanan mutasyonlu gen isimleri silindi
filter1 = filter1.drop_duplicates()
filter3 = filter3.drop_duplicates()

intersected2 = pd.merge(filter8, filter1, how='inner')            #ortak genler belirlendi
intersected3 = pd.merge(intersected2 , filter3 , how = 'inner')
"""
with open(w_skin_liver_malignant_melanoma,'w') as write_tsv:
    write_tsv.write(intersected3.to_csv(sep='\t', index=False))
"""