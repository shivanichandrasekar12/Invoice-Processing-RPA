import sys
from src.invoice_classifier import InvoiceAI

def run_automation(invoice_content):
    # Initialize the AI Brain
    ai_engine = InvoiceAI()
    
    # Process and Classify
    category = ai_engine.predict_department(invoice_content)
    
    # Return result to Blue Prism
    print(f"RESULT_START|{category}|RESULT_END")

if __name__ == "__main__":
    # Blue Prism passes the invoice text as an argument
    if len(sys.argv) > 1:
        run_automation(sys.argv[1])
    else:
        print("Error: No invoice text provided.")