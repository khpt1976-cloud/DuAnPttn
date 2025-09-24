# Everon Website Clone

Website bán chăn ga gối đệm Everon được tạo theo mẫu từ https://everonvn.com.vn/

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
├── backend/           # Python FastAPI backend
│   ├── main.py           # API server
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
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🛠️ Công nghệ sử dụng

### Frontend
- **React 18** với TypeScript
- **Styled Components** cho styling
- **Axios** cho API calls
- **React Icons** cho icons

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation

## 📱 Tính năng

### ✅ Đã hoàn thành
- [x] Header với logo và navigation
- [x] Hero section với search
- [x] Product grid hiển thị danh mục sản phẩm
- [x] Product cards với hình ảnh và rating
- [x] Footer với thông tin liên hệ
- [x] Responsive design cho mobile
- [x] Backend API với FastAPI
- [x] Kết nối frontend-backend

### 🔄 API Endpoints

- `GET /api/products` - Lấy tất cả sản phẩm
- `GET /api/products/{id}` - Lấy sản phẩm theo ID
- `GET /api/categories` - Lấy tất cả danh mục
- `GET /api/categories/{slug}` - Lấy danh mục theo slug
- `GET /api/search?q={query}` - Tìm kiếm sản phẩm

## 🎨 Thiết kế

Website được thiết kế theo mẫu của everonvn.com.vn với:
- Màu sắc chủ đạo: Xanh dương và đỏ
- Layout responsive
- Typography hiện đại
- Hiệu ứng hover và transition

## 📞 Thông tin liên hệ (Demo)

- **Showroom 1**: 47 Ngô Gia Tự, Long Biên, Hà Nội
- **Showroom 2**: 270 Phố Huế, Hai Bà Trưng, Hà Nội
- **Hotline**: 0984 725 199 - 0984 685 283

## 📝 Ghi chú

- Dự án này được tạo cho mục đích học tập và demo
- Hình ảnh được lấy từ website gốc everonvn.com.vn
- Dữ liệu sản phẩm là dữ liệu mẫu