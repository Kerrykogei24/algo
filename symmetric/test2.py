import tkinter as tk
from tkinter import ttk
from idea_algo import encrypt_decrypt_time as idea_encrypt_decrypt_time
from rc5_algo import encrypt_decrypt_time as rc5_encrypt_decrypt_time
from rc6_algo import encrypt_decrypt_time as rc6_encrypt_decrypt_time
import matplotlib.pyplot as plt

class CryptographyTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography Performance Test")
        self.algorithm_var = tk.StringVar(value="IDEA")
        self.key_size_var = tk.IntVar(value=128)
        self.data_size_var = tk.IntVar(value=1024)
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Algorithm selection
        ttk.Label(frame, text="Select Algorithm:").grid(row=0, column=0, sticky=tk.W)
        algorithm_combobox = ttk.Combobox(
            frame,
            textvariable=self.algorithm_var,
            values=["IDEA", "RC5", "RC6"],
        )
        algorithm_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Key size input
        ttk.Label(frame, text="Key Size (bits):").grid(row=1, column=0, sticky=tk.W)
        key_size_entry = ttk.Entry(frame, textvariable=self.key_size_var)
        key_size_entry.grid(row=1, column=1, padx=5, pady=5)

        # Data size input
        ttk.Label(frame, text="Data Size (bytes):").grid(row=2, column=0, sticky=tk.W)
        data_size_entry = ttk.Entry(frame, textvariable=self.data_size_var)
        data_size_entry.grid(row=2, column=1, padx=5, pady=5)

        # Run test button
        ttk.Button(
            frame,
            text="Run Test",
            command=self.run_test,
        ).grid(row=3, column=0, columnspan=2, pady=10)

        # Results label
        ttk.Label(frame, text="Results:").grid(row=4, column=0, sticky=tk.W)
        ttk.Label(
            frame, textvariable=self.result_var, wraplength=300, justify=tk.LEFT
        ).grid(row=4, column=1, padx=5, pady=5)

    def run_test(self):
        algorithm = self.algorithm_var.get()
        key_size = self.key_size_var.get()
        data_size = self.data_size_var.get()

        if algorithm == "IDEA":
            encryption_time, decryption_time = idea_encrypt_decrypt_time(
                key_size, data_size
            )
        elif algorithm == "RC5":
            encryption_time, decryption_time = rc5_encrypt_decrypt_time(
                key_size, data_size
            )
        elif algorithm == "RC6":
            encryption_time, decryption_time = rc6_encrypt_decrypt_time(
                key_size, data_size
            )
        else:
            # Code for homomorphic encryption if available
            encryption_time, decryption_time = 0.0, 0.0

        result_text = f"{algorithm} Performance Test\n"
        result_text += f"Key Size: {key_size} bits\n"
        result_text += f"Data Size: {data_size} bytes\n"
        result_text += f"Encryption Time: {encryption_time:.6f} seconds\n"
        result_text += f"Decryption Time: {decryption_time:.6f} seconds"

        self.result_var.set(result_text)

        # Draw the graph
        labels = ["Encryption Time", "Decryption Time"]
        times = [encryption_time, decryption_time]

        plt.bar(labels, times)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Algorithm")
        plt.title(f"{algorithm} Performance Test")

        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = CryptographyTestApp(root)
    root.mainloop()
