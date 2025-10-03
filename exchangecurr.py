import requests

def convert_currency(from_currency, to_currency, amount):
    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    

    try:
        # Request bhejte samay timeout add karna achhi practice hai.
        response = requests.get(url, params=params, timeout=10) 

        # HTTP Status Code check
        if response.status_code == 200:
            
            # 2. JSON decoding exception handling
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError:
                print("Error: Server ne sahi format (JSON) mein data nahi bheja.")
                return

            # 3. API ke internal success status ko check karna
            if data.get('success') == True:
                converted = data['result']
                print(f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
            else:
                
                error_info = data.get('error', {}).get('info', 'Unknown error message.')
                print(f"Error fetching exchange rates (API Internal Error): {error_info}")
        
        else:
            
            print(f"Error fetching exchange rates (HTTP Status: {response.status_code}).")
            
    # Network ya Connection errors ko handle karna
    except requests.exceptions.RequestException as e:
        print(f"A Network/Connection Error occurred. Check your internet connection or URL: {e}")
        
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")

convert_currency("usd", "inr", 100)
# convert_currency("xyz", "inr", 100)