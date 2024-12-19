library(dplyr)

ssd <- read.csv("~/Travaille/Docking_Automation/donne_ssd.csv")
agro<- read.csv("~/Travaille/Docking_Automation/donne_agro.csv")

tableau_proche <- ssd %>%
  group_by(Enzyme, Ligand) %>%
  mutate(OptimalEnergy = min(Energy)) %>%
  ungroup()
tableau_proche_r <- subset(tableau_proche, !(LB == 0 & UB == 0))
tableau_proche_r <- tableau_proche_r[, c("Enzyme", "Ligand","OptimalEnergy", "Energy", "LB", "UB", "num_torsions")]

###### TABLEAU DES DOCKING PERTINANT, ceux qu'on aurait choisis d'étudier en détaille/ potentiel in vitro 
# https://pmc.ncbi.nlm.nih.gov/articles/PMC3041641/                                                                                                    

tableau_select <- subset(tableau_proche_r, (UB <= 2))
tableau_select <- subset(tableau_select, !(Enzyme=='fold_cplip2_s180a_alphafold_model_4'))
tableau_select <- subset(tableau_select, !(Enzyme=='fold_cplip2_s180a_palmitic_acid_model_4'))
tableau_select <- subset(tableau_select, !(Ligand=='Verytryl_Alcohol'))

result_ssd_optim <- tableau_select %>%
  group_by(Enzyme, Ligand) %>%
  slice_min(order_by = Energy, with_ties = FALSE) %>%
  ungroup()

write.csv(result_ssd_optim,"result_ssd_optim.csv", row.names = FALSE)

###### TABLEAU DES DOCKING PERTINANT 

###### TABLEAU DES DOCKING comparables avec les agros

tableau_select <- subset(tableau_proche_r, (UB <= 20))
tableau_select <- subset(tableau_select, !(Enzyme=='fold_cplip2_s180a_alphafold_model_4'))
tableau_select <- subset(tableau_select, !(Enzyme=='fold_cplip2_s180a_palmitic_acid_model_4'))
tableau_select <- subset(tableau_select, !(Ligand=='Verytryl_Alcohol'))

result_ssd <- tableau_select %>%
  group_by(Enzyme, Ligand) %>%
  slice_min(order_by = Energy, with_ties = FALSE) %>%
  ungroup()

write.csv(result_ssd,"result_ssd.csv", row.names = FALSE)
###### TABLEAU DES DOCKING comparables avec les agros

patterns_to_remove_ssd <- c("_wt_Alphafold","_alphafold_model_4",'_wt', "fold_","_DUBLINIENSIS","_chaina")

# Function to remove patterns
remove_patterns <- function(name, patterns) {
  for (pattern in patterns) {
    name <- gsub(pattern, "", name)
  }
  return(name)
}

remove_first_space <- function(name) {
  sub(" ", "", name)
}


convert_to_lowercase <- function(name) {
  tolower(name)
}

# Apply the function to the 'names' column
result_ssd_formated <- result_ssd
result_agro_formated <- agro

result_ssd_formated$Enzyme <- sapply(result_ssd_formated$Enzyme, remove_patterns, patterns = patterns_to_remove_ssd)

# Add '_palmitic' to the modified names
result_ssd_formated$Enzyme <- gsub("_palmitic_acid_model_4", "(with palmitic acid)",result_ssd_formated$Enzyme)

patterns_to_remove_agro <- c("WT",'Wild type tannase','Wild type',"(different distance)","\\(\\)"," ","  ")

# Apply the function to the 'names' column
result_agro_formated$Enzyme <- sapply(result_agro_formated$Enzyme, remove_patterns, patterns = patterns_to_remove_agro)

# Add '_palmitic' to the modified names
result_agro_formated$Enzyme <- gsub("mutant", "_", result_agro_formated$Enzyme)

result_ssd_formated$Enzyme <- sapply(result_ssd_formated$Enzyme, convert_to_lowercase)
result_agro_formated$Enzyme <- sapply(result_agro_formated$Enzyme, convert_to_lowercase)

result_ssd_formated$Enzyme <- sapply(result_ssd_formated$Enzyme, remove_first_space)
result_agro_formated$Enzyme <- sapply(result_agro_formated$Enzyme, remove_first_space)

result_ssd_formated$Enzyme <- gsub("withpalmitic acid", "_palmitic",result_ssd_formated$Enzyme)
result_agro_formated$Enzyme <- gsub("withpalmiticacid", "_palmitic",result_agro_formated$Enzyme)

result_ssd_formated$Enzyme <- gsub("cplip2","cpip2", result_ssd_formated$Enzyme)
result_agro_formated$Enzyme <- gsub("/","_", result_agro_formated$Enzyme)

result_ssd_formated$Enzyme <- gsub("\\(|\\)", "", result_ssd_formated$Enzyme)
result_agro_formated$Enzyme <- gsub("\\(|\\)", "", result_agro_formated$Enzyme)

result_ssd_formated$Enzyme <- gsub("cpip2_s369a_y179f8", "cpip2_s369a_y179f", result_ssd_formated$Enzyme)
result_agro_formated$Enzyme <- gsub("cpip2_y179f_s69a", "cpip2_s369a_y179f", result_agro_formated$Enzyme)

write.csv(result_agro_formated,"result_agro_formated.csv", row.names = FALSE)
write.csv(result_ssd_formated,"result_ssd_formated.csv", row.names = FALSE)
