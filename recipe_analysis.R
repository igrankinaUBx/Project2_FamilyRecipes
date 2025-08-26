data <- read.csv('../processed/family_recipes.csv')
ing <- unlist(strsplit(paste(data$ingredients, collapse=';'), ';'))
ing <- trimws(ing)
tbl <- sort(table(ing), decreasing=TRUE)[1:10]
png('../results/top_ingredients_R.png', width=1000, height=500)
barplot(tbl, main='Top 10 ingredients (R)', las=2)
dev.off()
