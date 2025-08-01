import json
import os

def save_user_input():
    # Đảm bảo thư mục data tồn tại
    os.makedirs("data", exist_ok=True)

    # Nhập từ người dùng
    pain_point = input("Nhập pain point của bạn: ").strip()

    if not pain_point:
        print("❌ Pain point không được để trống.")
        return

    # Ghi vào file
    file_path = "data/input_user.json"
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({"pain_point": pain_point}, f, ensure_ascii=False, indent=2)
        print(f"✅ Pain point đã được lưu vào {file_path}")
    except Exception as e:
        print(f"❌ Lỗi khi lưu file: {e}")

if __name__ == "__main__":
    save_user_input()
