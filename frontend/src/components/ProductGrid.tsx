import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import ProductCard from './ProductCard';
import { apiService, Category } from '../services/api';
import product1 from '../assets/images/product1.jpg';
import product2 from '../assets/images/product2.jpg';
import product3 from '../assets/images/product3.jpg';

const GridContainer = styled.div`
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
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const CategoryTitle = styled.h2`
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0;
  text-transform: uppercase;
`;

const NavigationButtons = styled.div`
  display: flex;
  gap: 0.5rem;
`;

const NavButton = styled.button`
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  width: 35px;
  height: 35px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: all 0.3s ease;
  
  &:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.1);
  }
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
  }
`;

const CarouselContainer = styled.div`
  position: relative;
  overflow: hidden;
  margin-bottom: 1rem;
`;

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  
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
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
  
  &:hover {
    background: #1a3009;
  }
`;

const LoadingSpinner = styled.div`
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
  color: #666;
`;

const ProductGrid: React.FC = () => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);
  const [currentSlides, setCurrentSlides] = useState<{[key: number]: number}>({});

  const getItemsPerView = () => {
    if (window.innerWidth <= 480) return 1;
    if (window.innerWidth <= 768) return 2;
    if (window.innerWidth <= 1024) return 3;
    return 4;
  };

  const [itemsPerView, setItemsPerView] = useState(4);

  useEffect(() => {
    const handleResize = () => {
      setItemsPerView(getItemsPerView());
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const data = await apiService.getCategories();
        setCategories(data);
        // Initialize slide positions
        const initialSlides: {[key: number]: number} = {};
        data.forEach(category => {
          initialSlides[category.id] = 0;
        });
        setCurrentSlides(initialSlides);
      } catch (error) {
        console.error('Error fetching categories:', error);
        // Fallback data nếu API lỗi
        const fallbackData = [
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
                image: product1,
                title: "Màn Cửa Sổ Chống Muỗi Inox",
                price: "320.000đ",
                original_price: "450.000đ",
                rating: 5,
                category: "rem-man"
              },
              {
                id: 7,
                image: product2,
                title: "Rèm Cuốn Tự Động Cao Cấp",
                price: "850.000đ",
                original_price: "1.200.000đ",
                rating: 5,
                category: "rem-man"
              },
              {
                id: 17,
                image: product3,
                title: "Rèm Vải Cao Cấp Chống UV",
                price: "680.000đ",
                original_price: "850.000đ",
                rating: 5,
                category: "rem-man"
              }
            ]
          }
        ];
        setCategories(fallbackData);
        // Initialize slide positions for fallback data
        const initialSlides: {[key: number]: number} = {};
        fallbackData.forEach(category => {
          initialSlides[category.id] = 0;
        });
        setCurrentSlides(initialSlides);
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

  const nextSlide = (categoryId: number, totalProducts: number) => {
    setCurrentSlides(prev => {
      const currentSlide = prev[categoryId] || 0;
      const maxSlide = Math.max(0, totalProducts - itemsPerView);
      const newSlide = Math.min(currentSlide + itemsPerView, maxSlide);
      return { ...prev, [categoryId]: newSlide };
    });
  };

  const prevSlide = (categoryId: number) => {
    setCurrentSlides(prev => {
      const currentSlide = prev[categoryId] || 0;
      const newSlide = Math.max(0, currentSlide - itemsPerView);
      return { ...prev, [categoryId]: newSlide };
    });
  };

  const canGoNext = (categoryId: number, totalProducts: number) => {
    const currentSlide = currentSlides[categoryId] || 0;
    return currentSlide + itemsPerView < totalProducts;
  };

  const canGoPrev = (categoryId: number) => {
    const currentSlide = currentSlides[categoryId] || 0;
    return currentSlide > 0;
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
            <NavigationButtons>
              <NavButton
                onClick={() => prevSlide(category.id)}
                disabled={!canGoPrev(category.id)}
              >
                ‹
              </NavButton>
              <NavButton
                onClick={() => nextSlide(category.id, category.products.length)}
                disabled={!canGoNext(category.id, category.products.length)}
              >
                ›
              </NavButton>
            </NavigationButtons>
          </CategoryHeader>
          <CarouselContainer>
            <Grid>
              {category.products
                .slice(currentSlides[category.id] || 0, (currentSlides[category.id] || 0) + itemsPerView)
                .map((product, productIndex) => (
                <ProductCard
                  key={productIndex}
                  id={product.id}
                  image={getProductImage(product)}
                  title={product.title}
                  price={product.price}
                  originalPrice={product.original_price}
                  rating={product.rating}
                />
              ))}
            </Grid>
          </CarouselContainer>
          <ViewAllButton>Xem tất cả</ViewAllButton>
        </CategorySection>
      ))}
    </GridContainer>
  );
};

export default ProductGrid;