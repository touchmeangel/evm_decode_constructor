## EVM Constructor Decoder

Decode Solidity constructor arguments directly from Etherscan contract creation input data.

Supports any ABI-compatible constructor parameter types.

Docker image:
`touchmeangel/evm_decode_constructor`

### Usage
```
docker run --rm touchmeangel/evm_decode_constructor "<creation_input_data>" "<constructor_types>"
```

### Example
```
docker run --rm touchmeangel/evm_decode_constructor "0x608060405234801561001057600080fd5b..." "bytes32"
```

### Multiple parameters
```
docker run --rm touchmeangel/evm_decode_constructor "0x608060405234801561001057600080fd5b..." "address,uint256,bool"
```

### How it works

The tool:
- extracts constructor calldata from contract creation bytecode
- decodes arguments using standard EVM ABI rules
- prints decoded values

### Getting creation input data from Etherscan

1. Open the contract page on Etherscan
2. Go to the `Contract` tab
3. Open `Contract Creation Code`
4. Copy the full input data

### Supported types

Examples:
- address
- uint256
- bytes32
- string
- bool
- address[]
- uint256[]

### Example output

Decoded constructor arguments:
- bytes32: b'A very strong secret password :)'

### Etherscan example
![etherscan example][etherscan]


[etherscan]: https://github.com/touchmeangel/evm_decode_constructor/blob/main/images/etherscan.png?raw=true