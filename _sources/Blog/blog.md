# Blog

## 🗓️ September, 2020: pyCATHY is born 

I started to work on pyCATHY in order to learn how to use the CATHY code originally developed in Fortran (first version developed by A. Binley dated from ??). The pyCATHY package consists in a python wrapper easing the numerical modelling of hydrology by developing object oriented class and modules to interact with core CATHY functions.

  
```python
import CATHY

simu_hydro = CATHY()
```

The aim is to develop a version-agnostic wrapper allowing to work on the differences branches of CATHY. In particular we'd like to integrate Data Assimilation capabilities and the plant model to the wrapper in order to mimick a soil-plant-interaction experiment run in the laboratory using geoelectrical ERT and MALM methods.

### Code repository

https://github.com/BenjMy/pycathy_wrapper

### Try me

launch_buttons:
  colab_url: "https://colab.research.google.com/drive/1Zl-VpMbrESu9MbeNpgUvXS6nfluno_dG#scrollTo=be0ef8fe-51bb-4d86-b00a-fa027c286ecf"
  
  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Zl-VpMbrESu9MbeNpgUvXS6nfluno_dG#scrollTo=be0ef8fe-51bb-4d86-b00a-fa027c286ecf)

More interactive exemple in prep in the open-code section of the book.


<!---

## 🗓️ ??: mapping tree roots in earth dikes

The Mediterranean Basin is prone to a plethora of natural hazards among which floods. Hydraulic structures are built to mitigate flood risk on population and assets. This risk is particularly crucial in the French Mediterranean region where about 2000 km of dikes only on PACA region, protect a large population.

Roots are recognized as an environmental hazard when growing in hydraulic earth structures such as flood protecting or channel levees and dams. The aim of this thesis is to better assess how woody vegetation compromises levee integrity.

To this end, we have to design a methodology including non-destructive methods and geophysical models in order to detect and localize woody roots growing in earth dikes. Several geophysical methods are often used for exploration, detection and 3D tomography of soil. Among them, some have been developed for tree roots detection such as electric – electromagnetic or acoustic prospection.


## 🗓️ ??: Investigation of a local tree size gradient in a mixed oak-maple forest

--->
