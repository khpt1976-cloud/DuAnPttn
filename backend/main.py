from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
from pydantic import BaseModel
import os

app = FastAPI(title="Cửa Hàng Minh Hà API", description="API cho website Cửa Hàng Minh Hà", version="1.0.0")

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:12000", 
        "http://localhost:12001",
        "https://work-1-basmuwpezwxjzzuy.prod-runtime.all-hands.dev",
        "https://work-2-basmuwpezwxjzzuy.prod-runtime.all-hands.dev"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Models
class Product(BaseModel):
    id: int
    title: str
    image: str
    price: Optional[str] = None
    original_price: Optional[str] = None
    rating: int = 5
    category: str

class ProductDetail(BaseModel):
    id: int
    name: str
    image: str
    price: Optional[str] = None
    originalPrice: Optional[str] = None
    rating: int = 5
    category: str
    description: str
    features: List[str]
    specifications: dict

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
        "image": "/static/images/product1.jpg",
        "price": "1.150.000đ",
        "original_price": "1.210.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 2,
        "title": "Võng Xếp Duy Phương Khung Inox Phi 27",
        "image": "/static/images/product2.jpg",
        "price": "780.000đ",
        "original_price": "950.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 3,
        "title": "Võng Xếp Chấn Thái Sơn Vuông 40",
        "image": "/static/images/product1.jpg",
        "price": "1.050.000đ",
        "original_price": "1.155.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 4,
        "title": "Võng Xếp Duy Lợi Khung Thép Cỡ Lớn",
        "image": "/static/images/product2.jpg",
        "price": "1.548.000đ",
        "original_price": "1.720.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 13,
        "title": "Võng Xếp Minh Hà Premium Inox 304",
        "image": "/static/images/product3.jpg",
        "price": "1.350.000đ",
        "original_price": "1.500.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 14,
        "title": "Võng Xếp Gia Đình Cỡ Đại",
        "image": "/static/images/product1.jpg",
        "price": "1.680.000đ",
        "original_price": "1.850.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 15,
        "title": "Võng Xếp Cho Bé An Toàn",
        "image": "/static/images/product2.jpg",
        "price": "650.000đ",
        "original_price": "750.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 16,
        "title": "Võng Xếp Du Lịch Gấp Gọn",
        "image": "/static/images/product3.jpg",
        "price": "580.000đ",
        "original_price": "680.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 50,
        "title": "Võng Xếp Cao Cấp Nhập Khẩu",
        "image": "/static/images/product1.jpg",
        "price": "1.850.000đ",
        "original_price": "2.200.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    {
        "id": 51,
        "title": "Võng Xếp Thể Thao Outdoor",
        "image": "/static/images/product2.jpg",
        "price": "920.000đ",
        "original_price": "1.150.000đ",
        "rating": 5,
        "category": "vong-xep"
    },
    # Rèm màn (6 sản phẩm)
    {
        "id": 5,
        "title": "Rèm Cửa Chống Nắng Cao Cấp",
        "image": "/static/images/product3.jpg",
        "price": "450.000đ",
        "original_price": "600.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 6,
        "title": "Màn Cửa Sổ Chống Muỗi Inox",
        "image": "/static/images/product1.jpg",
        "price": "320.000đ",
        "original_price": "450.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 7,
        "title": "Rèm Cuốn Tự Động Cao Cấp",
        "image": "/static/images/product2.jpg",
        "price": "850.000đ",
        "original_price": "1.200.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 17,
        "title": "Rèm Vải Cao Cấp Chống UV",
        "image": "/static/images/product3.jpg",
        "price": "680.000đ",
        "original_price": "850.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 18,
        "title": "Màn Nhựa PVC Trong Suốt",
        "image": "/static/images/product1.jpg",
        "price": "280.000đ",
        "original_price": "350.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 19,
        "title": "Rèm Tre Tự Nhiên Cao Cấp",
        "image": "/static/images/product2.jpg",
        "price": "520.000đ",
        "original_price": "650.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 52,
        "title": "Rèm Cửa Sổ Chống Tia UV",
        "image": "/static/images/product3.jpg",
        "price": "380.000đ",
        "original_price": "480.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    {
        "id": 53,
        "title": "Màn Cửa Lưới Chống Côn Trùng",
        "image": "/static/images/product1.jpg",
        "price": "290.000đ",
        "original_price": "380.000đ",
        "rating": 5,
        "category": "rem-man"
    },
    # Giá phơi đồ (5 sản phẩm)
    {
        "id": 8,
        "title": "Giá Phơi Đồ Inox 3 Tầng Cao Cấp",
        "image": "/static/images/product1.jpg",
        "price": "680.000đ",
        "original_price": "850.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 9,
        "title": "Giá Phơi Đồ Thông Minh Gấp Gọn",
        "image": "/static/images/product2.jpg",
        "price": "420.000đ",
        "original_price": "550.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 20,
        "title": "Giá Phơi Đồ Treo Tường Tiết Kiệm",
        "image": "/static/images/product3.jpg",
        "price": "350.000đ",
        "original_price": "450.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 21,
        "title": "Giá Phơi Đồ Lắp Ráp Đa Năng",
        "image": "/static/images/product1.jpg",
        "price": "580.000đ",
        "original_price": "720.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 22,
        "title": "Giá Phơi Đồ Ngoài Trời Chống Gỉ",
        "image": "/static/images/product2.jpg",
        "price": "750.000đ",
        "original_price": "950.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 54,
        "title": "Giá Phơi Đồ Thông Minh Điều Khiển",
        "image": "/static/images/product3.jpg",
        "price": "1.250.000đ",
        "original_price": "1.550.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 55,
        "title": "Giá Phơi Đồ Gỗ Tự Nhiên",
        "image": "/static/images/product1.jpg",
        "price": "680.000đ",
        "original_price": "850.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    {
        "id": 56,
        "title": "Giá Phơi Đồ Mini Trong Nhà",
        "image": "/static/images/product2.jpg",
        "price": "320.000đ",
        "original_price": "420.000đ",
        "rating": 5,
        "category": "gia-phoi"
    },
    # Bàn ghế (6 sản phẩm)
    {
        "id": 10,
        "title": "Bộ Bàn Ghế Xếp Gọn Gia Đình",
        "image": "/static/images/product1.jpg",
        "price": "1.250.000đ",
        "original_price": "1.500.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 11,
        "title": "Ghế Xếp Thư Giãn Cao Cấp",
        "image": "/static/images/product2.jpg",
        "price": "650.000đ",
        "original_price": "800.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 23,
        "title": "Bàn Xếp Gọn Đa Năng",
        "image": "/static/images/product3.jpg",
        "price": "480.000đ",
        "original_price": "600.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 24,
        "title": "Ghế Xếp Inox Chống Gỉ",
        "image": "/static/images/product1.jpg",
        "price": "380.000đ",
        "original_price": "480.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 25,
        "title": "Bộ Bàn Ghế Picnic Gia Đình",
        "image": "/static/images/product2.jpg",
        "price": "1.850.000đ",
        "original_price": "2.200.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 26,
        "title": "Ghế Xếp Văn Phòng Ergonomic",
        "image": "/static/images/product3.jpg",
        "price": "920.000đ",
        "original_price": "1.150.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 57,
        "title": "Bàn Xếp Gọn Cao Cấp Nhập Khẩu",
        "image": "/static/images/product1.jpg",
        "price": "1.280.000đ",
        "original_price": "1.580.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    {
        "id": 58,
        "title": "Ghế Xếp Thư Giãn Massage",
        "image": "/static/images/product2.jpg",
        "price": "1.850.000đ",
        "original_price": "2.300.000đ",
        "rating": 5,
        "category": "ban-ghe"
    },
    # Giá treo đồ (8 sản phẩm)
    {
        "id": 12,
        "title": "Giá Treo Đồ Đa Năng Inox",
        "image": "/static/images/product3.jpg",
        "price": "380.000đ",
        "original_price": "480.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 27,
        "title": "Giá Treo Quần Áo Di Động",
        "image": "/static/images/product1.jpg",
        "price": "320.000đ",
        "original_price": "420.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 28,
        "title": "Giá Treo Đồ Gắn Tường",
        "image": "/static/images/product2.jpg",
        "price": "250.000đ",
        "original_price": "320.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 29,
        "title": "Giá Treo Đồ Cao Cấp 4 Tầng",
        "image": "/static/images/product3.jpg",
        "price": "580.000đ",
        "original_price": "720.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 30,
        "title": "Giá Treo Đồ Thông Minh Xoay 360",
        "image": "/static/images/product1.jpg",
        "price": "450.000đ",
        "original_price": "550.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 31,
        "title": "Giá Treo Đồ Gỗ Tự Nhiên",
        "image": "/static/images/product2.jpg",
        "price": "680.000đ",
        "original_price": "850.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 32,
        "title": "Giá Treo Đồ Mini Để Bàn",
        "image": "/static/images/product3.jpg",
        "price": "180.000đ",
        "original_price": "250.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    {
        "id": 33,
        "title": "Giá Treo Đồ Đứng Cao Cấp",
        "image": "/static/images/product1.jpg",
        "price": "750.000đ",
        "original_price": "950.000đ",
        "rating": 5,
        "category": "gia-treo"
    },
    # Sản phẩm giảm giá hot (8 sản phẩm)
    {
        "id": 34,
        "title": "Võng Xếp Giảm Giá Sốc 50%",
        "image": "/static/images/product2.jpg",
        "price": "590.000đ",
        "original_price": "1.180.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 35,
        "title": "Rèm Cửa Thanh Lý Giá Rẻ",
        "image": "/static/images/product3.jpg",
        "price": "299.000đ",
        "original_price": "599.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 36,
        "title": "Giá Phơi Đồ Outlet Sale",
        "image": "/static/images/product1.jpg",
        "price": "399.000đ",
        "original_price": "799.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 37,
        "title": "Bàn Ghế Combo Giá Sốc",
        "image": "/static/images/product2.jpg",
        "price": "999.000đ",
        "original_price": "1.999.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 38,
        "title": "Võng Xếp Hàng Trưng Bày",
        "image": "/static/images/product3.jpg",
        "price": "450.000đ",
        "original_price": "900.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 39,
        "title": "Rèm Màn Cuối Mùa Giảm 60%",
        "image": "/static/images/product1.jpg",
        "price": "240.000đ",
        "original_price": "600.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 40,
        "title": "Giá Treo Đồ Flash Sale",
        "image": "/static/images/product2.jpg",
        "price": "199.000đ",
        "original_price": "399.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    {
        "id": 41,
        "title": "Bàn Ghế Thanh Lý Kho",
        "image": "/static/images/product3.jpg",
        "price": "799.000đ",
        "original_price": "1.599.000đ",
        "rating": 5,
        "category": "giam-gia"
    },
    # Sản phẩm khác (8 sản phẩm)
    {
        "id": 42,
        "title": "Đệm Ngồi Cao Su Non",
        "image": "/static/images/product1.jpg",
        "price": "350.000đ",
        "original_price": "450.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 43,
        "title": "Gối Ôm Cao Cấp Memory Foam",
        "image": "/static/images/product2.jpg",
        "price": "280.000đ",
        "original_price": "380.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 44,
        "title": "Chăn Điều Hòa Mùa Hè",
        "image": "/static/images/product3.jpg",
        "price": "420.000đ",
        "original_price": "550.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 45,
        "title": "Ga Trải Giường Cotton 100%",
        "image": "/static/images/product1.jpg",
        "price": "320.000đ",
        "original_price": "420.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 46,
        "title": "Vỏ Gối Lụa Tơ Tằm",
        "image": "/static/images/product2.jpg",
        "price": "180.000đ",
        "original_price": "250.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 47,
        "title": "Nệm Cao Su Thiên Nhiên",
        "image": "/static/images/product3.jpg",
        "price": "2.500.000đ",
        "original_price": "3.200.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 48,
        "title": "Bộ Chăn Ga Gối Cao Cấp",
        "image": "/static/images/product1.jpg",
        "price": "850.000đ",
        "original_price": "1.100.000đ",
        "rating": 5,
        "category": "san-pham-khac"
    },
    {
        "id": 49,
        "title": "Khăn Trải Giường Nhung",
        "image": "/static/images/product2.jpg",
        "price": "220.000đ",
        "original_price": "320.000đ",
        "rating": 5,
        "category": "san-pham-khac"
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
    },
    {
        "id": 6,
        "name": "Giảm Giá Hot",
        "slug": "giam-gia",
        "products": [p for p in sample_products if p["category"] == "giam-gia"]
    },
    {
        "id": 7,
        "name": "Sản Phẩm Khác",
        "slug": "san-pham-khac",
        "products": [p for p in sample_products if p["category"] == "san-pham-khac"]
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

@app.get("/api/products/{product_id}", response_model=ProductDetail)
async def get_product(product_id: int):
    """Lấy thông tin chi tiết sản phẩm theo ID"""
    product = next((p for p in sample_products if p["id"] == product_id), None)
    if not product:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Không tìm thấy sản phẩm")
    
    # Tạo thông tin chi tiết cho sản phẩm
    detailed_product = {
        "id": product["id"],
        "name": product["title"],
        "image": product["image"],
        "price": product["price"],
        "originalPrice": product.get("original_price"),
        "rating": product["rating"],
        "category": product["category"],
        "description": get_product_description(product["id"], product["title"]),
        "features": get_product_features(product["id"], product["category"]),
        "specifications": get_product_specifications(product["id"], product["category"])
    }
    
    return detailed_product

def get_product_description(product_id: int, title: str) -> str:
    """Tạo mô tả sản phẩm dựa trên ID và tên"""
    descriptions = {
        "vong-xep": f"{title} là sản phẩm chất lượng cao, được thiết kế với công nghệ hiện đại và chất liệu bền bỉ. Sản phẩm mang lại sự thoải mái tối đa cho người sử dụng với khả năng gấp gọn tiện lợi, phù hợp cho mọi không gian sống.",
        "rem-man": f"{title} được sản xuất từ chất liệu cao cấp, có khả năng chống nắng và bảo vệ không gian sống của bạn. Thiết kế hiện đại, dễ lắp đặt và bảo trì, mang lại hiệu quả sử dụng lâu dài.",
        "gia-phoi": f"{title} với thiết kế thông minh, tiết kiệm không gian và tối ưu hóa việc phơi đồ. Chất liệu inox cao cấp chống gỉ sét, đảm bảo độ bền và thẩm mỹ cho ngôi nhà của bạn.",
        "ban-ghe": f"{title} được thiết kế ergonomic, mang lại sự thoải mái tối đa. Chất liệu cao cấp, khung chắc chắn và có thể gấp gọn dễ dàng, phù hợp cho nhiều mục đích sử dụng khác nhau.",
        "gia-treo": f"{title} giúp tối ưu hóa không gian lưu trữ với thiết kế thông minh và hiện đại. Chất liệu bền bỉ, khả năng chịu tải cao và dễ dàng lắp đặt.",
        "giam-gia": f"{title} - Sản phẩm chất lượng cao với mức giá ưu đãi đặc biệt. Đây là cơ hội tuyệt vời để sở hữu sản phẩm chính hãng với giá tốt nhất.",
        "san-pham-khac": f"{title} là sản phẩm bổ sung hoàn hảo cho ngôi nhà của bạn. Chất lượng đảm bảo, thiết kế tinh tế và mang lại giá trị sử dụng cao."
    }
    
    # Tìm category của sản phẩm
    product = next((p for p in sample_products if p["id"] == product_id), None)
    if product:
        category = product["category"]
        return descriptions.get(category, f"{title} là sản phẩm chất lượng cao từ Cửa Hàng Minh Hà.")
    
    return f"{title} là sản phẩm chất lượng cao từ Cửa Hàng Minh Hà."

def get_product_features(product_id: int, category: str) -> List[str]:
    """Tạo danh sách tính năng dựa trên category"""
    features_map = {
        "vong-xep": [
            "Khung inox cao cấp chống gỉ sét",
            "Vải bền bỉ, thoáng mát",
            "Gấp gọn dễ dàng, tiết kiệm không gian",
            "Thiết kế ergonomic thoải mái",
            "Trọng lượng nhẹ, dễ di chuyển",
            "Bảo hành chính hãng 12 tháng"
        ],
        "rem-man": [
            "Chất liệu chống UV hiệu quả",
            "Dễ dàng lắp đặt và tháo rời",
            "Thiết kế hiện đại, thẩm mỹ cao",
            "Khả năng chống thấm nước",
            "Bảo trì đơn giản",
            "Đa dạng màu sắc và kích thước"
        ],
        "gia-phoi": [
            "Inox 304 cao cấp chống gỉ",
            "Thiết kế thông minh, tối ưu không gian",
            "Khả năng chịu tải cao",
            "Gấp gọn tiện lợi khi không sử dụng",
            "Phù hợp cả trong nhà và ngoài trời",
            "Lắp đặt đơn giản, không cần dụng cụ phức tạp"
        ],
        "ban-ghe": [
            "Thiết kế ergonomic thoải mái",
            "Chất liệu cao cấp, bền bỉ",
            "Gấp gọn dễ dàng, tiết kiệm không gian",
            "Khung chắc chắn, ổn định",
            "Phù hợp nhiều mục đích sử dụng",
            "Trọng lượng nhẹ, dễ di chuyển"
        ],
        "gia-treo": [
            "Thiết kế đa năng, tiết kiệm không gian",
            "Chất liệu bền bỉ, chịu tải cao",
            "Lắp đặt dễ dàng, không cần khoan tường",
            "Phù hợp nhiều loại quần áo",
            "Thiết kế hiện đại, thẩm mỹ",
            "Có thể điều chỉnh chiều cao"
        ],
        "giam-gia": [
            "Sản phẩm chính hãng, chất lượng đảm bảo",
            "Giá ưu đãi đặc biệt, tiết kiệm chi phí",
            "Bảo hành đầy đủ như sản phẩm thường",
            "Số lượng có hạn, cơ hội hiếm có",
            "Phù hợp cho mọi gia đình",
            "Giao hàng nhanh chóng"
        ],
        "san-pham-khac": [
            "Chất lượng cao, an toàn cho sức khỏe",
            "Thiết kế tinh tế, hiện đại",
            "Dễ sử dụng và bảo quản",
            "Phù hợp cho mọi lứa tuổi",
            "Giá cả hợp lý, chất lượng tốt",
            "Bảo hành và hỗ trợ tận tình"
        ]
    }
    
    return features_map.get(category, [
        "Chất lượng cao, bền bỉ",
        "Thiết kế hiện đại, thẩm mỹ",
        "Dễ sử dụng và bảo trì",
        "Giá cả hợp lý",
        "Bảo hành chính hãng"
    ])

def get_product_specifications(product_id: int, category: str) -> dict:
    """Tạo thông số kỹ thuật dựa trên category"""
    specs_map = {
        "vong-xep": {
            "material": "Khung inox 304, vải polyester cao cấp",
            "size": "Dài 190cm x Rộng 60cm x Cao 35cm",
            "weight": "3.5 - 5.5 kg",
            "color": "Đa dạng màu sắc",
            "warranty": "12 tháng chính hãng"
        },
        "rem-man": {
            "material": "Vải polyester chống UV, khung nhôm",
            "size": "Tùy chỉnh theo yêu cầu",
            "weight": "1.5 - 3.0 kg/m²",
            "color": "Nhiều màu sắc lựa chọn",
            "warranty": "24 tháng"
        },
        "gia-phoi": {
            "material": "Inox 304 cao cấp",
            "size": "Cao 150-180cm, có thể điều chỉnh",
            "weight": "8 - 15 kg",
            "color": "Inox nguyên bản",
            "warranty": "36 tháng chống gỉ"
        },
        "ban-ghe": {
            "material": "Khung thép/inox, mặt gỗ/nhựa cao cấp",
            "size": "Đa dạng kích thước",
            "weight": "5 - 20 kg",
            "color": "Nhiều màu sắc",
            "warranty": "18 tháng"
        },
        "gia-treo": {
            "material": "Inox/thép sơn tĩnh điện",
            "size": "Cao 120-180cm, rộng 40-80cm",
            "weight": "3 - 8 kg",
            "color": "Trắng, đen, inox",
            "warranty": "24 tháng"
        },
        "giam-gia": {
            "material": "Tùy theo từng sản phẩm",
            "size": "Đa dạng",
            "weight": "Tùy sản phẩm",
            "color": "Nhiều lựa chọn",
            "warranty": "12-24 tháng"
        },
        "san-pham-khac": {
            "material": "Chất liệu cao cấp, an toàn",
            "size": "Đa dạng kích thước",
            "weight": "Tùy sản phẩm",
            "color": "Nhiều màu sắc",
            "warranty": "12 tháng"
        }
    }
    
    return specs_map.get(category, {
        "material": "Chất liệu cao cấp",
        "warranty": "12 tháng chính hãng"
    })

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

@app.get("/static/images/{image_name}")
async def get_image(image_name: str):
    """Serve hình ảnh sản phẩm"""
    image_path = f"static/images/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        # Trả về hình ảnh mặc định nếu không tìm thấy
        default_path = "static/images/product1.jpg"
        if os.path.exists(default_path):
            return FileResponse(default_path)
        else:
            raise HTTPException(status_code=404, detail="Image not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=12000)