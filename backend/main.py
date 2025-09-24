from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Cửa Hàng Minh Hà API", description="API cho website Cửa Hàng Minh Hà", version="1.0.0")

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:12000", "http://localhost:12001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Product(BaseModel):
    id: int
    title: str
    image: str
    price: Optional[str] = None
    original_price: Optional[str] = None
    rating: int = 5
    category: str

class Category(BaseModel):
    id: int
    name: str
    slug: str
    products: List[Product]

# Dữ liệu mẫu
sample_products = [
    # Võng xếp (8 sản phẩm)
    {
        "id": 1,
        "title": "Võng Xếp Ban Mai Inox Kiểu VIP",
        "image": "/api/images/product1.jpg",
        "price": "1.150.000đ",
        "original_price": "1.210.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 2,
        "title": "Võng Xếp Duy Phương Khung Inox Phi 27",
        "image": "/api/images/product2.jpg",
        "price": "780.000đ",
        "original_price": "950.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 3,
        "title": "Võng Xếp Chấn Thái Sơn Vuông 40",
        "image": "/api/images/product1.jpg",
        "price": "1.050.000đ",
        "original_price": "1.155.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 4,
        "title": "Võng Xếp Duy Lợi Khung Thép Cỡ Lớn",
        "image": "/api/images/product2.jpg",
        "price": "1.548.000đ",
        "original_price": "1.720.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 13,
        "title": "Võng Xếp Minh Hà Premium Inox 304",
        "image": "/api/images/product3.jpg",
        "price": "1.350.000đ",
        "original_price": "1.500.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 14,
        "title": "Võng Xếp Gia Đình Cỡ Đại",
        "image": "/api/images/product1.jpg",
        "price": "1.680.000đ",
        "original_price": "1.850.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 15,
        "title": "Võng Xếp Cho Bé An Toàn",
        "image": "/api/images/product2.jpg",
        "price": "650.000đ",
        "original_price": "750.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 16,
        "title": "Võng Xếp Du Lịch Gấp Gọn",
        "image": "/api/images/product3.jpg",
        "price": "580.000đ",
        "original_price": "680.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    # Rèm màn (6 sản phẩm)
    {
        "id": 5,
        "title": "Rèm Cửa Chống Nắng Cao Cấp",
        "image": "/api/images/product3.jpg",
        "price": "450.000đ",
        "original_price": "600.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 6,
        "title": "Màn Cửa Sổ Chống Muỗi Inox",
        "image": "/api/images/product1.jpg",
        "price": "320.000đ",
        "original_price": "450.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 7,
        "title": "Rèm Cuốn Tự Động Cao Cấp",
        "image": "/api/images/product2.jpg",
        "price": "850.000đ",
        "original_price": "1.200.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 17,
        "title": "Rèm Vải Cao Cấp Chống UV",
        "image": "/api/images/product3.jpg",
        "price": "680.000đ",
        "original_price": "850.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 18,
        "title": "Màn Nhựa PVC Trong Suốt",
        "image": "/api/images/product1.jpg",
        "price": "280.000đ",
        "original_price": "350.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 19,
        "title": "Rèm Tre Tự Nhiên Cao Cấp",
        "image": "/api/images/product2.jpg",
        "price": "520.000đ",
        "original_price": "650.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    # Giá phơi đồ (5 sản phẩm)
    {
        "id": 8,
        "title": "Giá Phơi Đồ Inox 3 Tầng Cao Cấp",
        "image": "/api/images/product1.jpg",
        "price": "680.000đ",
        "original_price": "850.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 9,
        "title": "Giá Phơi Đồ Thông Minh Gấp Gọn",
        "image": "/api/images/product2.jpg",
        "price": "420.000đ",
        "original_price": "550.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 20,
        "title": "Giá Phơi Đồ Treo Tường Tiết Kiệm",
        "image": "/api/images/product3.jpg",
        "price": "350.000đ",
        "original_price": "450.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 21,
        "title": "Giá Phơi Đồ Lắp Ráp Đa Năng",
        "image": "/api/images/product1.jpg",
        "price": "580.000đ",
        "original_price": "720.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 22,
        "title": "Giá Phơi Đồ Ngoài Trời Chống Gỉ",
        "image": "/api/images/product2.jpg",
        "price": "750.000đ",
        "original_price": "950.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    # Bàn ghế (6 sản phẩm)
    {
        "id": 10,
        "title": "Bộ Bàn Ghế Xếp Gọn Gia Đình",
        "image": "/api/images/product1.jpg",
        "price": "1.250.000đ",
        "original_price": "1.500.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 11,
        "title": "Ghế Xếp Thư Giãn Cao Cấp",
        "image": "/api/images/product2.jpg",
        "price": "650.000đ",
        "original_price": "800.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 23,
        "title": "Bàn Xếp Gọn Đa Năng",
        "image": "/api/images/product3.jpg",
        "price": "480.000đ",
        "original_price": "600.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 24,
        "title": "Ghế Xếp Inox Chống Gỉ",
        "image": "/api/images/product1.jpg",
        "price": "380.000đ",
        "original_price": "480.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 25,
        "title": "Bộ Bàn Ghế Picnic Gia Đình",
        "image": "/api/images/product2.jpg",
        "price": "1.850.000đ",
        "original_price": "2.200.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 26,
        "title": "Ghế Xếp Văn Phòng Ergonomic",
        "image": "/api/images/product3.jpg",
        "price": "920.000đ",
        "original_price": "1.150.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    # Giá treo đồ (4 sản phẩm)
    {
        "id": 12,
        "title": "Giá Treo Đồ Đa Năng Inox",
        "image": "/api/images/product3.jpg",
        "price": "380.000đ",
        "original_price": "480.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 27,
        "title": "Giá Treo Quần Áo Di Động",
        "image": "/api/images/product1.jpg",
        "price": "320.000đ",
        "original_price": "420.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 28,
        "title": "Giá Treo Đồ Gắn Tường",
        "image": "/api/images/product2.jpg",
        "price": "250.000đ",
        "original_price": "320.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 29,
        "title": "Giá Treo Đồ Cao Cấp 4 Tầng",
        "image": "/api/images/product3.jpg",
        "price": "580.000đ",
        "original_price": "720.000đ",
        "rating": 5,
        "category": "gia-treo"
    }
]

categories_data = [
    {
        "id": 1,
        "name": "Võng Xếp Cao Cấp",
        "slug": "vong-xep",
        "products": [p for p in sample_products if p["category"] == "vong-xep"]
    },
    {
        "id": 2,
        "name": "Rèm Màn Chống Nắng",
        "slug": "rem-man",
        "products": [p for p in sample_products if p["category"] == "rem-man"]
    },
    {
        "id": 3,
        "name": "Giá Phơi Đồ Thông Minh",
        "slug": "gia-phoi",
        "products": [p for p in sample_products if p["category"] == "gia-phoi"]
    },
    {
        "id": 4,
        "name": "Bàn Ghế Gia Đình",
        "slug": "ban-ghe",
        "products": [p for p in sample_products if p["category"] == "ban-ghe"]
    },
    {
        "id": 5,
        "name": "Giá Treo Đồ",
        "slug": "gia-treo",
        "products": [p for p in sample_products if p["category"] == "gia-treo"]
    }
]

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Cửa Hàng Minh Hà API đang hoạt động"}

@app.get("/api/products", response_model=List[Product])
async def get_products():
    """Lấy tất cả sản phẩm"""
    return sample_products

@app.get("/api/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Lấy thông tin sản phẩm theo ID"""
    product = next((p for p in sample_products if p["id"] == product_id), None)
    if not product:
        return {"error": "Không tìm thấy sản phẩm"}
    return product

@app.get("/api/categories", response_model=List[Category])
async def get_categories():
    """Lấy tất cả danh mục và sản phẩm"""
    return categories_data

@app.get("/api/categories/{category_slug}", response_model=Category)
async def get_category(category_slug: str):
    """Lấy danh mục theo slug"""
    category = next((c for c in categories_data if c["slug"] == category_slug), None)
    if not category:
        return {"error": "Không tìm thấy danh mục"}
    return category

@app.get("/api/search")
async def search_products(q: str):
    """Tìm kiếm sản phẩm"""
    results = [p for p in sample_products if q.lower() in p["title"].lower()]
    return {"query": q, "results": results, "total": len(results)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)