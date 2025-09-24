import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Product {
  id: number;
  title: string;
  image: string;
  price?: string;
  original_price?: string;
  rating: number;
  category: string;
}

export interface Category {
  id: number;
  name: string;
  slug: string;
  products: Product[];
}

export const apiService = {
  // Lấy tất cả sản phẩm
  async getProducts(): Promise<Product[]> {
    const response = await api.get('/api/products');
    return response.data;
  },

  // Lấy sản phẩm theo ID
  async getProduct(id: number): Promise<Product> {
    const response = await api.get(`/api/products/${id}`);
    return response.data;
  },

  // Lấy tất cả danh mục
  async getCategories(): Promise<Category[]> {
    const response = await api.get('/api/categories');
    return response.data;
  },

  // Lấy danh mục theo slug
  async getCategory(slug: string): Promise<Category> {
    const response = await api.get(`/api/categories/${slug}`);
    return response.data;
  },

  // Tìm kiếm sản phẩm
  async searchProducts(query: string): Promise<{query: string, results: Product[], total: number}> {
    const response = await api.get(`/api/search?q=${encodeURIComponent(query)}`);
    return response.data;
  },
};

export default apiService;