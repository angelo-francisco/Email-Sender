import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from utils.util import sendEmail
import threading as thr
import os

BASE_DIR = os.path.abspath(os.curdir)
IMAGE_DIR = os.path.join(BASE_DIR, "src/assets/img/icon.ico/")


def sendEmailUI(to: str, _from: str, subject: str, message: str):
    """
    Using sendEmail, this functions creates a progress bar and send simple emails,

    Args:
        to: receiver
        _from: emissor
        subject: content subject
        message: content
    """

    progressBarBox = tk.Toplevel(window)
    progressBarBox.title("Sending email...")
    progressBarBox.iconbitmap(IMAGE_DIR)
    progressBarBox.geometry("200x150")
    progressBarBox.resizable(False, False)

    progressBar = ttk.Progressbar(
        progressBarBox,
        mode="determinate",
        maximum=100,
    )
    progressBar.pack(pady=30)
    progressBar.start()

    def sendEmailThread():
        try:
            sendEmail(to=to, _from=_from, subject=subject, message=message)
            progressBar.stop()
            progressBarBox.destroy()
            messagebox.showinfo(title="Email Box", message="Email sent successfully!")
        except Exception as e:
            progressBar.stop()
            progressBarBox.destroy()
            messagebox.showerror(title="Error sending email", message=f"Error: {e}")
    thread = thr.Thread(target=sendEmailThread)
    thread.start()


window = ctk.CTk()
window.title("Email Sender")
window.geometry("300x450")
window.iconbitmap(IMAGE_DIR)
window.resizable(False, False)

to_entry = ctk.StringVar()
subject_entry = ctk.StringVar()
from_entry = ctk.StringVar()
message_entry = ctk.StringVar()

title = ctk.CTkLabel(window, text="Email Sender", font=("Arial", 30, "bold"))
title.pack(anchor="w", padx=25, ipady=20)

to_label = ctk.CTkLabel(window, text="To:", font=("Arial", 13, "bold"))
to_label.pack(anchor="w", padx=25)
to_entry = ctk.CTkEntry(window, width=250)
to_entry.pack(anchor="w", padx=25, pady=5)

from_label = ctk.CTkLabel(window, text="From:", font=("Arial", 13, "bold"))
from_label.pack(anchor="w", padx=25)
from_entry = ctk.CTkEntry(window, width=250)
from_entry.pack(anchor="w", padx=25, pady=5)

subject_label = ctk.CTkLabel(window, text="Subject:", font=("Arial", 13, "bold"))
subject_label.pack(anchor="w", padx=25)
subject_entry = ctk.CTkEntry(window, width=250)
subject_entry.pack(anchor="w", padx=25, pady=5)

message_label = ctk.CTkLabel(
    window, text="Write your message here:", font=("Arial", 13, "bold")
)
message_label.pack(anchor="w", padx=25)
message_entry = ctk.CTkTextbox(window, width=250, height=100)
message_entry.pack(anchor="w", padx=25)

sendButton = ctk.CTkButton(
    window,
    width=250,
    height=30,  
    text="Enviar Email",
    command=lambda: sendEmailUI(
        to_entry.get(), from_entry.get(), subject_entry.get(), message_entry.get('1.0', tk.END)
    ),
)
sendButton.pack(anchor="w", pady=10, padx=25)

window.mainloop()
