# Open codes

Contribution to the development of open source codes

```{warning}
🚧 This page is still under construction 🚧
```


---
## CAGS

````{margin}
{bdg-primary}`Database` 
{bdg-primary}`Community engagement`
````

**The Catalog of Agrogeophysical Survey** is a platform putting together a database/catalog of agrogeophysical surveys in order to promote {term}`FAIR` practicies and boost future research.

- Catalog
- Notebooks
- Geophysical Metadata manager

[![github](https://img.shields.io/badge/view-github-green?logo=github)](https://github.com/agrogeophy/catalog) 


The catalog is part of the FAIRsharing platform - See its [related databases](https://fairsharing.org/3765).

FAIRsharing.org: CAGS; Catalog of Agrogeophysical Studies, FAIRsharing ID: http://beta.fairsharing.org/3765, Last Edited: Monday, January 31st 2022, 7:26, Last Editor:delphinedauga,Last Accessed: Wednesday, February 2nd 2022, 18:57





### Useful links

- project log on [ResearchGate](https://www.researchgate.net/project/CAGS-Catalogue-of-AgroGeophysical-Studies)

```{figure} ../img/logo_big.png
---
scale: 30%
align: center
---
Project logo
© S. Garré
```

```{warning}
Found a bug 🐛/ a typo ? [Email me](mailto:benjamin.mary@unipd.it)
```


---
## pyTSEB

````{margin}
{bdg-primary}`Evapotranspiration` 
{bdg-primary}`Inversion`
````

Open-source python package aiming at inverting Land Surface Temperature data using the **energy balance** formulation by {cite:p}`norman2000surface`. 

[![github](https://img.shields.io/badge/view-github-green?logo=github)](https://github.com/hectornieto/pyTSEB) 

## Contributions
- Fixing bugs
- Code documentation

### How to install

Install using setup.py:

    git clone https://github.com/hectornieto/pyTSEB
    cd pyTSEB
    python setup.py develop|install
    import pyTSEB

Or you can create a conda environment:

    conda env create -f environment.yml

### How to use

See github documentation 

### Notebook example

<!--[🧮 Code repository](https://github.com/BenjMy/dEXP_imaging/tree/master/notebooks_JGR)-->
	
### How to cite


```{warning}
Found a bug 🐛/ a typo ? [Email me](mailto:benjamin.mary@ica.csic.es)
```


---
## pyDEXP

````{margin}
{bdg-primary}`Potential Field Theory` 
{bdg-primary}`Inversion`
````

Open-source python package aiming at processing potential field data using the **dEXP theory** formulated by {cite:p}`fedi_dexp_2005`. 

[![github](https://img.shields.io/badge/view-github-green?logo=github)](https://github.com/BenjMy/dEXP_imaging) 


### How to install

Install using setup.py:

    git clone https://github.com/BenjMy/dEXP_imaging
    cd dEXP_imaging
    python setup.py develop|install
    import dEXP


### How to use

<!-- - [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBenjMy%2FdEXP_imaging&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mkhuulee/RC_Final_Project/master)
-->
### Notebook example

[🧮 Code repository](https://github.com/BenjMy/dEXP_imaging/tree/master/notebooks_JGR)
	
### How to cite

**Mary, B.**, Peruzzo, L., Wu, Y., and Cassiani, G. (2022). Advanced Potential Field Analysis Applied to Mise‐à‐la‐Masse Surveys for Leakage Detection. JGR Solid Earth 127. [doi:10.1029/2022JB024747](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2022JB024747)


```{warning}
Found a bug 🐛/ a typo ? [Email me](mailto:benjamin.mary@unipd.it)
```


---
## pyCATHY
````{margin}
{bdg-primary}`Hydrogeology` 
{bdg-primary}`Data Assimilation`
````
Open-source python package wrapper aiming at **coupling hydrological forward modelling with geophysical data** by {cite:p}`camporese_surface-subsurface_2010`. 

[![github](https://img.shields.io/badge/view-github-green?logo=github)](https://github.com/BenjMy/pycathy_wrapper) 

```{figure} ../img/pressure_slow.gif
---
scale: 30%
align: center
---
Result of a controlled irrigation in a rhizotron using CATHY
© B. Mary
```




### How to install

Install using setup.py:

    git clone https://github.com/BenjMy/pycathy_wrapper
    cd pycathy_wrapper
    python setup.py develop|install
    import pyCATHY

### How to use

<!-- - [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBenjMy%2FdEXP_imaging&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mkhuulee/RC_Final_Project/master)
-->

### Notebook example

The CATHY repository provides the {cite:p}`WEILL2013196` dataset example to test the installation. On top of that, we provide a computational notebook code to reproduce the results using the **pyCATHY wrapper** (https://github.com/BenjMy/pycathy_wrapper). 

The notebook illustrate how to work interactively: execute single cell, see partial results at different processing steps (preprocessing, processing, output)... You can share it to work collaboratively on it by sharing the link and execute it from another PC without any installation required.


Saturated area dynamics and streamflow generation from coupled surface–subsurface simulations and field observations
Weill, S., Altissimo, M., Cassiani, G., Deiana, R., Marani, M., Putti, M. (2013) Advances in Water Resources. 10.1016/j.advwatres.2013.06.007




[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Zl-VpMbrESu9MbeNpgUvXS6nfluno_dG?usp=sharing)



### How to cite

```{warning}
Found a bug 🐛/ a typo ? [Email me](mailto:benjamin.mary@unipd.it)
```


---
## iCSD
Inversion of Current Source Density data. Application to imaging of plant roots.

[![github](https://img.shields.io/badge/view-github-green?logo=github)](https://github.com/BenjMy/icsd_dev) 

### How to install

Install using setup.py:

    git clone https://github.com/BenjMy/icsd_dev
    cd icsd_dev
    python setup.py develop|install
    import icsd
    
### How to use

### How to cite


```{warning}
Found a bug 🐛/ a typo ? [Email me](mailto:benjamin.mary@unipd.it)
```


### Glossary

```{glossary}
FAIR
  FAIR data are data which meet principles of findability, accessibility, interoperability, and reusability.[1] 
```




