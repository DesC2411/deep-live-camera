#!/usr/bin/env python3

from modules import core
from modules import ui
import ui
import core

def main():
    ui.init(start_function, destroy_function)  # Đảm bảo init được gọi trước
    core.run()  # Sau khi khởi tạo UI

if __name__ == "__main__":
    main()
