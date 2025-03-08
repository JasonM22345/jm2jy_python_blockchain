# Python Blockchain

### Author: https://github.com/JasonM22345
## Overview
This project is a simple blockchain implementation written in Python. It simulates a basic proof-of-work system where blocks are created, transactions are added, and the blockchain is validated. The blockchain is stored in a local directory (`jm2jy_Blockchain`), and each block is represented as a text file.

## Key Features
- **Block Creation:** Users can create new blocks, each referencing the previous block via a cryptographic hash.
- **Transactions:** Transactions can be added to existing blocks.
- **Proof of Work:** Each block requires a nonce that meets a specific target before being added to the chain.
- **Blockchain Validation:** The integrity of the blockchain can be verified by checking the hashes of previous blocks.
- **Persistence:** The blockchain is stored as text files, and the folder is cleared each time the program starts.

## How It Works (Algorithm Overview)
The blockchain follows a simplified Proof-of-Work (PoW) mechanism:
1. The **Genesis Block** (Block 0) is created at the start.
2. New **Blocks** are created sequentially, each referencing the hash of the previous block.
3. A **Nonce** (random number) is calculated to meet a target difficulty.
4. **Transactions** can be added to an existing block.
5. The **Blockchain is validated** by comparing stored hashes with recalculated hashes.

### Breakdown of the Algorithm
#### 1. **Folder and Genesis Block Creation**
- The program ensures that the `jm2jy_Blockchain` folder exists.
- If the folder exists, it is cleared before starting.
- A Genesis Block (Block 0) is created with an initial timestamp and a default nonce.

#### 2. **Creating a New Block**
- The hash of the previous block is computed using `sha256`.
- A new block file is created, containing:
  - Block number
  - Timestamp
  - Hash of the previous block
  - Transaction data
  - A valid nonce

#### 3. **Generating a Valid Nonce**
- The nonce is incremented until the SHA-256 hash of the block content meets the target.
- The required target is converted to a hexadecimal format for comparison.

#### 4. **Adding Transactions**
- The last nonce in the block is removed.
- A new transaction (timestamp) is appended to the block.
- A new nonce is calculated and appended.

#### 5. **Validating the Blockchain**
- The program iterates through all blocks.
- The stored hash of the previous block is compared with a recalculated hash.
- If any hash mismatch is found, the blockchain is deemed invalid.

## Installation and Execution
### Requirements
- Python 3.x
- Standard Python libraries (`os`, `sys`, `datetime`, `hashlib`, etc.)

### Running the Blockchain
```bash
python3 PythonBlockchain.py [target]
```
**Example:**
```bash
python3 PythonBlockchain.py abc
```
If no target is provided in the command-line arguments, the program will prompt for one.

### Menu Options
Once the program starts, users can interact with the blockchain through the following menu:
1. **Create New Block** - Generates a new block with proof-of-work.
2. **Add Transaction** - Adds a transaction to the latest block.
3. **Validate Chain** - Verifies blockchain integrity.
4. **Exit** - Terminates the program.

## Notes
- The blockchain folder (`jm2jy_Blockchain`) is cleared on each run to ensure a fresh start.
- The indexing of blocks starts from 1.
- The chain becomes invalid if the stored hash of a block does not match the recalculated hash of the previous block.

## License
This project is open-source and can be modified for learning purposes.
