import React from 'react';
import styled from 'styled-components';
import logo from '../assets/images/logo.png';

const HeaderContainer = styled.header`
  background: #2d5016;
  padding: 0;
`;

const TopBar = styled.div`
  background: #f8f9fa;
  padding: 0.5rem 0;
  border-bottom: 1px solid #e0e0e0;
`;

const TopBarContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1rem;
  font-size: 0.9rem;
`;

const ContactInfo = styled.div`
  display: flex;
  gap: 2rem;
  color: #666;
`;

const SearchContainer = styled.div`
  display: flex;
  align-items: center;
`;

const SearchInput = styled.input`
  padding: 0.4rem 0.8rem;
  border: 1px solid #ddd;
  border-radius: 3px;
  margin-right: 0.5rem;
  width: 200px;
`;

const SearchButton = styled.button`
  background: #2d5016;
  color: white;
  border: none;
  padding: 0.4rem 1rem;
  border-radius: 3px;
  cursor: pointer;
`;

const MainHeader = styled.div`
  background: white;
  padding: 1rem 0;
  text-align: center;
`;

const MainHeaderContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
`;

const Logo = styled.img`
  height: 80px;
  width: auto;
  margin-bottom: 0.5rem;
`;

const Slogan = styled.h1`
  color: #2d5016;
  font-size: 1.8rem;
  font-weight: bold;
  margin: 0.5rem 0;
  letter-spacing: 1px;
`;

const SubSlogan = styled.p`
  color: #666;
  font-size: 1rem;
  margin: 0;
`;

const NavigationBar = styled.div`
  background: #2d5016;
  padding: 0;
`;

const Navigation = styled.nav`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
`;

const NavLink = styled.a`
  color: white;
  text-decoration: none;
  font-weight: 500;
  padding: 1rem 1.5rem;
  font-size: 0.9rem;
  text-transform: uppercase;
  transition: background-color 0.3s;
  border-right: 1px solid rgba(255,255,255,0.1);

  &:hover {
    background-color: rgba(255,255,255,0.1);
  }

  &:last-child {
    border-right: none;
  }
`;

const Header: React.FC = () => {
  return (
    <HeaderContainer>
      <TopBar>
        <TopBarContent>
          <ContactInfo>
            <span>📞 0974.876.168 - Cửa Hàng Minh Hà</span>
            <span>📍 417 Ngô Gia Tự - Hải An - Hải Phòng</span>
          </ContactInfo>
          <SearchContainer>
            <SearchInput type="text" placeholder="Nhập từ khóa..." />
            <SearchButton>Tìm</SearchButton>
          </SearchContainer>
        </TopBarContent>
      </TopBar>

      <MainHeader>
        <MainHeaderContent>
          <Logo src={logo} alt="Cửa Hàng Minh Hà Logo" />
          <Slogan>CỬA HÀNG MINH HÀ<br />VÕNG - RÈM - MÀN - GIÁ PHƠI - BÀN GHẾ</Slogan>
          <SubSlogan>Chất lượng cao - Giá cả hợp lý - Bảo hành chính hãng</SubSlogan>
        </MainHeaderContent>
      </MainHeader>

      <NavigationBar>
        <Navigation>
          <NavLink href="#vong-xep">VÕNG XẾP</NavLink>
          <NavLink href="#rem-man">RÈM - MÀN</NavLink>
          <NavLink href="#gia-phoi">GIÁ PHƠI ĐỒ</NavLink>
          <NavLink href="#gia-treo">GIÁ TREO ĐỒ</NavLink>
          <NavLink href="#ban-ghe">BÀN GHẾ</NavLink>
          <NavLink href="#giam-gia">GIẢM GIÁ HOT</NavLink>
          <NavLink href="#san-pham-khac">SẢN PHẨM KHÁC</NavLink>
          <NavLink href="#lien-he">LIÊN HỆ</NavLink>
        </Navigation>
      </NavigationBar>
    </HeaderContainer>
  );
};

export default Header;