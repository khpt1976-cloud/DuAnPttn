# 🏪 Cửa Hàng Minh Hà - Website Bán Võng Xếp & Đồ Gia Dụng

Website thương mại điện tử chuyên bán võng xếp, rèm màn, giá phơi đồ, bàn ghế và các sản phẩm gia dụng khác.

## 🏗️ Cấu trúc dự án

```
DuAnPttn/
├── frontend/          # React TypeScript frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── services/      # API services
│   │   ├── assets/        # Hình ảnh và icons
│   │   └── styles/        # CSS styles
│   └── package.json
├── backend/           # Python Flask backend
│   ├── main.py           # Flask API server
│   ├── requirements.txt  # Python dependencies
│   └── venv/            # Virtual environment
├── start.sh          # Script khởi động
└── README.md
```

## 🚀 Cách chạy dự án

### Phương pháp 1: Sử dụng script tự động
```bash
cd DuAnPttn
./start.sh
```

### Phương pháp 2: Chạy thủ công

#### Backend (Terminal 1):
```bash
cd DuAnPttn/backend
source venv/bin/activate
python main.py
```

#### Frontend (Terminal 2):
```bash
cd DuAnPttn/frontend
npm start
```

## 🌐 Truy cập website

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## 🛠️ Công nghệ sử dụng

### Frontend
- **React 18** với TypeScript
- **Styled Components** cho styling
- **Axios** cho API calls
- **React Icons** cho icons

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **JSON** - Data storage

## 📱 Tính năng

### ✅ Đã hoàn thành
- [x] Header với logo và navigation menu
- [x] Trang chủ với carousel sản phẩm theo danh mục
- [x] Trang danh mục sản phẩm với filtering
- [x] Product cards với hình ảnh, rating và giá cả
- [x] Footer với thông tin liên hệ
- [x] Responsive design cho mobile và desktop
- [x] Backend API với Flask
- [x] Kết nối frontend-backend
- [x] Search functionality
- [x] Call-to-action sections
- [x] Floating action buttons (Gọi, Zalo, Facebook)

### 🔄 API Endpoints

- `GET /api/products` - Lấy tất cả sản phẩm
- `GET /api/products?category=<category>` - Lấy sản phẩm theo danh mục
- `GET /api/products/<id>` - Lấy chi tiết sản phẩm
- `GET /api/categories` - Lấy tất cả danh mục

### 📱 Danh mục sản phẩm
- 🛏️ Võng Xếp (10 sản phẩm)
- 🪟 Rèm - Màn (8 sản phẩm)
- 👔 Giá Phơi Đồ (6 sản phẩm)
- 👕 Giá Treo Đồ (5 sản phẩm)
- 🪑 Bàn Ghế (4 sản phẩm)
- 🔥 Giảm Giá Hot (4 sản phẩm)
- 🏠 Sản Phẩm Khác (4 sản phẩm)

## 🎨 Thiết kế

Website được thiết kế chuyên nghiệp với:
- Màu sắc chủ đạo: Xanh dương và trắng
- Layout responsive cho mọi thiết bị
- Typography hiện đại và dễ đọc
- Hiệu ứng hover và transition mượt mà
- Styled-components cho styling nhất quán

## 📞 Thông tin liên hệ

**Cửa Hàng Minh Hà**
- 📞 Hotline: 0974.876.168
- 📍 Địa chỉ: 417 Ngô Gia Tự, Hải An, Hải Phòng
- 🕐 Giờ mở cửa: Thứ 2 - Chủ nhật: 8:00 - 20:00
- 💬 Tư vấn 24/7

## 🌐 Demo

### Các trang chính:
- **Trang chủ**: `/`
- **Võng Xếp**: `/danh-muc/vong-xep`
- **Rèm Màn**: `/danh-muc/rem-man`
- **Giá Phơi Đồ**: `/danh-muc/gia-phoi`
- **Giá Treo Đồ**: `/danh-muc/gia-treo`
- **Bàn Ghế**: `/danh-muc/ban-ghe`
- **Giảm Giá Hot**: `/danh-muc/giam-gia`
- **Sản Phẩm Khác**: `/danh-muc/san-pham-khac`

## 📝 Ghi chú phát triển

- Website được thiết kế responsive, tương thích với mobile và desktop
- Sử dụng styled-components để đảm bảo styling nhất quán
- API backend có thể mở rộng để kết nối với database thực tế
- Có thể tích hợp payment gateway cho tính năng thanh toán
- SEO-friendly với React Router

---

**© 2025 Cửa Hàng Minh Hà - Chất lượng cao, Giá cả hợp lý, Bảo hành chính hãng**