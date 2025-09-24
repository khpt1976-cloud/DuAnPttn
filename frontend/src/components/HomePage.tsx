import React from 'react';
import styled from 'styled-components';

const HomeContainer = styled.main`
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
`;

const HeroSection = styled.section`
  text-align: center;
  padding: 40px 0;
  background: linear-gradient(135deg, #2d5016 0%, #4a7c59 100%);
  color: white;
  margin-bottom: 40px;
  border-radius: 10px;
`;

const MainTitle = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 20px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
`;

const SubTitle = styled.h2`
  font-size: 1.5rem;
  margin-bottom: 30px;
  font-weight: 300;
  opacity: 0.9;
`;

const CTAButton = styled.button`
  background: #ff6b35;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.2rem;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    background: #e55a2b;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 107, 53, 0.4);
  }
`;

const FeaturesSection = styled.section`
  margin: 60px 0;
`;

const SectionTitle = styled.h2`
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
  color: #2d5016;
`;

const FeaturesGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 40px;
`;

const FeatureCard = styled.div`
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  text-align: center;
  transition: transform 0.3s ease;
  
  &:hover {
    transform: translateY(-5px);
  }
`;

const FeatureIcon = styled.div`
  font-size: 3rem;
  margin-bottom: 20px;
`;

const FeatureTitle = styled.h3`
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: #2d5016;
`;

const FeatureDescription = styled.p`
  color: #666;
  line-height: 1.6;
`;

const SEOContent = styled.section`
  margin: 60px 0;
  background: #f8f9fa;
  padding: 40px;
  border-radius: 10px;
`;

const SEOText = styled.div`
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.8;
  color: #333;
  
  h3 {
    color: #2d5016;
    margin: 30px 0 15px 0;
    font-size: 1.4rem;
  }
  
  p {
    margin-bottom: 20px;
  }
  
  strong {
    color: #2d5016;
  }
`;

const HomePage: React.FC = () => {
  return (
    <HomeContainer>
      <HeroSection>
        <MainTitle>Võng Xếp Chính Hãng - Chất Lượng Cao</MainTitle>
        <SubTitle>Chuyên cung cấp võng xếp, rèm màn, giá phơi đồ, bàn ghế gia đình</SubTitle>
        <CTAButton>Xem Sản Phẩm Ngay</CTAButton>
      </HeroSection>

      <FeaturesSection>
        <SectionTitle>Tại Sao Chọn Cửa Hàng Minh Hà?</SectionTitle>
        <FeaturesGrid>
          <FeatureCard>
            <FeatureIcon>🏆</FeatureIcon>
            <FeatureTitle>Chất Lượng Đảm Bảo</FeatureTitle>
            <FeatureDescription>
              Tất cả sản phẩm đều là hàng chính hãng, được kiểm tra kỹ lưỡng trước khi giao đến tay khách hàng.
            </FeatureDescription>
          </FeatureCard>
          
          <FeatureCard>
            <FeatureIcon>💰</FeatureIcon>
            <FeatureTitle>Giá Cả Cạnh Tranh</FeatureTitle>
            <FeatureDescription>
              Cam kết giá tốt nhất thị trường với nhiều chương trình khuyến mãi hấp dẫn quanh năm.
            </FeatureDescription>
          </FeatureCard>
          
          <FeatureCard>
            <FeatureIcon>🚚</FeatureIcon>
            <FeatureTitle>Giao Hàng Nhanh</FeatureTitle>
            <FeatureDescription>
              Giao hàng toàn quốc, nhanh chóng và an toàn. Hỗ trợ kiểm tra hàng trước khi thanh toán.
            </FeatureDescription>
          </FeatureCard>
        </FeaturesGrid>
      </FeaturesSection>

      <SEOContent>
        <SEOText>
          <h3>Võng Xếp Chính Hãng - Lựa Chọn Hoàn Hảo Cho Gia Đình</h3>
          <p>
            <strong>Cửa Hàng Minh Hà</strong> tự hào là địa chỉ uy tín chuyên cung cấp các loại 
            <strong> võng xếp chính hãng</strong> với chất lượng cao và giá cả hợp lý tại Hải Phòng. 
            Chúng tôi cam kết mang đến cho khách hàng những sản phẩm tốt nhất từ các thương hiệu 
            nổi tiếng như <strong>võng xếp Duy Lợi</strong>, <strong>võng xếp Ban Mai</strong>, 
            và nhiều loại võng xếp inox cao cấp khác.
          </p>
          
          <h3>Đa Dạng Sản Phẩm Nội Thất Gia Đình</h3>
          <p>
            Ngoài <strong>võng xếp</strong>, chúng tôi còn cung cấp đầy đủ các sản phẩm nội thất 
            thiết yếu khác như <strong>rèm màn chống nắng</strong>, <strong>giá phơi đồ thông minh</strong>, 
            <strong>bàn ghế xếp gọn</strong>, và <strong>giá treo đồ đa năng</strong>. Tất cả đều 
            được tuyển chọn kỹ lưỡng để đảm bảo chất lượng và độ bền cao.
          </p>
          
          <h3>Dịch Vụ Chuyên Nghiệp</h3>
          <p>
            Với kinh nghiệm nhiều năm trong lĩnh vực nội thất gia đình, đội ngũ nhân viên của 
            <strong> Cửa Hàng Minh Hà</strong> luôn sẵn sàng tư vấn và hỗ trợ khách hàng chọn lựa 
            sản phẩm phù hợp nhất. Chúng tôi cam kết giao hàng nhanh chóng và hỗ trợ bảo hành 
            chu đáo cho tất cả sản phẩm.
          </p>
          
          <p>
            Liên hệ ngay với chúng tôi qua số điện thoại <strong>0974.876.168</strong> hoặc 
            ghé thăm cửa hàng tại <strong>417 Ngô Gia Tự, Hải An, Hải Phòng</strong> để được 
            tư vấn và trải nghiệm sản phẩm trực tiếp!
          </p>
        </SEOText>
      </SEOContent>
    </HomeContainer>
  );
};

export default HomePage;