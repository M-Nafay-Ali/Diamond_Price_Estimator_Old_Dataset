# 💎 GemValue Predictor: Premium Diamond Pricing Engine
An elegant, interactive, and AI-powered web application built to predict diamond values with luxury-tier precision. Powered by advanced Machine Learning techniques and optimized using hyperparameter tuning loops, this tool analyzes physical and chemical properties to generate real-time market valuations.
🌐 **Live Application:** [Deploy Link](https://diamond-price-estimator-olddataset.streamlit.app/)
---
## 🛠️ Project Architecture & Workflow
The machine learning core behind this app follows a rigorous pipeline designed directly inside a Kaggle notebook environment:
1. **Data Cleaning & Analysis:** Explored the dataset shape ($53,940 \text{ rows} \times 10 \text{ columns}$), missing records (`isnull().sum()`), and target distributions.
2. **Feature Preprocessing:** Designed an automated `ColumnTransformer` pipeline. 
   * **Numerical Columns** (`carat`, `depth`, `table`, `x`, `y`, `z`) were scaled using `StandardScaler`.
   * **Categorical Columns** (`cut`, `color`, `clarity`) were transformed cleanly via `OrdinalEncoder`.
3. **Data Splitting:** Partitioned dataset into an $80/20$ train-test split to protect against data leakage.
4. **Model Exploration & Tuning:** Implemented a robust `RandomizedSearchCV` cross-validation routine ($3\text{-fold CV}$) evaluating state-of-the-art boosting frameworks:
   * **XGBoost Regressor**
   * **LightGBM Regressor**
   * **CatBoost Regressor** (Chosen Champion)
5. **Insights:** Carat size and coordinate dimensions ($x, y, z$) were isolated as the most massive drivers of market value.
---
## 💎 Features of the Streamlit App
* **Premium Diamond Interface:** Custom dark luxury-mode aesthetics with a high-fidelity glowing title engine.
* **Responsive Control Sliders:** Finely calibrated step configurations to mimic realistic laboratory diamond attributes.
* **4 Cs Informational Dropdown:** Explains deep jewelry grading specs (Carat, Cut, Color, Clarity) directly to consumers.
* **Dynamic Appraisal Simulation:** Interactive animations and sound triggers (`st.balloons`) firing upon successful pricing calculations.
---
## 📊 Dataset Features Explained

| Attribute | Type | Description |
| :--- | :--- | :--- |
| **Carat** | Numerical | Weight of the diamond ($0.2 - 5.5$) |
| **Cut** | Categorical | Quality grade: Fair, Good, Very Good, Premium, Ideal |
| **Color** | Categorical | Diamond color scale ranging from D (Best) down to J (Worst) |
| **Clarity** | Categorical | Measurement of inclusions: IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1 |
| **Depth / Table** | Numerical | Total depth percentage and top width relative percentage |
| **X / Y / Z** | Numerical | Spatial lengths, widths, and structural thickness in mm |

---
## 🤝 Connect with the Developer
**Feel free to reach out for collaborations, queries, or feature extensions regarding this deployment!**
**Developer Name:-** M.Nafay Ali
**LinkedIn:-** [https://www.linkedin.com/in/mohammed-nafay-ali-16519138a?utm_source=share_via&utm_content=profile&utm_medium=member_android]
**Email Contact:-** englandengland271@gmail.com

**Developed under luxury constraints and advanced pipeline optimization routines.**
