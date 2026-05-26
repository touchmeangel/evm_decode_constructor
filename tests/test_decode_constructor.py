"""
Minimal pytest tests for decode_constructor.py
"""

from decode_constructor import decode_constructor_args, format_result


def test_decode_constructor_args_with_0x_prefix():
    """Test decoding with 0x prefix"""
    # Properly ABI-encoded: address (32 bytes) + uint256 (32 bytes)
    # Bytecode prefix (ignored) + constructor args
    input_data = (
        "0x608060405234801561001057600080fd5b50"
        + "000000000000000000000000742d35cc6634c0532925a3b844bc9e7595f12345"
        + "00000000000000000000000000000000000000000000000000000000000003e8"
    )

    decoded_args, param_types = decode_constructor_args(input_data, "address,uint256")

    assert len(decoded_args) == 2
    assert param_types == ["address", "uint256"]
    assert decoded_args[0].lower() == "0x742d35cc6634c0532925a3b844bc9e7595f12345"
    assert decoded_args[1] == 1000


def test_decode_constructor_args_without_0x_prefix():
    """Test decoding without 0x prefix"""
    input_data = (
        "608060405234801561001057600080fd5b50"
        + "000000000000000000000000742d35cc6634c0532925a3b844bc9e7595f12345"
        + "00000000000000000000000000000000000000000000000000000000000003e8"
    )

    decoded_args, param_types = decode_constructor_args(input_data, "address,uint256")

    assert len(decoded_args) == 2
    assert param_types == ["address", "uint256"]
    assert decoded_args[0].lower() == "0x742d35cc6634c0532925a3b844bc9e7595f12345"
    assert decoded_args[1] == 1000


def test_decode_single_uint256():
    """Test decoding single uint256"""
    # Just the constructor args (32 bytes = 64 hex chars)
    input_data = "0x00000000000000000000000000000000000000000000000000000000000003e8"

    decoded_args, param_types = decode_constructor_args(input_data, "uint256")

    assert len(decoded_args) == 1
    assert decoded_args[0] == 1000  # 0x3e8 = 1000


def test_decode_bool():
    """Test decoding boolean"""
    input_data = "0x0000000000000000000000000000000000000000000000000000000000000001"

    decoded_args, param_types = decode_constructor_args(input_data, "bool")

    assert len(decoded_args) == 1
    assert decoded_args[0] is True


def test_format_result_address():
    """Test formatting address"""
    result = format_result("0x742d35Cc6634C0532925a3b844Bc9e7595f0", "address")
    assert result.startswith("0x")
    assert result.islower() or result[2:].islower()


def test_format_result_uint256():
    """Test formatting uint256"""
    result = format_result(1000, "uint256")
    assert result == "1000"


def test_format_result_bool():
    """Test formatting boolean"""
    assert format_result(True, "bool") == "True"
    assert format_result(False, "bool") == "False"


def test_format_result_string():
    """Test formatting string"""
    result = format_result("hello", "string")
    assert result == '"hello"'


def test_param_types_with_spaces():
    """Test that spaces in param types are handled"""
    # Properly encoded uint256 (1000) + address
    input_data = (
        "0x"
        + "00000000000000000000000000000000000000000000000000000000000003e8"
        + "000000000000000000000000742d35cc6634c0532925a3b844bc9e7595f12345"
    )
    decoded_args, param_types = decode_constructor_args(input_data, "uint256, address")

    assert param_types == ["uint256", "address"]
    assert len(decoded_args) == 2
    assert decoded_args[0] == 1000
    assert decoded_args[1].lower() == "0x742d35cc6634c0532925a3b844bc9e7595f12345"
