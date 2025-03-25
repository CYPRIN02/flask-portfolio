"""MCP Client for Airtable integration"""
import os
import json
import requests
from flask import current_app

def use_mcp_tool(server_name, tool_name, arguments):
    """
    Use an MCP tool to interact with external services
    
    Args:
        server_name (str): The name of the MCP server
        tool_name (str): The name of the tool to use
        arguments (dict): The arguments to pass to the tool
        
    Returns:
        dict: The result of the tool execution
    """
    try:
        # For Airtable MCP server
        if server_name == "github.com/domdomegg/airtable-mcp-server" and tool_name == "create_record":
            return create_airtable_record(
                base_id=arguments.get('baseId'),
                table_id=arguments.get('tableId'),
                fields=arguments.get('fields')
            )
        else:
            raise ValueError(f"Unsupported MCP server or tool: {server_name}/{tool_name}")
    except Exception as e:
        current_app.logger.error(f"Error using MCP tool: {str(e)}")
        return None

def create_airtable_record(base_id, table_id, fields):
    """
    Create a record in Airtable using the Airtable API
    
    Args:
        base_id (str): The Airtable base ID
        table_id (str): The Airtable table ID
        fields (dict): The fields to set in the record
        
    Returns:
        dict: The created record data
    """
    # Get Airtable API key from environment variable
    api_key = os.environ.get('AIRTABLE_API_KEY')
    
    # If no API key is provided, use a mock response for development
    if not api_key:
        current_app.logger.warning("No Airtable API key found. Using mock response.")
        return {
            "id": "rec123456789",
            "createdTime": "2023-01-01T00:00:00.000Z",
            "fields": fields
        }
    
    # Airtable API endpoint
    url = f"https://api.airtable.com/v0/{base_id}/{table_id}"
    
    # Request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "fields": fields
    }
    
    # Make the API request
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        current_app.logger.error(f"Airtable API error: {response.status_code} - {response.text}")
        return None
