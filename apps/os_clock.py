# PyOS Bulut Uygulaması - Dijital Saat
lbl = tk.Label(window, text="", font=("Consolas", 28, "bold"), fg="#2980B9", bg="#F0F0F0")
lbl.pack(expand=True, fill="both")

def sync():
    try: 
        lbl.config(text=time.strftime("%H:%M:%S"))
    except: 
        pass
    window.after(1000, sync)

import time
sync()
