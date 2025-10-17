# amazon_recommendation_system.py
"""
Amazon Product Recommendation System
------------------------------------
This script builds an item-based collaborative filtering system
using sample Amazon product ratings data.
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

# =====================================================
# STEP 1: Loading Dataset
# =====================================================
# Replace with your CSV file (ensure it has columns: user_id, product_id, rating)
data = pd.read_csv("ratings_Beauty.csv")

# Preview the data
print("Sample Data:")
print(data.head())

# =====================================================
# STEP 2: Preparing the  Data
# =====================================================
# Drop missing values if any
data.dropna(inplace=True)

# Pivot to create user-item matrix
user_item_matrix = data.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)

print("\nUser-Item Matrix:")
print(user_item_matrix.shape)

# =====================================================
# STEP 3: Computing Item Similarity
# =====================================================
# Compute cosine similarity between products
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity,
                                  index=user_item_matrix.columns,
                                  columns=user_item_matrix.columns)

print("\nItem Similarity Matrix Shape:", item_similarity_df.shape)

# =====================================================
# STEP 4: Recommendation Function
# =====================================================
def get_similar_products(product_id, user_rating):
    """Return similar products weighted by the user's rating."""
    similar_scores = item_similarity_df[product_id] * (user_rating - 2.5)
    similar_scores = similar_scores.sort_values(ascending=False)
    return similar_scores

# =====================================================
# STEP 5: Generating Recommendations for a User
# =====================================================
def recommend_products(user_id):
    """Generate top product recommendations for a given user."""
    user_data = user_item_matrix.loc[user_id]
    similar_products = pd.Series(dtype='float64')

    for product, rating in user_data.items():
        if rating > 0:  # only consider rated products
            similar_products = similar_products.add(get_similar_products(product, rating), fill_value=0)

    # Sort and remove already-rated items
    similar_products = similar_products.sort_values(ascending=False)
    already_rated = user_data[user_data > 0].index
    recommendations = similar_products.drop(already_rated, errors='ignore').head(10)

    return recommendations

# =====================================================
# STEP 6: Example Usage
# =====================================================
# Pick a random user
sample_user = np.random.choice(user_item_matrix.index)
print(f"\nGenerating recommendations for user: {sample_user}")

recommendations = recommend_products(sample_user)
print("\n🎯 Top 10 Product Recommendations:")
print(recommendations)

# =====================================================
# STEP 7: Save Recommendations
# =====================================================
recommendations.to_csv("user_recommendations.csv")
print("\n✅ Recommendations saved to 'user_recommendations.csv'")
