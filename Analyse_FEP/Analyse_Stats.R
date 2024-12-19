# Load necessary libraries
library(dplyr)
library(ggplot2)
library("ROCR")
library("CEGO")

# Load the CSV files into data frames
ssd_results <- read.csv('result_ssd_formated.csv')
agros_results <- read.csv('result_agro_formated.csv')

# Create a mapping of ligand names from tableau_agros to result_ssd
ligand_mapping <- data.frame(
  Ligand_tableau_agros = c("Ferulic Acid", "Gallic Acid", "Caffeic Acid", "4-METHOXYPHENETHYL ALCOHOL", "CINNAMYL ALCOHOL", "DIMETHOXYBENZYL ALCOHOL"),
  Ligand_result_ssd = c("Ferulic_Acid", "Gallic_acid", "Caffeic_Acid", "4_Methoxyphenethyl_alcohol", "Cinnamyl_alcohol", "dimethoxybenzyl_alcohol")
)

# Merge the ligand mapping with tableau_agros to get the corresponding ligand names
agros_results <- agros_results %>%
  left_join(ligand_mapping, by = c("Ligand" = "Ligand_tableau_agros"))

# Merge the updated tableau_agros with result_ssd based on the enzyme name and ligand name
merged_data <- ssd_results %>%
  left_join(agros_results, by = c("Enzyme", "Ligand" = "Ligand_result_ssd"))

wilcox.test(merged_data [,"Vscore"], merged_data [,"Energy"], paired = TRUE)
wilcox.test(merged_data [,"distance"], merged_data [,"UB"], paired = TRUE)

par(mfrow = c(1, 2))  # Pour afficher deux graphiques côte à côte
boxplot(merged_data$Vscore, merged_data$Energy,
        names = c("Vscore", "Energy"),
        main = "Comparaison Vscore vs Energy",
        col = c("lightblue", "lightgreen"))

# Boîtes à moustaches pour distance vs UB
boxplot(merged_data$distance, merged_data$UB,
        names = c("distance", "UB"),
        main = "Comparaison distance vs UB",
        col = c("lightcoral", "lightgoldenrod"))


# Régression linéaire pour Vscore vs Energy
model_Vscore_Energy <- lm(Energy ~ Vscore, data = merged_data)

# Diagramme de dispersion avec droite de régression
plot(merged_data$Energy, merged_data$Vscore,
     main = "Régression linéaire : Vscore vs Energy",
     xlab = "Vscore", ylab = "Energy",
     pch = 16, col = "blue")
abline(model_Vscore_Energy, col = "orange", lwd = 2)  # Droite de régression

legend("topleft", legend = c("Régression"),
       col = c("orange"), lty = c(1, 2), lwd = 2)

model_distance_UB <- lm(UB ~ distance, data = merged_data)

# Diagramme de dispersion avec droite de régression
plot(merged_data$UB, merged_data$distance,
     main = "Régression linéaire : distance vs UB",
     xlab = "UB", ylab = "distance",
     pch = 16, col = "darkgreen")
abline(model_distance_UB, col = "orange", lwd = 2)  # Droite de régression

legend("topleft", legend = c("Régression"),
       col = c("orange"), lty = c(1, 2), lwd = 2)

model_LB_distance <- lm(LB ~ distance, data = merged_data)

plot(merged_data$LB, merged_data$distance,
     main = "Régression linéaire : distance vs LB",
     xlab = "LB", ylab = "distance",
     pch = 16, col = "darkgreen")
abline(model_LB_distance, col = "orange", lwd = 2)  # Droite de régression

legend("topleft", legend = c("Régression"),
       col = c("orange"), lty = c(1, 2), lwd = 2)

# Résumé du modèle pour Vscore vs Energy
summary(model_Vscore_Energy)

# Résumé du modèle pour distance vs UB
summary(model_distance_UB)

summary(model_LB_distance)

tau <- cor(merged_data$UB, merged_data$distance, method = "kendall")

selected_rows <- subset(merged_data, Enzyme == 'cala' & Ligand == 'Gallic_acid')
print(selected_rows)

selected_rows <- subset(merged_data, Enzyme == 'atan1p' & Ligand == 'Gallic_acid')
print(selected_rows)