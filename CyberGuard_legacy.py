import tkinter as tk
from tkinter import END, scrolledtext

# ==============================
# Main Window
# ==============================

root = tk.Tk()
root.title("CyberGuard AI")
root.geometry("1100x700")
root.configure(bg="#181818")

# ==============================
# Title
# ==============================

title = tk.Label(
    root,
    text="🛡 CYBERGUARD AI",
    font=("Arial", 22, "bold"),
    fg="cyan",
    bg="#1e1e1e"
)

title.pack(pady=15)
def show_message(message):
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, message)

# ==============================
# Left Menu
# ==============================

left_frame = tk.Frame(root, bg="#2b2b2b", width=250)
left_frame.pack(side="left", fill="y")
buttons = [
    "Password Analyzer",
    "URL Analyzer",
    "Email Analyzer",
    "Scam Detector",
    "File Scanner",
    "Dashboard",
    "Export Report"
]
for button in buttons:

    btn = tk.Button(
        left_frame,
        text=button,
        width=22,
        height=2,
        bg="#3b3b3b",
        fg="white",
        font=("Arial",10,"bold"),
        relief="flat",
        command=lambda b=button: show_message(f"{b}\n\nModule Ready...")
    )

    btn.pack(pady=8)

def password_module():

    output_box.delete(1.0, tk.END)

    output_box.insert(tk.END, "========== PASSWORD ANALYZER ==========\n\n")
    output_box.insert(tk.END, "Password Analyzer Module Loaded...\n")

def analyze_password():
    password = password_entry.get()

    if password == "":
        result_label.config(text="Please enter a password!")
        return

    result_label.config(
        text=f"Password Entered : {password}\n\nAnalysis will be connected next..."
    )


# ==============================
# Right Frame
# ==============================

right_frame = tk.Frame(root, bg="#1e1e1e")
right_frame.pack(side="right", fill="both", expand=True)

def clear_right_frame():
    for widget in right_frame.winfo_children():
        widget.destroy()

clear_right_frame()
def password_module():

    clear_right_frame()

    title = tk.Label(
    right_frame,
    text="🔐 Password Analyzer",
    font=("Arial",18,"bold"),
    bg="#1e1e1e",
    fg="cyan"
)

    password = password_entry.get()

    if password == "":
        result_label.config(text="Please enter a password!")
        return

    result_label.config(
        text=f"Password Entered : {password}\n\nAnalysis will be connected next..."
    )

title.pack(pady=20)

password_label = tk.Label(
    right_frame,
    text="Enter Password",
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white"
)

password_label.pack()

password_entry = tk.Entry(
    right_frame,
    width=40,
    font=("Arial",12),
    show="*"
)

password_entry.pack(pady=10)

result_label = tk.Label(
    right_frame,
    text="Result will appear here",
    font=("Arial",12),
    bg="#1e1e1e",
    fg="white"
)

result_label.pack(pady=20)

analyze_btn = tk.Button(
    right_frame,
    text="Analyze Password",
    font=("Arial",11,"bold"),
    bg="cyan",
    fg="black",
    command=analyze_password
)
output_text = tk.Text(
    right_frame,
    bg="black",
    fg="white",
    font=("Consolas",11)
)
output_text.pack(fill="both", expand=True)

# ==============================
# Output Box
# ==============================

output_box = scrolledtext.ScrolledText(
    right_frame,
    width=80,
    height=30,
    bg="black",
    fg="lime",
    font=("Consolas",11)
)

output_box.pack(padx=20,pady=20)

output_text.delete("1.0", END)
output_text.insert(END, "Hello")

# ==============================
# Status Bar
# ==============================

status = tk.Label(
    root,
    text="Status : Ready",
    bg="#333333",
    fg="white",
    anchor="w"
)

status.pack(side="bottom",fill="x")

root.mainloop()