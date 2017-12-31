
# coding: utf-8

# In[16]:

import pandas as pd


# In[17]:

excel_ds = 'dataset.xlsx'
subjects = pd.read_excel(excel_ds, index_col = 0)


# In[18]:

subjects.shape


# In[19]:

subjects.head()


# In[20]:

subjects.tail()


# In[21]:

best_composite_index = subjects.sort_values(['CompositeIndex'], ascending=False)


# In[22]:

best_composite_index[["CompositeIndex","CompositeIndicator","DistrictCode","UpazilaCode","Village","Sex",
                      "Disability","Religion","adolescent_girl","Lact_mother","Main_Sanitation_Option",
                      "Main_Water_Source","Beneficiary Type","Main_IGAName","FirstAssetYear",
                     "shp3_schoolAttending","shp3_cashSavings"]].head()


# In[23]:

best_composite_index[["CompositeIndex","CompositeIndicator","DistrictCode","UpazilaCode","Village","Sex",
                      "Disability","Religion","adolescent_girl","Lact_mother","Main_Sanitation_Option",
                      "Main_Water_Source","Beneficiary Type","Main_IGAName","FirstAssetYear",
                     "shp3_schoolAttending","shp3_cashSavings"]].tail()


# In[24]:

best_composite_indic = subjects.sort_values(['CompositeIndicator'], ascending=False)


# In[25]:

best_composite_indic[["CompositeIndex","CompositeIndicator","DistrictCode","UpazilaCode","Village","Sex",
                      "Disability","Religion","adolescent_girl","Lact_mother","Main_Sanitation_Option",
                      "Main_Water_Source","Beneficiary Type","Main_IGAName","FirstAssetYear",
                     "shp3_schoolAttending","shp3_cashSavings"]].head()


# In[26]:

best_composite_index[["CompositeIndex","CompositeIndicator","DistrictCode","UpazilaCode","Village","Sex",
                      "Disability","Religion","adolescent_girl","Lact_mother","Main_Sanitation_Option",
                      "Main_Water_Source","Beneficiary Type","Main_IGAName","FirstAssetYear",
                     "shp3_schoolAttending","shp3_cashSavings"]].tail()


# In[27]:

from bokeh.plotting import figure, show
from bokeh.io import output_notebook
output_notebook()


# In[28]:

sex1 = subjects.loc[subjects["Sex"]==1]
sex2 = subjects.loc[subjects["Sex"]==2]
TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
mp = figure(title="                          Does Sex have an impact on CIndex and CIndicator?",
            x_axis_label='CompositeIndex', 
            y_axis_label='CompositeIndicator', tools = TOOLS)

mp.circle(sex1["CompositeIndex"],sex1["CompositeIndicator"],legend="Sex 1", alpha=0.5, fill_color="blue", 
          fill_alpha=0.6, line_color="blue", size=6)
mp.circle(sex2["CompositeIndex"],sex2["CompositeIndicator"],legend="Sex 2", alpha=0.5, fill_color="red", 
          fill_alpha=0.6, line_color="red", size=6)
show(mp)



# In[29]:

from bokeh.charts import Bar, output_file, show

mp = Bar(subjects, 'Sex', values='CompositeIndex', agg = 'mean',
        title="     Mean of cIndex by Sex", bar_width=0.4, color = 'navy')

show(mp)


# In[30]:

from bokeh.charts import Bar, output_file, show

mp = Bar(subjects, label='DistrictCode', values='CompositeIndex', agg='median', group = 'Beneficiary Type',
        title="Median CompositeIndex by District Code grouped by Beneficiary Type", legend='top_right')

show(mp)


# In[31]:

from bokeh.charts import Histogram, output_file, show

mp = Histogram(subjects['CompositeIndicator'], title="Composite Indicator Distribution")

output_file("histogramCIndicator.html")

show(mp)


# In[32]:

from bokeh.charts import Histogram, output_file, show

mp = Histogram(subjects['CompositeIndex'], title="Composite Index Distribution")

output_file("histogramCIndex.html")

show(mp)


# In[33]:

from bokeh.charts import Bar, output_file, show

mp = Bar(subjects, label='UnionCode', values='CompositeIndicator', agg='mean', group = 'shp3_cashSavings',
        title="Median CompositeIndicator by Union Code grouped by Cash Savings", legend='top_right')

show(mp)


# In[34]:

from bokeh.charts import Bar, output_file, show

mp = Bar(subjects, label='DistrictCode', values='CompositeIndex', agg='mean', group = 'shp3_cashSavings',
        title="Median CompositeIndex by District Code grouped by Cash Savings", legend='top_right')

show(mp)


# In[60]:

from bokeh.plotting import figure, show

mp = figure(title="CompositeIndex and CompositeIndicator",
            x_axis_label='CompositeIndex', 
            y_axis_label='CompositeIndicator')

mp.circle(subjects['CompositeIndex'], subjects['CompositeIndicator'], size = 5, alpha = 0.8, 
          fill_color="red", line_color="navy", line_width=3)

show(mp)


# In[36]:

cIdic = subjects.loc[:,"CompositeIndicator"].values
print(len(cIdic))


# In[37]:

cIdex = subjects.loc[:,"CompositeIndex"].values
print(len(cIdex))


# In[38]:

len(subjects.CompositeIndex.unique()) # 189 classes with certain compositeIndex


# In[39]:

subjects_selected_cols = subjects[["CompositeIndex","CompositeIndicator","DistrictCode","UpazilaCode","Village","Sex",
                      "Disability","Religion","adolescent_girl","Lact_mother","Main_Sanitation_Option",
                      "Main_Water_Source","Beneficiary Type","Main_IGAName","FirstAssetYear",
                     "shp3_schoolAttending","shp3_cashSavings"]]


# In[40]:

import matplotlib.pyplot as plt
ax = subjects_selected_cols.plot(figsize=(15,10),kind = 'density',title = 'KDE of variables')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5));
plt.show()


# In[41]:

ax = subjects_selected_cols.plot(figsize=(15,10),kind = 'line',title = 'Variance of Variables')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5));
plt.show()


# In[42]:

import numpy as np
X = subjects[["DistrictCode","UpazilaCode","Sex","femaleHeaded","OldAges",
                      "Disability","Religion","adolescent_girl","Lact_mother","Main_Sanitation_Option",
                      "Main_Water_Source","Total_IGDValue",
                     "shp3_schoolAttending","shp3_cashSavings"]]

X.replace([np.inf, -np.inf], np.nan).dropna(axis=1)

y = subjects[["CompositeIndex"]]

y.replace([np.inf, -np.inf], np.nan).dropna(axis=1)


# In[43]:

from sklearn.preprocessing import StandardScaler, Imputer

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(X)
print(X)

X_std = StandardScaler().fit_transform(X)


# In[44]:

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X_std)


# In[45]:

print(X_std.shape)
print(Y_sklearn.shape)


# In[46]:

print(sklearn_pca.components_)


# In[47]:

print(sklearn_pca.explained_variance_)


# In[68]:

plt.figure(figsize=(15,10))
plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1],
            c=y.CompositeIndex, edgecolor='none', alpha=1,
            cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar().set_label('CompositeIndex');
plt.show()


# In[81]:

y2 = subjects[["Sex"]]

y2.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
#print(y2)
hi = y2.iloc[:,0]
print(max(hi))
print(min(hi))


# ### Looking for clusters
# 
# 1. *Todo*
# 
#   * A 3d scatter plot
#   * k-means

# In[82]:

plt.figure(figsize=(15,10))
plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1],
            c=y2.Sex, edgecolor='blue', alpha=1,
            cmap=plt.cm.get_cmap('nipy_spectral', 2))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar().set_label('Sex');
plt.show()


# In[77]:

y2 = subjects[["shp3_cashSavings"]]

y2.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
#print(y2)
hi = y2.iloc[:,0]
print(max(hi))
print(min(hi))


# In[79]:

plt.figure(figsize=(15,10))
plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1],
            c=y2.shp3_cashSavings, edgecolor='red', alpha=1,
            cmap=plt.cm.get_cmap('nipy_spectral', 2))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar().set_label('Cash Savings');
plt.show()


# In[86]:

# CompositeIndicator
y4 = subjects[["CompositeIndicator"]]

y4.replace([np.inf, -np.inf], np.nan).dropna(axis=1)
#print(y4)
hi = y4.iloc[:,0]
print(max(hi))
print(min(hi))


# In[88]:

plt.figure(figsize=(15,10))
plt.scatter(Y_sklearn[:, 0], Y_sklearn[:, 1],
            c=y4.CompositeIndicator, edgecolor='orange', alpha=1,
            cmap=plt.cm.get_cmap('nipy_spectral', 5))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar().set_label('CompositeIndicator');
plt.show()


# In[52]:

get_ipython().magic('load_ext py_d3')


# In[53]:

get_ipython().run_cell_magic('d3', '', '\n<g></g>\n\n<script>\nd3.select("g").text("Testing d3, ...")\n</script>')


# In[ ]:



