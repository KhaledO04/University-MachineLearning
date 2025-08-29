# Simple KNN Implementation - Copy this into your notebook cell

from sklearn.neighbors import KNeighborsRegressor

# Create KNN model with k=3
knn = KNeighborsRegressor(n_neighbors=3)

# Train the model
knn.fit(X, y.ravel())

# Make prediction for Cyprus
X_new = [[22587]]  # Cyprus' GDP per capita
y_pred_knn = knn.predict(X_new)
print(f"KNN prediction for Cyprus: {y_pred_knn[0]:.2f}")

# Get the score
knn_score = knn.score(X, y.ravel())
print(f"KNN R² score: {knn_score:.3f}")

# Compare with linear regression
print(f"Linear regression prediction: {y_pred[0][0]:.2f}")
print(f"Linear regression R² score: {model.score(X, y):.3f}")

# Test different k values
print("\nTesting different k values:")
for k in [1, 3, 5, 7]:
    knn_test = KNeighborsRegressor(n_neighbors=k)
    knn_test.fit(X, y.ravel())
    test_pred = knn_test.predict(X_new)
    test_score = knn_test.score(X, y.ravel())
    print(f"k={k}: prediction={test_pred[0]:.2f}, R²={test_score:.3f}") 