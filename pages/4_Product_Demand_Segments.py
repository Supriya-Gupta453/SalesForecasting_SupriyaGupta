import streamlit as st
import pandas as pd

st.title("📦 Product Demand Segments")

st.markdown("### Product Clustering using K-Means")

# Cluster Image
import os

image_path = "charts/product_clusters.png"

if os.path.exists(image_path):
    st.image(
        image_path,
        caption="Product Demand Clusters",
        width="stretch"
    )
else:
    st.warning("Image not found.")

# Cluster Table
cluster_data = pd.DataFrame({

"Sub-Category":[
"Copiers",
"Accessories",
"Art",
"Appliances",
"Envelopes",
"Bookcases",
"Furnishings",
"Fasteners",
"Supplies",
"Paper",
"Labels",
"Binders",
"Chairs",
"Machines",
"Phones",
"Storage",
"Tables"
],

"Cluster":[
0,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
2,
2,
2,
2,
2,
2
]

})

st.subheader("Cluster Membership")

st.dataframe(cluster_data, width="stretch")

st.subheader("Cluster Meaning")

st.markdown("""

### Cluster 0
**High Value Premium Products**

- High sales value
- Premium products
- Maintain inventory carefully

---

### Cluster 1
**Low Volume Stable Demand**

- Lower average sales
- Stable demand
- Keep moderate stock

---

### Cluster 2
**High Volume Products**

- Highest sales
- Fast-moving items
- Maintain higher inventory
- Monitor demand regularly

""")

st.success("Recommended Strategy: Maintain higher stock for Cluster 2 products while using optimized inventory planning for Clusters 0 and 1.")