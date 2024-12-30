import tkinter as tk
from tkinter import messagebox
import random
import os
import csv

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Trò chơi đoán số")
        self.root.configure(bg="#f0f8ff")  # Màu nền cho cửa sổ
        
        # Khởi tạo biến
        self.secret_number = None
        self.attempts = 0
        self.current_guesses = []
        self.game_count = 1
        self.history_file = "history.csv"  # File lưu trữ lịch sử
        self.player_name = ""  # Lưu tên người chơi
        
        # Tạo file lịch sử nếu chưa tồn tại
        if not os.path.exists(self.history_file):
            with open(self.history_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Tên người chơi", "Số bí mật", "Các số đã chọn", "Số lần đoán"])  # Tiêu đề cột

        # Tạo giao diện
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        # Tiêu đề
        self.title_label = tk.Label(self.root, text="Số May Mắn của bạn là?", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#00008b")
        self.title_label.pack(pady=10)

        # Hướng dẫn
        self.instruction_label = tk.Label(self.root, text="Hãy đoán một số từ 1 đến 1000 đi nào!", bg="#f0f8ff", fg="#00008b")
        self.instruction_label.pack()

        # Nhập tên người chơi và nút "Bắt đầu trò chơi"
        self.name_frame = tk.Frame(self.root, bg="#f0f8ff")  # Sử dụng Frame để nhóm lại
        self.name_frame.pack(pady=5)

        self.name_label = tk.Label(self.name_frame, text="Nhập tên người chơi:", bg="#f0f8ff", fg="#00008b")
        self.name_label.pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 14), bg="#fff", fg="#00008b", bd=2)
        self.name_entry.pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(self.name_frame, text="Bắt đầu trò chơi", command=self.start_game, bg="#32cd32", fg="white", font=("Arial", 14), bd=3, activebackground="#98fb98")
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Gợi ý
        self.hint_label = tk.Label(self.root, text="Gợi ý sẽ xuất hiện tại đây.", font=("Arial", 24, "italic"), bg="#f0f8ff", fg="#ff6347")
        self.hint_label.pack(pady=10)

        # Nhập số dự đoán
        self.input_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.input_frame.pack(pady=10)

        self.guess_entry = tk.Entry(self.input_frame, font=("Arial", 14), bg="#fff", fg="#00008b", bd=2)
        self.guess_entry.pack(side=tk.LEFT, padx=5)

        # Gắn sự kiện nhấn phím Enter
        self.guess_entry.bind("<Return>", self.check_guess_event)

        self.guess_button = tk.Button(self.input_frame, text="Đoán số", command=self.check_guess, bg="#4682b4", fg="white", font=("Arial", 14), bd=3, activebackground="#5f9ea0")
        self.guess_button.pack(side=tk.LEFT, padx=5)

        # Các nút điều khiển
        self.control_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.control_frame.pack(pady=10)

        self.quit_button = tk.Button(self.control_frame, text="Thoát", command=self.root.quit, bg="#ff6347", fg="white", font=("Arial", 14), bd=3, activebackground="#ff7f50")
        self.quit_button.pack(side=tk.LEFT, padx=10)

        # Nút Xem đáp án
        self.answer_button = tk.Button(self.control_frame, text="Xem đáp án", command=self.show_answer, bg="#ffa500", fg="white", font=("Arial", 14), bd=3, activebackground="#ffcc00")
        self.answer_button.pack(side=tk.LEFT, padx=10)

        # Hiển thị số lần đoán
        self.attempts_label = tk.Label(self.root, text="Số lần đoán: 0", font=("Arial", 12), bg="#f0f8ff", fg="#00008b")
        self.attempts_label.pack(pady=10)

        # Hiển thị các thông tin bổ sung
        self.info_label = tk.Label(self.root, text="Thông tin trò chơi sẽ xuất hiện tại đây.", font=("Arial", 12), bg="#f0f8ff", fg="#00008b")
        self.info_label.pack(pady=10)

    def start_game(self):
        # Lấy tên người chơi
        self.player_name = self.name_entry.get().strip()
        if not self.player_name:  # Kiểm tra xem người chơi có nhập tên hay không
            messagebox.showerror("Lưu ý", "Vui lòng nhập tên người chơi! Nhớ nhấn 'Bắt đầu trò chơi' đấy nhé")
            return
        
        # Reset trò chơi
        self.secret_number = random.randint(1, 1000)
        self.attempts = 0
        self.current_guesses = []
        self.guess_entry.delete(0, tk.END)
        
        # Đặt lại gợi ý
        self.hint_label.config(text="Gợi ý sẽ xuất hiện tại đây.")
        self.attempts_label.config(text="Số lần đoán: 0")
        
        # Cập nhật thông tin trò chơi (không hiển thị số bí mật)
        self.info_label.config(text=f"Tên người chơi: {self.player_name}\nCác số đã chọn: {self.current_guesses}\nSố lần đoán: {self.attempts}")

        messagebox.showinfo("Thông báo", f"Chào mừng {self.player_name} đến với trò chơi! Hãy đoán số mới!")

    def save_history(self):
        try:
            # Ghi thông tin lịch sử vào file CSV
            with open(self.history_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.player_name, self.secret_number, self.current_guesses, self.attempts])
            print(f"Lưu thành công: {self.player_name}, {self.secret_number}, {self.current_guesses}, {self.attempts}")
        except Exception as e:
            print(f"Lỗi khi lưu lịch sử: {e}")

    def show_answer(self):
        """ Hiển thị đáp án khi người chơi nhấn nút 'Xem đáp án' """
        messagebox.showinfo("Đáp án", f"Số bí mật là: {self.secret_number}")

    def check_guess_event(self, event):
        # Xử lý sự kiện Enter
        self.check_guess()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.current_guesses.append(guess)  # Lưu số đã đoán
            self.attempts_label.config(text=f"Số lần đoán: {self.attempts}")

            # Cập nhật lại thông tin trên giao diện
            self.info_label.config(text=f"Tên người chơi: {self.player_name}\nCác số đã chọn: {self.current_guesses}\nSố lần đoán: {self.attempts}")

            if guess > self.secret_number:
                self.hint_label.config(text="GỢI Ý NHỎ: Sai rồi đó bro! NÓ quá lớn rồi!")
            elif guess < self.secret_number:
                self.hint_label.config(text="GỢI Ý NHỎ: Bro lại sai rồi! của bro nhỏ quá :)")
            else:
                self.hint_label.config(text=f"Chúc mừng! Bro đã đoán đúng số may mắn của mình! QUá đỉnh! {self.secret_number}!")
                messagebox.showinfo("Chiến thắng", f"Bạn đã đoán đúng số {self.secret_number} sau {self.attempts} lần đoán!")
                
                # Lưu lịch sử sau khi đoán đúng
                self.save_history()
                
                # Cập nhật lại thông tin, hiển thị số bí mật sau khi đoán đúng
                self.info_label.config(text=f"Tên người chơi: {self.player_name}\nSố bí mật: {self.secret_number}\nCác số đã chọn: {self.current_guesses}\nSố lần đoán: {self.attempts}")
                
                self.start_game()  # Bắt đầu lại trò chơi
        except ValueError:
            messagebox.showerror("Lỗi", "DỪng nhập tào lao như thế chứ!")

# Tạo cửa sổ chính và chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

