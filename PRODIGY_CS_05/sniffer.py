from scapy.all import sniff
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading


def protocol_name(protocol_number):
    protocols = {1: "ICMP", 6: 'TCP', 17: 'UDP'}
    return protocols.get(protocol_number, 'Unknown')


def packet_details(packet):
    if packet.haslayer('IP'):
        source_ip = packet['IP'].src
        destination_ip = packet['IP'].dst
        protocol_num = packet['IP'].proto
        protocol = protocol_name(protocol_num)

        payload = "No Data"
        if packet.haslayer("Raw"):
            payload = packet["Raw"].load.decode(errors= "ignore")

        # Insert packet details into the text box
        text_output.insert(tk.END, f"Source: {source_ip} --> Destination: {destination_ip}  |  Protocol: {protocol}\n")
        text_output.insert(tk.END, f"Payload: {payload}\n\n")
        text_output.see(tk.END)  

# Start sniffing packets
def start_sniffing():
    sniff(prn=packet_details)

# Function to run the sniffer in a separate thread
def start_sniffer():
    if not sniffing_status.get():
        sniffing_status.set(True)
        update_status("Sniffing...") djskjdsjdvs
        sniff_thread = threading.Thread(target=start_sniffing)
        sniff_thread.setDaemon(True)
        sniff_thread.start()
    else:
        messagebox.showinfo("Info", "Sniffer is already running!")

# Stop the sniffer and exit the GUI
def stop_sniffer():
    root.quit()

# Clear the text output area
def clear_output():
    text_output.delete(1.0, tk.END)

# Update the status bar
def update_status(status):
    status_label.config(text=f"Status: {status}")

# GUI setup
root = tk.Tk()
root.geometry("700x500")
root.title("Professional Packet Sniffer Tool")
root.configure(bg="#2b2b2b")  # Set background color

# Set the sniffing status as a Tkinter variable
sniffing_status = tk.BooleanVar(value=False)

# Title Label
title_label = tk.Label(root, text="Network Packet Sniffer", font=("Helvetica", 16, "bold"), bg="#2b2b2b", fg="white")
title_label.grid(column=0, row=0, columnspan=2, pady=10)

# Scrolled Text Widget for packet output
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, bg="#1e1e1e", fg="lightgreen", insertbackground="white", font=("Consolas", 10))
text_output.grid(column=0, row=1, columnspan=2, padx=20, pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#2b2b2b")
button_frame.grid(column=0, row=2, columnspan=2, pady=10)

# Start Button
start_button = tk.Button(button_frame, text="Start Sniffing", command=start_sniffer, bg="green", fg="white", width=15, font=("Arial", 12, "bold"))
start_button.grid(column=0, row=0, padx=10)

# Stop Button
stop_button = tk.Button(button_frame, text="Stop Sniffing", command=stop_sniffer, bg="red", fg="white", width=15, font=("Arial", 12, "bold"))
stop_button.grid(column=1, row=0, padx=10)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear Output", command=clear_output, bg="blue", fg="white", width=15, font=("Arial", 12, "bold"))
clear_button.grid(column=2, row=0, padx=10)

# Status Bar
status_label = tk.Label(root, text="Status: Idle", bg="#2b2b2b", fg="white", anchor="w")
status_label.grid(column=0, row=3, columnspan=2, padx=10, pady=5, sticky="we")

# Start the GUI loop
root.mainloop()