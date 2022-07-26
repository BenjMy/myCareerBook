library(rmarkdown)
library(scholar)      # To request data from google scholar.
library(tidyverse)    # What do you do without?
library(hrbrthemes)
library(DT)

# Define the google scholar id
id <- '3kDP4-AAAAAJ&hl'       # Benjamin Mary

# Make an object called l with all the basic info of this id: name, affiliation, # of cites, H index, homepage ...
l <- get_profile(id)
name=l$name
tmp=strsplit(name, " ") %>% unlist()
last_name = tmp[length(tmp)]

# Show the last name
last_name


