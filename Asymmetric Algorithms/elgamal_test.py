import tkinter as tk
from tkinter import ttk
import elgamal_algorithm as elgamal
import time

def run_performance_analysis():
    p, g, a, A = elgamal.generate_keypair(7919)  # Choose a prime number p, e.g., 7919
    data_sizes = [16, 64, 128, 256, 512, 1024]

    result_text = "Performance Analysis\n"

    for data_size in data_sizes:
        plaintext = elgamal.generate_random_data(data_size)

        # Encryption Time
        start_time = time.time()
        K, c1 = elgamal.encrypt(p, g, A, int.from_bytes(plaintext, 'big'))
        encryption_time = time.time() - start_time

        # Decryption Time
        start_time = time.time()
        decrypted_plaintext = elgamal.decrypt(p, a, c1, K)
        decryption_time = time.time() - start_time

        # Avalanche Effect
        avalanche_effect_value = elgamal.avalanche_effect(p, g, A, plaintext)

        result_text += f"Data Size: {data_size} bytes\n"
        result_text += f"Encryption Time: {encryption_time:.6f} seconds\n"
        result_text += f"Decryption Time: {decryption_time:.6f} seconds\n"
        result_text += f"Avalanche Effect: {avalanche_effect_value:.3f}\n\n"

    result_var.set(result_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("ElGamal Performance Analysis")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Run Analysis Button
    analysis_button = ttk.Button(frame, text="Run Performance Analysis", command=run_performance_analysis)
    analysis_button.grid(row=0, column=0, columnspan=2, pady=10)

    # Results Label
    result_var = tk.StringVar()
    result_label = ttk.Label(frame, textvariable=result_var, wraplength=400, justify=tk.LEFT)
    result_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()
