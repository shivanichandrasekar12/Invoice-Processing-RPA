import logging
import datetime
import os

class AutomationLogger:
    def __init__(self, bot_name="Invoice_AI_Bot"):
        self.log_dir = "logs"
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            
        self.file_name = f"{self.log_dir}/execution_{datetime.date.today()}.log"
        
        logging.basicConfig(
            filename=self.file_name,
            level=logging.INFO,
            format=f'%(asctime)s | {bot_name} | %(levelname)s | %(message)s'
        )

    def log_step(self, step_name, status, details=""):
        """Logs a specific RPA step for Audit trails."""
        message = f"Step: {step_name} | Status: {status} | Details: {details}"
        logging.info(message)
        print(message)

    def log_exception(self, step_name, error):
        """Logs errors for rapid incident resolution in the Control Room."""
        logging.error(f"FAIL at {step_name}: {str(error)}")
