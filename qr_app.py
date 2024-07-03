import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image, ImageTk

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Application")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose an option")
        self.label.pack(pady=10)

        self.generate_btn = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_btn.pack(pady=5)

        self.scan_btn = tk.Button(self.root, text="Scan QR Code", command=self.scan_qr_code)
        self.scan_btn.pack(pady=5)

    def generate_qr_code(self):
        self.clear_frame()
        self.label = tk.Label(self.root, text="Enter the link to generate QR code")
        self.label.pack(pady=10)

        self.link_entry = tk.Entry(self.root, width=50)
        self.link_entry.pack(pady=5)

        self.generate_btn = tk.Button(self.root, text="Generate", command=self.save_qr_code)
        self.generate_btn.pack(pady=5)

    def save_qr_code(self):
        link = self.link_entry.get()
        if not link:
            messagebox.showerror("Error", "Please enter a valid link")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved to {file_path}")

    def scan_qr_code(self):
        self.clear_frame()
        self.label = tk.Label(self.root, text="Choose an option to scan QR code")
        self.label.pack(pady=10)

        self.camera_btn = tk.Button(self.root, text="Open Camera", command=self.scan_with_camera)
        self.camera_btn.pack(pady=5)

        self.upload_btn = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

    def scan_with_camera(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Unable to access the camera")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            decoded_objects = decode(frame)
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    points = hull

                for i in range(len(points)):
                    cv2.line(frame, tuple(points[i]), tuple(points[(i + 1) % len(points)]), (255, 0, 0), 3)

                x = obj.rect.left
                y = obj.rect.top
                w = obj.rect.width
                h = obj.rect.height

                qr_data = obj.data.decode("utf-8")
                cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                messagebox.showinfo("QR Code Data", qr_data)
                cap.release()
                cv2.destroyAllWindows()
                return

            cv2.imshow("QR Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return

        img = cv2.imread(file_path)
        decoded_objects = decode(img)
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode('utf-8')
            messagebox.showinfo("QR Code Data", qr_data)
        else:
            messagebox.showerror("Error", "No QR code found in the image")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
