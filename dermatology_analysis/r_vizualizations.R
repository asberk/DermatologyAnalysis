library(stringi)
library(ggplot2)
library(feather)
library(tidyverse)

# -----------------------------------------------------------------------------
# Load Data
# -----------------------------------------------------------------------------

df <- read_feather('data/intermediate/disease_avgs_melt.feather')

# -----------------------------------------------------------------------------
# Support Functions
# -----------------------------------------------------------------------------

underscore_to_hrf <- function(vec){
    return(stri_trans_totitle(gsub("_", " ", vec)))
}

# -----------------------------------------------------------------------------
# Plot 1:
# -----------------------------------------------------------------------------


plot1 <-
    df %>% 
    filter(feature != 'age', feature != "family_history") %>% 
    mutate(feature = underscore_to_hrf(feature)) %>% 
    ggplot(aes(feature, y=value, fill=disease)) +
    geom_bar(stat="identity") +
    coord_flip() +
    facet_wrap(~disease) +
    labs(y="Average Score\n(min score = 0, max score = 3)", x="Feature") +
    theme_minimal() +
    theme(legend.position = "none", 
          axis.title=element_text(size=8))


# Save plot1
ggsave("figures/plot1.png", plot=plot1, dpi=300, height=4)
