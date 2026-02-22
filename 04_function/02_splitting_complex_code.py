# you are creating a monthly report for a cafe's sales
# instead of putting all logic in one place , break it down 
# write a function generate_report() that calls , fetch_sales(), filter_valid_orders(), summarize_date()

def fetch_sales() :
    print(f"Fetching the sales data")

def filter_valid_orders():
    print(f"Filtering Valid Orders")

def summarize_date():
    print(f"Summarizing the data")

def generate_report() :
    fetch_sales()
    filter_valid_orders()
    summarize_date()
    print("Ready file")


generate_report()
