# Encryption Algorithms Test

This project demonstrates the implementation and comparison of various encryption algorithms, including DES, 3DES, AES, Blowfish, and RSA, using Python. It allows you to test the encryption and decryption performance of these algorithms and observe the avalanche effect.

## Prerequisites

- Python 3.x installed on your system
- Required Python libraries: pycryptodome, tkinter

### Creating a virtual environment
    ```bash
    python -m venv virtual
    pip install -r requirements

    ```

    
## Installation

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required Python libraries by running the following command:

   ```bash
   pip install pycryptodome tkinter


# Encryption Algorithms Test

This project demonstrates the implementation and comparison of various encryption algorithms, including DES, 3DES, AES, Blowfish, and RSA, using Python. It allows you to test the encryption and decryption performance of these algorithms and observe the avalanche effect.

## Prerequisites

- Python 3.x installed on your system
- Required Python libraries: pycryptodome, tkinter

## Installation

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required Python libraries by running the following command:

   ```bash
   pip install pycryptodome tkinter

## Generating RSA Key Pair

1. To test the RSA encryption and decryption, you need an RSA key pair. 
 You can generate a new RSA key pair using the provided generate_rsa_keypair.py script or using other methods.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to generate the RSA key pair:

    ```bash
    python generate_rsa_keypair.py
    ```


4. The script will generate an RSA key pair and display the public and private keys in the console. Make note of these keys for testing.


## Usage
1. Run the application by executing the following command:the first one test DES, 3DES, AES, Blowfish  and the second command test RSA: 

   ```bash
   python test.py
   python rsa_test.py


2. The application will open a graphical user interface (GUI) window.

3. Enter the data you want to encrypt and decrypt in the provided text field.

4. Click the "Run Test" button to start the encryption and decryption process.

5. After the tests are completed, a messagebox will appear displaying the encryption time, decryption time, and avalanche effect for each algorithm.

6. Close the GUI window to exit the application.

## Customization
1. To change the length of the random data generated for testing, modify the data_length variable in the test_algorithms() function of the test.py file.

2. You can modify the UI layout or enhance the functionality of the application as per your requirements by modifying the test.py file.


## License
MIT License

