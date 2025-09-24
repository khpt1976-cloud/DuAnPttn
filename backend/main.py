from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Everon API", description="API cho website Everon", version="1.0.0")

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
    {
        "id": 1,
        "title": "Bộ Everon Epm-22063",
        "image": "/api/images/product1.jpg",
        "price": "1.200.000đ",
        "original_price": "1.500.000đ",
        "rating": 5,
        "category": "bo-2023"
    },
    {
        "id": 2,
        "title": "Bộ Everon EST-22031",
        "image": "/api/images/product2.jpg",
        "price": "1.100.000đ",
        "original_price": "1.400.000đ",
        "rating": 5,
        "category": "bo-2023"
    },
    {
        "id": 3,
        "title": "Bộ Everon EPM-22062",
        "image": "/api/images/product1.jpg",
        "price": "1.300.000đ",
        "original_price": "1.600.000đ",
        "rating": 5,
        "category": "bo-2023"
    },
    {
        "id": 4,
        "title": "Bộ Everon ESTR-23055",
        "image": "/api/images/product2.jpg",
        "price": "1.250.000đ",
        "original_price": "1.550.000đ",
        "rating": 5,
        "category": "bo-2023"
    },
    {
        "id": 5,
        "title": "Đệm Bông Ép Vỏ Gấm Everon",
        "image": "/api/images/product3.jpg",
        "price": "2.500.000đ",
        "original_price": "3.000.000đ",
        "rating": 5,
        "category": "dem-bong-ep"
    },
    {
        "id": 6,
        "title": "Đệm Đa Năng Everon Giảm 50%",
        "image": "/api/images/product3.jpg",
        "price": "1.800.000đ",
        "original_price": "3.600.000đ",
        "rating": 5,
        "category": "dem-bong-ep"
    },
    {
        "id": 7,
        "title": "Đệm Bông Ép Everon Vỏ Chần",
        "image": "/api/images/product3.jpg",
        "price": "2.200.000đ",
        "original_price": "2.800.000đ",
        "rating": 5,
        "category": "dem-bong-ep"
    },
    {
        "id": 8,
        "title": "Bộ Everon EPC 26016 - Lá Thu Đỏ",
        "image": "/api/images/product1.jpg",
        "price": "1.400.000đ",
        "rating": 5,
        "category": "bo-2026"
    },
    {
        "id": 9,
        "title": "Bộ Everon ESTC-26007 - Cẩm Chướng Đỏ",
        "image": "/api/images/product2.jpg",
        "price": "1.350.000đ",
        "rating": 5,
        "category": "bo-2026"
    },
    {
        "id": 10,
        "title": "Bộ Everon CPT 26201 - Vườn Thú Trên Mây",
        "image": "/api/images/product1.jpg",
        "price": "1.500.000đ",
        "rating": 5,
        "category": "bo-2026"
    }
]

categories_data = [
    {
        "id": 1,
        "name": "Bộ 2023 Giảm Sốc",
        "slug": "bo-2023",
        "products": [p for p in sample_products if p["category"] == "bo-2023"]
    },
    {
        "id": 2,
        "name": "Đệm Bông Ép Everon",
        "slug": "dem-bong-ep",
        "products": [p for p in sample_products if p["category"] == "dem-bong-ep"]
    },
    {
        "id": 3,
        "name": "Bộ Everon 2026",
        "slug": "bo-2026",
        "products": [p for p in sample_products if p["category"] == "bo-2026"]
    }
]

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Everon API đang hoạt động"}

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