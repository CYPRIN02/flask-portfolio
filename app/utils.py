"""Utility functions for the Flask application"""
import datetime
from flask import current_app
from app.mcp_client import use_mcp_tool

def submit_to_airtable(name, email, subject, message):
    """
    Submit contact form data to Airtable
    
    Args:
        name (str): Name of the person submitting the form
        email (str): Email of the person submitting the form
        subject (str): Subject of the message
        message (str): Content of the message
        
    Returns:
        bool: True if submission was successful, False otherwise
    """
    try:
        # Get Airtable configuration from app config
        base_id = current_app.config['AIRTABLE_BASE_ID']
        table_id = current_app.config['AIRTABLE_TABLE_ID']
        
        # Prepare the record data
        record_data = {
            "Name": name,
            "Email": email,
            "Subject": subject,
            "Message": message,
            "Submission Date": datetime.datetime.now().isoformat(),
            "Status": "New"
        }
        
        # Create the record in Airtable
        result = use_mcp_tool(
            server_name="github.com/domdomegg/airtable-mcp-server",
            tool_name="create_record",
            arguments={
                "baseId": base_id,
                "tableId": table_id,
                "fields": record_data
            }
        )
        
        # Check if the record was created successfully
        if result and 'id' in result:
            current_app.logger.info(f"Contact form submission saved to Airtable with ID: {result['id']}")
            return True
        else:
            current_app.logger.error(f"Failed to save contact form to Airtable: {result}")
            return False
            
    except Exception as e:
        current_app.logger.error(f"Error submitting to Airtable: {str(e)}")
        return False