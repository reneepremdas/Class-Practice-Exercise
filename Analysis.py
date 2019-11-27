#Import LIbraries
import pandas as pd 

#################################################################
#TO DO: Best selling platforms for NA/EU and JP 
#TO DO: Visualize Call of Duty Sales, in North America by Platform 
###################################################################

#Read CSV
raw_data = pd.read_csv('video_games_sales.csv')

#Create Function 
def best_seller(df, agg_col): 
	"""
	THIS FUNCTION CREATES A GROUPBY BY A USER-SPECIFIED COLUMN AND RETURNS THE SORTED DF.

	DF = A DATAFRAME YOU WOULD LIKE TO TRANSFORM.
	agg_col = WHAT COLUMN WOULD YOU LIKE TO PERFORM THE AGGREGATE ON? 
	"""

	#RESET INDEX TO ALLOW FOR ILLOC
	best_seller_df = df.groupby('Platform')[agg_col].sum().reset_index()
	best_seller_df = best_seller_df.sort_values(agg_col, ascending=FALSE)
	return best_seller_df

#Apply function to different regions
best_selling_na = best_seller(raw_data, "NA_Sales")
best_selling_eu = best_seller(raw_data, "EU_Sales")
best_selling_jp = best_seller(raw_data, "JP_Sales")

#Return a statement depicting the top genre
print("The best selling genre in NA is {}".format(best_selling_na.iloc[0,0]))
print("The best selling genre in EU is {}".format(best_selling_eu.iloc[0,0]))
print("The best selling genre in JP is {}".format(best_selling_jp.iloc[0,0]))