import tkinter as tk
from tkinter import ttk
from performance_analysis import *

class CryptographyTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography Performance Test")
        self.data_size_var = tk.IntVar(value=1024)
        self.result_text = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Data size input
        ttk.Label(frame, text="Data Size (bytes):").grid(row=0, column=0, sticky=tk.W)
        data_size_entry = ttk.Entry(frame, textvariable=self.data_size_var)
        data_size_entry.grid(row=0, column=1, padx=5, pady=5)

        # Run test button
        ttk.Button(
            frame,
            text="Run Test",
            command=self.run_test,
        ).grid(row=1, column=0, columnspan=2, pady=10)

        # Results label
        ttk.Label(frame, text="Results:").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(
            frame,
            textvariable=self.result_text,
            wraplength=300,
            justify=tk.LEFT,
        ).grid(row=2, column=1, padx=5, pady=5)

    def run_test(self):
        data_size = self.data_size_var.get()

        elgamal_results = run_elgamal_tests(data_size)
        diffie_hellman_results = run_diffie_hellman_tests(data_size)
        dsa_results = run_dsa_tests(data_size)
        rsa_results = run_rsa_tests(data_size)

        result_text = "ElGamal Performance Analysis:\n" + elgamal_results + "\n"
        result_text += "Diffie-Hellman Performance Analysis:\n" + diffie_hellman_results + "\n"
        result_text += "DSA Performance Analysis:\n" + dsa_results + "\n"
        result_text += "RSA Performance Analysis:\n" + rsa_results + "\n"

        self.result_text.set(result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptographyTestApp(root)
    root.mainloop()
