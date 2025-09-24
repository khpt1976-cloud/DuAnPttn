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
            name: "BỘ 2023 GIẢM SỐC",
            slug: "bo-2023",
            products: [
              {
                id: 1,
                image: product1,
                title: "BỘ EVERON EPM-22063",
                price: "3.414.000 đ",
                original_price: "4.517.000 đ",
                rating: 5,
                category: "bo-2023"
              },
              {
                id: 2,
                image: product2,
                title: "BỘ EVERON EST-22031",
                price: "3.162.000 đ",
                original_price: "4.217.000 đ",
                rating: 5,
                category: "bo-2023"
              },
              {
                id: 3,
                image: product1,
                title: "BỘ EVERON EPM-22062",
                price: "3.300.000 đ",
                original_price: "4.374.000 đ",
                rating: 5,
                category: "bo-2023"
              },
              {
                id: 4,
                image: product2,
                title: "BỘ EVERON ESTR-23055",
                price: "1.199.000 đ",
                original_price: "1.599.000 đ",
                rating: 5,
                category: "bo-2023"
              }
            ]
          },
          {
            id: 2,
            name: "ĐỆM BÔNG ÉP EVERON",
            slug: "dem-bong-ep",
            products: [
              {
                id: 5,
                image: product3,
                title: "ĐỆM BÔNG ÉP VỎ GẤM EVERON",
                price: "1.752.000 đ",
                original_price: "2.190.000 đ",
                rating: 5,
                category: "dem-bong-ep"
              },
              {
                id: 6,
                image: product3,
                title: "ĐỆM ĐA NĂNG EVERON GIẢM 50%",
                price: "745.000 đ",
                original_price: "1.490.000 đ",
                rating: 5,
                category: "dem-bong-ep"
              },
              {
                id: 7,
                image: product3,
                title: "BẢNG GIÁ VỎ EVERON NĂM 2025",
                price: "1.771.000 đ",
                original_price: "2.214.000 đ",
                rating: 5,
                category: "dem-bong-ep"
              },
              {
                id: 8,
                image: product3,
                title: "ĐỆM BÔNG ÉP EVERON VỎ CHẦN",
                price: "2.072.000 đ",
                original_price: "2.590.000 đ",
                rating: 5,
                category: "dem-bong-ep"
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