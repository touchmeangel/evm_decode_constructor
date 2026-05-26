"""
Practical utility: Decode constructor arguments from Etherscan input data

Usage:
    python decode_constructor.py <input_data> <param_types>

Example:
    python decode_constructor.py "0x6080604..." "address,uint256"
"""

import sys
from eth_abi import decode

def decode_constructor_args(input_data_hex, param_types_str):
    """
    Decode constructor arguments from deployment transaction input data.
    
    Args:
        input_data_hex (str): Full input data from Etherscan (with or without 0x)
        param_types_str (str): Comma-separated parameter types (e.g., "address,uint256,bool")
    
    Returns:
        tuple: Decoded constructor arguments
    """
    if input_data_hex.startswith('0x'):
        input_data_hex = input_data_hex[2:]
    
    param_types = [t.strip() for t in param_types_str.split(',')]
    
    args_hex_length = len(param_types) * 64
    
    constructor_args_hex = input_data_hex[-args_hex_length:]
    
    constructor_args_bytes = bytes.fromhex(constructor_args_hex)
    decoded_args = decode(param_types, constructor_args_bytes)
    
    return decoded_args, param_types


def format_result(value, param_type):
    """Format decoded value based on its type"""
    if param_type == 'address':
        return f"0x{value[2:].lower()}" if value.startswith('0x') else value
    elif param_type.startswith('uint') or param_type.startswith('int'):
        return str(value)
    elif param_type == 'bool':
        return str(value)
    elif param_type == 'string':
        return f'"{value}"'
    else:
        return str(value)


def main():
    if len(sys.argv) < 3:
        print("Usage: python decode_constructor.py <input_data> <param_types>")
        print("\nExample:")
        print('  python decode_constructor.py "0x6080604..." "address,uint256"')
        print("\nSupported types: address, uint8, uint256, int256, bool, bytes32, etc.")
        print("Note: For dynamic types (string, arrays), decoding is more complex")
        return
    
    input_data = sys.argv[1]
    param_types_str = sys.argv[2]
    
    try:
        decoded_args, param_types = decode_constructor_args(input_data, param_types_str)
        
        print("=" * 70)
        print("DECODED CONSTRUCTOR ARGUMENTS")
        print("=" * 70)
        
        for i, (value, param_type) in enumerate(zip(decoded_args, param_types)):
            formatted_value = format_result(value, param_type)
            print(f"Parameter {i + 1} ({param_type}): {formatted_value}")
        
        print("=" * 70)
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure input data is valid hex")
        print("2. Verify parameter types are correct")
        print("3. For dynamic types (string, arrays), manual calculation may be needed")


if __name__ == "__main__":
    main()