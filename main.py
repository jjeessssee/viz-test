import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# --- Configuration ---
OUTPUT_PLOT_FILE = 'tip_analysis_scatterplot.png'

def run_analysis():
    """
    Loads data, performs simple analysis, and generates a plot
    using Pandas, Matplotlib, and Seaborn.
    """
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting data analysis...")

    # 1. Load Data (Seaborn built-in dataset)
    # The load_dataset function returns a Pandas DataFrame directly
    try:
        df = sns.load_dataset("tips")
    except Exception as e:
        print(f"Error loading tips dataset: {e}")
        return

    # 2. Pandas Analysis and Transformation
    print(f"Data loaded. Total records: {len(df)}")

    # Calculate the tip percentage (a new feature)
    df['tip_percentage'] = 100 * (df['tip'] / df['total_bill'])

    # Display some summary statistics of the new feature
    print("\n--- Summary of Tip Percentage ---")
    print(df['tip_percentage'].describe().round(2))
    print("---------------------------------")


    # 3. Visualization using Matplotlib (for structure) and Seaborn (for style/plot)
    
    # Set the style for better visualization
    sns.set_theme(style="whitegrid")
    
    # Create the figure and axes using Matplotlib
    plt.figure(figsize=(10, 6)) 
    
    # Generate a scatter plot using Seaborn:
    # X-axis: total bill amount
    # Y-axis: calculated tip percentage
    # Hue: Color-code by the day of the week
    sns.scatterplot(
        data=df, 
        x="total_bill", 
        y="tip_percentage", 
        hue="day", 
        s=80 # Set size of points
    )
    
    # Add title and labels using Matplotlib functions
    plt.title('Tip Percentage vs. Total Bill, by Day of Week')
    plt.xlabel('Total Bill ($)')
    plt.ylabel('Tip Percentage (%)')
    plt.legend(title='Day')

    # 4. Save the plot
    plt.savefig(OUTPUT_PLOT_FILE)
    print(f"\nPlot saved successfully as '{OUTPUT_PLOT_FILE}'")

    print("Script finished.")

if __name__ == "__main__":
    run_analysis()