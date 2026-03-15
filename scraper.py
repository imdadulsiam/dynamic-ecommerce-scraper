import json
from playwright.sync_api import sync_playwright

def scrape_and_save_shirts():
    url = "https://zayvir.com/collections/mens-shirts" # Hypothetical target URL
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to the site...")
        page.goto(url, wait_until="networkidle")
        
        # Explicit wait for the CSS selector
        page.wait_for_selector('.product-card', timeout=10000)
        
        extracted_data = []
        products = page.query_selector_all('.product-card')
        
        for product in products:
            name_el = product.query_selector('.shirt-name')
            price_el = product.query_selector('.shirt-price')
            
            name = name_el.inner_text().strip() if name_el else "N/A"
            raw_price = price_el.inner_text().strip() if price_el else "0"
            
            # --- THE CLEANING PROCESS YOU REQUESTED ---
            # Removing "Tk", removing commas, and stripping extra spaces
            clean_price_str = raw_price.replace("Tk", "").replace(",", "").strip()
            
            # Converting to float
            try:
                final_price = float(clean_price_str)
            except ValueError:
                final_price = 0.0 # Fallback just in case of an error
                
            extracted_data.append({"name": name, "price": final_price})
            
        browser.close()

    # --- THE SAVING PROCESS YOU REQUESTED ---
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, indent=4)
        
    print("Success! Clean data saved to data.json")

if __name__ == "__main__":
    scrape_and_save_shirts()
