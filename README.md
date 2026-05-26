## EVM Constructor Decoder

Decode Solidity constructor arguments directly from Etherscan contract creation input data.

Supports any ABI-compatible constructor parameter types.

Docker image:
`touchmeangel/evm_decode_constructor`

Lightweight, simple, and useful for:
- smart contract reverse engineering
- auditing deployed contracts
- CTF challenges
- EVM research
- inspecting hidden constructor values
- automation pipelines

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
- separates runtime bytecode from constructor arguments
- decodes arguments using standard Solidity ABI rules
- prints decoded values in human-readable format

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
- tuple
- bytes
- dynamic arrays

### Example output

Decoded constructor arguments:
- bytes32: b'A very strong secret password :)'

### Etherscan example

![etherscan example][etherscan]

Thats the calldata you want to decode

```
docker run --rm touchmeangel/evm_decode_constructor "0x608060405234801561001057600080fd5b5060405161013938038061013983398101604081905261002f91610045565b6000805460ff191660019081179091555561005e565b60006020828403121561005757600080fd5b5051919050565b60cd8061006c6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c8063cf309012146037578063ec9b5b3a146057575b600080fd5b60005460439060ff1681565b604051901515815260200160405180910390f35b60666062366004607f565b6068565b005b806001541415607c576000805460ff191690555b50565b600060208284031215609057600080fd5b503591905056fea2646970667358221220fc7b38e6559928e1e1112f630b03a26ee6eb52d794080ecd75435ef82810dd9b64736f6c634300080c0033412076657279207374726f6e67207365637265742070617373776f7264203a29" "bytes32"
```

### Notes

- Constructor argument types must match the original Solidity constructor signature
- Input data should include the full contract creation bytecode
- Works with standard ABI encoding

### Contributing

Contributions, improvements, and bug reports are welcome.

Ideas for future improvements:
- automatic constructor type inference
- ABI import support
- JSON output mode
- recursive tuple formatting
- Foundry/Hardhat integration

Feel free to open issues or submit pull requests.

### License

`Apache 2.0`

[etherscan]: https://github.com/touchmeangel/evm_decode_constructor/blob/main/images/etherscan.png?raw=true