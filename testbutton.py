from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver_path = r"V:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Khởi tạo Chrome driver
driver = webdriver.Chrome(service=service)

# Mở trang web
driver.get("https://e-commerce-for-testing.onrender.com")
time.sleep(5)

try:
    # Tìm nút Login và nhấn vào nó
    button = driver.find_element(By.XPATH, "//button[@class='chakra-button css-h211ee' and text()='Login']")
    button.click()
    print("True 'Login'")

    # Đăng nhập với email và mật khẩu sai
    email_input = driver.find_element(By.ID, "field-:r0:")
    email_input.send_keys("hyng@gmail.com")  # Email sai
    print("True Email")
    
    password_input = driver.find_element(By.ID, "field-:r1:")
    password_input.send_keys("admin1444")  # Mật khẩu sai
    print("True Password")

    # Nhấn nút 'Sign In' để đăng nhập
    sign_in_button = driver.find_element(By.XPATH, "//button[@class='chakra-button css-1qqymvj' and text()='Sign In']")
    sign_in_button.click()
    print("True 'Sign In'")

    # Kiểm tra thông báo lỗi nếu đăng nhập sai
    try:
        # Giả sử có thông báo lỗi sau khi đăng nhập sai
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'chakra-alert')]")
        if error_message.is_displayed():
            print("Flase: ", error_message.text)
        else:
            print("Flase")
    except Exception as e:
        print("Flase")
    
    time.sleep(2)  # Dừng một chút trước khi đăng nhập lại đúng

    email_input = driver.find_element(By.ID, "field-:r0:")
    driver.execute_script("arguments[0].value = '';", email_input)  # Xóa trường nhập bằng JavaScript
    time.sleep(1)  # Đảm bảo input đã được làm mới
    email_input.send_keys("superadmin@gmail.com")  # Email đúng
    print("True Email")

    password_input = driver.find_element(By.ID, "field-:r1:")
    driver.execute_script("arguments[0].value = '';", password_input)  # Xóa trường nhập bằng JavaScript
    time.sleep(1)  # Đảm bảo input đã được làm mới
    password_input.send_keys("admin123")  # Mật khẩu đúng
    print("True Password")

    # Nhấn nút 'Sign In' để đăng nhập
    sign_in_button.click()
    print("True 'Sign In'")

    # Kiểm tra xem đăng nhập có thành công không
    try:
        # Kiểm tra thông báo lỗi đăng nhập (nếu có)
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'chakra-alert')]")
        if error_message.is_displayed():
            print("Flase: ", error_message.text)
        else:
            print("True")
    except Exception as e:
        print("I don't know")

except Exception as e:
    print("ERROR:", e)

# Chờ người dùng nhấn Enter để kết thúc
input("Exit ")

# Đóng trình duyệt
driver.quit()
