########
# Name: Wikipedia
# Author: Zane Wolf
# Date Created: 2/19/2021
# Purpose: To scrape transcripts of star trek shows from 
########

#housekeeping
library(rvest)
library(purrr)
library(stringr)
library(stringi)
library(dplyr)
library(ggthemes)
library(ggplot2)
library(magrittr)
library(data.table)
library(tidyverse)

# grab the url of the page you would like to scrape
url <- "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"

webpage <- read_html(url)

tables <-  webpage %>%
  html_nodes("table.wikitable") %>%
  html_table(fill=T) # returns a tibble. tibbles are weird. 

#  I now have an R table 
df <- tables[[1]] #extract the table

# however, it's rather unweildy and I'd rather have a table where the column is simply 'Nobel' and the value in that column is the prize (Chemistry/Physics/Medicine/etc)

df_colnames <- colnames(df)


df_melted <- melt(df, id.vars=c("Year"), measure.vars=c(df_colnames[2:7]))

# and need to separate out names where there were multiple recipients each year
df_melted %>% separate_rows(value, sep=";", convert=TRUE)


