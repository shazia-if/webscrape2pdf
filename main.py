import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
from webscraper import fetch_webpage_content
from pdf_generator import save_to_pdf

# Function to generate PDFs from the selected CSV and folder
def generate_pdfs(csv_file, folder):
    try:
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows():
            url = row['link']
            pdf_name = row['name']
            print(f"Processing: {url} | Saving as: {pdf_name}.pdf")
            
            text = fetch_webpage_content(url)
            content = text.encode('latin-1', 'replace').decode('latin-1') #tried to fix encoding error here
            
            if content:
                save_to_pdf(content, pdf_name, folder)
            else:
                print(f"Skipping {url}, no content found.")
        
        messagebox.showinfo("Success", "PDF generation completed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open a file dialog to select a CSV file
def select_csv_file():
    file_path = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    csv_file_entry.delete(0, tk.END)
    csv_file_entry.insert(0, file_path)

# Function to open a directory dialog to select a folder
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

# Function triggered by the Start button
def start_processing():
    csv_file = csv_file_entry.get()
    folder = folder_entry.get()
    
    if not csv_file or not folder:
        messagebox.showwarning("Input Required", "Please select both a CSV file and an output folder.")
        return
    
    generate_pdfs(csv_file, folder)

# Initialize the main application window
app = tk.Tk()
app.title("Webpage to PDF Converter")

# Window layout
# CSV file selection
tk.Label(app, text="Select CSV File:").grid(row=0, column=0, padx=10, pady=10)
csv_file_entry = tk.Entry(app, width=50)
csv_file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_csv_file).grid(row=0, column=2, padx=10, pady=10)

# Output folder selection
tk.Label(app, text="Select Output Folder:").grid(row=1, column=0, padx=10, pady=10)
folder_entry = tk.Entry(app, width=50)
folder_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

# Start button
tk.Button(app, text="Start", command=start_processing, width=20).grid(row=2, column=1, pady=20)

# Run the application
app.mainloop()
