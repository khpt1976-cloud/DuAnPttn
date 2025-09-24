import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import ProductCard from './ProductCard';
import { apiService, Category } from '../services/api';
import product1 from '../assets/images/product1.jpg';
import product2 from '../assets/images/product2.jpg';
import product3 from '../assets/images/product3.jpg';

const GridContainer = styled.section`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
`;

const MainTitle = styled.h1`
  text-align: center;
  font-size: 1.8rem;
  color: #2d5016;
  margin-bottom: 2rem;
  font-weight: bold;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
`;

const CategorySection = styled.div`
  margin-bottom: 2rem;
`;

const CategoryHeader = styled.div`
  background: #2d5016;
  color: white;
  padding: 0.8rem 1.5rem;
  margin-bottom: 1rem;
  border-radius: 5px;
  text-align: center;
`;

const CategoryTitle = styled.h2`
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0;
  text-transform: uppercase;
`;

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 1rem;
  
  @media (max-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }
  
  @media (max-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
  @media (max-width: 480px) {
    grid-template-columns: 1fr;
  }
`;

const ViewAllButton = styled.button`
  display: block;
  margin: 0 auto;
  background: #2d5016;
  color: white;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    background: #1a3009;
  }
`;

const LoadingSpinner = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  font-size: 1.2rem;
  color: #666;
`;

const ProductGrid: React.FC = () => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        setLoading(true);
        const data = await apiService.getCategories();
        setCategories(data);
      } catch (err) {
        console.error('Error fetching categories:', err);
        // Fallback to static data
        setCategories([
          {
            id: 1,
            name: "VÕNG XẾP CAO CẤP",
            slug: "vong-xep",
            products: [
              {
                id: 1,
                image: product1,
                title: "Võng Xếp Ban Mai Inox Kiểu VIP",
                price: "1.150.000đ",
                original_price: "1.210.000đ",
                rating: 5,
                category: "vong-xep"
              },
              {
                id: 2,
                image: product2,
                title: "Võng Xếp Duy Phương Khung Inox Phi 27",
                price: "780.000đ",
                original_price: "950.000đ",
                rating: 5,
                category: "vong-xep"
              },
              {
                id: 3,
                image: product1,
                title: "Võng Xếp Chấn Thái Sơn Vuông 40",
                price: "1.050.000đ",
                original_price: "1.155.000đ",
                rating: 5,
                category: "vong-xep"
              },
              {
                id: 4,
                image: product2,
                title: "Võng Xếp Duy Lợi Khung Thép Cỡ Lớn",
                price: "1.548.000đ",
                original_price: "1.720.000đ",
                rating: 5,
                category: "vong-xep"
              }
            ]
          },
          {
            id: 2,
            name: "RÈM MÀN CHỐNG NẮNG",
            slug: "rem-man",
            products: [
              {
                id: 5,
                image: product3,
                title: "Rèm Cửa Chống Nắng Cao Cấp",
                price: "450.000đ",
                original_price: "600.000đ",
                rating: 5,
                category: "rem-man"
              },
              {
                id: 6,
                image: product3,
                title: "Màn Cửa Sổ Chống Muỗi Inox",
                price: "320.000đ",
                original_price: "450.000đ",
                rating: 5,
                category: "rem-man"
              },
              {
                id: 7,
                image: product3,
                title: "Rèm Cuốn Tự Động Cao Cấp",
                price: "850.000đ",
                original_price: "1.200.000đ",
                rating: 5,
                category: "rem-man"
              },
              {
                id: 8,
                image: product1,
                title: "Giá Phơi Đồ Inox 3 Tầng Cao Cấp",
                price: "680.000đ",
                original_price: "850.000đ",
                rating: 5,
                category: "gia-phoi"
              }
            ]
          }
        ]);
      } finally {
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  const getProductImage = (product: any) => {
    // Map API image paths to local images for demo
    if (product.image?.includes('product1')) return product1;
    if (product.image?.includes('product2')) return product2;
    if (product.image?.includes('product3')) return product3;
    return product.image || product1;
  };

  if (loading) {
    return (
      <GridContainer>
        <LoadingSpinner>Đang tải sản phẩm...</LoadingSpinner>
      </GridContainer>
    );
  }

  return (
    <GridContainer>
      <MainTitle>🏆 Võng Xếp Chính Hãng - Sản Phẩm Nổi Bật</MainTitle>
      {categories.map((category, index) => (
        <CategorySection key={index}>
          <CategoryHeader>
            <CategoryTitle>{category.name}</CategoryTitle>
          </CategoryHeader>
          <Grid>
            {category.products.map((product, productIndex) => (
              <ProductCard
                key={productIndex}
                image={getProductImage(product)}
                title={product.title}
                price={product.price}
                originalPrice={product.original_price}
                rating={product.rating}
              />
            ))}
          </Grid>
          <ViewAllButton>Xem tất cả</ViewAllButton>
        </CategorySection>
      ))}
    </GridContainer>
  );
};

export default ProductGrid;