import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def custom_describe(df, columns):
    """
    Generates a summary DataFrame for specified columns with statistical metrics 
    and inline distribution plots.

    Parameters:
    ----------
    df : pandas.DataFrame
        The input DataFrame containing the data.
    columns : list of str
        List of column names to include in the summary.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame containing relevant statistics based on column type:
            - Numeric: Distrib., Mean, Median, Dispersion, Min., Max.
            - Categorical: Distrib., Mode, Unique
    """
    
    # Create empty lists for numeric and categorical summaries
    numeric_summary = []
    categorical_summary = []

    for col in columns:
        try:
            # Validate column existence
            if col not in df.columns:
                print(f"Warning: Column '{col}' not found in DataFrame. Skipping.")
                continue

            # Generate Distribution Plot
            fig, ax = plt.subplots(figsize=(2, 1))
            
            # Numeric Columns
            if pd.api.types.is_numeric_dtype(df[col]):
                mean = round(df[col].mean(), 3)
                median = round(df[col].median(), 3)
                dispersion = round(df[col].std(), 3)
                min_val = round(df[col].min(), 3)
                max_val = round(df[col].max(), 3)

                sns.histplot(df[col], bins=10, kde=False, ax=ax)

                # Remove axes
                ax.set_xticks([])
                ax.set_yticks([])
                ax.axis('off')

                # Convert plot to Base64
                buffer = BytesIO()
                plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
                plt.close(fig)

                buffer.seek(0)
                img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
                distrib_image = f'<img src="data:image/png;base64,{img_base64}" width="100"/>'

                numeric_summary.append({
                    'Attribute': col,
                    'Distrib.': distrib_image,
                    'Mean': mean,
                    'Median': median,
                    'Dispersion': dispersion,
                    'Min.': min_val,
                    'Max.': max_val
                })
            
            # Categorical Columns
            else:
                mode = df[col].mode()[0] if not df[col].mode().empty else "No mode"
                unique = df[col].nunique()

                df[col].value_counts().nlargest(5).plot(kind='bar', ax=ax)

                # Remove axes
                ax.set_xticks([])
                ax.set_yticks([])
                ax.axis('off')

                # Convert plot to Base64
                buffer = BytesIO()
                plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
                plt.close(fig)

                buffer.seek(0)
                img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
                distrib_image = f'<img src="data:image/png;base64,{img_base64}" width="100"/>'

                categorical_summary.append({
                    'Attribute': col,
                    'Distrib.': distrib_image,
                    'Mode': mode,
                    'Unique': unique
                })

        except Exception as e:
            print(f"An error occurred while processing column '{col}': {e}")

    # Convert summaries to DataFrames
    numeric_df = pd.DataFrame(numeric_summary).set_index('Attribute') if numeric_summary else pd.DataFrame()
    categorical_df = pd.DataFrame(categorical_summary).set_index('Attribute') if categorical_summary else pd.DataFrame()

    # Combine and return the final summary DataFrame
    summary = pd.concat([numeric_df, categorical_df])

    # Enable inline HTML rendering for Jupyter Notebook
    summary._repr_html_ = lambda: summary.to_html(escape=False)

    return summary